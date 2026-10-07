# Building Wekomkom screens in Figma

## The file

| | |
| --- | --- |
| Working file | `zyYKIr49PoDeO9vroOG27F` — "Design wekomkom (Copy)", editable by the connected account (mamediarradieng@esp.sn) |
| Original | `a2r1R8eCYmxaTiLNIW7x9m` — read-only for this account (the MCP returns "you don't have edit access"). Never target it. |
| Design system page | `7:27` "00 — Wekomkom Design System" (sections 00–30, 192 components) |
| Designer's page | `0:1` "Ecran de base de notre designer" — the source of truth. **Never modify it.** |
| Canonical page | `461:27` « 22 — Assemblage final »: all 558 screens in 9 zones / 42 parcours, with the codes used in dev tickets. Screen ids per parcours are in `references/flows/*.md`. Read-only reference: put new work on the working pages. |
| Flow pages (working pages) | `114:27` 01 Pilote · `141:27` 02 Arrivée · `191:27` 03 Opportunité · `202:27` 04 Adia · `223:27` 05 Partager · `231:27` 06 Suivre · `245:27` 07 Ma carte · `254:27` 08 Préparation · `265:27` 09 Explorer · `349:65` 10 Alertes · `357:27` 11 Relais · `365:27` 12 Bureau · `386:16542` 13 Messages · `386:16543` 14 Vue acteur mobile · `386:16544` 15 Relais · `386:16545` 16 Confiance · `436:27` 17 Acheteurs · `436:28` 18 Mon compte · `441:27` 19 Moussa · `448:27` 20 Bailleurs · `450:27` 21 Tablette · `461:27` 22 Assemblage final |

If the user gives another Wekomkom file URL, check access first (`get_metadata`),
then confirm the same design-system page exists before reusing these IDs.

## Before any `use_figma` call

1. Load the `figma:figma-use` skill (mandatory), and `figma:figma-generate-design` for full screens. Pass `skillNames: "figma-use"` (or `"figma-use,figma-generate-design"`).
2. Read `references/design-dna.md` and `references/components.md` from this skill.
3. Inspect the target page first (read-only call): what exists, where there is free canvas.

## Fonts — known pitfall

The plugin environment exposes **Open Sans Regular, SemiBold, Bold** (plus Light,
ExtraBold, Condensed…), but **not "Open Sans Medium"**, although 16+ text styles
use Medium (Body/Default, Body/Large, Body/Message, Label/Button, Meta/Date…).

- Load fonts with `for (const s of ['Regular','SemiBold','Bold']) await figma.loadFontAsync({family:'Open Sans', style:s})`. Do **not** load Medium; it throws.
- Instances that *contain* Medium text can still be created and placed. Their TEXT properties mapped to Regular/SemiBold/Bold nodes can be set (tested: Carte opportunité Titre, Organisme, Montant).
- Setting text on a node whose font is Medium will fail. Leave that text as is and tell the user, or ask them to install the static Open Sans family (with Medium) on the machine running Figma. **Never swap Medium for another weight to work around it.**
- Note the style spelling: `SemiBold` (one word) in this file.

## Screen anatomy (measured on 1.01-H01 · Premier accueil, id 463:2243)

| Layer | Position / size | Made of |
| --- | --- | --- |
| Screen frame | 390 × 844, clips content, vertical overflow | fill = paint style `Gradient/Fond` |
| Navigation/Barre d’état | x 0, y 0, 390 × 54 | instance `69:2491` (Ton=Sombre on light) |
| Navigation/En-tête | x 17, y 64, 356 × 44 | instance `69:2633` (pick Type) |
| Contenu | x 17, y 124, width 356, vertical auto-layout, gap 24 (closest token: space/25) | instances of cards, titles, lists |
| Fond · bas | x 0, y 725, 390 × 119 | white fade gradient (0 → 96 % → 100 %) behind the tab bar |
| Navigation/Barre d’onglets | x 17, y 761, 356 × 63 | instance `69:2543` (Actif = current tab) |

Screens without tabs (conversation with Adia, flows, sheets) drop the tab bar and
usually use En-tête Type=Retour / Fermer / Parcours. Tall scrolling screens keep
width 390 and grow in height (e.g. 390 × 1515), or keep 844 with vertical overflow.

