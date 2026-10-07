---
name: JAMBAARS AI — Event announcement poster
description: Square announcement poster for a JAMBAARS AI program event (Demo Day, pitch session, etc.), with date/location banner and a featured speaker photo.
based_on:
  - assets/DEMO-DAY-FINALE-Annonce.png
  - assets/DEMO-DAY.png
canvas: 2160x2160px (1:1 square — Instagram/LinkedIn square post)
---

# JAMBAARS AI — Event announcement poster

## When to use
This is a **layout/style reference**, not a recurring-program recipe: the
JAMBAARS AI Demo Days it was measured from were one-off sessions and may
never repeat under that name. Reach for this file whenever a new brief
needs a single-event announcement — one headline, one date/location,
optionally one featured photo — regardless of which CONCREE program is
actually running it. Not for listing multiple speakers — use
`jambaars-speaker-lineup.md` for that.

## Adapting this template to a new, unrelated event
- Swap the header logos, headline colors, and gradient banner colors for
  the *new* event's real program identity and partners — don't default back
  to "JAMBAARS AI" or its green/orange pairing unless the new brief is
  genuinely another JAMBAARS AI session.
- Keep the compositional bones (two-tone headline + body + tagline +
  gradient date/location banner + featured photo + partner footer) only as
  far as they fit the new event; drop or resize a zone that doesn't apply
  (e.g. no featured photo available) rather than filling it with a
  placeholder.
- Re-derive the palette from the new event's own sourced material instead
  of reusing the green/orange read below — that pairing belongs to the
  JAMBAARS AI instances it was observed in.

## Canvas & background
- 2160×2160px, 1:1.
- White background (`#ffffff`) with a very faint checkerboard/grid texture
  visible across the whole canvas (subtle, near-white, decorative only —
  never let it compete with text contrast).
- Thin decorative outline swirl/line art in pale green, loosely traced
  behind the headline area — optional, low-contrast, never crosses text.

## Zones (top to bottom, left to right)
1. **Header lockup** (top ~y 60–260px): JAMBAARS AI program logo (icon +
   wordmark + "Sénégal" subtitle) on the left; a small accent
   diamond/sparkle glyph near the horizontal center; the co-branding partner
   logo (e.g. "SEN HUB IA") on the right. All three sit on one baseline.
2. **Headline block** (~y 340–650px, left ~60% of canvas width, text-left
   aligned): two-line bold display headline, each line a different accent
   color (line 1 green, line 2 orange/red observed) — reserve this two-color
   split for the event name split across exactly two short phrases.
3. **Body paragraph** (~y 680–1120px, same left column, max-width ~60% of
   canvas): 1 short paragraph (3–5 sentences) in dark gray body copy, plus
   one bold short tagline line using a tilde/middle-dot separator between
   3 short session-format words (e.g. "Pitchs ~ Networking ~ After Work").
   A small accent-colored diamond/sparkle glyph sits to the right of the
   paragraph, vertically centered against it.
4. **Featured photo** (right ~35–40% of canvas, full-bleed to the right and
   bottom edges): one portrait/action photo of a speaker or past-event
   moment, corner-clipped with a soft inward curve at the bottom-left corner
   of the photo only, revealing the gradient banner beneath it.
5. **Date/location banner** (bottom ~y 1720–1900px, spans from the left edge
   to just under the photo): a rounded-corner pill/banner filled with a
   warm orange-to-red gradient, holding two lines in white bold text, each
   preceded by a small icon: a calendar icon + date/time line, then a pin
   icon + venue line.
6. **Footer partner strip** (bottom ~y 2000–2160px): a left-aligned row of
   grayscale/full-color partner and institutional logos (ministry, embassy,
   hub, CONCREE, telecom sponsor), all vertically centered on one line, with
   even spacing; a short right-aligned closing line in bold dark text
   ("Restez connectés aux temps forts" observed) sits on the gradient
   corner that continues from the banner up into this strip.

## Color palette (approximate — verify against source PNG for exact hex)
- Background: white `#ffffff`.
- Headline accent 1 (green): ~`#1E9254`.
- Headline accent 2 (orange/red): ~`#E8622C` to ~`#D93A3A` (used as a
  gradient on the bottom banner too).
- Body text: dark warm gray, ~`#3A3A38`.
- Tagline text: same green as accent 1.
- Banner text: white on the orange/red gradient.

## Typography
- Display headline: extra-bold/black weight, all caps, tight leading
  (~1.05), no letter-spacing reduction needed at this size since it's short.
- Body paragraph: regular weight, generous line-height (~1.4).
- Tagline: bold, same size as body but heavier weight, brand-colored.
- Banner date/location: bold, white, medium size, one line each.

## Content slots (fill these, never invent values)
- `{{program_logo}}`, `{{copresenting_partner_logo}}`
- `{{headline_line_1}}` (e.g. program/series name), `{{headline_line_2}}`
  (e.g. "JAMBAARS AI")
- `{{body_paragraph}}` — what the event is, in 3–5 sentences
- `{{format_tags}}` — 2–4 short session formats separated by "~"
- `{{featured_photo}}` — real photo, reused from `assets/`/`imagery/` or
  sourced fresh; never a generated stand-in for a named real person/event
- `{{event_date_time}}`, `{{event_venue}}`
- `{{footer_partner_logos[]}}`, `{{footer_closing_line}}`

## Do / Don't
- Do keep exactly one featured photo and one headline pair per poster.
- Do keep the gradient banner confined to the bottom band; never let body
  text overlap it.
- Don't stretch the checkerboard texture into a visible grid — it must stay
  a whisper-level background texture.
- Don't invent partner logos for the footer strip; use only real, sourced
  marks.
