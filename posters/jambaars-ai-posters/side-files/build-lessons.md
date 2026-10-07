# Build lessons — read before building any poster (saves the iteration loop)

These come from building the Idea Lab carousel / spotlight / dossier preview
(`examples/06a-idea-lab-cover-pro.html (+ 06b topic, 06c spotlight, 06d dossier)`). Following them gets
a complete, clean result on the first pass.

## 0. Design PRO, not a basic copy-paste (applies to every poster)

A poster must look art-directed. Stacking logo + photo + text in flat boxes is
a failure. Build these layers, back to front (reference:
`yeah-posters/examples/07-yeah-space-pro.html`):

1. **Atmospheric background:** layered radial + linear gradients from the
   program palette (never one flat color), plus a fine grain overlay
   (`mix-blend-mode:overlay`, 15–20%).
2. **Hero photo as a transparent watermark:** the real photo of the theme is
   NOT pasted as a rectangle. Use it full-bleed behind the content at
   35–55% opacity with `mix-blend-mode:luminosity` (or multiply), a
   `mask-image` radial/linear fade so its edges dissolve, and a gradient tint
   in the brand color on top. Text stays fully readable over it.
3. **Filigranes (watermarks):** a repeated motif tied to the theme (leaves,
   dots, geometric shapes) at 6–10% opacity, and the program logo enlarged,
   rotated and at ~5% opacity in a corner. Subtle: you notice them only when
   you look for them.
4. **Light:** 1–2 blurred radial glows (brand accent) behind the main subject
   to create depth.
5. **Glass cards:** secondary info (speakers, details) sits in translucent
   cards — `backdrop-filter:blur`, 1.5px translucent border, soft shadow,
   inner top highlight.
6. **Typography:** a display font for headlines (e.g. Fredoka / program
   font), gradient-filled hero word with a layered drop-shadow, small
   uppercase tracked labels (e.g. "THÈME ——"), strong size hierarchy.
7. **Icon chips:** date/time/place get line icons inside rounded gradient
   chips, not bare emojis.
8. **Subjects with presence:** circular portraits/avatars with a gradient
   ring and glow, name in an overlapping pill.
9. **Clean footer:** partners on a white rounded bar with a shadow cast
   upward; clip crop edges (`clip-path:inset`) to hide scan artifacts.

Always check contrast on the watermarked areas and view the render.

## 1. Deliver a COMPLETE result the first time

The user wants logos, real photos and real structure in the first render —
never gray boxes, `{{placeholders}}` where a real asset exists, or "logo here"
labels. Placeholders are only for content the brief genuinely lacks (a name,
a date, a figure). Logos and images are always filled in.

## 2. Logos: crop the real ones, never redraw

- Real marks live inside the source posters (`references/source-posters/`)
  and in `assets/`. Check `assets/` first; it already holds: `concree-logo.svg`
  (light backgrounds), `logo-concree-dark.png` (dark backgrounds),
  `logo-idealab.png`, `logo-mesri.png`, `logo-koica.png`, `logo-kpc.png`,
  `funders-expertise-giz.png`, `partners-cover-strip.png`,
  `partners-spotlight-strip.png`.
- For a missing logo, crop it from a source poster with
  `side-files/crop_logo.py` (upscales 4x, makes the paper/dark background
  transparent so no gray box shows). Usage:
  `python side-files/crop_logo.py <source.png> x1,y1,x2,y2 <assets/out.png> light|dark`
  Open the result with the Read tool to confirm it is clean before using it.
- Never recolor, redraw or approximate a real partner mark. If no real mark
  exists, ask the user for the file; do not invent a logo.
- Source posters are 700px, so small logos are soft. Say so in the delivery
  message and offer to swap in original files.
- Choose the partner set for the right program/background: light strip for
  light slides, `partners-spotlight-strip.png` on a WHITE bar for dark cards.

## 3. Images: REAL photos by default, never leave a zone empty

