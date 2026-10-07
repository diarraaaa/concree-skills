---
name: idea-lab-posters
description: Generate an Idea Lab program poster, carousel, startup spotlight card, or program dossier page (cohort launch, multi-slide Instagram carousel with cover + topic slides, named-startup/founder spotlight, or text-led info-deck slide) by adapting one of four real, evidence-based layout patterns to a new cohort's actual details. Trigger on English requests ("create/design/make a poster/carousel/dossier for Idea Lab...", "startup spotlight card") and on French requests ("crée/fais/génère une affiche/un carrousel/un dossier pour Idea Lab...", "affiche de lancement de cohorte", "carte startup") for the Idea Lab program.
user-invocable: true
---

# Idea Lab — poster, carousel & dossier skill

This is the **agent-usable entry point**. Read it first.

**Language:** this skill's own instructions stay in English for reliable
instruction-following; the content you generate (every headline, label, and
placeholder) follows the brief's real language — French by default for
CONCREE/Idea Lab work.

Event types (3 pro posters): appel à candidatures (`06a`), slide thématique (`06b`), spotlight startup (`06c`); dossier page `06d`. Always deliver the 3 types as one simple file (`side-files/build_presentation.py`, see `build-lessons.md` §8).

## Folder map

```
skills/idea-lab-posters/
├── SKILL.md                     ← you are here
├── examples/
│   ├── 05-idea-lab-cohort-launch.html
│   └── 06a-idea-lab-cover-pro.html (+ 06b topic, 06c spotlight, 06d dossier)  ← carousel cover+topic, spotlight, dossier (complete)
├── assets/                      ← REAL logos, ready to use (transparent PNG/SVG)
│   ├── concree-logo.svg         ← CONCREE, light backgrounds
│   ├── logo-concree-dark.png    ← CONCREE, dark backgrounds
│   ├── logo-idealab.png         ← Idea Lab lockup
│   ├── logo-mesri.png · logo-koica.png · logo-kpc.png
│   ├── funders-expertise-giz.png
│   ├── partners-cover-strip.png · partners-spotlight-strip.png
│   ├── photos/                  ← real free-licensed theme photos + credits.json
│   ├── people/                  ← MAQUETTE face crops (public figures, CC) + credits.json
│   └── example-photo-innovation.png  ← real CONCREE site photo
├── references/
│   ├── overview.md
│   ├── idea-lab-cohort-launch.md
│   ├── idea-lab-carrousel-slide.md         ← example 06 (cover + topic)
│   ├── idea-lab-startup-spotlight-card.md  ← example 06 (spotlight)
│   ├── idea-lab-program-dossier-slide.md   ← example 06 (dossier)
│   └── source-posters/
└── side-files/
    ├── build-lessons.md          ← READ FIRST: logos, illustrations, layout pitfalls, visual check
    ├── crop_faces.py             ← detect + crop faces, writes a contact sheet
    ├── build_presentation.py     ← merge all posters into ONE html with sections (Desktop deliverable)
    ├── crop_logo.py              ← crop a real logo from a source poster, transparent bg
    ├── fetch_photo.py            ← download real free-licensed photos (Wikimedia Commons) when none supplied
    ├── checklist.md              ← P0/P1/P2 checklist — read before rendering
    └── figma-build-notes.md      ← read if building directly in a Figma file (not HTML)
```

## What this skill does

Produces a single Idea Lab visual — a cohort-launch poster, a multi-slide
carousel, a startup/founder spotlight card, or a program dossier page —
by picking the layout pattern that matches the brief's *format* and
adapting it to the new cohort's real content. No specific Idea Lab cohort
(a given cohort number, a given call theme, a given startup) is assumed to
recur — every source this pack was built from was one specific cohort's
material.

## Step 1 — pick the pattern file by format

| If the brief is... | Open this file | Canvas |
| --- | --- | --- |
| Launching a new program cohort with an external partner | `references/idea-lab-cohort-launch.md` | Square 1:1 |
| A multi-slide Instagram/LinkedIn carousel (cover + topic slides) | `references/idea-lab-carrousel-slide.md` | Square 1:1 (1080×1080), multi-slide |
| Introducing one named startup/founder/laureate (photo + pitch) | `references/idea-lab-startup-spotlight-card.md` | Square 1:1 (1080×1080) |
| A multi-page text dossier/PDF explaining the program (no photo, paragraph-led) | `references/idea-lab-program-dossier-slide.md` | Landscape deck page |

