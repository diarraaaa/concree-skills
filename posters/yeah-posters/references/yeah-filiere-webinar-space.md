---
name: YEAH — Filière webinar/Space poster
description: Portrait poster announcing a YEAH (Yaakaar Jeunesse & Entrepreneuriat) session on an agricultural value-chain topic, either a Twitter/X Space or a Zoom webinar, with cutout speaker portraits.
based_on:
  - assets/SPACE-25-MAI.png
  - assets/SPACE-05-juin.png
  - assets/WEBINAIRE-MAGUE.png
  - assets/WEBINAIRE-YEAH.png
  - assets/Agenda-Space-X-YEAH.png
  - assets/Agenda-Space2-X-YEAH.png
  - assets/Instagram-post---*.png (all are this same template, themed differently)
canvas: 2160x2700px or 3240x4050px (4:5 portrait — Instagram portrait post)
---

# YEAH — Filière webinar/Space poster

## When to use
This is a **layout/style reference**, not a recurring-program recipe: the
YEAH filière sessions it was measured from were a run of one-off episodes
and the series itself may never repeat under that name again. Reach for
this file whenever a new brief needs a cutout-portrait discussion
announcement (X/Twitter Space or webinar format) — regardless of which
CONCREE program or topic is actually running it. This is the single
most-reused template in the source evidence — every file named
`Instagram-post---*.png` inspected turned out to be this same template with
a different theme, not a separate design, which is itself the proof that
one composition here served many different one-off topics.

## Adapting this template to a new, unrelated event
- Swap the header/program logos, script-headline gradient, badge, and
  credit-bar color for the *new* event's real program identity and topic —
  don't default back to "YEAH" or its green/orange-yellow pairing unless
  the new brief is genuinely another YEAH session.
- Keep the cutout-portrait-plus-pill-tag composition and the
  format-badge-swap mechanic (Space vs. Webinar vs. any other live format);
  replace the theme illustration with whatever is actually relevant to the
  new topic, or drop that zone if nothing fits.
- Re-derive the palette from the new event's own sourced material instead
  of reusing the forest-green/gold read below.

## Canvas & background
- 4:5 portrait, 2160×2700px (or 3240×4050px at higher export resolution —
  same ratio).
- Full-bleed dark green background (deep forest green, near-black at the
  edges) with a subtle repeating leaf/sprout line-art pattern scattered
  across it at low opacity — decorative texture only, never a hard grid.

## Zones (top to bottom)
1. **Header lockup** (~y 60–260px): co-organizer logo top-left (e.g.
   "Consortium Jeunesse Sénégal"), funder/partner logo top-right in a small
   "En partenariat avec" label + logo (e.g. Mastercard Foundation), both in
   white/light color for contrast against the dark background.
2. **Program logo** (~y 300–500px, centered): the YEAH wordmark
   (icon + "YEAH" + "YAAKAAR JEUNESSE & ENTREPRENEURIAT" subtitle), white,
   centered.
3. **Format badge** (~y 560–680px, centered): a pill-shaped outline badge
   (thin light-yellow border, transparent fill) containing a small colored
   dot + platform icon + label — either "SPACE - X (twitter)" or
   "WÉBINAIRE" observed. This badge is the single element that changes
   between the Space and Webinar variants of this template; everything else
   stays the same.
