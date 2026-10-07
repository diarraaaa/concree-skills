# Wekomkom — component catalog

All components live on page **"00 — Wekomkom Design System"** (page id `7:27`) of the
Figma file `zyYKIr49PoDeO9vroOG27F`. They are local (not a published library), so
instances can only be created inside this file. IDs below are the component or
component-set node IDs; get one with `await figma.getNodeByIdAsync(id)`.

Names and variant values are in French with typographic apostrophes (’). Property
keys for TEXT / BOOLEAN / INSTANCE_SWAP carry a `#id` suffix. Read them from
`componentPropertyDefinitions` on the set before calling `setProperties`.

Status of each block in Figma: *Repris* (cloned pixel-exact from the designer),
*Dérivé* (built by extending his rules), *Extension proposée* (new, to validate).

## Templates (section 04)

| ID | Component | Props | Notes |
| --- | --- | --- | --- |
| 34:1576 | Gabarits/Écran mobile | Contenu (swap), Barre d’onglets (bool) | 390×844, Gradient/Fond, Grid/Mobile, status bar, header, content margin 18, floating tab bar 20 from bottom. Check every screen at 360 wide. |
| 34:1607 | Gabarits/Écran bureau | Panneau Adia (bool) | 1280×800: sidebar 260, main column (reading max 640), Adia panel 380 on the right. Sheets become dialogs. |

## Actions (08)

