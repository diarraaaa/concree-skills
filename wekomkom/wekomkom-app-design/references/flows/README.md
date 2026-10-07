# Flows of the reference file — index

The Wekomkom Figma file holds **558 screens in 42 parcours** (sommaire of 5 Oct. 2026).
The canonical copy is page **`461:27` « 22 — Assemblage final »**: nine zones, one per
type of user, each parcours starting with its own sommaire. Pages 01–21 are the
designer's *working pages*, with their history and their **Guide de test** (what the
flow must teach, hypotheses, decisions « Tranché le 4 octobre 2026 »). Page `0:1`
(« Ecran de base de notre designer ») is where the work started; it is not a screen
to build from.

**Before designing anything, open the fiche of the parcours.** Check that the screen
does not already exist (same intent, maybe another title). If it exists, start from
it; a new version must say what it changes.

## Which skill or fiche

| Zone (page 22 section) | Who | Where to look |
| --- | --- | --- |
| 1 · Entrepreneure · application mobile `463:1934` | Aïssatou, transformatrice de mil à Koungheul | this skill, fiches below |
| 2 · Startup · Moussa `463:47912` | Moussa Konaté, Kawral (Dakar) | this skill, [2.01-moussa-startup.md](2.01-moussa-startup.md) |
| 3 · Structures · vue acteur mobile `463:48222` | Mariama (Mutuelle Jappo), Adja (Saveurs du Saloum), agents | skill **wekomkom-vue-acteur-design** |
| 4 · Relais `463:50482` (incl. tablette 1180 × 820) | Khady Sarr, relais | skill **wekomkom-relais-design** |
| 5 · Bailleurs `463:51164` | programme Kaffrine Entreprendre | skill **wekomkom-pilotage-design** |
| 6 · Équipe de CONCREE · back-office `463:51326` | Codou Mbaye | skill **wekomkom-vue-acteur-design** |
| 7 · Phase ultérieure · bureau `463:51697` (1280 × 800) | Aïssatou and Mariama on a computer | this skill, [7.01-bureau.md](7.01-bureau.md) |
| 8 · État et secteur public `506:28413` | Ndèye Fall, Direction de l'entrepreneuriat | skill **wekomkom-pilotage-design** |
| 9 · Socle commun à tous les rôles `511:53930` | every role | this skill, [9-socle-commun.md](9-socle-commun.md) (all skills read it) |

Zone 1 fiches:

| Fiche | Parcours |
| --- | --- |
| [1.01-arrivee-accueil.md](1.01-arrivee-accueil.md) | 1.01 Arrivée et accueil · 1.17 Les cercles de l'accueil |
| [1.02-ma-carte.md](1.02-ma-carte.md) | 1.02 Ma carte Komkom |
| [1.03-explorer.md](1.03-explorer.md) | 1.03 Explorer |
| [1.04-1.08-demande.md](1.04-1.08-demande.md) | 1.04 Découvrir une opportunité · 1.05 Préparer avec Adia · 1.06 Ma préparation · 1.07 Partager et envoyer · 1.08 Suivre ses démarches |
| [1.09-1.10-messages-alertes.md](1.09-1.10-messages-alertes.md) | 1.09 Messages · 1.10 Alertes et notifications |
| [1.11-1.12-relais-confiance.md](1.11-1.12-relais-confiance.md) | 1.11 Parler à quelqu'un · 1.12 Confiance |
| [1.13-1.16-profil-compte.md](1.13-1.16-profil-compte.md) | 1.13 Entre pairs · 1.14 Mon compte · 1.15 Compétences et parcours de soutien · 1.16 Mes entreprises |

## Screen codes

`1.08-R05 · Information demandée` = parcours 1.08, screen R05. The code is unique on
page 22, the same in Figma, the guides, the prototype and dev tickets. A new screen:

1. takes the parcours number of the flow it belongs to (never a number already used for another parcours);
2. takes the letter of the row it extends, and the **next free number** in that row (e.g. after `1.08-R13`, `1.08-R14`); a state takes the `S` form of the row (`DS5`, `PS6`…);
3. is named `<parcours>-<code> · <titre en français>`.

A screen that belongs to no parcours (a fictional page, an exploration) says so in its
name: `… (fictif)`.

## Rules from the final pass (5 Oct. 2026) — they override older screens

- **Accueil**: no maturity level any more. It shows the real opportunities that match the person, ranked for now (date, distance, what is missing), each with **Correspondance/Jauge de préparation** (left: what is missing · middle: presque prête · right: « Tu peux candidater maintenant »). An opportunity is never hidden because the person is not ready. Preparation actions (NINEA, ventes, prévisionnel, Relais, avec Adia) are separate cards, **tinted background + dashed outline**. The « Accès au financement » block is no longer used.
- **Cercles (Navigation/Raccourci)**: Pour moi → stories, one per opportunity (1.17-P01…P04) · Komkomnews → episode of the week in story (1.03-K02) · Spotlight → most recent video (1.17-S01) · Acteurs → new actors in stories when the ring is lit, the actor map otherwise. Gradient ring = something new; grey ring = nothing new. Red dot on the profile photo = unread message (no Messages tab).
- **Photos**: Aïssatou's photo and Adia's face are applied through the components (avatar, conversation bubble, « ce qui manque » row). New mock-ups reuse those components instead of initials.
- **Every input zone has a micro and a paperclip.** Events open on a calendar.
- **Sign-up** by phone or e-mail, with a code in both cases (1.01-E10 to E10d). « J'ai déjà un compte » opens a classic two-tab login, Téléphone / E-mail (1.14-C01, C01m, C02m). Adia never asks a number or an address of someone who already has an account.
- **Zone géographique**: the same chip at the top of content screens (Explorer, opportunités, événements, Insights, tableaux de bord) opens the sheet « Où regarder ? » (9.03). Anything from another country says so, with its currency and an indicative equivalent.
- **Six separate things, linked**: the person (profile, carte Komkom, skills, support history) · the company · the structure · the role (person ↔ organisation) · the agent card (belongs to the structure) · the support history (what was received ≠ what it brought). At a scan you see the person, then the organisation she acts for.
- Dashboards never show a number below 5. All people, organisations, amounts and dates are sample data.

## Data shared across all flows (fictional)

Aïssatou Diallo (mil, thiakry and arraw, Koungheul, team of 3 since 2019) · Mutuelle Jappo
(Kaolack / Koungheul; Mariama Ndiaye, chargée de crédit) · Saveurs du Saloum (boutique,
Adja) · Centre d'appui de Kaffrine (Astou) · Khady Sarr, relais, Chambre de commerce de
Kaffrine · Fatou Sarr / Fatou Ka · Codou Mbaye (équipe CONCREE) · Moussa Konaté (Kawral) ·
programme Kaffrine Entreprendre · Ndèye Fall (Direction de l'entrepreneuriat). Reuse
them; no partnership is real.
