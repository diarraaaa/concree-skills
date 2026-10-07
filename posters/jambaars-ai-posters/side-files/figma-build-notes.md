# Building directly in Figma (not just HTML)

The `examples/*.html` files and the "Reuse workflow" in `SKILL.md` show the
HTML output path. A poster can also be built **natively inside a Figma
file** using the `use_figma` tool (Figma Plugin API) instead of — or in
addition to — the HTML render. Load the `figma-use` skill first; it owns
the Plugin API rules. The notes below are specific lessons from building
these poster patterns natively in Figma, on top of that skill's general
guidance.

## Minimum legible text size

On these large export canvases (2160–3240px wide), text under ~26–28px
reads as noticeably too small once the frame is viewed at normal zoom or
exported — even though it looked fine while zoomed into the Plugin API
editor. Treat these as floors, not just the pattern file's literal
approximate sizes:
- Body copy / paragraph / role text: **≥ 28px**.
- Small labels (eyebrow text, footer logos row, badge text): **≥ 26px**.
- Never go below 22px for anything meant to be read, even a secondary
  label.
If a pattern file's own Typography section implies something smaller,
bump it to these floors rather than following the literal px — the
pattern files describe *relative* hierarchy, not exact minimums.

## Fictional / placeholder content (demo posters, no real brief yet)

When asked to fill a poster with fictional data before real details exist:
- **Never render a real photo (stock, generated-photoreal, or reused site
  asset) under a fictional person's name.** That misattributes a real or
  real-looking likeness to a made-up identity. Use an abstract avatar
  instead: a solid-color circle/shape with the person's initials, clearly
  not a photograph.
- **Never leave a QR code that looks functional but isn't.** If the
  pattern calls for a registration QR and no real URL exists yet, draw an
  obviously-placeholder QR-pattern graphic and label it explicitly, e.g.
  "(exemple fictif — non fonctionnel)" directly beside it.
- **Illustrative art is fine as a stand-in for a missing real photo** (a
  featured photo, a theme/sector photo) — generate a flat-design,
  non-photorealistic SVG illustration (abstract figures, sector-relevant
  icons/motifs) rather than leaving the zone empty or faking a photo. This
  gives a real preview of the composition without misrepresenting anyone
  real. Keep illustration colors inside the pattern's own documented
  palette.

## Uploading illustration SVGs via `upload_assets`

- Request one upload URL per asset (`count: N`), then POST each file with
  `multipart/form-data` (`-F "file=@path"` in curl) — this preserves the
  filename as the Figma layer name.
- **Do not assume output order matches request order when POSTing
  multiple uploads in parallel** (e.g. several `curl ... &` backgrounded
  in one shell call). The responses can interleave in completion order,
  not launch order. Always read each response's own `placedOnNodeId` /
  `imageHash` and verify which asset landed where — take a screenshot
  after placing multi-asset uploads before moving on, and be ready to swap
  nodes between frames if they land reversed.
- An uploaded SVG lands as a new top-level node on the current page, not
  as a fill on an existing node (`nodeIds` is ignored for SVGs). Reparent
  it into the target frame with `frame.appendChild(node)`, then explicitly
  set `x`, `y`, and `resize(w, h)` — don't assume it's already positioned
  correctly.
- Z-order after `appendChild` places the node **last** (frontmost). For a
  background/theme illustration meant to sit behind text and cards, follow
  with `frame.insertChild(0, node)` to send it to the back. For an
  illustration placed late that should NOT cover an existing element
  (e.g. a credit tag), either reorder the covered element back to front
  with `insertChild(frame.children.length - 1, node)`, or simpler: resize
  the illustration so its bounds don't reach the other element at all —
  the latter is more robust than relying on z-order alone.

## Text node sizing gotcha (Plugin API)

`textAutoResize = 'HEIGHT'` does not reliably recompute `height`
synchronously right after a `resize()` call in the same script — reading
`.height` immediately afterward can still report the old value, and the
rendered text silently clips instead of wrapping visibly. The reliable
pattern for a wrapped, non-clipping text box:
```js
text.textAutoResize = 'NONE';
text.resize(width, generousFixedHeight); // pick a height with real margin, not the tightest estimate
```
Also watch for a second, easy-to-miss cause of the same symptom: a
sibling shape (e.g. a photo circle/card) positioned **on top of** the
text's bounding box in z-order, silently covering the tail end of a line.
If text looks clipped, check both the box height *and* what else overlaps
its bounds before assuming it's a wrap/height bug.

## Don't leave a bordered content box mostly empty

If a pattern's zone (e.g. an outlined info box) has a fixed height from
the source poster but this brief's actual content is shorter, **resize the
box to wrap its content with modest padding** rather than keeping the
original tall box with a large empty gap at the bottom. A noticeably
top-heavy box with dead space below reads as unfinished.
