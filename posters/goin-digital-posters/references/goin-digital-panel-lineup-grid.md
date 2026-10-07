---
name: Goin' Digital — Panel lineup grid with QR
description: Portrait poster announcing a Goin' Digital panel session with a moderator plus a grid of multiple named panelists (not one single featured photo), a registration QR code, and the same dark editorial background as the single-panelist variant.
based_on:
  - Idea Lab figma file "IDEA LAB" (figma.com/design/QiEzqqxt6esRZxLCZpAjkR), frame "Goin Digital - VISUEL INTERVENANTES"
canvas: 1080x1350px (4:5 portrait — Instagram portrait post)
---

# Goin' Digital — Panel lineup grid with QR

## When to use
This is a **layout/style reference**, not a recurring-program recipe: the
"Femmes leaders et technologies" panel it was measured from is one specific
session and will not recur. Reach for this file whenever a brief needs to
announce a panel with a **moderator plus several named panelists shown
together** (3–4 observed) alongside a registration QR code — this is the
multi-person counterpart to `goin-digital-panel-announcement.md`, which is
for exactly **one** featured panelist photo. If the brief names only one
speaker, use that file instead; if it names a moderator plus a lineup, use
this one.

## Adapting this template to a new, unrelated event
1. Swap `{{concree_logo}}` co-branding logos, the program wordmark, and the
   accent color for the *new* event's real partners and palette — don't
   default back to "Goin'Digital" or its yellow/lime accent unless the new
   brief is genuinely another Goin' Digital session.
2. Keep the compositional bones (moderator photo on top + panelist photo
   row below + QR registration block + footer) only as far as they fit; if
   the brief has only 2 panelists, keep the row evenly spaced rather than
   stretching photos to fill 4 slots.
3. Re-derive the palette from the new event's own sourced material instead
   of reusing this file's yellow/navy read.
4. Every value in **Content slots** below must come from the new event's
   real, confirmed people — never invent a panelist name or title.

## Canvas & background
- 4:5 portrait, 1080×1350px.
- Solid dark navy-to-black background — same flat, texture-free, editorial
  feel as `goin-digital-panel-announcement.md`; the two templates share one
  visual system and are meant to be recognizable as the same program.

## Zones (top to bottom)
1. **Header lockup** (top band): CONCREE logo top-left on a small white
   rounded card; funder/partner logos (e.g. Expertise France, GIZ) top-right,
   each on their own compact white card.
2. **Program wordmark + session badge** (below header, left-aligned):
   "Goin'Digital" wordmark (mixed yellow/white) above a small pill-outline
   badge naming the format (e.g. "PANEL").
3. **Session headline** (below the badge, left-aligned, full width): a bold
   white multi-line headline stating the session topic, sentence case, with
   at most one key phrase in the yellow accent color.
4. **Moderator photo + tag** (centered, below the headline): one circular
   headshot photo of the moderator, smaller than the panelist photos below
   it, paired with a solid yellow rounded-rectangle name tag directly under
   the circle holding "Modératrice"/"Modérateur" (small label) + full name
   (bold) + role (regular, 1 line).
5. **Panelist photo row** (below the moderator, full width, evenly spaced
   horizontally): 3–4 circular headshot photos in one row, each sized
   smaller than the moderator's, each paired with its own solid yellow
   rounded-rectangle name tag directly beneath it holding "Panéliste"
   (small label) + full name (bold) + title/affiliation (regular, wraps to
   2 lines max). All circles sit on one shared baseline.
6. **Event details row** (below the photo grid, left-aligned, stacked): the
   event date (bold, yellow numeral/date string), venue line with a small
   yellow pin icon, and time line with a small yellow clock icon — three
   short lines, not a boxed banner.
7. **QR registration block** (bottom-left, beside the details row): a real,
   functional QR code on a white square, paired with a short white
   instruction line ("Scannez le code QR pour vous inscrire") to its right.
8. **Footer partner strip** (bottom band): a plain white band with a row of
   institutional/funder logos (ministry, EU cofinancing mark, cooperation
   mark, foreign affairs mark), evenly spaced, centered as a group.

## Color palette (approximate — verify against source PNG for exact hex)
- Background: near-black navy, ~`#0B1620` to ~`#16212E` (gradient toward a
  slightly lighter navy mid-canvas, matching the single-panelist variant).
- Accent (badge outline, wordmark highlight, date, icons): bright
  yellow/lime, ~`#E8E23A`.
- Headline text: white `#ffffff`.
- Name tags: solid yellow ~`#E8E23A` fill, dark navy ~`#111827` text.
- Footer band: white `#ffffff`, full-color institutional logos.

## Typography
- Program wordmark: bold, mixed yellow ("Goin'") + white ("Digital").
- Headline: bold sans, sentence case, 2–3 lines max.
- Name tags: role label small/regular, name bold larger, title/affiliation
  regular wrapping to at most 2 lines — identical type treatment for the
  moderator tag and every panelist tag, only the role label text differs.
- Event details: bold for the date numeral, regular for venue/time lines.

## Content slots (fill these, never invent values)
- `{{concree_logo}}`, `{{funder_partner_logos[]}}`
- `{{session_format}}` (e.g. "PANEL"), `{{session_headline}}`
- `{{moderator_photo}}`, `{{moderator_name}}`, `{{moderator_role}}`
- `{{panelist_photos[]}}`, `{{panelist_names[]}}`,
  `{{panelist_titles[]}}` — one triplet per panelist, 3–4 observed
- `{{event_date}}`, `{{event_venue}}`, `{{event_time_range}}`
- `{{registration_qr}}` — must encode a real, working registration URL
- `{{footer_partner_logos[]}}`

## Do / Don't
- Do keep every headshot in this template **circular** — this is the detail
  that visually distinguishes the grid variant from
  `goin-digital-panel-announcement.md`'s single hard-edged full-bleed photo.
- Do give the moderator's photo and tag slightly more visual weight
  (centered, on its own row) than the panelist row beneath it.
- Do generate a real QR code pointing at the actual registration link; never
  place a decorative/non-functional QR graphic.
- Don't mix this grid layout with the single full-bleed photo from the
  other Goin' Digital file in the same brief — pick one variant based on
  whether the brief has one featured speaker or a multi-person lineup.
- Don't crowd more than 4 panelist circles into the row; if the brief has
  more, consider a second row rather than shrinking photos past legibility.