Read the matched file **in full** before building — it carries the exact
zone layout, an approximate color read, typography treatment, and a
content-slot checklist. Its `source-posters/` sibling folder has the real
captured poster/slide it was measured from.

Every pattern now has a rendered example: `examples/05-…` (cohort launch) and
`examples/06a…06d` (carousel cover + topic, spotlight, dossier). Open the one
matching the brief and use it as the quality bar — a result must be at least
this complete (real logos, illustrations, partner strip, no gray boxes).

## Step 2 — never assume recurrence

- Keep the Idea Lab logo and accent treatment only as far as the new brief
  is genuinely another Idea Lab cohort/campaign — this is a single-program
  skill, so the branding stays constant, but the cohort number, call theme,
  partner names, startup names, and founder details must come from the new
  brief.
- Build one card per startup/laureate when using
  `idea-lab-startup-spotlight-card.md`, and one slide per sub-theme when
  using `idea-lab-carrousel-slide.md` — never invent a startup, founder,
  pitch, or sub-theme.
- Keep `idea-lab-program-dossier-slide.md` strictly paragraph/text-led —
  no large photo, no accent shapes, no CTA pill. If the brief wants visual
  punch instead, route it to one of the other three patterns.
- Never invent a date, name, metric, partner, or figure; ask for any real
  value the brief doesn't supply.

## Step 3 — check the checklist before rendering

- **Also read uild-lessons.md §10** (faults found in 8 posters by another model: leaked template names, white-on-white logos, fake QR, same face twice, same skeleton twice…) and tick the P0 block « added after the CONCREE GPT audit » in the checklist.

Read `side-files/checklist.md` and confirm every P0 item before delivering
the final poster/slide.

## Reuse workflow

1. Read `side-files/build-lessons.md` (mandatory), this `SKILL.md`, and open
   the matching example (`05-…` or `06a…06d`) for the quality bar.
2. Match the brief to one row in the Step 1 table and open that pattern
   file in full, plus its real source image in
   `references/source-posters/`.
3. Fill every content slot with real, provided values — ask rather than
   invent.
4. Reuse the real logos in `assets/` (crop missing ones with
   `side-files/crop_logo.py`) and draw a rich SVG illustration where no real
   photo exists — never deliver gray boxes or `{{logo}}` placeholders.
   **If the user supplies no image, fetch a real free-licensed photo** with
   `side-files/fetch_photo.py` (see `build-lessons.md` §3) — real photos for
   themes/ambiance, never as the portrait of a named or fictional person.
   Build the deliverable as a single self-contained HTML file at the
   pattern's canvas size — or build it natively inside a Figma file with
   the `use_figma` tool if the brief asks for a Figma deliverable rather
   than an HTML render; read `side-files/figma-build-notes.md` first for
   lessons specific to building these patterns in the Plugin API (minimum
   legible text size, placeholder conventions for fictional content, SVG
   illustration upload gotchas).
5. Render a headless screenshot, LOOK at it, fix overlaps/clipping, then run
   `side-files/checklist.md`. Open the final HTML in the user's browser.
   If the Figma MCP reports its plan limit, deliver HTML and say Figma is
   pending — do not retry.

## Provenance

Authored from real Idea Lab posters captured in the CONCREE design-system
project and the "IDEA LAB" Figma file
(`figma.com/design/QiEzqqxt6esRZxLCZpAjkR`) — including a UCAD/makerspace
program dossier and a Cohorte 10 carousel series found during a full file
survey. Colors are visual approximations — verify against the cited source
image for pixel-exact values. This skill was split out of a combined
`poster-design` skill on 2026-10-01 so each CONCREE program's poster
conventions can be triggered and maintained independently — see the
sibling skills `jambaars-ai-posters`, `yeah-posters`, and
`goin-digital-posters` for the other programs.
