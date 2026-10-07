---
name: wekomkom-app-design
description: Design new Wekomkom entrepreneur app screens (zones 1, 2, 7, 9 of the reference file, with one fiche per group of pages) — Design new Wekomkom mobile app screens that look drawn by the Chief Designer, either directly in the Wekomkom Figma file (built from its 192 components, variables and styles) or as HTML prototypes in OpenDesign (built from the same tokens). Use for any request to create, mock up, extend or redesign a Wekomkom / Komkom screen, flow or state (accueil, Ma carte Komkom, Explorer, opportunités, conversation avec Adia, démarches, profil, états vides/erreurs/hors ligne). Trigger on English ("design/make/mock up a Wekomkom screen", "new Komkom flow in Figma", "prototype this in OpenDesign") and French requests ("crée/fais/dessine un écran Wekomkom", "maquette Komkom", "nouveau parcours dans Figma", "prototype OpenDesign Wekomkom").
user-invocable: true
---

# Wekomkom app design

This is the agent entry point. Read it first.

**Language:** these instructions are in English; everything you put on a screen is
in **French** (tutoiement respectueux), unless the brief asks otherwise.

Wekomkom connects Senegalese entrepreneurs to support, financing and markets. Its
assistant is **Adia**, its identity card the **carte Komkom**. The design system was
extracted pixel-exact from the Chief Designer's mock-ups into the Figma file below;
this skill packages it.

## Folder map

```
wekomkom-app-design/
├── SKILL.md                       ← you are here
├── references/
│   ├── design-dna.md              ← principles, 9 visual traits, voice, forbidden words, formats, a11y
│   ├── tokens.md                  ← every variable, gradient, effect, grid and text style
│   ├── components.md              ← catalog of components with Figma node IDs and variants
│   ├── figma-workflow.md          ← file IDs, screen anatomy, font pitfall, tested build snippet
│   ├── opendesign-workflow.md     ← project setup, HTML authoring, render check
│   ├── flows/                     ← ONE FICHE PER GROUP OF PAGES of the reference file
│   │   ├── README.md              ← index of the 9 zones, screen codes, final-pass rules, shared data
│   │   ├── 1.01-arrivee-accueil.md · 1.02-ma-carte.md · 1.03-explorer.md
│   │   ├── 1.04-1.08-demande.md · 1.09-1.10-messages-alertes.md · 1.11-1.12-relais-confiance.md
│   │   ├── 1.13-1.16-profil-compte.md · 2.01-moussa-startup.md · 7.01-bureau.md
│   │   └── 9-socle-commun.md      ← profile, scan, geography, card/QR for every role (read by all skills)
│   └── screens/                   ← reference renders: accueil-premier, ma-carte, explorer, conversation-adia
├── assets/
│   ├── wekomkom-tokens.css        ← all tokens as --wk-* CSS variables + text-style classes
│   ├── wekomkom-components.css    ← shared HTML building blocks (capture-safe), load after the tokens
│   ├── logo-mark-color.svg · logo-mark-white.svg · logotype.svg (currentColor)
├── examples/
│   ├── accueil.html               ← 1.01-H01 Premier accueil rebuilt in HTML from the tokens
│   ├── opportunite-detail.html    ← exploration « Détail d'une opportunité » (capture-safe, tall scroll)
│   ├── flow-demande/              ← explorations Préparer avec Adia · Avant d'envoyer · Suivi de ta demande
│   │                                 (built on wekomkom-components.css; best HTML starting point)
│   └── fictif/                    ← fictional pages, tests of the skill: 1.13-X01 Acheter à plusieurs ·
│                                     1.03-X02 Foire de Kaffrine · 1.12-X03 Mon groupe d'épargne ·
│                                     1.06-X04 Noter mes ventes à voix haute · 1.11-X05 Rendez-vous avec Khady
│                                     (Figma: page « Wekomkom — page fictive » 73:2 of the posters file; next free X06)
│   Note: the « 1.04-D01…D04 » codes in these examples predate the fiches and collide with
│   page 22 (1.04-D01 is « Pour toi »). Use them for HTML structure, not as references of the product.
└── side-files/
    └── checklist.md               ← P0/P1/P2 checks before delivering
```

## Sibling skills (same design system, other users)

