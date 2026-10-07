---
name: Idea Lab — Multi-slide carousel (cover + topic slides)
description: Two-role Instagram carousel for an Idea Lab call-for-applications campaign — a cover slide naming the cohort/theme and a repeatable topic slide used for each sub-theme or detail slide that follows it.
based_on:
  - Idea Lab figma file "IDEA LAB" (figma.com/design/QiEzqqxt6esRZxLCZpAjkR), frames "idea lab Carrousel 1- C10" (cover) and "Idea lab Carrousel 4 - C10" (topic slide, numbered "2")
canvas: 1080x1080px (1:1 square — Instagram carousel post)
---

> **Rendered example:** `../examples/06a-idea-lab-cover-pro.html` (+ 06b, 06c, 06d) (open it before building). Real logos: `../assets/`. Build rules: `../side-files/build-lessons.md`.

# Idea Lab — Multi-slide carousel (cover + topic slides)

## When to use
This is a **layout/style reference**, not a recurring-program recipe: the
"Idea Lab Cohorte 10" call-for-applications campaign it was measured from is
one specific cohort and will not necessarily repeat under that name or those
partners. Reach for this file whenever a brief needs a **multi-slide
Instagram/LinkedIn carousel** — a cover slide that announces a call/theme,
followed by one or more topic/detail slides — rather than a single static
poster. Not for a single standalone announcement — use
`jambaars-event-announcement.md` or `idea-lab-cohort-launch.md` for that.

Unlike every other file in this pack, this template has **two distinct slide
roles** that are always built together as a set, numbered in sequence.

## Adapting this template to a new, unrelated event
- Swap the program logo, accent triangle colors, and partner footer for the
  *new* campaign's real identity and funders — don't default back to "IDEA
  Lab" or its green/orange/red triangle accents unless the new brief is
  genuinely another Idea Lab cohort.
- Keep the two-role structure (circular-photo cover + half-bleed-photo topic
  slides) and the running page-number badge on every slide after the cover.
- Re-derive the palette from the new campaign's own sourced material instead
  of reusing the read below.
- Build as many topic slides as the brief has sub-themes/details; each one
  follows the **same** topic-slide zone layout, just with new photo, title,
  and body copy — do not vary the composition slide-to-slide.

## Canvas & background (both slide roles)
- 1080×1080px, 1:1, repeated identically for every slide in the set so the
  carousel swipes cleanly.
- Background: very light warm gray/off-white (`#f3f1ee` approx.) with a
  faint paper-grain texture — same whisper-level texture treatment as the
  JAMBAARS template, never competing with text.

## Slide role A — Cover slide (slide 1 only)
1. **Header lockup** (top-left): program logo lockup (icon + wordmark); a
   small accent sparkle glyph may sit beside the wordmark.
2. **Partner/sponsor mark** (top-right): a single co-branding or sponsor logo
   (e.g. "concree"), right-aligned.
3. **Eyebrow + cohort label** (upper-right area, right-aligned, two lines):
   a muted/outlined all-caps call-to-action line (e.g. "APPEL A
   CANDIDATURE") above a bold, darker all-caps cohort/batch label (e.g.
   "COHORTE 10").
4. **Accent triangle cluster** (right of the eyebrow block): 2–3 small solid
   triangles in different accent colors (yellow, red, green observed),
   purely decorative, loosely clustered, never overlapping text.
5. **Theme headline** (right ~60% of canvas, below the eyebrow, left-aligned
   text starting roughly at horizontal center): bold display headline, 2
   short lines, dark near-black, stating the cohort's call theme (e.g.
   "Santé de la mère et de l'enfant").
6. **Circular photo** (left edge, large circle bleeding off the left and
   partially the bottom edge, roughly 55–60% of canvas height): one portrait
   photo relevant to the theme, masked to a hard circle (not a half-bleed
   rectangle — this is what distinguishes the cover from topic slides).
