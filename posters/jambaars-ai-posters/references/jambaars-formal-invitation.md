---
name: JAMBAARS AI — Formal letter-style invitation
description: Portrait letter-format invitation card (salutation + body paragraphs, no photo) for inviting named or general recipients to a specific program event.
based_on:
  - Idea Lab figma file "IDEA LAB" (figma.com/design/QiEzqqxt6esRZxLCZpAjkR), frame "Invitation"
canvas: 600x900px (2:3 portrait — print/PDF or shareable image invitation)
---

# JAMBAARS AI — Formal letter-style invitation

## When to use
This is a **layout/style reference**, not a recurring-program recipe: the
"Reveal & MVP Showcase" invite it was measured from is one specific JAMBAARS
AI event and will not recur under that name. Reach for this file whenever a
brief needs a **formal, text-led invitation** — a letter addressed to
"Madame, Monsieur" (or a named recipient) explaining an event and inviting
attendance — rather than a headline-led visual announcement poster. This is
the only letter-format file in this pack; every other template is
photo/headline-led. Not for a visual social-media announcement — use
`jambaars-event-announcement.md` for that instead, even for the same event.

## Adapting this template to a new, unrelated event
- Swap the header logos for the *new* event's real program and co-branding
  partner — don't default back to "JAMBAARS AI" / "SEN HUB IA" unless the
  new brief is genuinely that same program.
- Keep the letter structure (salutation → what/when/where paragraph →
  significance paragraph → warm closing line → footer) — this is what reads
  as a formal invitation rather than a marketing poster.
- Re-derive the decorative line-art and corner-blob accent color from the
  new program's palette; the faint outline swirl and orange corner shape
  below belong to this specific sourced instance.
- Never invent the recipient, event name, date, time, or venue — ask for any
  value the brief doesn't supply.

## Canvas & background
- 600×900px, 2:3 portrait — sized for a printable/shareable letter card
  rather than a square social post.
- White background (`#ffffff`), with a very faint pale-orange decorative
  outline swirl/line-art motif in the upper-left quadrant — low-contrast,
  purely decorative, never crossing body text.
- A soft orange-to-red gradient blob occupies the bottom-right corner,
  bleeding off both the right and bottom edges, as the only strong color
  accent on the page.

## Zones (top to bottom)
1. **Header lockup** (top band): program logo (icon + wordmark + country
   subtitle) on the left; co-branding partner logo on the right, both
   vertically centered on one baseline, sitting inside a thin full-width
   rounded-corner border that frames the whole letter.
2. **Salutation** (just below the header, left-aligned): a single short
   line greeting the recipient generically ("Madame, Monsieur,") or by name
   if the brief supplies one.
3. **Body paragraph 1 — the invitation itself** (left-aligned, regular
   body text, generous line-height): names the program, the event, and
   states the date/time/venue inline as bold text within the sentence
   (not as a separate banner/pill — this is what distinguishes the letter
   format from every poster template in this pack).
4. **Body paragraph 2 — context/significance** (same column, below a blank
   line): 1 short sentence giving the event's significance (e.g. "this
   event also marks phase 3 — market launch").
5. **Body paragraph 3 — closing framing** (same column): 1–2 sentences
   framing the opportunity for the reader, ending in a bolded warm closing
   line expressing that the recipient's presence matters.
6. **Decorative corner accent** (bottom-left, small): a single small solid
   diamond/sparkle glyph in the program's accent color, sitting just above
   the footer, purely decorative.
7. **Footer partner strip** (bottom band, above the gradient corner): a row
   of institutional/funder logos, evenly spaced, left-to-center aligned,
   full-color, sitting on the white background just above where the
   gradient corner blob begins.

## Color palette (approximate — verify against source PNG for exact hex)
- Background: white `#ffffff`.
- Body text: near-black, ~`#1a1a1a`.
- Bolded inline details (event name, date, time, venue): same near-black,
  bold weight only — no color change, unlike the poster templates in this
  pack which use accent color for emphasis.
- Decorative swirl: very pale orange, near-white, ~5–10% opacity.
- Corner gradient blob: orange-to-red, ~`#E8622C` to ~`#D93A3A`.
- Border frame: thin pale gray/orange hairline, ~`#e5d9cf`.

## Typography
- Header wordmark: same lockup treatment as the program's other materials.
- Salutation: regular weight, same size as body.
- Body paragraphs: regular weight, comfortable line-height (~1.5–1.6) for
  letter readability; key facts (event name, date, time, venue) set in
  **bold** inline rather than pulled into a separate zone.
- Closing line: bold, slightly larger emphasis than the surrounding
  paragraph, reads as the letter's one call-to-warmth moment.

## Content slots (fill these, never invent values)
- `{{program_logo}}`, `{{copresenting_partner_logo}}`
- `{{recipient_salutation}}` (generic "Madame, Monsieur," or a real name)
- `{{program_name}}`, `{{event_name}}`, `{{event_date}}`, `{{event_time}}`,
  `{{event_venue}}` — all woven into paragraph 1 as bold inline text
- `{{event_significance_sentence}}` (paragraph 2)
- `{{closing_framing_text}}`, `{{closing_warm_line}}` (paragraph 3)
- `{{footer_partner_logos[]}}`

## Do / Don't
- Do keep every key fact (date/time/venue) as **bold inline text within a
  sentence** — never extract them into a separate banner or pill; that
  would break the letter format this template exists for.
- Do keep exactly one thin bordered frame around the whole letter — it is
  what visually separates this from a borderless marketing poster.
- Don't add a large photo or headline treatment — if the brief wants a
  photo-led visual, route it to `jambaars-event-announcement.md` instead.
- Don't let the decorative swirl or corner blob exceed low-contrast,
  background-level visibility — this template's hierarchy is text-first.
