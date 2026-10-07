---
name: goin-digital-posters
description: Generate a Goin' Digital program poster announcing an in-person panel/conference, either with one featured panelist or a moderator plus a multi-person lineup, including a registration QR code, by adapting one of two real, evidence-based layout patterns to a new session's actual details. Trigger on English requests ("create/design/make a poster/flyer for Goin Digital...", "panel poster with QR") and on French requests ("crée/fais/génère une affiche/un poster pour Goin Digital...", "affiche panel", "affiche avec QR code") for the Goin' Digital program.
user-invocable: true
---

# Goin' Digital — poster skill

This is the **agent-usable entry point**. Read it first.

**Language:** this skill's own instructions stay in English for reliable
instruction-following; the content you generate (every headline, label, and
placeholder) follows the brief's real language — French by default for
CONCREE/Goin' Digital work.

**Before building, read `side-files/build-lessons.md`** — real logos (crop, never redraw), real photos fetched with `side-files/fetch_photo.py` when none is supplied, layout pitfalls, and a mandatory headless-screenshot check so the first render is complete. `side-files/build_presentation.py` merges all posters into one html with sections; `side-files/crop_faces.py` crops faces for mockup photos; `side-files/crop_logo.py` crops a logo from a source poster with a transparent background.

Event types (3 pro posters): panel 1 intervenant (`08`), panel multi-intervenants (`12`), atelier (`13`). Always deliver the 3 types as one simple file (`side-files/build_presentation.py`, see `build-lessons.md` §8).

## Folder map

```
skills/goin-digital-posters/
├── SKILL.md                     ← you are here
├── examples/
│   └── 04-goin-digital-panel-announcement.html
├── assets/
│   └── concree-logo.svg         ← real CONCREE wordmark
├── references/
│   ├── overview.md
│   ├── goin-digital-panel-announcement.md
│   ├── goin-digital-panel-lineup-grid.md  ← no rendered example yet
│   └── source-posters/
└── side-files/
    ├── checklist.md              ← P0/P1/P2 checklist — read before rendering
    └── figma-build-notes.md      ← read if building directly in a Figma file (not HTML)
```

## What this skill does

Produces a single Goin' Digital panel/conference announcement poster
(HTML, ready to export as an image), picking the layout pattern that
matches whether the brief has ONE featured speaker or a moderator + MULTIPLE
panelists, and adapting it to the new session's real content. No specific
Goin' Digital session (a given panel topic, a given date) is assumed to
recur — every source this pack was built from was a one-off.

## Step 1 — pick the pattern file by panelist count

| If the brief is... | Open this file | Canvas |
| --- | --- | --- |
| An in-person panel/conference with ONE featured speaker photo + QR registration | `references/goin-digital-panel-announcement.md` | 4:5 portrait (3240×4050) |
| An in-person panel/conference with a moderator + MULTIPLE named panelists (3–4) + QR registration | `references/goin-digital-panel-lineup-grid.md` | 4:5 portrait (1080×1350) |

Read the matched file **in full** before building — it carries the exact
zone layout, an approximate color read (dark navy + yellow/lime accent),
typography treatment, and a content-slot checklist. Its `source-posters/`
sibling folder has the real captured poster it was measured from.

`goin-digital-panel-lineup-grid.md` has no rendered `examples/` file yet —
read the pattern file plus its `source-posters/` image directly before
building from it.

## Step 2 — never assume recurrence

- Keep the Goin' Digital wordmark and dark navy/yellow-lime accent pairing
  only as far as the new brief is genuinely another Goin' Digital session —
  this is a single-program skill, so the branding stays constant, but the
  session topic, date, venue, and named people must come from the new
  brief.
- Don't mix the two patterns in the same brief — pick one based on whether
  the brief has one featured speaker or a multi-person lineup.
- Never invent a panelist name, title, date, venue, or QR destination; ask
  for any real value the brief doesn't supply.
- Generate a real QR code pointing at the actual registration link; never
  place a decorative/non-functional QR graphic.

## Step 3 — check the checklist before rendering

- **Also read uild-lessons.md §10** (faults found in 8 posters by another model: leaked template names, white-on-white logos, fake QR, same face twice, same skeleton twice…) and tick the P0 block « added after the CONCREE GPT audit » in the checklist.

Read `side-files/checklist.md` and confirm every P0 item before delivering
the final poster.

## Reuse workflow

0. Open `examples/08-goin-digital-panel-pro.html` (dark navy + lime layout, Dakar photo watermark, arch portrait frame, QR block) — the "pro" quality bar: layered, real logos, real photo.
1. Read this `SKILL.md` and look at `examples/04-goin-digital-panel-announcement.html`
   once for the target quality bar.
2. Match the brief to one row in the Step 1 table and open that pattern
   file in full, plus its real source poster in
   `references/source-posters/`.
3. Fill every content slot with real, provided values — ask rather than
   invent.
4. Build the poster as a single self-contained HTML file at the pattern's
   canvas size — or build it natively inside a Figma file with the
   `use_figma` tool if the brief asks for a Figma deliverable rather than
   an HTML render; read `side-files/figma-build-notes.md` first for
   lessons specific to building these patterns in the Plugin API (minimum
   legible text size, placeholder/QR conventions for fictional content,
   SVG illustration upload gotchas, sizing a bordered info box to its
   actual content).
5. Run `side-files/checklist.md` before delivery.

## Provenance

Authored from real Goin' Digital posters captured in the CONCREE
design-system project and the "IDEA LAB" Figma file
(`figma.com/design/QiEzqqxt6esRZxLCZpAjkR`). Colors are visual
approximations — verify against the cited source image for pixel-exact
values. This skill was split out of a combined `poster-design` skill on
2026-10-01 so each CONCREE program's poster conventions can be triggered
and maintained independently — see the sibling skills `jambaars-ai-posters`,
`yeah-posters`, and `idea-lab-posters` for the other programs.
