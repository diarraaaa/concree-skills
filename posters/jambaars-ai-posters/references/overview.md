# JAMBAARS AI — poster skill pack

Agents: start at [`../SKILL.md`](../SKILL.md), the agent-usable entry point
that directs everything in this skill. This overview is the human-readable
version of the same index, kept in sync with it.

This folder documents **poster layout/style patterns** observed in real
JAMBAARS AI campaign visuals — three representative source posters are
copied locally into [`source-posters/`](source-posters/) for quick visual
reference. Each file below was written after visually inspecting at least
one real source asset per family — nothing here is invented from filenames
alone.

## These are inspiration, not recurring-event recipes

Every poster this pack is based on — a Demo Day, a Reveal & MVP Showcase, a
speaker panel — was a one-off session. Treat each type file as
**compositional DNA to adapt**, not a fill-in-the-blanks recipe for
reproducing the same named event: match a brief to whichever template's
*format* fits, then swap the event name, date, speakers, and photos for the
new brief's real, current details. Each type file has its own "Adapting
this template" section spelling out what to change versus what composition
to keep.

## Poster types in this pack

| File | Format | Canvas | Based on (real source assets) |
| --- | --- | --- | --- |
| [`jambaars-event-announcement.md`](jambaars-event-announcement.md) | Single-event announcement | Square 1:1 (2160×2160) | `source-posters/DEMO-DAY-FINALE-Annonce.png` |
| [`jambaars-speaker-lineup.md`](jambaars-speaker-lineup.md) | 3–4 speaker grid | Square 1:1 (2160×2160) | `source-posters/INTERVENANTS-2.png` |
| [`jambaars-formal-invitation.md`](jambaars-formal-invitation.md) | Letter-style invitation | Portrait 2:3 (600×900) | `source-posters/JAMBAARS-Formal-Invitation.png` (captured from the "IDEA LAB" Figma file, frame "Invitation") |

## How to use this pack

1. Open the matching type file for the brief's format (see the table above
   or Step 1 in `../SKILL.md`).
2. Follow its canvas size and zone layout exactly — these are load-bearing
   composition choices (logo lockup position, photo bleed side, footer
   partner strip), not arbitrary style.
3. Fill the content slots listed at the bottom of the type file with real
   event details. Never invent a name, date, or metric — ask if a slot's
   real value isn't provided.
4. Reuse real speaker/partner photography when it already exists in the
   project's `assets/`, `imagery/`, or `logos/` folders; otherwise flag
   that a real photo is needed rather than drawing a placeholder person.
5. Keep hex values labeled "approximate" as a starting point; sample the
   cited source image directly if pixel-exact brand color matching is
   required for print or paid media.
