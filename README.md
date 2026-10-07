# Skills Claude — CONCREE

Skills Claude Code des projets CONCREE : affiches des programmes et écrans de l'app Wekomkom.

## Structure

```
posters/                      Affiches des programmes
  yeah-posters/               YEAH (webinaires, Spaces)
  goin-digital-posters/       Goin' Digital (panels, QR d'inscription)
  idea-lab-posters/           Idea Lab (cohortes, carrousels, cartes startup)
  jambaars-ai-posters/        JAMBAARS AI (événements, invitations)
wekomkom/                     Écrans de l'app Wekomkom (Figma)
  wekomkom-app-design/        Entrepreneure : parcours, fiches, écrans fictifs
  wekomkom-pilotage-design/   Bailleurs et pilotage
  wekomkom-relais-design/     Relais locaux
  wekomkom-vue-acteur-design/ Structures et acteurs professionnels
```

Chaque skill est un dossier avec un `SKILL.md` (déclencheur + marche à suivre) et, selon le cas : `references/`, `examples/`, `side-files/` (leçons de fabrication `build-lessons.md`, `checklist.md`, `qr.py`), `assets/`.

## Installer

Copier le dossier du skill voulu dans `~/.claude/skills/` (global) ou `<projet>/.claude/skills/` :

```bash
cp -r posters/yeah-posters ~/.claude/skills/
```

## Points à connaître

- **Affiches** : fond cuit en JPEG (`.deco` / `.content`), pas de masques ni de blend modes (mal capturés par Figma). Lire `side-files/build-lessons.md` (§10 : fautes relevées lors d'un audit) et passer `side-files/checklist.md` avant tout rendu.
- **Wekomkom** : seules Open Sans Regular / SemiBold / Bold sont chargeables dans Figma (pas Medium). Fichier de travail et pages : `wekomkom-app-design/references/figma-workflow.md`.
- Les affiches utilisent des outils Node/Python/Chrome locaux (Playwright, Pillow, `qr.py`) ; voir chaque `SKILL.md`.
