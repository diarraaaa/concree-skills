"""Crop a real logo out of a source poster and make its background transparent.

python crop_logo.py <source> x1,y1,x2,y2 <out.png> light|dark [scale=4] [lo] [hi]

light = paper/white background becomes transparent (logos on light slides)
dark  = near-black background becomes transparent (logos on dark slides)
lo/hi tune the transparency ramp (light default 205/238; dark default 55/95;
use e.g. dark 95 135 for a mid-dark green background).
"""
import sys

import numpy as np
from PIL import Image


def main() -> None:
    src, box, out, mode = sys.argv[1:5]
    scale = int(sys.argv[5]) if len(sys.argv) > 5 else 4
    lo_arg = float(sys.argv[6]) if len(sys.argv) > 6 else None
    hi_arg = float(sys.argv[7]) if len(sys.argv) > 7 else None
    x1, y1, x2, y2 = (int(v) for v in box.split(","))
    im = Image.open(src).convert("RGB").crop((x1, y1, x2, y2))
    im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
    px = np.array(im).astype(float)
    if mode == "light":
        lo, hi = lo_arg or 205, hi_arg or 238
        alpha = np.clip((hi - px.min(axis=2)) / (hi - lo), 0, 1)
    else:
        lo, hi = lo_arg or 55, hi_arg or 95
        alpha = np.clip((px.max(axis=2) - lo) / (hi - lo), 0, 1)
    rgba = np.dstack([px, alpha * 255]).astype("uint8")
    Image.fromarray(rgba, "RGBA").save(out)
    print(out, rgba.shape[1], "x", rgba.shape[0])


if __name__ == "__main__":
    main()
