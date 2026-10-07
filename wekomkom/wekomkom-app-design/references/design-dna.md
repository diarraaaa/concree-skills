# Wekomkom — design DNA, voice and rules

Source: the "00 — Wekomkom Design System" page of the Figma file (sections 00 README,
01 Design DNA, 25 Accessibilité, 26 Contenu). Summarised here so you can design
without reopening Figma. When this file and Figma disagree, Figma wins.

## What Wekomkom is

A platform that connects each Senegalese entrepreneur to the right resource at the
right time: support (accompagnement), financing (financement), market (marché). It
does not finance or coach by itself; it makes the connection possible and follows
it. The assistant is **Adia**. The person's identity card is the **carte Komkom**
(a QR code that structures scan).

The system must hold on an entry-level phone, in the sun, on a connection that
drops, for someone who prefers speaking to writing.

Target feeling: « Cette plateforme me comprend, sait où j'en suis et peut m'aider à
trouver ce dont j'ai besoin pour avancer. » / « Je suis attendue, et quelqu'un garde
le fil pour moi. » Serious without being administrative, warm without being childish.

## Seven product principles (they decide when in doubt)

1. **Une chose à la fois.** One question per message, one primary button per screen, at most one dark card. The rest waits.
2. **Le système porte la complexité.** Criteria, matching, priorities work behind the scenes; the screen shows their conclusion in plain words.
3. **Toujours une suite.** No dead end: a "pas encore" offers what is open now, an error says what to do, an empty state explains and proposes.
4. **Comprendre avant de demander.** Adia rephrases, never re-asks what Wekomkom knows, only asks if the answer changes what comes next.
5. **Dire d'où ça vient.** Every piece of information carries its source and date. Never promise a decision that belongs to an organisation.
6. **Parler aussi bien qu'écrire.** Voice is a first-class input; everything that matters can be listened to.
7. **Simple, jamais simpliste.** Everyday words, careful finish. No screen should look "for beginners".

## Nine visual traits (every new screen keeps all of them)