Priority order for every image zone (cover circle, topic photo, hero photo):
1. **Photo supplied by the user / project** (their folder, the CONCREE site
   photo `assets/example-photo-innovation.png`, source posters).
2. **No photo supplied → fetch a real, freely-licensed photo that matches the
   subject.** Run
   `python side-files/fetch_photo.py "<short English keywords>" assets/photos 4 [landscape|portrait|square|any]`
   (Wikimedia Commons; CC0 / public domain / CC BY / CC BY-SA only). Tips:
   - Use SHORT keywords (2–3 words, English: "Senegal agriculture",
     "Senegal women farmers"). Long queries return nothing.
   - Run 2–4 queries, build a contact sheet (PIL thumbnails) and LOOK at
     every candidate. File titles lie (a "farmers" hit can be a coffee shop).
     Keep only photos that truly show the theme, sharp, uncluttered, with
     room for the text card.
   - Copy kept files to descriptive names in `assets/photos/` and delete the
     rest; keep `credits.json` in sync.
   - Credit: CC BY / CC BY-SA require attribution on publication. List the
     photo credits in the delivery message and keep `credits.json`.
3. Only if nothing suitable exists after 3+ queries: flat SVG illustration
   (varied people, objects, 3–5 palette colors), and say so.

Identity rules (non-negotiable):
- A real photo may illustrate a THEME, scene or ambiance (field, seedling,
  market, meeting). It must NEVER be shown as the portrait of a named person,
  real or fictional — for a fictional speaker/founder/laureate use an
  illustrated avatar or initials, labeled as example.
- A photo of an identifiable stranger used as ambiance must not carry a
  caption naming anyone.
- Keep the pattern's shape signal: circle crop on a cover, rounded-right
  rectangle on topic slides, hard rectangle on spotlight; set
  `object-position` so the subject is not cut and not hidden by cards.


### People (speakers, panelists, founders)

