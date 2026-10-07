---
name: Goin' Digital — Panel announcement poster
description: Portrait poster announcing a Goin' Digital panel/conference session, with a bordered info box, QR registration code, and a full-bleed panelist photo.
based_on:
  - assets/Goin-Digital---paneliste-01.png
  - assets/Goin-Digital---prolongee.png
  - assets/Goin-Digital---IA-Senegal-2.png
  - assets/Visuel-25-septembre-GD.png
canvas: 3240x4050px (4:5 portrait — Instagram portrait post)
---

# Goin' Digital — Panel announcement poster

## When to use
This is a **layout/style reference**, not a recurring-program recipe: the
"Goin' Digital" panels it was measured from were one-off sessions and may
never happen again exactly like this. Reach for this file whenever a new
brief needs an in-person panel/conference announcement with one featured
speaker photo and a registration QR code — regardless of which CONCREE
program is actually running it — and treat the dark, editorial-conference
composition below as the reusable DNA to adapt, not a template to refill
with the same program name.

## Adapting this template to a new, unrelated event
1. Swap `{{concree_logo}}` co-branding logos, the program wordmark, and the
   accent color for whatever the *new* event's real partners and palette
   are — do not default back to "Goin'Digital" or its yellow/lime accent
   unless the new brief is genuinely another Goin' Digital session.
2. Keep the compositional bones (bordered info box + full-bleed photo +
   QR registration) only if they still fit the new event's format; drop the
   QR block entirely for a virtual-only event rather than leaving a fake
   code.
3. Re-derive the palette note below from the new event's own sourced
   material (brand guide, past assets, or explicit instruction) instead of
   reusing this file's yellow/navy read — that combination belongs to the
   Goin' Digital instances it was observed in, not to "panel posters" as a
   category.
4. Everything in **Content slots** below still applies structurally; every
   value in it must come from the new event's real details.

## Canvas & background
- 4:5 portrait, 3240×4050px.
- Solid dark navy-to-black background (near-black at the very top/bottom,
  slightly lighter navy through the middle) — flat, no texture or pattern,
  giving it a more corporate/editorial feel than the YEAH template.

## Zones (top to bottom)
1. **Header lockup** (~y 40–220px): CONCREE logo top-left on a small white
   rounded card (only the logo gets a white background patch — the rest of
   the header stays on the dark background); a small "En partenariat avec"
   label top-right above 2 partner/funder logos (e.g. Expertise France,
   GIZ), both logos also sitting on their own compact white card.
2. **Bordered info box** (~y 380–2400px, left ~55% of canvas, right edge
   overlapped by the panelist photo): a large rounded-rectangle outline in
   a bright yellow/lime accent color, 2px-equivalent stroke, no fill,
   containing:
   - Program wordmark ("Goin'Digital", mixed yellow/white weight) at top.
   - A small pill-outline badge naming the session format (e.g. "PANEL").
   - A bold white multi-line headline stating the session topic, with the
     single most important phrase set in the yellow accent color inline
     (e.g. "Femmes leaders et technologies:" in white, "au-delà de la
     réussite..." continuing in white — the accent is used sparingly, not
     for the whole headline).
   - The event date as a large bold yellow numeral (day) + smaller white
     month/year beside it.
   - Venue line and time line, each with a small yellow icon.
   - A QR code (real, functional, generated for the actual registration
     link) bottom-left of this box, paired with a short white instruction
     line ("Scannez le code QR pour vous inscrire").
3. **Panelist photo** (~y 300–3400px, right ~45% of canvas, full-bleed to
   the right and top edges, overlapping the info box's right border): one
   large portrait photo, professional headshot style, cropped tight at the
   bottom.
4. **Panelist credit tag** (~y 3350–3550px, bottom-right over the photo): a
   solid yellow rounded rectangle, positioned inside the photo's bottom
   edge with even inset margins, holding "Panéliste" (small) + full name
   (bold, larger) + title/affiliation (regular, wraps to 2 lines max) in
   dark navy text.
5. **Footer partner strip** (~y 3700–4050px): a plain white band with a row
   of institutional/funder logos (ministry, EU cofinancing mark, embassy,
   bilateral cooperation mark), evenly spaced, centered as a group.

## Color palette (approximate — verify against source PNG for exact hex)
- Background: near-black navy, ~`#0B1620` to ~`#16212E`.
- Accent (box outline, wordmark highlight, date numeral): bright
  yellow/lime, ~`#E8E23A`.
- Body headline text: white `#ffffff`.
- Panelist credit tag: solid yellow ~`#E8E23A` fill, dark navy
  ~`#111827` text.
- Footer band: white `#ffffff`, full-color institutional logos.

## Typography
- Program wordmark: bold, mixed yellow ("Goin'") + white ("Digital") in one
  lockup.
- Headline: bold sans, 3–4 lines max, sentence case (not all-caps) — this
  template reads more editorial/conference than the caps-heavy JAMBAARS
  template.
- Date numeral: extra-bold, large, yellow.
- Credit tag: "Panéliste" label small/regular, name bold larger, role
  regular wrapping to at most 2 lines.

## Content slots (fill these, never invent values)
- `{{concree_logo}}`, `{{funder_partner_logos[]}}`
- `{{session_format}}` (e.g. "PANEL", "CONFÉRENCE")
- `{{session_headline}}` — sentence-case, with at most one phrase in accent
  color
- `{{event_day}}`, `{{event_month_year}}`, `{{event_venue}}`,
  `{{event_time_range}}`
- `{{registration_qr}}` — must encode a real, working registration URL
- `{{panelist_photo}}` — real photo of the named panelist
- `{{panelist_name}}`, `{{panelist_title}}`
- `{{footer_partner_logos[]}}`

## Do / Don't
- Do keep the accent yellow confined to the outline box, wordmark, date
  numeral, and credit tag — the background and headline body stay
  dark/white so the yellow keeps its signal value.
- Do generate a real QR code pointing at the actual registration link;
  never place a decorative/non-functional QR graphic.
- Don't crop the panelist photo to a rounded/clipped shape — this template's
  photo is a hard-edged full-bleed rectangle, unlike the JAMBAARS templates.
- Don't pull CONCREE's site accent (`#ff9900`) into this poster; the
  program's own yellow/lime is a different, cooler-toned accent.
- Do size the outline box's height to the brief's actual content (headline
  + date/venue + any added body copy + QR block) plus modest padding,
  rather than keeping a fixed tall box that leaves a large empty gap at
  the bottom — a top-heavy box with dead space below reads as unfinished.
  If the brief's content is sparse, consider adding a short "À propos"
  description and a mini agenda/program list inside the box rather than
  just enlarging whitespace.
- Do keep every body/label line inside this box at ≥28px on the
  3240×4050 canvas (or ≥26px for the smallest footer/header labels) —
  smaller reads as illegible once exported. See
  `../side-files/figma-build-notes.md` for the full minimum-size rule.
