# Poster render checklist

Read this before rendering the final poster. Fix every P0 failure in place;
do not ship a poster with an open P0.

## P0 — blocking

- [ ] Canvas size matches the chosen pattern exactly (1:1 2160×2160 or 4:5
      2160×2700 / 3240×4050) — not a stretched or resized variant.
- [ ] Every logo shown is the real mark for the program/partner named in
      this brief — never a redrawn, generic, or prior-program logo left
      over from the pattern's source example.
- [ ] Every photo is real (reused from the project or freshly sourced) and
      correctly depicts who/what it claims. No generated or stock
      stand-in for a named real person, speaker, or event.
- [ ] Photos and colors reflect **this brief's** program and subject, not a
      leftover copy-paste from the `examples/` reference file for the
      chosen pattern. A different brief must produce different imagery,
      not the same entrepreneur/innovation stock photo every time — unless
      the brief itself is genuinely about that same subject again.
- [ ] Every date, time, venue, name, role, partner, and QR destination is
      real and supplied by the brief — nothing invented or guessed.
- [ ] If the pattern calls for a QR code, it encodes the real registration
      URL — never a decorative/non-functional graphic.
- [ ] Accent color used no more than twice on the poster; it is the new
      event's real color (or CONCREE's site accent as fallback), not a
      leftover from a different program's palette.
- [ ] No text overlaps a photo's face or main subject; any overlay badge
      sits fully inside the image bounds with consistent inset spacing.
- [ ] Text fits its container with no clipping, overflow, or orphaned
      words on a final line.

- [ ] Every image zone shows a REAL photo (supplied, or fetched with
      `side-files/fetch_photo.py`) matching the theme — never an empty box, and
      never a photo used as the portrait of a named or fictional person.

- [ ] Design is layered and art-directed (gradient background + grain,
      hero photo as a masked transparent watermark, filigree motif/logo at
      5–10%, glows, glass cards) — not flat boxes on a flat color. See
      `build-lessons.md` §0.

- [ ] People photos: supplied photo, else mockup photos (free-licensed, face-
      cropped) with the visible tag `MAQUETTE · PHOTOS ILLUSTRATIVES` and
      fictional names — or an illustrated avatar. Credits recorded.

## P1 — should

- [ ] Zone layout (header lockup, headline block, body, photo treatment,
      footer partner strip) matches the chosen pattern file's structure.
- [ ] Body text ≥4.5:1 contrast against its background; large text/icons
      ≥3:1.
- [ ] Display headline follows the pattern's word/line limits rather than
      being shrunk to fit more copy.
- [ ] `data-od-id="kebab-case-id"` present on page regions, headline,
      CTAs, and repeated cards (speaker cards, credit-bar entries).
- [ ] Footer partner logos evenly spaced, consistent sizing, on one
      baseline.

## P2 — nice to have

- [ ] Restrained decorative accents (sparkle/diamond glyphs, subtle
      background texture) present where the pattern calls for them, not
      added elsewhere.
- [ ] Format-badge swap (e.g. Space vs. Webinaire) implemented as a single
      swappable element rather than a rebuilt section.
- [ ] Hover/focus states defined for any interactive element (links,
      buttons) if the poster will be viewed as a live HTML page rather
      than exported as a static image.

## P0 — added after the "CONCREE GPT" audit (see build-lessons.md §10)

- [ ] No pattern/model name and no process text on the canvas (MODÈLE · …, QR EXEMPLE, long disclaimers). Only one small MAQUETTE · PHOTOS ILLUSTRATIVES pill.
- [ ] « fictif » appears only after names/roles/venue, never in the headline or body copy.
- [ ] The programme's own logo is in the header; every logo is visible on its background (no white-on-white), the partner strip is centred, with no crop artefacts (black ticks, frame lines).
- [ ] Overlap and overflow audit done on the final render (pills, QR, captions); no word wrapped out of its box.
- [ ] Each face is used once in the delivery, under one fictional name.
- [ ] QR is real (side-files/qr.py) or absent — never a drawn imitation.
- [ ] The posters of one programme use different skeletons, not the same layout re-texted.
- [ ] Scratch/hidden frames removed from the Figma page; frames named « Programme — Sujet · Format ».