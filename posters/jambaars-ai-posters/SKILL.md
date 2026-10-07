---
name: jambaars-ai-posters
description: Generate a JAMBAARS AI program poster or invitation (single-event announcement, 3-4 speaker lineup grid, or formal letter-style invitation) by adapting one of three real, evidence-based layout patterns to a new event's actual details. Trigger on English requests ("create/design/make a poster/flyer/invitation for JAMBAARS AI...") and on French requests ("crée/fais/génère une affiche/un poster/une invitation pour JAMBAARS AI...", "affiche d'événement JAMBAARS") for the JAMBAARS AI Sénégal program.
user-invocable: true
---

# JAMBAARS AI — poster & invitation skill

This is the **agent-usable entry point**. Read it first — it directs
everything else in this skill.

**Language:** this skill's own instructions stay in English for reliable
instruction-following; the content you generate (every headline, label, and
placeholder) follows the brief's real language — French by default for
CONCREE/JAMBAARS work.

**Before building, read `side-files/build-lessons.md`** — real logos (crop, never redraw), real photos fetched with `side-files/fetch_photo.py` when none is supplied, layout pitfalls, and a mandatory headless-screenshot check so the first render is complete. `side-files/build_presentation.py` merges all posters into one html with sections; `side-files/crop_faces.py` crops faces for mockup photos; `side-files/crop_logo.py` crops a logo from a source poster with a transparent background.

Event types (3 pro posters): demo day (`09`), intervenants (`14`), invitation formelle (`15`). Always deliver the 3 types as one simple file (`side-files/build_presentation.py`, see `build-lessons.md` §8).

## Folder map

```
skills/jambaars-ai-posters/
├── SKILL.md                     ← you are here
├── examples/                    ← rendered few-shot examples
│   ├── 01-event-announcement.html
│   └── 02-speaker-lineup.html
├── assets/
│   ├── concree-logo.svg         ← real CONCREE wordmark
│   └── example-photo-entrepreneur.png  ← real CONCREE site photo
├── references/
│   ├── overview.md               ← human-readable index
│   ├── jambaars-event-announcement.md
│   ├── jambaars-speaker-lineup.md
│   ├── jambaars-formal-invitation.md  ← no rendered example yet
│   └── source-posters/           ← real captured posters each pattern was measured from
└── side-files/
    ├── checklist.md              ← P0/P1/P2 checklist — read before rendering
    └── figma-build-notes.md      ← read if building directly in a Figma file (not HTML)
```

## What this skill does

Produces a single JAMBAARS AI event poster or invitation (HTML, ready to
export as an image/PDF), by picking the layout pattern that best matches
the brief's *format* and adapting it to the new event's real content. No
specific JAMBAARS AI session is assumed to recur — every example this pack
was built from was a one-off cohort/Demo Day. The reusable asset is the
**composition**, not the specific event name.

## Step 1 — pick the pattern file by format

| If the brief is... | Open this file | Canvas |
| --- | --- | --- |
| One event, one headline, one date/location, optional single photo | `references/jambaars-event-announcement.md` | 1:1 square (2160×2160) |
| Listing 3–4 named confirmed speakers with photos | `references/jambaars-speaker-lineup.md` | 1:1 square (2160×2160) |
| A formal letter-style invitation (salutation + paragraphs, no photo) | `references/jambaars-formal-invitation.md` | 2:3 portrait (600×900) |

Read the matched file **in full** before building — it carries the exact
zone layout, an approximate color read, typography treatment, and a
content-slot checklist. Its `source-posters/` sibling folder has the real
captured poster it was measured from. If nothing fits, say so and propose
a new layout rather than forcing content into the wrong pattern.

`jambaars-formal-invitation.md` has no rendered `examples/` file yet — read
the pattern file plus its `source-posters/` image directly before building
from it.

## Step 2 — never assume recurrence

Every pattern file was observed in a specific JAMBAARS AI session (Demo
Day, Reveal & MVP Showcase, a speaker panel) that **will not necessarily be
the one in the new brief**:
- Keep the JAMBAARS AI logo lockup and green/orange accent pairing only if
  the new brief is genuinely another JAMBAARS AI event — this is a
  single-program skill, so the branding stays constant, but the specific
  event name, date, speakers, and photo must come from the new brief.
- Never invent a date, name, metric, partner, or QR destination; ask for
  any real value the brief doesn't supply.
- Source real photos from the project's `assets/`, `logos/`, `imagery/`
  folders first; never substitute a generated or stock stand-in for a
  named real person or event.

Each pattern file also carries its own "Adapting this template" guidance —
follow that over anything summarized here if the two ever seem to differ.

## Step 3 — check the checklist before rendering

- **Also read uild-lessons.md §10** (faults found in 8 posters by another model: leaked template names, white-on-white logos, fake QR, same face twice, same skeleton twice…) and tick the P0 block « added after the CONCREE GPT audit » in the checklist.

Read `side-files/checklist.md` and confirm every P0 item before delivering
the final poster. Fix any failure in place; do not ship a poster that fails
a P0 check.

## Reuse workflow

0. Open `examples/09-jambaars-demo-day-pro.html` (light layout, checker/arc filigree, curved real photo, gradient date band, speaker chips) — the "pro" quality bar: layered, real logos, real photo.
1. Read this `SKILL.md` and look at the matching `examples/*.html` once for
   the target quality bar.
2. Match the brief to one row in the Step 1 table and open that pattern
   file in full, plus its real source poster in
   `references/source-posters/` if present.
3. Fill every content slot in the pattern file's checklist with real,
   provided values — ask rather than invent.
4. Build the poster as a single self-contained HTML file at the pattern's
   canvas size — or build it natively inside a Figma file with the
   `use_figma` tool if the brief asks for a Figma deliverable rather than
   an HTML render; read `side-files/figma-build-notes.md` first for
   lessons specific to building these patterns in the Plugin API
   (minimum legible text size, placeholder conventions for fictional
   content, SVG illustration upload gotchas).
5. Run `side-files/checklist.md` before delivery.

## Provenance

Authored from real posters captured in the CONCREE design-system project
and the "IDEA LAB" Figma file (`figma.com/design/QiEzqqxt6esRZxLCZpAjkR`).
Colors listed in each pattern file are visual approximations — verify
against the cited source image for pixel-exact values. This skill was
split out of a combined `poster-design` skill on 2026-10-01 so each CONCREE
program's poster conventions can be triggered and maintained independently
— see the sibling skills `yeah-posters`, `goin-digital-posters`, and
`idea-lab-posters` for the other programs.
