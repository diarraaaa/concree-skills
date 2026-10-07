# Wekomkom — tokens and styles

Read from the Figma file's local variables and styles. In HTML, use
`assets/wekomkom-tokens.css` (same names, `--wk-` prefix, `/` → `-`).
In Figma, bind the **role** variables (collection *Color*, *Dimension*), never the
primitives (`color/blue/500`…), and apply the named text/effect/paint styles.

## Variable collections

| Collection | Count | Mode | Use |
| --- | --- | --- | --- |
| Primitives | 72 | Value | Raw palette. Not used directly. |
| Color | 73 | Light | Role tokens → bind these. |
| Dimension | 41 | Value | space, radius, size, layout, border-width |
| Motion | 7 | Value | durations and easings (strings) |
| Contenu | 4 | Valeur | fixed prices (strings) |
| Dataviz | 11 | Mode 1 | chart colors |

## Color roles (resolved)

| Group | Token → value |
| --- | --- |
| bg | canvas #FFFFFF · surface #FFFFFF · surface-subtle #F9F9FA · surface-muted #F1F4F6 · surface-sunken #F4F6F8 · surface-inverse #22364D · surface-inverse-raised white 6 % · brand-subtle #EAF4FD · selected #E7F3FA · scrim black 40 % |
| fg | primary #223245 · title #22364D · secondary #445972 · body #64748B · muted #5E6F86 · disabled #B5C1D0 · inverse #FFFFFF · inverse-muted #DFE5EC · brand #0958A5 · action #015AA9 · positive #357A11 · positive-inverse #59B224 · attention #A15C00 · accent #FF9900 · critical #FC121B · system #000610 |
| icon | primary #223245 · secondary #445972 · muted #6E7F93 · subtle #B5C1D0 · brand #0958A5 · action #015AA9 · inverse #FFFFFF · positive #59B224 · attention #FF9900 · critical #FC121B |
| border | default #E2E7EA · subtle #DFE5EC · control #DFE5EC · focus #0958A5 · selected #0958A5 · positive #59B224 · attention #FF9900 · info #015AA9 · critical #FC121B · inverse #DFE5EC 10 % |
| action | primary #0958A5 · primary-hover #015AA9 · primary-pressed #03345E · secondary #FFFFFF · secondary-pressed #F9F9FA · selected #015AA9 · tint #015AA9 6 % · tint-pressed #015AA9 10 % · glass black 10 % · disabled #F1F4F6 · critical #FC121B |
| control | selected #0958A5 · on #59B224 · off #F1F5FA |
| status | positive-bg #59B224 10 % · positive-bg-subtle 8 % · attention-bg #FF9900 10 % · attention-bg-subtle 8 % · info-bg #015AA9 8 % · critical-bg #FC121B 8 % · neutral-bg #F4F6F8 |
| brand / decor | gradient-start #0958A5 · gradient-end #59B224 · decor positive #59B224 · attention #FF9900 · notification #F73029 · sand #EFE3D2 |

Dataviz: seq-1…5 #CDE2FB #86B6EF #3987E5 #1C5CAB #0D366B · cat-1 #0958A5 · cat-2 #EB6834 · cat-3 #1BAF7A · cat-4 #EDA100 · neutre #B5C1D0 · piste #EEF2F6.

## Dimension

- **space/**: 0, 2, 5, 10, 15, 20, 25, 30, 40, 60, 80
- **layout/**: gutter-mobile 18 · gutter-tablet 32 · gutter-desktop 40 · content-max 1200 · reading-max 640 · sidebar 260
- **radius/**: xs 5 · sm 10 · md 15 · lg 20 · xl 25 · pill 30 · 2xl 40 · full 100
- **size/**: touch-min 48 · control-lg 50 · control-md 42 · control-compact 38 · control-sm 32 · badge 24 · icon-sm 16 · icon-md 20 · icon-lg 24 · icon-button-md 40 · avatar-sm 32 · avatar-md 40 · avatar-lg 64
- **border-width/**: hairline 1 · control 1.5 · focus 2

## Motion

duration instant 100 · fast 150 · base 220 · slow 320 ms; easing standard
`cubic-bezier(0.2,0,0,1)`, enter `cubic-bezier(0,0,0.2,1)`, exit `cubic-bezier(0.4,0,1,1)`.

## Paint styles (gradients)

| Style | Value | Where |
| --- | --- | --- |
| Gradient/Fond | #EAF4FD 0 % → #F7FFF3 40 % → #FFFFFF 100 %, vertical | Background of every mobile screen ("l'aube") |
| Gradient/Marque horizontale · verticale · diagonale | #0958A5 → #59B224 | Listen button, Adia, carte Komkom, "new" ring on shortcuts. Never on an action button. |
| Gradient/Carte sombre | #22364D 50 % → #223245 | Overlay on a photo in the one dark card |
| Gradient/Avatar | #E8F5E1 → #EFE3D2 48 % → #DDE9F5 | Avatar fallback |
| Gradient/Adia | #FF9900 24 % → #59B224 69 % | Adia mark |

## Effect styles

| Style | Value |
| --- | --- |
| Elevation/1 Card | drop shadow 0 4 8, black 5 % |
| Elevation/2 Floating | drop shadow 0 0 6, black 10 % (toasts, floating) |
| Elevation/3 Overlay | both of the above (sheets, dialogs) |
| Focus/Ring | spread 2 white + spread 4 #0958A5 |

## Grid styles

Grid/Mobile 4 columns, gutter 10, margin 18 · Grid/Tablet 8 / 20 / 32 · Grid/Desktop 12 / 20 / 40.

## Text styles (font: Open Sans; Figma style names "Regular", "Medium", "SemiBold", "Bold")

| Group | Styles (size, weight) |
| --- | --- |
| Display / Number | Display/Number 48 Bold · Number/Stat 24 Bold · Number/Medium 20 Bold · Number/Calendar 18 Medium |
| Title | Title/Page, Greeting, Section, Tile 20 Bold · Title/Card Large 18 Bold · Title/Header, Card, Card Single, Subsection 16 Bold |
| Body | Body/Large 16 Medium · Body/Message, Message Short, Input 15 Medium · Body/Default, Paragraph, Relaxed 14 Medium · Body/Small 12 Regular · Body/Small Strong, Compact 12 Medium |
| Label | Label/Large 16 Bold · Label/Medium, Navigation, Tab, Button Light, Value 14 Bold · Label/Button, Item, Item Tight 14 Medium · Label/Small, Compact, Small Multi 12 Bold |
| Meta | Meta/Default, Pill Outline 12 SemiBold · Meta/Small, Multi, Overline 12 Regular · Meta/Label, Compact, Date 12 Medium · Meta/Caption 11 Medium · Meta/Micro 10 Medium |
| System | System/Status 17 SF Pro Semibold (status bar only) |
| Doc (documentation pages only) | Doc/Display 64 · H1 40 · H2 28 · H3 20 · Body 16 · Body Strong 16 · Caption 13 · Code 13 Roboto Mono |

Line heights are the designer's (often tight, e.g. 16/12, 14/12). Always apply the
style rather than retyping values.