1. **Supplied photo:** always preferred (face-centered crop in the pattern's frame).
2. **No photo supplied, user wants to SEE the rendering (mockup):** use
   free-licensed photos of people from Wikimedia Commons — public figures are
   fine for a mockup — and ALWAYS add a visible tag on the poster
   (`MAQUETTE · PHOTOS ILLUSTRATIVES`), keep the names/roles fictional, and
   say in the delivery message that these are placeholders to replace before
   any publication.
   - Fetch: `fetch_photo.py "cat:<Commons category of the person>" <dir> 4 any 700`
     (categories of named public figures work; free-text "portrait" searches
     return old/PD portraits; "unidentified people" categories are not
     professional portraits).
   - Crop: `crop_faces.py <out_dir> <photos...>` then LOOK at `_sheet.png`;
     pick sharp front-facing faces, drop false positives (clothes, posters).
   - Keep the chosen crops in `assets/people/` with `credits.json`
     (author + license). Mix genders/ages to fit each role.
3. **No photo and no mockup request:** illustrated avatar (flat SVG bust with
   ring/glow), labeled "(personnage fictif)".
- Never pair a real person's photo with a *real* different identity or claim
  an endorsement; fictional names + maquette tag only.

## 4. Layout pitfalls already hit (check each)

- Footer partner strip must sit on the plain background BELOW the
  illustration. Reserve ~130px (1080 canvas) and shrink the circle/photo
  instead of letting the strip overlap it.
- On dark cards the partner strip goes on a white bar of ≥170px, with logos
  ≥140px tall, or they become unreadable specks.
- Text cards must not cover the main subject of the photo/illustration; a
  small edge overlap is the pattern, covering faces/objects is a bug.
- Accent triangles must be fully visible — never tucked behind a card or
  colliding with a headline line.
- Logo crops with opaque backgrounds show a visible box on textured paper;
  always use the transparent crops from `crop_logo.py`.
- Add a short fade on an illustration's edge where it meets a flat dark
  background, to avoid a hard vertical seam.

## 5. Verify visually before telling the user it is done

Render and LOOK at it; do not trust the code.

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --hide-scrollbars --window-size=1800,2700 "--screenshot=$env:TEMP\prev.png" "file:///<path>/file.html"
```

Then Read the PNG and fix: overlaps, clipped text, missing logos, boxes
around logos, tiny partner strips. Re-render once after fixes. Finally open
the HTML in the user's browser (`Start-Process <path>`).

## 6. Figma path

If the Figma MCP answers "tool call limit on the Starter plan", stop trying:
every call (read or write) is blocked. Deliver the HTML preview, say the
Figma push is pending, and do not spend further calls. Call `get_metadata`
once at the start of a Figma task to learn whether you are blocked.

## 7. Delivery message

French when the user writes French. Say: file path, what each page shows,
which content is fictional, logo sharpness caveat, and what is pending
(Figma). Keep it short.

## 8. Deliverable: ONE simple file, 3 posters per program

- For each program produce **3 posters, one per event type**, each with a
  clearly different display (layout, palette mood, composition) — not three
  recolors of the same template:
  - Idea Lab: appel à candidatures (cover) · slide thématique · spotlight startup
  - YEAH: Space sur X · webinaire (grille de visio) · atelier présentiel (photo diagonale, clair)
  - Goin'Digital: panel 1 intervenant (arche) · panel multi-intervenants (modératrice + 4) · atelier (fond citron)
  - JAMBAARS AI: demo day (annonce) · intervenants (cadres courbes) · invitation formelle (2:3, lettre)
- Show them in ONE html file, kept simple: program name as heading, the 3
  posters side by side with only the event type as caption, click = full screen
  (←/→/Esc). **No explanatory text, no hero, no rules, no credits table in
  the file** (credits stay in `assets/**/credits.json` and in the chat reply).
- Build with `side-files/build_presentation.py` (inlines images as base64);
  edit its `SECTIONS` list, run it, open `Desktop/Affiches-CONCREE.html`.
- Poster files live in each skill's `examples/` (`NN-<program>-<type>-pro.html`).


## §9 Designs REJETES par l'utilisateur : a ne pas reproduire

Exemples deplaces dans `examples/_a-ne-pas-reproduire/`. Ne jamais s'en servir comme base.

- **YEAH Atelier** (fond creme + bandeau photo en haut + gros titre sur la photo + deux cartes info + pastille facilitateur + vide a droite) : mise en page "gabarit" plate, zones vides, hierarchie faible. Meme la version refaite en arche + etapes n'a pas convaincu : eviter le schema "photo + titre + liste d'etapes + carte facilitateur" pour un atelier, chercher une composition vraiment differente.
- **Goin'Digital Atelier** (fond lime plat + gros mot ATELIER + photo inclinee + 3 cartes navy + QR) : bloc lime uni, texte trop uniforme, photo petite, aspect "template". A ne pas refaire, y compris avec la photo d'atelier et les etapes 01/02/03.
- Regle generale : si deux iterations d'un meme squelette sont refusees, changer de squelette (pas de retouche de details), et ne pas mettre l'affiche dans la presentation tant qu'elle n'est pas validee.
- Bug a eviter : un selecteur generique `.parent div{...}` ecrase les classes des enfants (cadre photo cache par une etiquette). Nommer chaque bloc.


## §10 Faults found in an audit of 8 posters made by another model ("CONCREE GPT" file) — never repeat

Source: Figma file `9yKwIpG0J3NcKq9dZKfTUj`, page "Affiches fictives — CONCREE GPT" (Goin'Digital ×2, Idea Lab ×2, Jambaars AI ×2, YEAH ×2). The user judged them "pas bons". Each fault below breaks a rule already written in this skill; the **Instead** line is the fix. Applies to every program.

### A. Process text leaked onto the poster (worst, most visible)
- Header lines such as `GO IN' DIGITAL · MODÈLE · PANEL ANNOUNCEMENT`, `MODÈLE · PANEL LINEUP GRID`, `MODÈLE · STARTUP SPOTLIGHT`, `MODÈLE · FORMAL INVITATION`, and QR captions like `QR EXEMPLE NON FONCTIONNEL` / `QR NON FONCTIONNEL`. Pattern names are build vocabulary, not poster copy.
- A long disclaimer line in a low-contrast colour (`MAQUETTE FICTIVE · PHOTOS DE PERSONNES RÉELLES · PARTENAIRES ILLUSTRATIFS`, yellow on beige, orange on green).
- The word « fictif/fictive » sprinkled through the real copy: « Un parcours fictif… », « Hub numérique fictif », « projets fictifs », « Quatre voix fictives », « chiffre fictif », « Appel fictif », « Édition fictive ».
- **Instead:** the poster carries ONE small pill `MAQUETTE · PHOTOS ILLUSTRATIVES` (red/accent, ≥14px, contrast ≥4.5:1, same spot on every poster). Fictional is marked only as « (fictif) » after a name/role/venue, at most once per item. Headlines, subtitles and body copy read as if the event were real. The pattern/model name goes in the Figma frame name or the delivery message, never on the canvas.

### B. Not art-directed (breaks §0)
- Flat navy / green / beige backgrounds with one ghosted photo at ~20% and no grain, glow, filigree, glass card or gradient headline. Result: "template" look, big dead areas.
- The hero photo is either dimmed into mud (Goin' panel portrait, Idea Lab farmer, YEAH cashew-apple background) or pasted as a hard rectangle on a ghost copy of itself (Jambaars demo day: a dull phone snapshot of a classroom).
- **Instead:** follow the §0 stack. One strong, sharp subject (circle, arch or masked cut-out) with a ring and glow; the background is atmosphere, not the subject. If the only photo available is weak (low-res, cluttered, phone snapshot), do not make it the hero: crop to a detail, use an illustration, or pick another photo with `fetch_photo.py`.

### C. Logos and the partner strip
- The programme's own logo is missing: Goin' Digital posters show only CONCREE; Idea Lab shows CONCREE + Idea Lab on the cover. **Instead:** the programme logo leads the header; CONCREE appears as an organiser/partner, once.
- White-on-white logos, invisible: Consortium Jeunesse Sénégal and Mastercard Foundation sit in white boxes with white lettering. **Instead:** use the dark/white variant that matches the background, or no box.
- Crop artefacts shipped: thin black frame lines around the Expertise France + giz logos, black corner ticks at the top of the YEAH partner strip. They come from the source crop, and `clip-path:inset` does not survive the Figma capture. **Instead:** crop the asset itself (`crop_logo.py`) and look at it at 100% before using it; never rely on `clip-path` to hide scan edges in anything bound for Figma.
- Two logos left of centre in a huge white bar (right half empty); the same partner set shown twice on one poster (Idea Lab cover: small white card AND footer strip); ministry logo a few pixels wide next to a giant KOICA. **Instead:** one strip, logos centred on one baseline with equal visual weight (normalise heights), bar height fitted to the logos (§4).
- Invitation: partner strip clipped on the right by a decorative corner shape. **Instead:** decoration never touches the logo zone.

### D. Text and element collisions
- A label overflowing its pill: « Marième Fall / Modératrice · / fictive » with « fictive » falling out below the orange box. **Instead:** size pills to the longest line (hug), shorten the role (« Modératrice »), `white-space:nowrap`.
- The QR block sits on top of the third speaker card (Goin' line-up) and on the date line. **Instead:** a fixed footer row reserved for date + QR; check bounding boxes.
- A caption box straddling a photo edge and overlapping the info card (Goin' portrait caption).
- **Instead (all):** after the render, run an overlap audit on the actual canvas (every text node's bounds against every other and against the frame) and fix before telling the user it is done (§5). In Figma, set `textAutoResize = 'WIDTH_AND_HEIGHT'` / hug on short labels so they never wrap.

### E. Fake or wrong functional elements
- A hand-drawn "QR" made of three squares. A decorative QR is forbidden by the checklist. **Instead:** generate a real one (`side-files/qr.py`) for a real or clearly placeholder URL and say which; if no URL exists, leave the QR out and write the registration instruction in words.
- The letter-style invitation has no signature, no reply instruction, no date/venue emphasis and no RSVP; the body is four equal paragraphs. **Instead:** date/time/venue stand out as a block, one action (« Confirmer votre présence » + contact or QR), signatory name and role.

### F. People and photos
- One face under two identities across the file: the same woman is « Awa Ndiaye » (moderator, Goin') and « Marième Fall » (moderator, YEAH); the shopkeeper is « Fatou Ba », « Ndeye Ba, fondatrice Teranga BioLab » and « Aïssatou Sarr ». **Instead:** one photo = one fictional identity for the whole delivery; keep a small table photo → name and check it.
- A real photo of a shopkeeper presented as the portrait of a startup founder whose name is invented, with the caption « Portrait réel · visuel d'illustration » in a white block. **Instead:** apply the identity rules of §3; a theme photo must not carry a founder's name (use an avatar) or the mockup tag must be visible and the name fictional.
- Speaker photos as unequal rectangles at different heights, floating at the right with big empty space left of them (YEAH). **Instead:** circle portraits of the same size on a clear grid, moderator distinguished by a ring.

### G. Layout and hierarchy
- Half-empty canvases: YEAH webinar/Space have a headline of ~40px top-left, nothing under it, speakers on the right, a date box floating mid-left, a cashew thumbnail orphaned bottom-left, and an orange bar that merely repeats the three names already shown on the cards. **Instead:** the headline is the hero (≥ 90px on a 1080 canvas), every zone has a job, and nothing is repeated.
- Display type: handwriting-style italic yellow script for the YEAH headline instead of the display font (Fredoka). **Instead:** programme display font, size hierarchy 3:1 between headline and body.
- Accent colour overused: yellow in 8+ places on Goin', orange for bar + pills + labels on YEAH. Checklist: no more than twice. **Instead:** one accent for the hero word and one for the call to action; everything else white or tints.
- Idea Lab cover: the "partners" card, a "Mentorat · prototypage / Expérimentation terrain" card and the footer compete; the headline is on top of the busiest part of the photo. Jambaars demo day: a heavy orange band cuts the poster in two and the photo is a flat rectangle. **Instead:** one block of secondary info; the band/card never splits the subject.
- Redundant header on every poster (`GO IN' DIGITAL` + blank space + disclaimer) that pushes the content down and leaves the header unbalanced. **Instead:** logos row, then one pill, then the headline.

### H. Same skeleton twice
- The two YEAH posters (webinaire and Space) are the same layout with the text swapped, on the same blurred cashew background. Rule already written: three clearly different compositions per programme. **Instead:** different composition, background and focal point per event type (see `examples/orange/` for three distinct ones).

### I. Deliverable hygiene (Figma)
- Twelve hidden "Asset original — masqué" frames left at the top of the page; frames named after the template (`… · modèle panel-lineup-grid`). **Instead:** delete scratch frames; name frames « Programme — Sujet · Format ».
- Mixed canvas sizes without reason (3240×4050, 2160×2160, 1080×1350, 600×900 in one file). **Instead:** state the size per format once; keep each at the pattern's size.
- Contrast: yellow or orange small caps on beige or green, grey logos on photos. **Instead:** measure ≥4.5:1 for text under 24px.

### J. Self-check before saying "done" (the audit that was skipped)
1. Open the frame at 100% and read every line aloud: no pattern names, no process words.
2. Count « fictif » on the canvas: only on names/roles/venue, never in headline or body.
3. Overlap and overflow audit on all text nodes; no word broken by wrapping.
4. Logos visible on their background, centred strip, no black ticks or frame lines.
5. Each face appears once in the file, under one name.
6. Any QR is real and scannable, or absent.
7. Compare the three posters of the programme side by side: three different skeletons.
