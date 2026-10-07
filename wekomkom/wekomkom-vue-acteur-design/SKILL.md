---
name: wekomkom-vue-acteur-design
description: Design Wekomkom screens for the professional side of the app — structures (financeurs such as mutuelles, structures d'appui, chambres de commerce, acheteurs/boutiques, their agents and teams) and the CONCREE team's back-office (modération, vérifications, décisions). Mobile 390 px, same design system as the entrepreneur app. Use for requests like "écran vue acteur", "accueil de la structure", "répondre à une demande", "publier une opportunité", "côté mutuelle / boutique / acheteur", "carte d'agent", "équipe de la structure", "back-office CONCREE", "modération", "file à vérifier". Not for the entrepreneur's own screens (use wekomkom-app-design), relais (wekomkom-relais-design) or bailleurs / État (wekomkom-pilotage-design).
user-invocable: true
---

# Wekomkom — vue acteur (structures and CONCREE back-office)

Zones **3 · Structures · vue acteur mobile** and **6 · Équipe de CONCREE · back-office**
of the reference file (page `461:27` « 22 — Assemblage final », file
`zyYKIr49PoDeO9vroOG27F`). Everything visual comes from the main skill; this skill adds
who the users are, what they do, and the rules of their screens.

## Step 1 — load the shared system (do not duplicate it)

From the sibling skill `../wekomkom-app-design/`:
- `references/design-dna.md` (principles, nine visual traits, voice, formats, a11y) — read in full;
- `references/components.md`, `references/tokens.md`;
- `references/figma-workflow.md` (Figma route) or `references/opendesign-workflow.md` (HTML route), and `assets/` (tokens, components CSS, logos);
- `references/flows/README.md` (codes, final-pass rules, shared data) and `references/flows/9-socle-commun.md` (profile, scan, card and QR for every role);
- `side-files/checklist.md` before delivering.

Then read the fiche of the parcours here:
- [references/zone-3-structures.md](references/zone-3-structures.md) — 3.01 to 3.11
- [references/zone-6-back-office.md](references/zone-6-back-office.md) — 6.01

## What changes on the actor side

- **Users are professionals at work**: Mariama Ndiaye (chargée de crédit, Mutuelle Jappo), Astou (conseillère, Centre d'appui de Kaffrine), Adja (gérante, Saveurs du Saloum), agents de terrain (Fatou Kane, Ousseynou Faye), Codou Mbaye (équipe CONCREE). Still **tu**, short sentences; precise words are allowed when they are the job's words (accord, versement, critères, pièces, échantillon, commande d'essai), never jargon toward the entrepreneur and never « score / matching / éligible » about a person.
- **Accueil d'une structure** (3.03-Y01): header « Bonjour Mariama » + « Mutuelle Jappo · financeur · structure vérifiée par CONCREE »; cercles Explorer · Spotlight · Acteurs · Insights; **« À FAIRE AUJOURD'HUI »** = the one dark card (e.g. « 2 demandes attendent ta réponse » + the usual delay); then menu rows (Demandes reçues · Mes opportunités · Pièces demandées · Proposer une vidéo · Mes rendez-vous · L'équipe · Alertes); tab bar with Carte / Explorer and the **QR button in the centre**; floating button « Créer une opportunité » (Actions/Bouton flottant). Photo with red dot = unread messages.
- **Structured answers, not messages.** Répondre opens a sheet: Demander une information ou une pièce · Proposer un rendez-vous · Donner un accord · Ne pas retenir (raison obligatoire) · Indiquer que l'argent est versé (après un accord seulement). « Envoyer un message » is a separate, secondary action.
- **Show what the entrepreneur chose to show, and say so**: « Tu la vois comme financeur », « Elle a choisi de ne pas te montrer son numéro. Tu peux lui écrire dans Wekomkom. », « Tu te sers de sa demande pour l'étudier, sans la transmettre à d'autres. » Every document shows its proof level and who verified it.
- **Every decision shows the text the other person will read** (back-office and structures alike).
- Forms are frequent here (Formulaires/Champ, Ligne de choix): one topic per screen, a clear primary button at the bottom, errors under the field.
- Same visual traits: dawn background, white cards, one dark card, pills, brand gradient only on listen / Adia / carte Komkom.

## Naming and placement

Codes per `../wekomkom-app-design/references/flows/README.md`: e.g. `3.03-Y14 · …`,
`6.01-D15 · …`. Place new Figma screens on the matching working page (14 for 3.02–3.07,
17 for 3.08, 16 for 6.01, 01 for 3.01) — never on page `0:1` — or on the dedicated page
the user names.
