---
name: wekomkom-pilotage-design
description: Design Wekomkom screens for the people who steer and fund the ecosystem without seeing individuals — bailleurs (programme funders) and the State / public sector (Direction de l'entrepreneuriat) — with aggregated figures, regional maps, analyses, programme design and reports, always anonymous (never a number under 5). Use for "vue bailleur", "ce qui avance", "où agir", "analyses", "rapport du mois", "vue de l'État", "piloter à l'échelle du pays", "équité entre les territoires", "carte des régions", "indicateurs Wekomkom". Not for a structure's own screens (wekomkom-vue-acteur-design) nor the entrepreneur app (wekomkom-app-design).
user-invocable: true
---

# Wekomkom — pilotage (bailleurs and État)

Zones **5 · Bailleurs** (section `463:51164`) and **8 · État et secteur public** (section
`506:28413`) of page `461:27` « 22 — Assemblage final », file `zyYKIr49PoDeO9vroOG27F`.
Working page `448:27` « 20 — Bailleurs et pairs » (Guide `449:25609`) for 5.01; 5.02 and
8.01 exist only on page 22.

## Step 1 — load the shared system

From `../wekomkom-app-design/`: `references/design-dna.md` (read in full),
`components.md`, `tokens.md`, `figma-workflow.md` or `opendesign-workflow.md`, `assets/`,
`references/flows/README.md`, `references/flows/9-socle-commun.md` (profiles 9.01-P05
bailleur and P06 État, Zone géographique 9.03). Run `side-files/checklist.md` at the end.

## The one rule that decides everything: nobody is recognisable

- Totals only, by zone and period. **A number under 5 is never shown, even by crossing filters** — show « Moins de 5 » (5.01-B04, B06). Filters that would isolate a person are refused with an explanation.
- A bailleur never sees a person nor what she shared. The État sees nothing personal without a partnership and consent; a unique identifier exists only under partnership (8.01-E07, E08).
- **A connection counts when it happened**: « confirmée par les deux » vs « par l'entrepreneure seule » stay distinct. An agreement is not counted as money paid; a contested payment is not counted (B02).

## How the screens look (mobile 390, same system)

- Same dawn background, white cards, one dark card at most, pills, semantic colours. Still « tu » (« Bonjour Ndèye »), short sentences, the forbidden words still apply (write « tableau de bord » or better the thing itself, never « dashboard »).
- **Key figures as cards**: big number (Bold) + one-line label + scope/date in Meta (« 2 340 · entrepreneures accompagnées · janv. à oct. 2026 »). Absolute numbers before percentages. Amounts per design-dna formats (« 2,9 Mds FCFA » acceptable for national totals).
- **Regional map of Senegal** as a tile grid with region codes (LG, SL, MT, DK, TH, DB, FK, KL, KF, TB, ZG, SD, KD, KG): darker = more, legend « Peu · Beaucoup »; **under-covered regions framed in orange** with the threshold written (« Encadré orange : moins de 2 appuis pour 1 000 entreprises recensées »). Colour never alone: the value is written in each tile.
- Every view ends with **its source and date** (« Source : Wekomkom, appuis confirmés au 1er octobre 2026 » / « … et répertoire national des entreprises, 2025 »).
- A context line under the greeting: programme or institution + « données au … ».
- Chips on top: Zone géographique (9.03), secteur, type d'appui, public.
- « Regarder de plus près » menu rows lead to the analyses.

## Screens (page 22 ids)

**5.01 Ce qui avance** `463:51167` (programme Kaffrine Entreprendre) — B01 Ce qui avance `463:51171` · B02 Par type de connexion `463:51211` · B03 Ce que le programme prend en charge (services de relais, cartes en main) `463:51242` · B04 Comment on compte `463:51266` · B05 Recevoir le rapport (PDF et tableau, same totals) `463:51285` · B06 Un chiffre trop petit `463:51299`

**5.02 Décider où agir** `504:28131` — a map, analyses and a crossed exploration (zone, secteur, type d'appui, population), then help to design a programme. B07 Où agir : vue d'ensemble `504:28173` (tall) · B08 Les analyses `504:28332` · B09 Croiser zone, secteur, appui, public `504:28537` · B10 Avant de lancer un programme `505:28611` · B11 Ce qui existe déjà `505:28676` · B12 Plusieurs programmes `505:28792` · B13 Plusieurs pays `519:57317`

**8.01 Piloter à l'échelle du pays** `506:28416` — Ndèye Fall, analyste à la Direction de l'entrepreneuriat (sample name). E01 Accueil · le pays `506:28458` (tall: 12 480 inscrites, 2 340 accompagnées, 214 structures actives, 2,9 Mds FCFA accordés; appuis pour 1 000 entreprises par région, moyenne 2,4) · E02 Équité entre les territoires `506:28631` · E03 Parcours des entrepreneures `506:28797` · E04 Financements et programmes `506:28914` · E05 Résultats `506:53120` · E06 Où intervenir `506:53196` · E07 Ce que tu peux voir `506:53254` · E08 Identifiant unique, sous partenariat `506:53317` · E09 Comparer avec d'autres pays `519:57462`

All totals are fictional. Components: Navigation/En-tête, Statuts/Chip, Cartes/Ligne de
menu, Cartes/Encadré, Formulaires/Champ, Superpositions/Option de feuille,
Retours/Bannière. There is no chart component in the system: draw maps and bars from
tokens (`bg/surface-muted` → `blue` scale, `border/attention` for the orange frame) and
keep them simple.

Codes: next free 5.01-B14 (B continues across 5.01/5.02), 8.01-E10. Place new Figma
screens on page 20 or on the page the user names, never on page `0:1`.
