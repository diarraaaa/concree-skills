"""Download the Sora + Open Sans woff2 subsets used by the posters and cache them.

Writes fonts.css next to this script with @font-face rules pointing at local
woff2 files, so a screenshot renders with the real typefaces even when Chrome
has no network access. The published HTML keeps its Google Fonts <link>; only
the screenshot harness injects fonts.css.
"""
import os
import re
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CSS_URL = ("https://fonts.googleapis.com/css2?"
           "family=Sora:wght@400;600;700;800&family=Open+Sans:wght@400;600;700&display=swap")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main():
    css = get(CSS_URL).decode("utf-8")
    out = []
    n = 0
    for block in re.findall(r"@font-face\s*\{[^}]*\}", css):
        m = re.search(r"url\((https://[^)]+\.woff2)\)", block)
        if not m:
            continue
        url = m.group(1)
        fam = re.search(r"font-family:\s*'([^']+)'", block).group(1)
        wt = re.search(r"font-weight:\s*(\d+)", block).group(1)
        rng = re.search(r"unicode-range:\s*([^;]+);", block)
        rng = rng.group(1).strip() if rng else None
        # keep only latin / latin-ext subsets -> small cache
        if rng and not any(ch in rng for ch in ("U+0000-00FF", "U+0100-02BA")):
            continue
        name = "%s-%s-%d.woff2" % (fam.lower().replace(" ", ""), wt, n)
        n += 1
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            with open(path, "wb") as f:
                f.write(get(url))
        loc = re.search(r"local\('([^']+)'\)", block)
        new = ("@font-face{font-family:'%s';font-style:normal;font-weight:%s;"
               "font-display:swap;src:url('%s') format('woff2');%s}"
               % (fam, wt, name, ("unicode-range:" + rng + ";") if rng else ""))
        out.append(new)
    with open(os.path.join(HERE, "fonts.css"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("wrote fonts.css with %d faces" % len(out))


if __name__ == "__main__":
    main()
