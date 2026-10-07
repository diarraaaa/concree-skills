---
name: Idea Lab — Program dossier / info-deck slide
description: Text-led white-page slide for a multi-page program dossier/PDF deck (cover + content pages) explaining a cohort program's partners, goals, and structure — paragraph-driven, not photo/headline-led like the social-media poster templates in this pack.
based_on:
  - Idea Lab figma file "IDEA LAB" (figma.com/design/QiEzqqxt6esRZxLCZpAjkR), UCAD/makerspace program dossier pages "Présentation du programme", "Qu'est-ce que le programme IDEA LAB", "Présentation des partenaires du programme"
canvas: 1920x1358px approx. (16:11 landscape — PDF/slide-deck page, verify exact ratio against source before building)
---

> **Rendered example:** `../examples/06a-idea-lab-cover-pro.html` (+ 06b, 06c, 06d) (open it before building). Real logos: `../assets/`. Build rules: `../side-files/build-lessons.md`.

# Idea Lab — Program dossier / info-deck slide

## When to use
This is a **layout/style reference**, not a recurring-program recipe: the
UCAD/makerspace program dossier it was measured from is one specific
cohort's documentation and will not recur under that name. Reach for this
file whenever a brief needs a **multi-page informational document** —
explaining what a program is, who its partners are, how it works — meant to
be read as a PDF/deck rather than scrolled as a social post. This is the
only **paragraph-led, white-page** template in this pack; every other file
is photo/headline-led and sized for Instagram/LinkedIn. Not for an
announcement or call-to-action visual — use `jambaars-event-announcement.md`
or `idea-lab-carrousel-slide.md` for those, even for the same program.

## Adapting this template to a new, unrelated event
- Swap the program logo and partner/funder logos for the *new* program's
  real identity — don't default back to "IDEA Lab" or its KOICA/Consortium
  KPC/MESRI partner set unless the new brief is genuinely the same program.
- Keep the plain white paragraph-first structure — this template's entire
  purpose is to read as a formal document, not a marketing visual; resist
  the urge to add photos, accent shapes, or poster-style treatments.
- Build one slide per section the brief needs (what the program is, who
  runs it, what it includes, partner credits, etc.) — each follows the same
  zone layout, only the headline and body text change.
- Never invent a partner name, figure (e.g. "600 start-ups"), or program
  detail; ask for any real value the brief doesn't supply.

## Canvas & background
- Landscape deck page (approx. 1920×1358px — verify the exact ratio against
  the source file before building; this is a PDF/slide export, not a fixed
  social-media canvas like every other template in this pack).
- White background (`#ffffff`) with the same whisper-level paper-grain
  texture used across the Idea Lab templates — subtle, never competing with
  text contrast.

## Zones (top to bottom, left to right)
1. **Header lockup** (top-left): Idea Lab program logo (icon + wordmark),
   small, consistent position across every page in the deck.
2. **Slide headline** (upper area, left-aligned, full width or ~80%): a
   bold headline in the program's teal/green accent color, either sentence
   case (e.g. "Qu'est-ce que le programme IDEA LAB") or all-caps (e.g.
   "PRÉSENTATION DES PARTENAIRES DU PROGRAMME") depending on the slide's
   register — section-title slides run all-caps, explainer slides run
   sentence case.
3. **Body column** (left ~65–70% of canvas, below the headline): one or more
   paragraphs of regular-weight dark gray/near-black body text, generous
   line-height, justified or left-aligned. A lead-in sentence may be set in
   **bold** immediately before a bullet list continues the thought (observed
   pattern: bold lead sentence → bullet list of program components).
4. **Partner logo sidebar** (right ~25–30% of canvas, vertically stacked,
   optional — present on content pages that credit specific funders): 1–3
   institutional/partner logos stacked with even vertical spacing, each at
   a modest, consistent size, right-aligned as a column. Omit this zone
   entirely on pages that don't need partner credit (don't leave empty
   space reserved for it).
5. **Page number** (bottom-right corner): a plain bold number in the
   program's accent teal/green color, no background chip, incrementing
   sequentially across the deck.

## Color palette (approximate — verify against source for exact hex)
- Background: white `#ffffff`.
- Headline: teal/green accent, ~`#1E8E6E` to ~`#1E9254` (same family as the
  green used elsewhere in Idea Lab/JAMBAARS materials — verify per-program).
- Body text: near-black warm gray, ~`#2a2a28`.
- Page number: same teal/green as the headline.
- Partner logos: full-color, as sourced — never recolor a real partner mark.

## Typography
- Program wordmark: same lockup treatment as the program's other materials.
- Headline: bold/extra-bold, teal/green, either sentence case or all-caps
  depending on slide register (section divider vs explainer).
- Body paragraphs: regular weight, dark gray, generous line-height (~1.4–1.5)
  for document readability — this is denser, smaller-scale text than any
  poster template in this pack.
- Bold lead-in sentence (before a bullet list): same size as body, bold
  weight only, no color change.
- Page number: bold, plain, no decoration.

## Content slots (fill these, never invent values)
- `{{program_logo}}`
- `{{slide_headline}}`, `{{headline_case}}` (sentence case vs all-caps)
- `{{body_paragraphs}}` — one or more real paragraphs
- `{{bullet_list_items[]}}` (optional, follows a bold lead-in sentence)
- `{{partner_logos[]}}` (optional sidebar, omit zone if not needed)
- `{{page_number}}`

## Do / Don't
- Do keep this template strictly paragraph/text-led — no large photo, no
  accent shapes, no CTA pill. If the brief wants visual punch, route it to
  `idea-lab-carrousel-slide.md` or another poster template instead.
- Do omit the partner-logo sidebar on pages that don't credit a specific
  partner, rather than leaving a visibly empty column.
- Do keep headline case consistent with the slide's role (all-caps reads as
  a section divider, sentence case reads as an explainer) rather than
  mixing arbitrarily within one deck.
- Don't shrink body text past comfortable document-reading size to force
  more content onto one page — split into an additional page instead.
- Don't pull in the louder accent colors (yellow/orange) used by the
  Goin' Digital or carousel templates — this document-style template stays
  in the calmer teal/green + white/gray register.
