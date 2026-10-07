"""Detect faces in photos and save square, face-centered crops + a contact sheet.

python crop_faces.py <out_dir> <photo1.jpg> [photo2.jpg ...]

Writes <out_dir>/<name>-<n>.jpg (640x640) and <out_dir>/_sheet.png (numbered).
LOOK at the sheet (Read tool) and keep only sharp, front-facing, well-framed
faces; Haar detection gives false positives (clothes, posters, blurry crowd).
Requires: pip install opencv-python pillow numpy
"""
import os
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = None


def main() -> None:
    out_dir, files = sys.argv[1], sys.argv[2:]
    os.makedirs(out_dir, exist_ok=True)
    casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    saved = []
    for f in files:
        try:
            pil = Image.open(f).convert("RGB")
        except Exception:
            continue
        sc = min(1.0, 1600 / max(pil.size))
        small = pil.resize((int(pil.width * sc), int(pil.height * sc))) if sc < 1 else pil
        g = cv2.cvtColor(np.array(small), cv2.COLOR_RGB2GRAY)
        for n, (x, y, w, h) in enumerate(casc.detectMultiScale(g, 1.08, 8, minSize=(70, 70))):
            x, y, w, h = (v / sc for v in (x, y, w, h))
            cx, cy, s = x + w / 2, y + h / 2 + h * 0.12, w * 2.3
            box = (int(cx - s / 2), int(cy - s / 2), int(cx + s / 2), int(cy + s / 2))
            if box[0] < 0 or box[1] < 0 or box[2] > pil.width or box[3] > pil.height:
                continue
            name = os.path.join(out_dir, os.path.splitext(os.path.basename(f))[0][:40] + f"-{n}.jpg")
            pil.crop(box).resize((640, 640), Image.LANCZOS).save(name, quality=92)
            saved.append(name)
    W, cols = 170, 10
    sheet = Image.new("RGB", (W * cols, W * max(1, (len(saved) + cols - 1) // cols)), "white")
    d = ImageDraw.Draw(sheet)
    for i, f in enumerate(saved):
        im = Image.open(f)
        im.thumbnail((W - 4, W - 4))
        sheet.paste(im, ((i % cols) * W + 2, (i // cols) * W + 2))
        d.text(((i % cols) * W + 6, (i // cols) * W + 6), str(i), fill="red")
    sheet.save(os.path.join(out_dir, "_sheet.png"))
    for i, f in enumerate(saved):
        print(i, f)


if __name__ == "__main__":
    main()