Place new screens on the relevant flow page, in a row, 40–60 px apart, right of the
existing content (scan `page.children` for the max x). Name them like the file:
`<flow>.<n>-<code> · <titre en français>` (e.g. `1.03-X05 · Filtrer par région`).

## Tested build snippet

Build with component instances, never by redrawing. Bind spacing/colours to variables
and apply named styles. Do not detach instances ("une instance détachée est une dette").

```js
for (const s of ['Regular', 'SemiBold', 'Bold']) await figma.loadFontAsync({ family: 'Open Sans', style: s });

// Instance of a component or of one variant of a set: inst('73:2527', { 'Hiérarchie': 'Principal', 'Taille': 'Grand' })
async function inst(id, variant = {}) {
  const node = await figma.getNodeByIdAsync(id);
  const comp = node.type === 'COMPONENT_SET'
    ? (node.children.find(c => Object.entries(variant).every(([k, v]) => c.variantProperties[k] === v)) || node.defaultVariant)
    : node;
  return comp.createInstance();
}
// Set a TEXT / BOOLEAN / INSTANCE_SWAP property by its visible label (keys carry a #id suffix)
function setProp(instance, label, value) {
  const key = Object.keys(instance.componentProperties).find(k => k.split('#')[0] === label);
  if (!key) throw new Error(`No property "${label}" on ${instance.name}: ${Object.keys(instance.componentProperties).join(', ')}`);
  instance.setProperties({ [key]: value });
}
const paintStyle = async name => (await figma.getLocalPaintStylesAsync()).find(s => s.name === name);
const variable = async name => (await figma.variables.getLocalVariablesAsync()).find(v => v.name === name);

const page = await figma.getNodeByIdAsync('265:27');            // target flow page
await figma.setCurrentPageAsync(page);
const maxX = Math.max(0, ...page.children.map(n => n.x + n.width));

const screen = figma.createFrame();
screen.name = '1.03-X05 · Filtrer par région';
screen.resize(390, 844); screen.x = maxX + 60; screen.y = 0;
await screen.setFillStyleIdAsync((await paintStyle('Gradient/Fond')).id);
screen.clipsContent = true; screen.overflowDirection = 'VERTICAL';

const content = figma.createAutoLayout('VERTICAL', { name: 'Contenu' });
screen.appendChild(content); content.x = 17; content.y = 124; content.resize(356, 100);
content.counterAxisSizingMode = 'FIXED'; content.primaryAxisSizingMode = 'AUTO';
content.setBoundVariable('itemSpacing', await variable('space/25'));

const card = await inst('24:756', { 'État': 'Ouverte' });        // Opportunités/Carte opportunité
content.appendChild(card); card.layoutSizingHorizontal = 'FILL';
setProp(card, 'Titre', 'Prêt équipement pour les transformatrices');
setProp(card, 'Montant', 'Jusqu’à 3 000 000 FCFA');

const status = await inst('69:2491', { 'Ton': 'Sombre' });      screen.appendChild(status); status.x = 0;  status.y = 0;
const header = await inst('69:2633', { 'Type': 'Explorer' });   screen.appendChild(header); header.x = 17; header.y = 64;
const tabs   = await inst('69:2543', { 'Actif': 'Explorer' });  screen.appendChild(tabs);   tabs.x = 17;   tabs.y = 761;

await screen.screenshot();
return { screenId: screen.id, contentId: content.id, cardId: card.id };
```

Instances keep their own variable bindings and styles. For anything you draw yourself
(a section title frame, a wrapper), bind `fills`/`strokes` to *Color* roles with
`figma.variables.setBoundVariableForPaint(paint, 'color', variable)` (it returns a new
paint; reassign the array) and padding/gap/radius to *Dimension* tokens, and apply text
styles with `await text.setTextStyleIdAsync(styleId)`.

## Validate

1. One `screen.screenshot()` after composition; compare to `references/screens/*.png`.
2. Check: nothing clipped, nothing overlapping the tab bar (content needs a bottom margin ≈ 107 px when the tab bar is shown), only one dark card, one primary button.
3. Run the checklist in `side-files/checklist.md`.
4. Return every created node ID.