1. **L'aube en fond.** Top of every mobile screen goes from very pale blue to very pale green, then white → `Gradient/Fond` (`#EAF4FD → #F7FFF3 40% → #FFFFFF`). Never a flat grey background.
2. **Des cartes posées, pas empilées.** White, 1 px hairline (`border/default` #E2E7EA), almost invisible shadow (`Elevation/1 Card`), radius 15. The card stands out by contrast, not shadow. Never a stronger shadow or a coloured border.
3. **Un seul moment sombre.** One night-blue card per screen (`bg/surface-inverse` #22364D, often over a real photo with `Gradient/Carte sombre`) carries what matters now, often with an orange number. Either *Prochaine action* or *Opportunité à la une*, never both side by side.
4. **Tout ce qui se touche est rond.** Buttons, chips, tabs, tab bar = pills (`radius/pill` 30). Containers `radius/md` 15 or `radius/lg` 20. Nothing angular under the finger.
5. **Le dégradé veut dire « connecter ».** Blue CONCREE → growth green (`Gradient/Marque horizontale`). Reserved for three objects: the listen button, Adia, the carte Komkom. An action button stays solid blue.
6. **La couleur sert.** Blue to act, green for what is fine, orange for what needs attention or deserves to be seen (an amount). Everything else is a scale of bluish greys. Semantic tokens only; a colour never decorates a category.
7. **Petit libellé, valeur forte.** Discreet 12 px label (`Meta/Default`), value in bold (`Label/Value`). Titles Bold, running text Medium.
8. **Respiration par 5.** Gaps 10 and 15, padding 20, screen margin 18 (the designer's screens place content at x 17, 356 wide). `space/*` tokens only, no gap "by eye".
9. **Des gens, et une voix.** Real photos of Senegalese entrepreneurs in important cards (no stock imagery), and a listen button next to everything that matters (moment cards, Adia messages).

## Kept-as-is designer values (do not "clean up")

- Two action blues: `#0958A5` primary buttons, `#015AA9` navigation, links, tints.
- Near-duplicates (#0A58A5, #23374E, #16324F, #03345E) stay inside cloned components; do not use them for new work.
- Tight line heights (16/12, 14/12, 12/8) are real styles; use the "Multi" variants for two lines.
- `#6E7F93` text (4.0:1), orange `#FF9900` and green `#59B224` on light are allowed only in framed use (size, icon, word). Orange text on light backgrounds is forbidden for body text; use `fg/attention` #A15C00.
- Eight radii: 5, 10, 15, 20, 25, 30, 40, 100. No invented value.

## Voice (French UI, Wolof via voice and Adia)

- Respectful **tu**, short sentences, the person's own words.
- Adia explains why she asks when it helps. She never promises what an organisation will decide.

| Write | Avoid |
| --- | --- |
| « Tu notes tes ventes quelque part ? » | « Quel est ton niveau de gestion financière ? » |
| « Pour cette demande, il reste une chose à préparer. » | « Ton score de readiness est insuffisant. » |
| « Je garde ce que tu m'as déjà dit. » | « Le registre des faits est synchronisé. » |
| « On peut regarder ça avec une personne. » | « Redirection vers le parcours de remédiation. » |
| « Ce document a été ajouté ; il reste à vérifier. » | « Document certifié » after a simple upload |
| « On peut préparer ta demande. La mutuelle décidera ensuite. » | « Tu vas obtenir ce financement. » |
| « Ça te correspond » / « Pas encore pour toi » | « Éligible » / « Non éligible » |

**Forbidden words on the entrepreneur side** (internal or actor-view only): score,
note, éligible / éligibilité, certifié, validé, readiness, palier, dimension,
dashboard, matching, scoring, remédiation.

Matching status vocabulary: **Ça te correspond · Une chose à préparer · À éclaircir · Pas encore pour toi**
(criteria: Ça va · À préparer · À éclaircir · À confirmer). Proof levels: Dit par toi · Reçu · Vérifié · À éclaircir · Vérifié par l'IA · Vérification demandée.

### Formats

| Data | Format | Example |
| --- | --- | --- |
| Amount | Whole number, thin space, FCFA after | 3 000 000 FCFA (spoken: « jusqu'à 3 millions de FCFA ») |
| Date | Day + short month, year if different | 30 oct. · 12 sept. 2025 |
| Close deadline | Under 7 days, in days left | Encore 6 jours |
| Time | 24 h | 15 h · 9 h 30 |
| Phone | Country code apart, pairs | +221 77 123 45 67 |
| Duration | Plain words | Environ 10 minutes · 3 mois |
| Number | Absolute value over percentage | 3 sur 5 · 2 choses à préparer |

Fixed prices (variable collection "Contenu"): carte en main 2 500 FCFA, livraison
1 000 FCFA, carte + livraison 3 500 FCFA, carte virtuelle 1 000 FCFA.

### Writing formulas

| Element | Formula | Example |
| --- | --- | --- |
| Button | Verb + object, 1–4 words | Voir cette opportunité · Préparer ma demande |
| Error | What happened + what is kept + what to do | L'envoi n'a pas abouti. Ton fichier est gardé. Réessaie quand le réseau revient. |
| Empty state | What is happening + what Wekomkom does + a next step | Rien pour l'instant. Je te préviens dès qu'il y a quelque chose. Élargir à la région ? |
| Adia question | One question, with the why if needed | Tu notes tes ventes quelque part ? C'est ce que la mutuelle regarde en premier. |
| Refusal | The fact, the reason if known, what's next | Non retenue cette fois. Raison : moins de 6 mois de ventes notées. Voici ce qui est ouvert maintenant. |

Quick-reply labels use the person's words: « Trouver de l'argent », not « Financement ».
Components must hold text 30 % longer (French long, Wolof, mixed). Buttons wrap to two
lines rather than truncate. Amount, deadline, opportunity name and status are never
truncated; only search lists may cut after 2 lines. No text inside images. While Wolof
voice does not exist, say so: « Lecture en français ».

## Accessibility (WCAG AA minimum)

- Text contrast 4.5:1 (3:1 above 18.66 px bold). Control outlines 3:1 (`border/control`).
- 12 px minimum text; 16 px body in conversation; layout follows system text size.
- Touch targets 48 (`size/touch-min`); buttons 50 and 42 with space around.
- Focus: `Focus/Ring` (2 px white + 2 px blue) on every control.
- Colour is never the only carrier of meaning: status = icon + word; category = icon + word.
- Errors under the field, with icon and a sentence saying what to do.
- Respect reduced motion: simple fade; nothing depends on an animation.
- Screen reader: icon buttons named; toggles announce « visible / masqué »; statuses read with their word.
- No dashboards, tables, gauges-with-percentages for the entrepreneur: one next action and simple lists.
- No document (NINEA…) required to start. Never infantilising: no childish illustrations, no over-the-top congratulations.
- Opportunities targeting women and regions outside Dakar are surfaced through reasons, not badges.

Seven people to replay every flow with: speaks better than reads French · reads
slowly · doesn't know financial terms · discovering support structures · mostly uses
WhatsApp · doesn't understand "dashboard" · project not yet formalised.