7. **CTA pill** (bottom-right area, overlapping the circle's right edge):
   a solid dark rounded-rectangle pill holding 1–2 lines of white body text
   (what the call offers, e.g. a seed grant) plus a right-pointing arrow
   icon at its left edge.
8. **Footer partner strip** (bottom band): 2–3 real funder/institutional
   logos, evenly spaced, centered as a group, on the plain background (no
   dividing bar).

## Slide role B — Topic / detail slide (slide 2+, repeat per sub-theme)
1. **Header lockup** (top-left) + **partner mark** (top-right): identical
   position/treatment to the cover slide, for visual continuity across the
   swipe.
2. **Accent triangle** (right side, mid-height): one single solid triangle
   accent (not the 2–3 cluster used on the cover) — lighter visual weight
   now that the slide carries less chrome.
3. **Sub-theme headline** (right ~65% of canvas, upper-mid area,
   left-aligned): bold display headline, 2 lines, dark near-black, naming
   this slide's specific sub-topic (e.g. "Soutien aux Femmes Vulnérables").
4. **Half-bleed photo** (left edge, large rounded-corner rectangle bleeding
   off the left edge only, roughly 35–40% of canvas width, mid-height to
   bottom): one photo relevant to this sub-topic — a **rectangle with
   rounded right-side corners**, not a circle (this is what distinguishes a
   topic slide from the cover).
5. **Body text card** (bottom-right, overlapping the photo's right edge): a
   large dark rounded-rectangle card holding 1 short paragraph (3–4 lines)
   of white body copy explaining this sub-topic.
6. **Slide number badge** (bottom-right corner, below/beside the card): a
   plain bold number (e.g. "2") in dark text, no background chip — tells the
   viewer their position in the swipe sequence. Increment by one per topic
   slide (cover slide is unnumbered).

## Color palette (approximate — verify against source PNG for exact hex)
- Background: off-white/warm gray, ~`#f3f1ee`.
- Headline text: near-black, ~`#1a1a1a`.
- Accent triangles: yellow ~`#f5a623`, red ~`#e8503a`, green ~`#2fa84f`.
- Dark card/pill fill (CTA pill, body text card): deep navy-black,
  ~`#0c1b2a`.
- Card/pill text: white `#ffffff`.
- Eyebrow line: muted outline gray; cohort label: dark, bolder weight.

## Typography
- Program wordmark: mixed-weight lockup (icon + two-tone wordmark), small,
  consistent across every slide.
- Eyebrow line: regular weight, all caps, wide letter-spacing, muted color.
- Cohort/batch label: bold, all caps, darker than the eyebrow line.
- Headline (cover and topic): extra-bold, sentence case, tight leading,
  2 lines max.
- Body copy (cards/pills): regular weight, white, comfortable line-height,
  short (never more than ~4 lines before the card must grow).
- Slide number: bold, plain, no decoration.

## Content slots (fill these, never invent values)
- `{{program_logo}}`, `{{sponsor_logo}}`, `{{footer_partner_logos[]}}`
- `{{cta_label}}` (e.g. "APPEL A CANDIDATURE"), `{{cohort_label}}` (e.g.
  "COHORTE 10")
- `{{cover_theme_headline}}`, `{{cover_photo}}`, `{{cover_cta_text}}`
- Per topic slide: `{{slide_number}}`, `{{topic_headline}}`,
  `{{topic_photo}}`, `{{topic_body_text}}`
- Real funder/institutional logos only — never invent a partner mark

## Do / Don't
- Do keep the cover's photo **circular** and every topic slide's photo a
  **rounded rectangle** — mixing the two breaks the slide-role signal that
  tells the viewer "this is the start" vs "this is a detail".
- Do number every topic slide sequentially starting at a value consistent
  with its position (cover is unnumbered, first topic slide is commonly "2"
  if the cover counts as slide 1).
- Do reuse the exact same header/footer position across all slides in the
  set — that repetition is what makes the swipe read as one carousel.
- Don't put a CTA pill with an arrow on topic slides — the arrow/CTA pill is
  cover-only; topic slides use a plain text card with no arrow.
- Don't vary the canvas size between slides in the same carousel.