| Who | Skill |
| --- | --- |
| Structures (financeurs, structures d'appui, chambres de commerce, acheteurs, agents) and the CONCREE back-office | `wekomkom-vue-acteur-design` |
| Relais, and the guichet tablet (1180 × 820) | `wekomkom-relais-design` |
| Bailleurs and État (aggregated, anonymous figures) | `wekomkom-pilotage-design` |

This skill covers the entrepreneur app (zone 1), the startup persona (zone 2), the later
desktop phase (zone 7) and the shared base (zone 9). The siblings load this skill's
design-dna, tokens, components, workflows and assets instead of copying them.

## Step 1 — understand the brief

Open `references/flows/README.md`, find the parcours, and read its fiche. **Check that
the screen does not already exist** in the reference file (558 screens): if it does,
start from it and say what changes. Give new screens a free code of that parcours.

Identify: which flow (accueil, Ma carte, Explorer, opportunité, Adia, démarches,
profil, messages, relais…; the flows README lists them all), which screen(s) and states, which persona (default:
Aïssatou, transformatrice de mil à Koungheul), and the output target:

- **Figma** → new screens inside the Wekomkom Figma file.
- **OpenDesign** → HTML prototype in an OpenDesign project.

If the target isn't stated, ask once (both is fine). Never invent facts the brief
doesn't support (organisation names, amounts, dates); use plausible placeholders
only when the user asks for a mock-up and say they are placeholders.

## Step 2 — read the system

The fiche of the parcours comes first: its rules (« Tranché le 4 octobre ») are product
decisions, not suggestions. Then:

Always read `references/design-dna.md` in full, then `references/components.md`.
Open the closest reference image in `references/screens/`. Read `references/tokens.md`
when you need an exact value.

Hard rules (details in design-dna.md):
- Dawn gradient background; white cards with 1 px hairline, faint shadow, radius 15.
- One useful action = one primary button; at most one dark card per screen.
- Everything tappable is a pill or round. Spacing in steps of 5 (10/15/20/25), margin 17–18.
- Blue = act, green = fine, orange = attention / amount. Semantic tokens only.
- Blue→green gradient only on the listen button, Adia and the carte Komkom.
- Real photos, a listen button next to what matters, source + date on information.
- No forbidden words (score, éligible, certifié, validé, readiness, palier, dashboard, matching…).

## Step 3a — Figma

Read `references/figma-workflow.md` and follow it. In short:
1. Load the `figma:figma-use` skill (and `figma:figma-generate-design` for full screens) before any `use_figma` call.
2. Work only in file `zyYKIr49PoDeO9vroOG27F`, on the matching flow page. Never edit page `0:1` (designer) or the read-only original file.
3. Build from component instances (IDs in components.md) with the tested `inst()` / `setProp()` helpers; bind variables, apply styles; never detach.
4. Load Open Sans Regular / SemiBold / Bold only. "Open Sans Medium" is not available to the plugin; don't swap weights to work around it.
5. Screenshot once, compare with the reference, fix, return all node IDs and the Figma link (`https://www.figma.com/design/zyYKIr49PoDeO9vroOG27F/?node-id=<id with - instead of :>`).

## Step 3b — OpenDesign

Read `references/opendesign-workflow.md` and follow it. In short:
1. Create or reuse an OpenDesign project; write `wekomkom-tokens.css` and the logo SVGs into it.
2. Author each screen from `examples/accueil.html`, using only `var(--wk-…)` tokens and the component patterns.
3. Render-check with headless Edge or the project's preview URL; compare with the references.
4. Give the user the preview link.
5. If they want it in Figma too ("fais-le dans Figma avec OpenDesign"), capture the
   OpenDesign page into the target Figma file (section "Sending an OpenDesign screen
   to Figma" in opendesign-workflow.md). The capture lands on the first page: move it
   to its own page, and never alter other pages.

## Step 4 — check before delivering

Run every P0 item in `side-files/checklist.md`. Report anything you could not do
(e.g. a Medium-font text you could not edit in Figma) instead of hiding it.

## Keeping this skill current

The Figma file is the source of truth. If a component ID no longer resolves, or the
user says the system changed, re-read the design-system page (`7:27`) with a
read-only `use_figma` call (list `COMPONENT_SET`/`COMPONENT` nodes with their
`componentPropertyDefinitions`; list local variables, paint, text and effect styles)
and update `components.md`, `tokens.md` and `assets/wekomkom-tokens.css`.
