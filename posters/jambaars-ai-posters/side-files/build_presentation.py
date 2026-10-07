"""Build ONE simple self-contained HTML file from the poster examples.

python build_presentation.py [out.html]

One section per program (name only), 3 posters per program (one per event
type), click a poster for full-screen (arrows / Esc). Images are inlined as
base64 so the file works anywhere (Google Fonts still need internet).
Edit SECTIONS to add or change posters. Default output: Desktop/Affiches-CONCREE.html
"""
import base64
import html
import io
import os
import re
import sys

from PIL import Image

SK = os.path.join(os.path.expanduser("~"), ".claude", "skills")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.expanduser("~"), "Desktop", "Affiches-CONCREE.html")

SECTIONS = [
    {"title": "Idea Lab", "frames": [
        ("Appel à candidatures", "idea-lab-posters/examples/06a-idea-lab-cover-pro.html", 1080, 1080),
        ("Slide thématique", "idea-lab-posters/examples/06b-idea-lab-topic-pro.html", 1080, 1080),
        ("Spotlight startup", "idea-lab-posters/examples/06c-idea-lab-spotlight-pro.html", 1080, 1080)]},
    {"title": "YEAH", "frames": [
        ("Space sur X", "yeah-posters/examples/07-yeah-space-pro.html", 1080, 1350),
        ("Webinaire", "yeah-posters/examples/10-yeah-webinaire-pro.html", 1080, 1350)]},
    {"title": "Goin'Digital", "frames": [
        ("Panel", "goin-digital-posters/examples/08-goin-digital-panel-pro.html", 1080, 1350),
        ("Panel multi-intervenants", "goin-digital-posters/examples/12-goin-digital-lineup-pro.html", 1080, 1350)]},
    {"title": "JAMBAARS AI", "frames": [
        ("Demo Day", "jambaars-ai-posters/examples/09-jambaars-demo-day-pro.html", 1080, 1080),
        ("Intervenants", "jambaars-ai-posters/examples/14-jambaars-intervenants-pro.html", 1080, 1080),
        ("Invitation", "jambaars-ai-posters/examples/15-jambaars-invitation-pro.html", 1080, 1620)]},
]

_cache = {}


