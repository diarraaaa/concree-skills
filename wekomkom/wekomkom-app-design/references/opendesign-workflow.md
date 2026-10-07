# Building Wekomkom prototypes in OpenDesign

OpenDesign is the local design workspace (MCP server `open-design`). In replies to
the user, call it "OpenDesign"; never repeat tool names or ids as product copy.

Default approach: **write the HTML yourself** from this skill's tokens and example,
then hand the user the OpenDesign preview. It is faithful to the Figma system and
deterministic. Use OpenDesign's own generation run only when the user asks for it
(see the last section).

## Steps

1. **Project.** Reuse one if the user names it (`list_projects`), otherwise
   `create_project` with a clear French name, e.g. `Wekomkom — Explorer · Filtrer par région`.
   Keep all Wekomkom screens of one request in one project.
2. **Shared files** (once per project, with `write_file`):
   - `wekomkom-tokens.css` ← contents of `assets/wekomkom-tokens.css`
   - `wekomkom-components.css` ← contents of `assets/wekomkom-components.css` (status bar,
     header, cards, pills, switches, buttons, listen, conversation, timeline, toast)
   - `assets/logo-mark-color.svg`, `assets/logo-mark-white.svg`, `assets/logotype.svg` ← from `assets/`
3. **Screens.** For each screen, start from `examples/accueil.html` (structure, class
   names, the 390 × 844 `.screen` frame, status bar, header, content column, floating
   tab bar). Then:
   - change the stylesheet link to `wekomkom-tokens.css` and logo paths to `assets/…`;
   - compose the content from the patterns in `references/components.md` (same names
     in HTML comments, e.g. `<!-- Opportunités/Carte opportunité -->`) using only
     `var(--wk-…)` tokens: no raw hex, no off-scale spacing or radius;
   - write French copy that follows `references/design-dna.md` (tu, short sentences,
     no forbidden words, formats for amounts and dates).
   Create the first file with `create_artifact` (name `index.html` or
   `<flow>-<screen>.html`); iterate with `write_file`.
   For several screens, either one file per screen or a single `index.html` that lays
   the 390 px screens side by side with their names above them.
4. **Check** before handing over. Render locally with headless Edge (see below) or
   open the project's `previewUrl` (`get_project`), then compare with
   `references/screens/*.png` and run `side-files/checklist.md`.
5. **Deliver** the preview link and a one-line summary per screen.

Photos: the system requires real photos of Senegalese entrepreneurs. Use photos the
user provides; otherwise use the `--wk-gradient-avatar` initials fallback for people and
a neutral `--wk-bg-surface-inverse` block labelled « Photo réelle » for the dark card.
Never use stock or AI-generated faces.

Icons: inline SVG, 24 px box, stroke 1.8, `currentColor`, always with a visible label
except universal gestures (back, close, search). Match the Figma icon names.

## Local render check (Windows)

```powershell
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
& $edge --headless=new --disable-gpu --hide-scrollbars --window-size=440,900 --virtual-time-budget=4000 `
  --screenshot="$env:TEMP\wk-screen.png" "file:///C:/path/to/screen.html"
```

Then read the PNG and compare it to the reference. Fix and re-render once.

## Sending an OpenDesign screen to Figma (capture)

Use this when the user wants the OpenDesign prototype *as a Figma frame* (e.g. in
the CONCREE posters file `snjiINPtxBPtgxvUi4QrEl`). The result is a pixel-faithful
frame made of raw layers, not instances of the Wekomkom components; for a
component-based screen inside the Wekomkom file, use `figma-workflow.md` instead.
Tested on 2026-10-06 with `examples/opportunite-detail.html` → node `61:2`.

1. Author the HTML so it captures cleanly: no `mask-image`, `background-clip:text`,
   blend modes or `::before/::after` drawings (use real elements and inline SVG).
   Give the screen root a class (`.screen`).
2. Put the HTML and `wekomkom-tokens.css` in the OpenDesign project (`create_artifact` /
   `write_file`, or copy into the project's `resolvedDir`). OpenDesign serves them at
   `http://127.0.0.1:<port>/api/projects/<project-id>/raw/<file>`; the port is in the
   project's `studioUrl` (`get_project`). Check with `curl` that both return 200.
3. Make a temporary copy `_capture-<name>.html` with, before `</head>`:
   `<script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>`,
   a `window.scrollTo(0,0)` on load, and `html,body{overflow:hidden!important}`.
4. `generate_figma_design` with the target `fileKey` → capture id. Open in the default
   browser (PowerShell) **one capture at a time**:
   `Start-Process "<raw url of the copy>#figmacapture=<id>&figmaendpoint=<url-encoded endpoint>&figmadelay=1500&figmaselector=.screen"`
5. Poll `generate_figma_design` with the same `captureId` every ~5 s until completed
   (took 4 polls). Screenshot the returned node and compare with the local render.
6. **Choose the destination page up front.** Without `nodeId`, the capture lands on
   the file's *first* page. Create (or reuse) a dedicated page with `use_figma`, then
   pass its id as `nodeId` to `generate_figma_design`: the capture goes straight
   there (tested with page `62:2`). Afterwards set x/y (row, 60 px apart) and rename
   the frame `<flow>.<n>-<code> · <titre>`. Never rename or touch other pages'
   content (another session may own it).
7. Delete the temporary `_capture-*.html` copy from the project.

## Using OpenDesign's generation run (only on request)

1. Make sure the project already contains `wekomkom-tokens.css`, the logos and one
   finished example screen (step 2–3 above) so the run has something to imitate.
2. `start_run` with a prompt that includes: the screen brief; "Use only the CSS
   variables in wekomkom-tokens.css and copy the structure of <example file>";
   the nine visual traits and the forbidden-words list from `design-dna.md`;
   "French copy, tutoiement respectueux". Pass a fresh `requestId` UUID.
3. Poll `get_run` until it finishes, then review the output against the checklist
   and fix with `write_file` where it drifted (raw colours, wrong radii, extra dark
   cards, gradient on an action button, forbidden words).
