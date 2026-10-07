---
name: JAMBAARS AI — Speaker lineup poster
description: Square poster listing multiple named speakers/intervenants for a JAMBAARS AI event, each with photo, name, and role.
based_on:
  - assets/INTERVENANTS-2.png
canvas: 2160x2160px (1:1 square — Instagram/LinkedIn square post)
---

# JAMBAARS AI — Speaker lineup poster

## When to use
This is a **layout/style reference**, not a recurring-program recipe: the
JAMBAARS AI Demo Day it was measured from was a one-off session and may
never repeat under that name. Reach for this file whenever a new brief
needs to announce 3–4 confirmed speakers in a grid — regardless of which
CONCREE program is running the event. For a single-speaker teaser or the
event announcement itself, use `jambaars-event-announcement.md` instead.

## Adapting this template to a new, unrelated event
- Swap the header logos, title-block colors, and card border accent for the
  *new* event's real program identity — don't default back to "JAMBAARS AI"
  or its green/orange pairing unless the new brief is genuinely another
  JAMBAARS AI session.
- Keep the grid-of-cards composition and the name+role caption pattern; the
  number of cards should match the real speaker count, not always 3–4.
- Re-derive the palette from the new event's own sourced material instead
  of reusing the green/orange read below.

## Canvas & background
- 2160×2160px, 1:1, white background, same faint checkerboard texture and
  pale decorative line-art swirl as the event-announcement template — this
  is the same header/footer chrome, reused with a different body.

## Zones (top to bottom)
1. **Header lockup** (~y 60–260px): identical to the event-announcement
   template — program logo left, co-branding partner logo right.
2. **Title block** (~y 380–560px, centered): one line combining the event
   name and series in green bold caps (e.g. "DEMO DAY FINAL ~ JAMBAARS AI"),
   with a second, larger word directly beneath in the orange/red accent
   color naming the section (e.g. "Intervenants"). Two small accent
   diamond/sparkle glyphs flank this block left and right.
3. **Speaker grid** (~y 780–1750px): a single row of 3–4 equal-width cards,
   evenly spaced with generous gutters. Each card:
   - A portrait photo (headshot or waist-up), clipped with a soft inward
     curve at the bottom-left corner only (same clip language as the
     event-announcement template's featured photo), framed by a thin accent
     border (orange or brand-alternating per card is acceptable).
   - Below the photo: the person's full name in bold dark text, then their
     role/affiliation in smaller muted gray text, both left-aligned to the
     photo's left edge.
4. **Footer partner strip** (~y 2000–2160px): identical structure to the
   event-announcement template — left-aligned row of partner/institutional
   logos on one baseline.

## Color palette (approximate — verify against source PNG for exact hex)
- Background: white `#ffffff`.
- Title line 1 (event/series name): ~`#1E9254` green.
- Title line 2 (section label, e.g. "Intervenants"): ~`#E8622C` orange.
- Speaker name: near-black, ~`#1A1A1A`.
- Speaker role: muted gray, ~`#6B6B68`.
- Card photo border accent: orange, ~`#F2A65A` to `#E8622C`.

## Typography
- Title line 1: bold caps, medium-large size.
- Title line 2 (section label): extra-bold/black, noticeably larger than
  line 1 — it is the visual focal point of the title block.
- Speaker name: bold, medium size, tight leading.
- Speaker role: regular weight, small size, 2 lines max before truncating
  gracefully (never let a role wrap into 3+ lines and collide with the next
  card).

## Content slots (fill these, never invent values)
- `{{program_logo}}`, `{{copresenting_partner_logo}}`
- `{{event_title_line}}`, `{{section_label}}` (e.g. "Intervenants")
- `{{speakers[]}}` — for each: `{{photo}}` (real, sourced), `{{full_name}}`,
  `{{role_affiliation}}`
- `{{footer_partner_logos[]}}`

## Do / Don't
- Do keep the grid to 3–4 cards max on one row at this canvas width; for 5+
  speakers, split into two lineup posters rather than shrinking cards until
  names wrap awkwardly.
- Do give every card the same photo aspect ratio and clip treatment — mixed
  crops read as unfinished.
- Don't caption a card with only a name and no role, or vice versa — both
  are required per the source evidence.
- Don't substitute a placeholder avatar for a named real speaker; source the
  real photo or ask for one.
