"""Render a poster HTML to a full-page PNG with headless Chrome.

python shot.py <poster.html> [out.png]

The canvas size is auto-detected from the first CSS rule that sets both
width and height (the .poster/.slide root). Chrome captures the whole page at
--window-size, so a poster laid out at zoom<1 is captured at the size Chrome
reports back. Default output: <skills>/.shots/<name>.png
"""
import os
import re
import subprocess
import sys

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SKILLS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def detect(src):
    for m in re.finditer(r"\{([^{}]*)\}", src):
        body = m.group(1)
        w = re.search(r"(?<![-\w])width\s*:\s*(\d+)px", body)
        h = re.search(r"(?<![-\w])height\s*:\s*(\d+)px", body)
        if w and h and int(w.group(1)) >= 400 and int(h.group(1)) >= 400:
            return int(w.group(1)), int(h.group(1))
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    html_path = os.path.abspath(args[0])
    shot_dir = os.path.join(SKILLS, ".shots")
    os.makedirs(shot_dir, exist_ok=True)
    out = os.path.abspath(args[1]) if len(args) > 1 else os.path.join(shot_dir, os.path.splitext(os.path.basename(html_path))[0] + ".png")
    src = open(html_path, encoding="utf-8").read()
    size = detect(src) or (1080, 1350)
    if "--w" in flags:
        size = (int(flags[flags.index("--w") + 1]), size[1])
    if "--h" in flags:
        size = (size[0], int(flags[flags.index("--h") + 1]))
    w, h = size
    profile = os.path.join(shot_dir, "profile")
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
           "--no-sandbox", "--disable-crash-reporter", "--disable-breakpad",
           "--no-first-run", "--no-default-browser-check",
           f"--user-data-dir={profile}", "--force-device-scale-factor=1",
           "--virtual-time-budget=5000", "--allow-file-access-from-files",
           f"--window-size={w},{h}", f"--screenshot={out}",
           "file:///" + html_path.replace("\\", "/")]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if not os.path.exists(out):
        print("chrome failed", r.returncode)
        print((r.stderr or "")[-2000:])
        return 1
    try:
        from PIL import Image
        im = Image.open(out)
        print(f"canvas {w}x{h} -> {out} ({im.width}x{im.height})")
    except Exception:
        print(f"canvas {w}x{h} -> {out} ({os.path.getsize(out)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
