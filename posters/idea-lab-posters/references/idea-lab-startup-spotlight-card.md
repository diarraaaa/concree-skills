---
name: Idea Lab — Startup/laureate spotlight card
description: Dark portrait-photo card introducing one named cohort startup/laureate — headshot, startup name, one-paragraph pitch, and a founder credit tag — built once per startup in a cohort showcase series.
based_on:
  - Idea Lab figma file "IDEA LAB" (figma.com/design/QiEzqqxt6esRZxLCZpAjkR), frame "KORA" (repeated as one frame per cohort startup — SOTILMA, OOMUS, XAMLE, BIBLI, SEKHEM-ETHOS, Scanimal Health, SMART PARK, MAKEDA, SmartAgroMap, Jang Tech, 2IP COACHING, Vroom Africa, TEWLU, SuufScan observed as the same template)
canvas: 1080x1080px (1:1 square — Instagram/LinkedIn square post)
---

> **Rendered example:** `../examples/06a-idea-lab-cover-pro.html` (+ 06b, 06c, 06d) (open it before building). Real logos: `../assets/`. Build rules: `../side-files/build-lessons.md`.

# Idea Lab — Startup/laureate spotlight card

## When to use
This is a **layout/style reference**, not a recurring-program recipe: "Kora
Metrics" and the other named startups it was measured from are one specific
cohort's laureates and will not recur. Reach for this file whenever a brief
needs to **introduce one named startup, founder, or cohort laureate** with a
photo + short pitch — it is built once per person/company and the same
brief commonly asks for a whole series (one card per cohort member). Not for
a group photo of multiple people on one card — use
`goin-digital-panel-lineup-grid.md` or `jambaars-speaker-lineup.md` for that.

## Adapting this template to a new, unrelated event
- Swap the program logo, funder/partner footer, and accent treatment for the
  *new* program's real identity — don't default back to "Idea Lab" or its
  Expertise France/GIZ footer unless the new brief is genuinely the same
  cohort program.
- Keep the compositional bones (dark card + large right-side headshot +
  name/pitch block + bottom founder-credit tag) — this reads as a
  professional "founder spotlight" format regardless of program.
- Build one card per startup/laureate named in the brief; never invent a
  startup name, pitch, or founder — ask for any missing one.
- Re-derive the palette from the new program's own material instead of
  reusing the near-black read below if a different brand is specified.

## Canvas & background
- 1080×1080px, 1:1.
- Solid dark charcoal-to-black background (`#1c1c1c` approx.), flat, no
  texture — gives a premium, editorial "founder profile" feel distinct from
  the lighter carousel/cover templates in this pack.

## Zones (top to bottom, left to right)
1. **Header lockup** (top band): two funder/partner logos top-center on
   small individual white cards (e.g. "Expertise France", "GIZ"), plus a
   thin "Mis en oeuvre par" label above them.
2. **Program logo** (upper-left, below the header band): CONCREE or program
   logo, left-aligned, sitting directly on the dark background (no white
   card needed here, unlike the funder logos above).
3. **Headshot photo** (right ~45–55% of canvas, full-bleed to the right and
   top edges, roughly top-third to bottom edge): one professional
   headshot/portrait of the founder, hard-edged rectangular crop (no circle
   or rounded mask), cropped tight.
4. **Pitch card** (left ~55% of canvas, vertically centered, overlapping
   under the headshot's left edge): a large rounded-rectangle outline (thin
   light stroke, no fill — background shows through), containing:
   - Startup name as a bold white headline (1 line, large).
   - A short pitch paragraph (2–4 sentences) in regular-weight light gray
     body text describing what the startup does and its value proposition.
5. **Founder credit tag** (bottom-right, overlapping the headshot's bottom
   edge): a solid white rounded-rectangle card holding the founder's full
   name (bold, dark text) above the startup's own logo/wordmark (small,
   full color) — this is the one zone with a light/white fill against the
   otherwise all-dark card.
6. **Footer partner strip** (bottom band): a row of institutional/funder
   logos (ministry, EU cofinancing mark, cooperation mark, embassy),
   evenly spaced, centered as a group, white/full-color marks on the dark
   background.

## Color palette (approximate — verify against source PNG for exact hex)
- Background: near-black charcoal, ~`#1c1c1c`.
- Pitch card outline: thin light gray/white stroke, ~`#ffffff` at low
  opacity, no fill.
- Headline (startup name): white `#ffffff`.
- Body pitch text: light gray, ~`#d6d6d6`.
- Founder credit tag: solid white `#ffffff` fill, dark text ~`#111111`.
- Footer logos: full-color/white marks as sourced — never recolor a real
  partner logo.

## Typography
- Startup name: bold/extra-bold, white, large, 1 line.
- Pitch paragraph: regular weight, light gray, comfortable line-height
  (~1.4), 2–4 sentences max — this card has no scroll, so keep it short.
- Founder name (credit tag): bold, dark, medium size.
- Funder/program labels: small, regular weight.

## Content slots (fill these, never invent values)
- `{{funder_partner_logos[]}}` (top band), `{{program_logo}}`
- `{{startup_headshot}}` — real photo of the named founder; never a
  generated or stock stand-in for a named real person
- `{{startup_name}}`, `{{startup_pitch_paragraph}}`
- `{{founder_full_name}}`, `{{startup_wordmark_logo}}`
- `{{footer_institutional_logos[]}}`

## Do / Don't
- Do build one card per startup/founder when the brief lists a cohort —
  reuse this exact layout for each, only swapping photo/name/pitch/logo.
- Do keep the pitch card as an **outline only** (no fill) so the dark
  background and headshot stay visually dominant.
- Do keep the founder credit tag as the only light/white-filled zone on the
  card — that contrast is what makes it readable as a "credit" rather than
  body content.
- Don't crop the headshot to a circle or rounded shape — this template's
  photo is a hard-edged full-bleed rectangle.
- Don't let the pitch paragraph run past 4 sentences; shorten rather than
  shrink the type past readable size.
