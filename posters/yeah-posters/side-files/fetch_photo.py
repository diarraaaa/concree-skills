"""Download real, freely-licensed illustrative photos from Wikimedia Commons.

python fetch_photo.py "<search terms>|cat:<Commons category>" <out_dir> [count=4] [orientation=any|landscape|portrait|square] [min_px=1200]

Use "cat:Men of Senegal in the 2020s" to pull files from a Commons category
(better for people portraits than free-text search). Retries on HTTP 429.

Saves JPEGs (1600px wide max) and appends attribution to <out_dir>/credits.json.
Only keeps CC0 / public domain / CC BY / CC BY-SA files >= 1200px on the long side.
Look at every downloaded image (Read tool) before using it: it must really show
the subject of the brief. Use for theme/ambiance imagery only, never as the
portrait of a named (or fictional) person.
"""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA = "poster-skill/1.0 (illustrative photo fetch)"
OK = re.compile(r"^(cc0|public domain|pd|cc[- ]by(?:[- ]sa)?|attribution)", re.I)


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code != 429 or attempt == 4:
                raise
            time.sleep(15 * (attempt + 1))


def strip(html: str) -> str:
    return re.sub(r"<[^>]+>", "", html or "").strip()


def main() -> None:
    query, out_dir = sys.argv[1], sys.argv[2]
    count = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    orient = sys.argv[4] if len(sys.argv) > 4 else "any"
    min_px = int(sys.argv[5]) if len(sys.argv) > 5 else 1200
    os.makedirs(out_dir, exist_ok=True)
    params = {"action": "query", "format": "json", "prop": "imageinfo",
              "iiprop": "url|size|mime|extmetadata", "iiurlwidth": "1600"}
    if query.startswith("cat:"):
        params.update({"generator": "categorymembers", "gcmtitle": "Category:" + query[4:],
                       "gcmtype": "file", "gcmlimit": "60"})
    else:
        params.update({"generator": "search", "gsrnamespace": "6", "gsrsearch": query, "gsrlimit": "30"})
    data = json.loads(get(API + "?" + urllib.parse.urlencode(params)))
    pages = sorted(data.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 0))
    credits_path = os.path.join(out_dir, "credits.json")
    credits = json.load(open(credits_path, encoding="utf-8")) if os.path.exists(credits_path) else []
    saved = 0
    for p in pages:
        if saved >= count:
            break
        i = p["imageinfo"][0]
        meta = i.get("extmetadata", {})
        lic = meta.get("LicenseShortName", {}).get("value", "")
        w, h = i["width"], i["height"]
        if i["mime"] not in ("image/jpeg", "image/png") or not OK.match(lic) or max(w, h) < min_px:
            continue
        ratio = w / h
        if (orient == "landscape" and ratio < 1.2) or (orient == "portrait" and ratio > 0.85) or (orient == "square" and not 0.85 <= ratio <= 1.2):
            continue
        name = re.sub(r"[^A-Za-z0-9]+", "-", p["title"].replace("File:", ""))[:40].strip("-").lower()
        path = os.path.join(out_dir, f"{name}-{p['pageid']}.jpg")
        try:
            data = get(i.get("thumburl") or i["url"])
        except Exception as e:  # skip a failed download, keep going
            print("skip", p["title"], e)
            continue
        with open(path, "wb") as f:
            f.write(data)
        time.sleep(1.5)
        credits.append({
            "file": os.path.basename(path), "title": p["title"], "license": lic,
            "author": strip(meta.get("Artist", {}).get("value", "")),
            "source": i.get("descriptionurl"),
        })
        print(path, f"{w}x{h}", lic)
        saved += 1
    json.dump(credits, open(credits_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if not saved:
        print("No suitable photo found: try other keywords (English works best).")


if __name__ == "__main__":
    main()
