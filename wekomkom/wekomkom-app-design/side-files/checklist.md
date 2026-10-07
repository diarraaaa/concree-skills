# Before delivering a Wekomkom screen

From the design system's « Avant de livrer » list (section 01) plus the visual traits.
P0 must all pass. Fix P1 unless the brief says otherwise.

## P0 — blocking

- [ ] **Not a duplicate.** The parcours fiche (`references/flows/`) was read; the screen does not already exist in the reference file, or the delivery says what it changes compared to the existing one.
- [ ] **Free, correct code** (`<parcours>-<row><n> · <titre>`), not already used on page 22; fictional pages say « (fictif) ».
- [ ] **The parcours' decisions are respected** (« Tranché le 4 octobre » and the final-pass rules in flows/README.md).
- [ ] **One useful thing.** The single most useful action on this screen carries the only primary button.
- [ ] **At most one dark card** (Prochaine action *or* Opportunité à la une, never both).
- [ ] **Background is the dawn gradient** (`Gradient/Fond` / `--wk-gradient-canvas`), not flat grey or white.
- [ ] **Semantic tokens only**: every colour from a Color role, every gap/padding from `space/*`, every radius from `radius/*`. No raw hex in new work.
- [ ] **Brand gradient only on** the listen button, Adia, the carte Komkom (and the "new" shortcut ring). Action buttons are solid blue.
- [ ] **No forbidden word**: score, note, éligible/éligibilité, certifié, validé, readiness, palier, dimension, dashboard, matching, scoring, remédiation.
- [ ] **Fits 360 px wide** in long French (and +30 % text): nothing cut. Amount, deadline, opportunity name and status never truncated.
- [ ] **Built from components** (Figma: instances from page `7:27`, nothing detached; HTML: the documented patterns).
- [ ] **Designer's page `0:1` untouched**, original file `a2r1R8eCYmxaTiLNIW7x9m` untouched.

## P1 — quality

- [ ] Cards: white, 1 px `border/default`, `Elevation/1`, radius 15. No coloured border, no heavier shadow.
- [ ] Everything tappable is a pill or round; touch targets ≥ 48.
- [ ] Status and category = icon + word, never colour alone. Orange/green text on light only in framed use.
- [ ] Small label 12 px + bold value pattern for facts; titles Bold, body Medium.
- [ ] A listen button next to what matters (moment card, Adia messages).
- [ ] Every information shows where it comes from and when (Confiance/Source).
- [ ] Empty, loading, offline and error states considered (sections 21–24); none is a dead end.
- [ ] Copy: tu, short sentences, verb + object buttons, formats (3 000 000 FCFA · 30 oct. · 15 h · +221 77 123 45 67).
- [ ] Real photos or the documented placeholder; no stock or AI faces.
- [ ] Focus ring visible on controls (HTML: `--wk-focus-ring`).

## P2 — polish

- [ ] Screen name follows `<flow>.<n>-<code> · <titre>` and sits in the right flow page/row.
- [ ] Bottom margin keeps the last content above the floating tab bar.
- [ ] Compared side by side with the closest reference in `references/screens/`.