def data_uri(path):
    if path in _cache:
        return _cache[path]
    ext = os.path.splitext(path)[1].lower()
    if ext in (".jpg", ".jpeg"):
        im = Image.open(path).convert("RGB")
        im.thumbnail((1500, 1500))
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=82)
        raw, mime = buf.getvalue(), "image/jpeg"
    elif ext == ".png":
        im = Image.open(path)
        if im.width > 1700:
            im = im.resize((1700, int(im.height * 1700 / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "PNG", optimize=True)
        raw, mime = buf.getvalue(), "image/png"
    else:
        raw, mime = open(path, "rb").read(), "image/svg+xml" if ext == ".svg" else "application/octet-stream"
    uri = f"data:{mime};base64," + base64.b64encode(raw).decode()
    _cache[path] = uri
    return uri


def inline(doc, base_dir):
    def sub_attr(m):
        p = os.path.normpath(os.path.join(base_dir, m.group(2)))
        return f'{m.group(1)}"{data_uri(p)}"' if os.path.exists(p) else m.group(0)

    def sub_url(m):
        p = os.path.normpath(os.path.join(base_dir, m.group(1)))
        return f"url({data_uri(p)})" if os.path.exists(p) else m.group(0)

    doc = re.sub(r'(src=)"(\.\./[^"]+)"', sub_attr, doc)
    doc = re.sub(r"url\((\.\./[^)\"']+)\)", sub_url, doc)
    doc = re.sub(r'<p class="note">.*?</p>', "", doc, flags=re.S)
    override = ("<style>html,body{margin:0!important;padding:0!important;background:transparent!important;display:block!important}"
                ".poster,.slide{zoom:1!important;box-shadow:none!important;margin:0!important}</style>")
    return doc.replace("</head>", override + "</head>", 1)


def frame_html(label, rel, w, h):
    path = os.path.join(SK, rel)
    doc = inline(open(path, encoding="utf-8").read(), os.path.dirname(path))
    return (f'<figure class="frame" data-w="{w}" data-h="{h}"><div class="stage">'
            f'<iframe loading="lazy" scrolling="no" width="{w}" height="{h}" srcdoc="{html.escape(doc, quote=True)}" '
            f'title="{html.escape(label)}"></iframe></div><figcaption>{html.escape(label)}</figcaption></figure>')


PAGE = """<!doctype html><html lang="fr"><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Affiches CONCREE</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{background:#101318;color:#eef1f4;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;padding:32px clamp(12px,3vw,40px) 64px}
section{max-width:1500px;margin:0 auto 56px}
h2{font-size:28px;font-weight:700;margin-bottom:18px;letter-spacing:-.5px}
.frames{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px;align-items:start}
.frame{margin:0}
.stage{position:relative;overflow:hidden;border-radius:10px;box-shadow:0 14px 36px rgba(0,0,0,.5);cursor:zoom-in}
.stage iframe{border:0;display:block;transform-origin:0 0;background:#fff;pointer-events:none}
figcaption{margin-top:8px;font-size:14px;color:#9aa4b2}
#lb{position:fixed;inset:0;z-index:50;background:rgba(5,7,10,.95);display:none;align-items:center;justify-content:center}
#lb.on{display:flex}#lb .box{position:relative;overflow:hidden;border-radius:8px}
#lb iframe{border:0;display:block;transform-origin:0 0;background:#fff}
#lb button{position:fixed;background:rgba(255,255,255,.14);color:#fff;border:0;border-radius:50%;width:46px;height:46px;font-size:22px;cursor:pointer}
#lb .x{top:14px;right:14px}#lb .pv{left:14px;top:50%}#lb .nx{right:14px;top:50%}
@media(max-width:900px){.frames{grid-template-columns:1fr}}
</style></head><body>
__SECTIONS__
<div id="lb"><div class="box"><iframe scrolling="no"></iframe></div><button class="x" aria-label="Fermer">&times;</button><button class="pv" aria-label="Précédent">&lsaquo;</button><button class="nx" aria-label="Suivant">&rsaquo;</button></div>
<script>
const frames=[...document.querySelectorAll('.frame')];
function fit(){frames.forEach(f=>{const w=+f.dataset.w,h=+f.dataset.h,ifr=f.querySelector('iframe'),st=f.querySelector('.stage');
  const s=f.getBoundingClientRect().width/w;ifr.style.transform='scale('+s+')';st.style.height=(h*s)+'px';});}
fit();addEventListener('resize',fit);
const lb=document.getElementById('lb'),lbf=lb.querySelector('iframe'),box=lb.querySelector('.box');let cur=0;
function show(i){cur=(i+frames.length)%frames.length;const f=frames[cur],w=+f.dataset.w,h=+f.dataset.h;
  lbf.srcdoc=f.querySelector('iframe').srcdoc;lbf.width=w;lbf.height=h;
  const s=Math.min((innerWidth-110)/w,(innerHeight-40)/h);lbf.style.transform='scale('+s+')';box.style.width=(w*s)+'px';box.style.height=(h*s)+'px';lb.classList.add('on');}
frames.forEach((f,i)=>f.querySelector('.stage').addEventListener('click',()=>show(i)));
lb.querySelector('.x').onclick=()=>lb.classList.remove('on');lb.querySelector('.pv').onclick=()=>show(cur-1);lb.querySelector('.nx').onclick=()=>show(cur+1);
lb.addEventListener('click',e=>{if(e.target===lb)lb.classList.remove('on')});
addEventListener('keydown',e=>{if(!lb.classList.contains('on'))return;if(e.key==='Escape')lb.classList.remove('on');if(e.key==='ArrowRight')show(cur+1);if(e.key==='ArrowLeft')show(cur-1);});
</script></body></html>"""


def main():
    secs = []
    for s in SECTIONS:
        frames = "".join(frame_html(*f) for f in s["frames"])
        secs.append(f'<section><h2>{html.escape(s["title"])}</h2><div class="frames">{frames}</div></section>')
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(PAGE.replace("__SECTIONS__", "".join(secs)))
    print(OUT, round(os.path.getsize(OUT) / 1e6, 1), "MB")


if __name__ == "__main__":
    main()
