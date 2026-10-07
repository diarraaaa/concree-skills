---
name: wekomkom-relais-design
description: Design Wekomkom screens for the relais — people attached to a local institution (chambre de commerce, Espace Sénégal Services) who help entrepreneurs in person — including becoming a relais, their day, their paid or free services, receipts, reports, handing over cards, and the shared guichet tablet (1180 × 820 landscape). Use for "écran relais", "accueil du relais", "Khady", "services et prix du relais", "devenir relais", "charte", "tablette du guichet", "session d'une personne sans téléphone", "présences à une séance". For what the entrepreneur sees of her relais (« Je préfère parler à quelqu'un »), use wekomkom-app-design (fiche 1.11).
user-invocable: true
---

# Wekomkom — relais (mobile and guichet tablet)

Zone **4 · Relais** of the reference file (page `461:27` « 22 — Assemblage final »,
section `463:50482`, file `zyYKIr49PoDeO9vroOG27F`). Working pages: `386:16544` « 15 —
Relais » (Guide `433:23398`) for 4.01–4.03, `450:27` « 21 — Tablette » (Guide
`453:2286`) for 4.04.

## Step 1 — load the shared system

From `../wekomkom-app-design/`: `references/design-dna.md` (read in full),
`components.md`, `tokens.md`, `figma-workflow.md` or `opendesign-workflow.md`, `assets/`,
`references/flows/README.md`, `references/flows/9-socle-commun.md` (relais profile
9.01-P04, relais card 9.04-C4/Q4), and `references/flows/1.11-1.12-relais-confiance.md`
(the entrepreneur's side of the same relationship). Run `side-files/checklist.md` at the end.

## Who and why

Khady Sarr, relais of the Chambre de commerce de Kaffrine, antenne de Koungheul
(fictional, like Modou Faye, Awa Ba, Rama Diop, Fatou Ka, Bineta Sow, Daba Faye, the
tariffs and the programme Kaffrine Entreprendre; no partnership is concluded). A relais
offers local services: some free, some covered by a structure or a programme, some
paid. **The price always shows before the entrepreneur commits.**

## Rules (Règles posées, 4 Oct. 2026)

- Profile says: attachment, zone, languages, availability, verification status, services and prices, « Envoyer un message ».
- **Delays**: at 2 days without an answer the relais' structure is warned; at 4 days the entrepreneur can choose another relais and CONCREE is alerted. The relais accueil says it plainly (« Aïssatou attend ta réponse depuis 2 jours. Ta chambre de commerce est prévenue. À 4 jours… »). A relais who can't help says so; she picks another relais and he loses access (P02).
- **Becoming relais**: by invitation of one's institution; fill the profile, sign the charter, CONCREE checks identity and attachment. Before that: invisible, no request visible (J01–J06).
- **Prices**: a service has a price set before any request; it doesn't change for a request already made (P03). The relais sends a receipt when paid; an amount different from the displayed price shows (P04, P05). « À refaire » says why, and the service is paid only when done (P06).
- A relais can **prepare** a request with the entrepreneur; she alone sends it, and it carries « Préparée avec Khady Sarr » (Q04, R06). She confirms a meeting (P01).
- An authorised relais can verify a document; the verification carries his name and date and is **not an official approval** (Q05).
- An absence removes the relais from the list; the people he follows are warned (P07).
- A relais targeted by a report gives his version; he doesn't know who reported (P09).
- A carte en main is handed only to the person whose name it bears, on presentation of her ID (P10, P11).
- After a withdrawal the relais loses access and keeps no copy, photo or print (Q06, Q07).
- The chambre de commerce sees its relais' delays, invites and can suspend them (3.07-V05…V08, in wekomkom-vue-acteur-design).

## The guichet tablet (4.04) — a different format

- **Landscape 1180 × 820**, built with the system's components (cards, choice rows, buttons, callouts). Not the desktop of the later phase (7.01): a **shared tool** at the counter of an antenne, a chambre de commerce or an Espace Sénégal Services.
- **Nothing is kept on the tablet.** An entrepreneur's session opens with her card, in front of her, after seeing her ID, and closes when she leaves or by itself after **10 minutes without a gesture** (T03, T04, T06).
- A person without a phone has a full space: her card is her key. Nothing leaves without her consent; Adia speaks Wolof if she wants (T04).
- A **permanent banner** says whose session it is, who helps, and when it closes (« Session de Daba Faye · avec Khady Sarr, relais · se ferme seule à 11:42 sans geste » + « Fermer la session »). Reassurance line: « Khady lit avec toi. Rien ne part sans ton accord, et rien ne reste sur cette tablette. »
- At a session, cards are scanned at the entrance; each person also confirms on her phone if she has one; the institution only sees the total (T05).
- Layout: left navigation rail (Cartes/Ligne de menu with icons home · scan · users · calendar · id-card), content in columns, Adia panel in conversation style.

## Screens (page 22 ids)

**4.01 Devenir relais** `463:50485` — J01 Une invitation à devenir relais `463:50489` · J02 Ton profil de relais `463:50506` · J03 Ta charte `463:50523` · J04 Te faire vérifier `463:50537` · J05 Vérification en cours `463:50547` · J06 Tu es relais `463:50559`

**4.02 La journée du relais** `463:50580` — Q01 Accueil du relais `463:50584` · Q02 Une demande d'aide `463:50624` · Q03 Tes services `463:50650` · Q04 Préparer avec elle `463:50662` · Q05 Vérifier une pièce `463:50677` · Q06 Entrepreneures accompagnées `463:50695` · Q07 Ton rattachement `463:50729`

**4.03 Le travail du relais** `463:50759` — P01 Proposer un moment `463:50763` · P02 Passer la main à un autre relais `463:50783` · P03 Ajouter un service `463:50819` · P04 Service fait `463:50840` · P05 Reçu envoyé `463:50861` · P06 À refaire : dire pourquoi `463:50880` · P07 Tes disponibilités `463:50895` · P08 Ta charte signée `463:50907` · P09 Un signalement te concerne `463:50919` · P10 Remettre une carte `463:50932` · P11 Carte remise `463:50950`

**4.04 La tablette du guichet** `463:50961` (1180 × 820) — T01 L'accueil du guichet `463:50965` · T02 Scanner une carte `463:51018` · T03 Ouvrir la session d'une personne `463:51040` · T04 La session de Daba `463:51070` · T05 Séance du jour : les présences `463:51107` · T06 Session fermée `463:51136`

Relais accueil anatomy (Q01): « Bonjour Khady » + « Relais · Chambre de commerce de
Kaffrine, antenne de Koungheul »; « À FAIRE AUJOURD'HUI » dark card with the overdue
request and « Lui répondre »; « Demandes d'aide · 3 nouvelles » list (name, service,
pris en charge / price, date, pill « Depuis 2 jours » / « Nouvelle »); links « Tes
services et tes prix », « Cartes Komkom à remettre · 2 »; tab bar.

Components: Formulaires/Ligne de choix, Formulaires/Champ, Relais/Service, Statuts/Pastille,
Statuts/Chip, Démarches/Étape, Retours/Bannière, Cartes/Encadré, Cartes/Ligne de menu,
Icône/id-card.

Codes: next free J07, Q08, P12, T07. Place new Figma screens on page 15 (4.01–4.03) or
21 (4.04), never on page `0:1`.
