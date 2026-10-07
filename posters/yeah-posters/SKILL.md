---
name: yeah-posters
description: Generate a YEAH (Yaakaar Jeunesse & Entrepreneuriat) program poster for a filière webinar or Space/discussion session, with moderator + panelist cutouts and an agenda variant, by adapting a real, evidence-based layout pattern to a new session's actual details. Trigger on English requests ("create/design/make a poster/flyer for YEAH...", "webinar poster", "Space announcement") and on French requests ("crée/fais/génère une affiche/un poster pour YEAH...", "affiche webinaire", "affiche Space") for the YEAH program.
user-invocable: true
---

# YEAH — poster skill

This is the **agent-usable entry point**. Read it first.

**Language:** this skill's own instructions stay in English for reliable
instruction-following; the content you generate (every headline, label, and
placeholder) follows the brief's real language — French by default for
CONCREE/YEAH work.

**Before building, read `side-files/build-lessons.md`** — real logos (crop, never redraw), real photos fetched with `side-files/fetch_photo.py` when none is supplied, layout pitfalls, and a mandatory headless-screenshot check so the first render is complete. `side-files/build_presentation.py` merges all posters into one html with sections; `side-files/crop_faces.py` crops faces for mockup photos; `side-files/crop_logo.py` crops a logo from a source poster with a transparent background.

Event types (3 pro posters): Space sur X (`07`), webinaire (`10`), atelier présentiel (`11`). Always deliver the 3 types as one simple file (`side-files/build_presentation.py`, see `build-lessons.md` §8).

## Folder map

```
skills/yeah-posters/
├── SKILL.md                     ← you are here
├── examples/
│   └── 03-yeah-filiere-webinar-space.html
├── assets/
│   └── concree-logo.svg         ← real CONCREE wordmark
├── references/
│   ├── overview.md
│   ├── yeah-filiere-webinar-space.md
│   └── source-posters/
└── side-files/
    ├── checklist.md              ← P0/P1/P2 checklist — read before rendering
    └── figma-build-notes.md      ← read if building directly in a Figma file (not HTML)
```

## What this skill does

Produces a single YEAH filière webinar or Space/discussion poster (HTML,
ready to export as an image), adapting the one documented layout pattern to
the new session's real content. No specific session (a given webinar
topic, a given filière like mangue or anacarde) is assumed to recur — every
source this pattern was built from was a one-off topic reusing the same
template, re-themed each time (see the "Instagram post" note in
`references/overview.md`).

## Step 1 — read the pattern file

Open `references/yeah-filiere-webinar-space.md` **in full** before
building — it carries the exact zone layout (moderator + panelist cutouts,
agenda banner variant, format badge Space vs. Webinaire), an approximate
color read (YEAH green + Mastercard Foundation co-branding), typography
treatment, and a content-slot checklist. Its `source-posters/` sibling
folder has a real captured poster for direct visual comparison.

This is currently the only pattern in this skill. If a brief needs a YEAH
visual that doesn't fit this format (e.g. a speaker-grid lineup, a cohort
launch), say so rather than forcing it into this template — that shape of
poster hasn't been observed for YEAH yet.

## Step 2 — never assume recurrence

- Keep the YEAH logo, "Yaakaar Jeunesse & Entrepreneuriat" wordmark, and
  Mastercard Foundation co-branding only as far as the new brief is
  genuinely another YEAH session — this is a single-program skill, so the
  branding stays constant, but the topic, filière, date, moderator, and
  panelists must come from the new brief.
- Swap the format badge between "Space" and "Webinaire" based on what the
  brief actually describes.
- Never invent a date, name, filière, or partner; ask for any real value
  the brief doesn't supply.

## Step 3 — check the checklist before rendering

- **Also read uild-lessons.md §10** (faults found in 8 posters by another model: leaked template names, white-on-white logos, fake QR, same face twice, same skeleton twice…) and tick the P0 block « added after the CONCREE GPT audit » in the checklist.

Read `side-files/checklist.md` and confirm every P0 item before delivering
the final poster.

## Reuse workflow

1. Read this `SKILL.md` and look at `examples/07-yeah-space-pro.html` (the layered "pro" bar — real logos, watermark photo, glass cards) and `examples/03-yeah-filiere-webinar-space.html`
   once for the target quality bar.
2. Open `references/yeah-filiere-webinar-space.md` in full.
3. Fill every content slot with real, provided values — ask rather than
   invent.
4. Build the poster as a single self-contained HTML file at the pattern's
   canvas size — or build it natively inside a Figma file with the
   `use_figma` tool if the brief asks for a Figma deliverable rather than
   an HTML render; read `side-files/figma-build-notes.md` first for
   lessons specific to building this pattern in the Plugin API (minimum
   legible text size, placeholder conventions for fictional content, SVG
   illustration upload gotchas).
5. Run `side-files/checklist.md` before delivery.

## Provenance

Authored from real YEAH posters captured in the CONCREE design-system
project. Colors are visual approximations — verify against the cited
source image for pixel-exact values. This skill was split out of a
combined `poster-design` skill on 2026-10-01 so each CONCREE program's
poster conventions can be triggered and maintained independently — see the
sibling skills `jambaars-ai-posters`, `goin-digital-posters`, and
`idea-lab-posters` for the other programs.