| ID | Component | Variants |
| --- | --- | --- |
| 73:2527 | Actions/Bouton | Hiérarchie: Principal · Secondaire · Contour · Teinté · Blanc · Verre · Neutre · Désactivé — Taille: Grand · Moyen · Compact. Grand 50 high (Principal #0958A5); Moyen 46 #015AA9 with Adia icon; Compact square r10 / tinted pill 36 / white 41 on dark / glass 38 on gradient. |
| 73:2545 | Actions/Lien | Style: Pilule (“Voir”, h28, tint 5 %) · Texte · Contour (r40, h42) · Icône |
| 73:2609 | Actions/Bouton icône | Action: Retour (34) · Retour plein · Retour parcours (42) · Réglages (40) · Fermer (38) · Fermer sur photo · Plus · Documents (red counter) · Envoyer (38 blue) · Ajouter · Rechercher · Favori sur photo · Partager sur photo |
| 13:204 | Actions/Bouton icône générique | Style: Neutre · Teinté · Principal · Sur sombre — Taille: Grand · Moyen — État: Défaut · Appui · Désactivé; Icône (swap) |
| 73:2561 | Actions/Bouton écouter | Forme: Rond (41, brand gradient) · Avec libellé (32 + « Écouter ») · Puce sombre (« Écouter en wolof ») |
| 493:1965 | Actions/Bouton flottant | — |
| 543:41 | Actions/À faire | Avec Adia: Non · Oui |

## Forms (09)

| ID | Component | Variants |
| --- | --- | --- |
| 14:305 | Formulaires/Champ | Type: Une ligne · Plusieurs lignes — État: Défaut · Focus · Rempli · Erreur · Désactivé; label, hint, help, error texts; icons before/after. Height 50, value Body/Large. |
| 14:333 | Formulaires/Recherche | État: Défaut · Focus · Rempli |
| 14:384 | Formulaires/Liste de choix | État ×5 |
| 14:442 | Formulaires/Téléphone | État: Défaut · Focus · Rempli · Erreur |
| 14:458 | Formulaires/Case de code | État: Vide · Focus · Rempli · Erreur |
| 16:193 | Formulaires/Case à cocher | Coché, État |
| 16:204 | Formulaires/Choix unique | Choisi, État |
| 16:266 | Formulaires/Ligne de choix | Contrôle: Case · Choix unique · Interrupteur — Sélectionné |
| 83:1956 | Formulaires/Interrupteur | État: Activé · Désactivé — Style: Partage (green) · Réglage (blue) |
| 16:325 | Formulaires/Document | État: Vide · Envoi · Reçu · Vérifié · Échec · Vérifié par l’IA · Vérification demandée |
| 83:2043 | Formulaires/Calendrier | Type: Mois |
| 16:351 | Formulaires/Jour | État: Défaut · Aujourd’hui · Sélectionné · Événement · Hors mois · Passé |

## Chips and statuses (10)

| ID | Component | Variants |
| --- | --- | --- |
| 76:2180 | Statuts/Pastille | Ton: Positif · Attention · Info · Neutre · Critique — Forme: Plein · Contour — Surface: Clair · Sombre. h24, r30, Bold 12. |
| 76:2198 | Statuts/Niveau de preuve | Niveau: Dit par toi · Reçu · Vérifié · À éclaircir · Vérifié par l’IA · Vérification demandée |
| 76:2236 | Statuts/Puce | Type: Neutre · Positif · Positif fort · Attention · Échéance · Lieu · Délai (chips on dark cards) |
| 76:2202 | Statuts/Compteur | Nombre |
| 76:2251 | Statuts/Étiquette de catégorie | Surface: Clair · Sombre |
| 76:2267 | Statuts/Chip | Style: Choix · Option · Filtre — État: Défaut · Choisi |

## Cards and lists (11)

| ID | Component | Variants |
| --- | --- | --- |
| 78:2110 | Cartes/Ligne d’information | Valeur · Libellé et valeur · Avec pastille · Statut et date · Contact |
| 78:2149 | Cartes/Ligne de partage | Interrupteur · Modifier et interrupteur · Verrouillé · Réglage · Lien · Interrupteur coupé · Réglage activé |
| 78:2196 | Cartes/Identité | Personne · Lieu · Résumé acteur · Profil |
| 76:2286 | Cartes/Avatar | Initiales · Photo · Organisation · Adia · Vide |
| 78:2246 | Cartes/Ligne de menu | Simple · Notification · Organisation · Réglage · Aide · Icône · Icône et compteur · Organisation initiales |
| 78:2286 | Cartes/Connexion récente | Il t’a scanné · Il t’a scanné · vert · Tu l’as scanné |
| 78:2309 | Cartes/Section repliable | Fermée · Ouverte |
| 78:2337 | Cartes/Préparation | Note · Documents · Demandes |
| 78:2394 | Cartes/Activité | Entreprise · Recherche · Partenariat confirmé · Partenariat contrat · Offre |
| 78:2408 | Cartes/Événement | — |
| 78:2435 | Cartes/Code komkom | — |
| 78:2441 | Cartes/Note | Confiance |
| 78:2425 | Cartes/Titre de section | Style: Accueil · Icône · Icône 2 · Profil |
| 18:466 | Cartes/Encadré | Ton: Info · Positif · Attention · Neutre (1–3 sentences, fg/secondary) |
| 18:269 | Utilitaires/Emplacement | placeholder slot |

## Navigation (12)

| ID | Component | Variants |
| --- | --- | --- |
| 69:2491 | Navigation/Barre d’état | Ton: Sombre (on light) · Clair (on photo/dark) — 390×54 |
| 69:2633 | Navigation/En-tête | Type: Accueil · Titre et réglages · Retour et réglages · Retour · Fermer · Explorer · Profil · Parcours; Message non lu (bool) |
| 69:2543 | Navigation/Barre d’onglets | Actif: Accueil · Ma carte · Explorer — 356×63 capsule, active pill #015AA9 160×50 |
| 69:2652 | Navigation/Onglet | Actif · Inactif |
| 69:2685 | Navigation/Sélecteur | Style: Icône · Gris · Filtres — Actif: Gauche · Droite (segmented control, e.g. Ma carte / Ma préparation) |
| 69:2734 | Navigation/Raccourci | Sujet: Pour moi · Komkomnews · Spotlight · Acteurs · Explorer · Insights — Nouveau: Oui (gradient ring) · Non (thin grey ring) |
| 69:2750 | Navigation/Pagination | Position 1–3 |
| 69:2772 | Navigation/Progression de story | — |
| 20:493 / 20:494 | Navigation/Entrée latérale · Barre latérale | desktop sidebar |

## Sheets (13)

| ID | Component | Variants |
| --- | --- | --- |
| 21:528 | Superpositions/Feuille | Type: Choix · Détail · Confirmation. Bottom sheet, top corners 28, Elevation/3, scrim. Max 85 % height. |
| 21:382 | Superpositions/Option de feuille | Défaut · Choisie |
| 21:536 | Superpositions/Boîte de dialogue | — |

## Wekomkom patterns (14–20)

| ID | Component | Variants / role |
| --- | --- | --- |
| 24:756 | Opportunités/Carte opportunité | État: Ouverte · Appui · Fermée; show amount/meta/why/status, verified source, keep. Reading order: category + status → title → organisation → amount → deadline/place → why → action. |
| 24:803 | Opportunités/Ligne opportunité | compact list row |
| 531:2075 | Opportunités/Pour toi maintenant | Préparation: Pas encore · Presque · Prête (home feed card) |
| 79:2370 | Opportunités/Carte à la une | Image: Avec photo · Sans photo — dark 356×464 carousel card, amount Bold #FF9900 |
| 79:2401 | Opportunités/Carte connexion | — |
| 79:2669 | Opportunités/Story | Démarche · Il manque des preuves · Ça te correspond · Peut t’accompagner |
| 24:587 | Opportunités/Fait clé | Montant · Échéance · Lieu · Public |
| 88:2074 | Explorer/Carte à la une | Komkom News · Cartographie |
| 88:2105 | Explorer/Tuile de catégorie | Demi · Large · Large sombre |
| 25:730 | Correspondance/Pourquoi pour toi | 2–3 reasons (detail page) |
| 25:718 / 25:726 | Correspondance/Critère · Raison | Critère État: Ça va · À préparer · À éclaircir · À confirmer |
| 25:1015 | Correspondance/Bilan | Ça te correspond · Une chose à préparer · À éclaircir · Pas encore pour toi |
| 528:2130 | Correspondance/Jauge de préparation | Surface: Sombre · Clair — Position: Pas encore · Presque · Prête |
| 79:2224 | Prochaine action/Démarrer | Surface: Sombre · Clair (gauge + title + duration + button) |
| 79:2193 | Prochaine action/Signal | Presque · À préciser · Échéance · Arrivé · Prêt |
| 79:2280 / 80:2067 | Prochaine action/Jauge · Jauge icône | — |
| 80:2610 | Conversation/Message | Émetteur: Adia · Moi · Personne — Statut: Aucun · En attente · Fait · Document. Adia: white card 333 wide r20; Moi: bubble #E7F3FA right-aligned. |
| 80:2643 | Conversation/Saisie | Saisie · Action et saisie · Texte saisi |
| 26:898 | Conversation/Réponse rapide | Défaut · Appui · Choisie (outlined pills) |
| 26:915 / 26:928 / 26:939 / 26:1048 | Conversation/Réflexion · Ligne comprise · Compris · Sujet | — |
| 80:2616 / 80:2625 | Conversation/Champ · Vérification | — |
| 84:2046 | Voix/Panneau vocal | Écoute · Transcription · Relecture · Pas entendu · Adia parle · Micro bloqué |
| 82:1980 / 82:2010 / 82:2045 | Préparation/Avancement · Sujet · Élément | profile understood |
| 28:1003 / 28:1146 | Profil/Ce que Wekomkom a compris · Pour aller plus loin | — |
| 82:2094 | Démarches/Marche | Terminé · En cours · À venir |
| 29:1203 | Démarches/Étape | Fait · En cours · À venir · À regarder |
| 29:1481 | Démarches/Suivi de demande | En attente · Information demandée · Accord reçu · Non retenue |
| 82:2152 / 82:2158 / 82:2195 | Démarches/Candidature · Pièce à fournir · Preuve | — |
| 29:1489 | Démarches/Avant de partager | — |
| 28:1196 | Confiance/Source | Vérifiée · À vérifier · Ancienne |
| 61:2551 | Confiance/Carte komkom | Format: Compacte · Identité · Pleine (brand gradient, QR) |
| 61:2462 / 28:1251 | Utilitaires/QR | Code · Pictogramme |
| 61:2550 | Utilitaires/Logo | Marque couleur · Marque blanche · Logotype blanc |

## System states (21–24)

| ID | Component | Variants |
| --- | --- | --- |
| 30:1361 | Retours/Toast | Ton: Neutre · Succès · Erreur · Hors ligne (inverse bg, r15, 16 above tab bar, 4 s) |
| 30:1425 | Retours/Bannière | Ton: Info · Succès · Attention · Erreur |
| 30:1448 | Retours/Progression | Barre · Segments |
| 11:37 / 30:1459 / 30:1460 / 30:1478 | Chargement/Indicateur · Squelette · Carte opportunité · Recherche en cours | skeletons |
| 31:1491 | États/État vide | Rien pour toi maintenant · Première visite · Rien de gardé · Aucun résultat |
| 31:1580 | États/Erreur | Notre côté · Opportunité fermée · Hors ligne |
| 31:1647 | Connexion/Bandeau | Hors ligne · Reconnexion · De retour · Envois en attente |
| 31:1667 | Connexion/Élément en attente | En attente · Envoyé · Échec |

## Messages, trust, profiles (29–30)

383:58 Messages/Conversation · 383:63 Messages/Suivi enregistré · 383:368 Relais/Service
(Gratuit · Pris en charge · Payant) · 493:2001 Profil/Niveau de compétence ·
493:2054 Profil/Ligne de compétence · 493:2123 Profil/Appui reçu · 495:1997
Identité/Affiliation · 495:2002 Confiance/Carte collaborateur · 495:2032 / 495:2040 /
495:2049 Dataviz/Chiffre · Barre · Carte des régions · 517:2008 Filtres/Zone.

## Icons (06)

70 icons, `Icône/<name>`, 24×24 box, stroke 1.8 or filled. Always paired with a label
except universal gestures. Names: alert, arrow-left, arrow-right, banknote, bell, book,
bookmark, building, calendar, calendar-day, camera, check, check-circle, chevron-down,
chevron-left, chevron-right, clock, close, close-circle, cloud-check, document, edit,
external, eye, eye-off, filter, globe, help, history, home, hourglass, id-card, image,
info, insights, list, lock, logout, message, mic, more, paperclip, pause, pause-filled,
phone, pin, play, play-filled, plus, qr, refresh, scan, search, send, settings, share,
shield-check, skip, speaker-wave, stop, store, tag, trash, upload, user, users, volume,
wifi-off, zap. Find one with `page.query('COMPONENT[name="Icône/home"]')`.
