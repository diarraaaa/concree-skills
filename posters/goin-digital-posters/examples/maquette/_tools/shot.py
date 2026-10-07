"""Render a poster HTML to a PNG with headless Chrome (screenshot harness).

python shot.py <poster.html> <out.png> [--zoom 1] [--scale 1]

Differences from the reference `shot.py`:
* `--zoom` overrides the root `.poster{zoom}` for the capture only (the file on
  disk is untouched), so the shot comes out at the real 1080x1350 layout.
* The page chrome is neutralised (body padding/centering) so the poster starts
  at 0,0 and a full-page capture is exactly the poster.
* `_tools/fonts.css` (locally cached Sora / Open Sans woff2) is injected after
  the document's own styles so the screenshot uses the real typefaces even
  when Chrome has no network access.
"""
import os
import re
import subprocess
import sys

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
HERE = os.path.dirname(os.path.abspath(__file__))

FIX = ("<style id='shotfix'>html,body{margin:0!important;padding:0!important;"
       "gap:0!important;display:block!important;background:#000!important;"
       "overflow:hidden!important}.note{display:none!important}"
       "%(zoom)s</style>")


def main():
    argv = sys.argv[1:]
    args = [a for a in argv if not a.startswith("--")]
    def flag(name, default=None):
        if name in argv:
            return argv[argv.index(name) + 1]
        return default
    html_path = os.path.abspath(args[0])
    out = os.path.abspath(args[1]) if len(args) > 1 else os.path.join(HERE, "shot.png")
    zoom = flag("--zoom")
    scale = flag("--scale", "1")
    src = open(html_path, encoding="utf-8").read()
    m = re.search(r"\.poster\{[^}]*?width:\s*(\d+)px[^}]*?height:\s*(\d+)px", src)
    if not m:
        m = re.search(r"width:\s*(\d+)px[^}]*?height:\s*(\d+)px", src)
    w, h = (int(m.group(1)), int(m.group(2))) if m else (1080, 1350)

    head = "<head>"
    inject = ""
    fonts = os.path.join(HERE, "fonts.css")
    if os.path.exists(fonts):
        css = open(fonts, encoding="utf-8").read()
        inject += "<style id='shotfonts'>%s</style>" % css
    inject += FIX % {"zoom": (".poster{zoom:%s!important}" % zoom) if zoom else ""}
    mh = re.search(r"<head[^>]*>", src, re.I)
    src = src[:mh.end()] + inject + src[mh.end():]
    tmp = os.path.join(HERE, "_render.html")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(src)

    os.makedirs(os.path.dirname(out), exist_ok=True)
    profile = os.path.join(HERE, "_chrome-profile")
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
           "--no-sandbox", "--disable-crash-reporter", "--disable-breakpad",
           "--no-first-run", "--no-default-browser-check",
           "--user-data-dir=" + profile,
           "--force-device-scale-factor=" + scale,
           "--virtual-time-budget=8000",
           "--allow-file-access-from-files",
           "--window-size=%d,%d" % (w, h),
           "--screenshot=" + out,
           "file:///" + tmp.replace("\\", "/")]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if not os.path.exists(out):
        print("chrome failed rc=%s" % r.returncode)
        print((r.stderr or "")[-2000:])
        return 1
    try:
        from PIL import Image
        im = Image.open(out)
        print("canvas %dx%d -> %s (%dx%d)" % (w, h, out, im.width, im.height))
    except Exception:
        print("canvas %dx%d -> %s (%d bytes)" % (w, h, out, os.path.getsize(out)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