4. **Theme block** (~y 780–1400px, left-aligned, max-width ~85%):
   - Eyebrow "Thème" in white italic/bold, small.
   - A large script-style bold headline naming the value chain (e.g. "La
     Mangue,"), rendered in an orange-to-yellow gradient fill.
   - 1–2 more lines directly beneath, same script style, smaller, in solid
     yellow, stating the session's specific angle (e.g. "Entreprendre dans
     une filière à fort potentiel" / "Opportunités et mécanisme de
     financement").
   - A short white regular-weight sentence beneath, phrased as the guiding
     question or scope of the discussion.
5. **Date/time block** (~y 1450–1650px, left-aligned): two lines, each with
   a small yellow line-icon (calendar, clock) followed by bold white text —
   day+date on one line, start time (+ platform if Zoom) on the next.
6. **Speaker cutouts** (~y 1150–2100px, right side, overlapping the theme
   block's right margin): 2–4 individually cut-out (transparent background)
   portrait photos of speakers/moderator, layered with a slight vertical
   offset/stagger, each anchored to a small rounded pill tag giving a
   microphone icon + name (bold) + role (regular, smaller) directly below
   or beside that speaker's photo. The moderator's pill is typically the
   most prominent (widest, positioned first).
7. **Theme illustration** (~y 2150–2500px, bottom-left): a product/produce
   photo or icon relevant to the filière (e.g. whole + sliced mango, cashew
   nuts), placed small, bottom-left, partially bleeding off the left edge.
8. **Speaker credit bar** (~y 2450–2600px, spans most of the width): a
   solid orange rounded-rectangle bar listing the remaining named
   panelists (2–3 more), each as name (bold) + role/affiliation (regular,
   smaller), evenly spaced in columns.
9. **Footer** (~y 2600–2700px): a white rounded-top band with "Projet mis
   en œuvre par" centered above a row of implementing-partner logos
   (CONCREE plus 4–5 others observed), evenly spaced, grayscale-safe.

## Color palette (approximate — verify against source PNG for exact hex)
- Background: deep forest green, ~`#0F3324` to near-black at edges.
- Script headline gradient: ~`#F5A623` (top) to ~`#FCE38A` (bottom/tail).
- Secondary headline lines: solid ~`#F2C244` yellow.
- Body/eyebrow/date text: white `#ffffff`.
- Format badge border: pale yellow, ~`#E8DFA0`; badge dot: orange
  ~`#F2934B`.
- Speaker name pill: orange fill ~`#F2934B`, white text.
- Credit bar: solid orange ~`#F2934B` to ~`#F08A3C`, white text.
- Footer band: white `#ffffff`, dark logos.

## Typography
- Program logo & headers: bold sans, white.
- Script headline: a bold rounded/script display face with a slight
  upward flourish on terminals — distinct from the body sans; keep it to
  1 short noun phrase + 1 short qualifying phrase, never a full sentence.
- Body/date text: regular weight sans, generous line-height for the short
  question line.
- Speaker pill text: bold name / regular role, small size — must stay
  legible against the orange fill (use white).

## Content slots (fill these, never invent values)
- `{{co_organizer_logo}}`, `{{funder_partner_logo}}`
- `{{format}}` — `space` or `webinaire` (drives the badge label/icon)
- `{{filiere_name}}` (e.g. "La Mangue"), `{{session_angle}}` (e.g.
  "Opportunités et mécanisme de financement")
- `{{guiding_question}}` — one short sentence
- `{{session_date}}`, `{{session_time}}`, `{{platform_detail}}` (e.g.
  "sur ZOOM" for webinars)
- `{{moderator}}` — real photo, name, role
- `{{panelists[]}}` (2–4) — real photo (when available) or name + role for
  the credit bar
- `{{filiere_illustration}}` — real product photo relevant to the theme
- `{{footer_partner_logos[]}}`

## Do / Don't
- Do treat "Space" vs "Webinaire" as a one-badge swap — do not redesign the
  rest of the poster per format.
- Do keep the script headline to at most 2 short lines; if the filière name
  plus angle run long, shorten the angle line rather than shrinking type
  below legibility.
- Don't caption a speaker photo without their name+role pill, and don't add
  a pill without a photo unless the source data genuinely lacks one (in
  which case, say so rather than fabricating a headshot).
- Don't recolor the script headline gradient toward CONCREE's site orange
  (`#ff9900`) — this program's gradient is warmer/more yellow; match the
  source, not the site tokens.
