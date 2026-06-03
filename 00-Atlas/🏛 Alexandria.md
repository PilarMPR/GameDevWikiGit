---
type: moc
tags: [moc, home]
---
# Hot Potato — Síntesis de diseño

Todo lo del wiki teórico que aplica directamente a Hot Potato. Se actualiza cuando se ingiere material nuevo relevante o cuando una decisión de diseño conecta con teoría existente.

Ver el GDD en: [[../../HotPotato/_index]]

---

## El juego en una frase

Un jugador es la Patata (chaser). Los runners ganan FAP trolleando. El que sea la Patata al acabar PIERDE. Partidas de ~2 min, 2–8 jugadores, UE5, Steam.

---

## Core loop y MDA

**Mecánica:** tag asimétrico + FAP acumulativo + movimiento con parkour.
**Dinámica:** presión constante sobre la Patata, incentivo de trolleo para runners, información pública (quién tiene el rol).
**Estética:** tensión social, humillación cómica, caos controlado.

MDA aplicado (s011): el diseñador lee M→D→A. Una mecánica de tag simple genera dinámicas sociales ricas (señalamiento, alianzas temporales, trolleo) que producen la estética de "fiesta caótica". Ver [[../concepts/theory/mda-framework]].

---

## Teoría de la diversión aplicada

Koster (s016): fun = aprender patrones. En HP el patrón que se aprende es leer quién va a por ti, cuándo pasar el rol, cómo huir. El juego es divertido mientras ese patrón sigue siendo challenging — aquí entra el FAP como capa de profundidad que extiende el tiempo de aprendizaje sin complicar la lectura.

El riesgo: si el patrón se vuelve trivial (siempre pásalo al más cercano y ya), el juego se agota rápido. El anti-camp system y el diseño de ítems son los mecanismos que mantienen el patrón complejo. Ver [[../concepts/theory/theory-of-fun]].

---

## Flow channel

Con partidas de 2 min y 2–8 jugadores, el flow channel tiene características especiales (s005, ch.9):
- El umbral de aburrimiento es bajísimo — no hay tiempo para aburrise.
- El umbral de frustración es más relevante: si siempre eres Patata pierdes el hilo.
- La **escalada dinámica** (la Patata se vuelve más rápida con el tiempo) es el mecanismo de flow: sube el challenge a medida que el match avanza y el jugador se acomoda.

Ver [[../concepts/player/flow-channel]].

---

## Game feel y 3Cs

HP es un juego donde el **feel del movimiento es central** — los runners deben sentir que huir es satisfactorio en sí mismo (s007). Los tres building blocks de Swink:
1. **Real-time control:** input responsivo, sin input lag perceptible. El wave dash es el move de alto skill cap que requiere precisión temporal.
2. **Simulated space:** las físicas de parkour y slide deben sentirse coherentes — la arena es legible, los saltos predecibles.
3. **Polish:** VFX y sonido en el tag hit, en el FAP, en la transición de rol. Son los momentos emocionalmente más cargados.

Ver [[../concepts/feel-and-controls/game-feel]] · [[../concepts/feel-and-controls/input-and-controls]].

---

## Diseño asimétrico de roles

HP no es un brawler — es un tag game asimétrico. La asimetría (Patata vs Runners) crea experiencias radicalmente diferentes desde la misma partida. Referentes:
- **DBD** — terror radius, presión psicológica del hunter (ver [[../../HotPotato/research]])
- **Among Us** — lectura social, información asimétrica

El riesgo del diseño asimétrico: si un rol es objetivamente más divertido, los jugadores evitan el otro. HP lo resuelve haciendo que ser Patata sea humillante pero legible: pierdes, pero está claro por qué perdiste. Ver [[../analyses/among-us]] · [[../concepts/mechanics/multiplayer-systems]].

---

## Balance y FAP

El FAP es el sistema de victoria de los runners. Su balance es el punto más crítico del juego:

- FAP muy fácil de ganar → runners pasivos (esperan ítems en vez de trollear)
- FAP muy difícil → runners no ven progreso, pierden motivación
- La tabla de multiplicadores del GDD es el primer punto de calibración. Ver [[../../HotPotato/gdd-mechanics]].

Principio de Adams (s006): el balance no es simetría, es que ninguna estrategia domine a todas las demás. En HP: que pasar siempre el rol al más cercano no sea siempre la mejor estrategia → de ahí el boomerang y el anti-camp.

Ver [[../concepts/mechanics/game-balance]].

---

## Partidas cortas y retención

2 minutos es muy corto. Implicaciones de diseño:
- La curva de interés (s005) debe tener su pico en el último tercio — el anti-camp escalado cumple esto.
- El "one more game" loop requiere que la derrota sea inmediatamente legible y no frustrante.
- El lobby flow (slot machine, cage VFX) es parte del loop de retención — la anticipación antes de la partida.

Ver [[../concepts/player/player-psychology]] · [[../concepts/mechanics/game-loops]].

---

## Preguntas abiertas con respaldo teórico

*(Conectadas con [[../../HotPotato/open-questions]])*

- **Q1 (duración):** 120s puede ser demasiado corto para que el FAP system se sienta completo. Koster sugiere que el jugador necesita tiempo para "grokear" el patrón. Testear con 180s.
- **Q4 (boomerang):** Si la Patata no tiene contramedida al boomerang, viola el principio de Adams de que ninguna estrategia domine. Necesita al menos una respuesta (slide, caer, super jump).
- **Q5 (wave dash timing):** 0.25s LandingWindow es el parámetro de skill cap. Demasiado permisivo → el wave dash no se siente como logro. Demasiado estricto → inaccesible para casual players en un party game.

# 🏛 Alexandria — Game Design Library

The Library of Alexandria for game design. Every idea in the canon, one note at a time. Navigate by discipline, by bridge, or by the Hot Potato workspace.

---

## Syntheses — Working Knowledge (start here)

Cross-source topic compendiums. Everything the canon says on a practical topic, in one place.

- [Movement, Controls & Game Feel](../05-Syntheses/Movement%2C%20Controls%20%26%20Game%20Feel.md) — feel, 3Cs, camera, input, polish
- [Game Loops & Systems](../05-Syntheses/Game%20Loops%20%26%20Systems.md) — loops, mechanics, emergence, MDA, feedback
- [Player Psychology, Motivation & Flow](../05-Syntheses/Player%20Psychology%2C%20Motivation%20%26%20Flow.md) — flow, fun theory, motivation, player types
- [Game Balance](../05-Syntheses/Game%20Balance.md) — methods, transitive/intransitive, 12 balance types
- [Level Design, Pacing & Indirect Control](../05-Syntheses/Level%20Design%2C%20Pacing%20%26%20Indirect%20Control.md) — spaces, interest curves, indirect control
- [Narrative, World & Characters](../05-Syntheses/Narrative%2C%20World%20%26%20Characters.md) — story/game tension, world-building, characters
- [Iteration, Playtesting & Production](../05-Syntheses/Iteration%2C%20Playtesting%20%26%20Production.md) — process, prototyping, playtesting
- [Monetization, Retention & F2P](../05-Syntheses/Monetization%2C%20Retention%20%26%20F2P.md) — revenue models, retention, ethics

---

## Discipline Maps

| Discipline | MOC | Start here |
|---|---|---|
| 🧩 Mechanics | [Mechanics](disciplines/Mechanics.md) | [mechanics-definition](../10-Library/notes/mechanics-definition.md) → [mda-framework-overview](../10-Library/notes/mda-framework-overview.md) |
| 🎮 Feel & Controls | [Feel & Controls](disciplines/Feel%20%26%20Controls.md) | [game-feel-definition](../10-Library/notes/game-feel-definition.md) → [feedback-system-design](../10-Library/notes/feedback-system-design.md) |
| 🧠 Player | [Player](disciplines/Player.md) | [flow-channel-definition](../10-Library/notes/flow-channel-definition.md) → [player-motivation-maslow](../10-Library/notes/player-motivation-maslow.md) |
| 📖 Narrative | [Narrative](disciplines/Narrative.md) | [story-narrative-approaches](../10-Library/notes/story-narrative-approaches.md) → [indirect-control-methods](../10-Library/notes/indirect-control-methods.md) |
| 🗺️ Level Design | [Level Design](disciplines/Level%20Design.md) | [level-design-principles](../10-Library/notes/level-design-principles.md) → [spatial-design-principles](../10-Library/notes/spatial-design-principles.md) |
| 🔄 Production | [Production](disciplines/Production.md) | [iterative-design-process](../10-Library/notes/iterative-design-process.md) → [playtesting-methods](../10-Library/notes/playtesting-methods.md) |
| 💻 Programming | [Programming](disciplines/Programming.md) | (to be built) |
| 🎨 Art & Tech | [Art & Tech](disciplines/Art%20%26%20Tech.md) | (to be built) |
| 🔬 Theory | [Theory](disciplines/Theory.md) | [game-as-system](../10-Library/notes/game-as-system.md) → [mda-framework-overview](../10-Library/notes/mda-framework-overview.md) |
| 📱 Interface | [Interface](disciplines/Interface.md) | [norman-hcd-vocabulary](../10-Library/notes/norman-hcd-vocabulary.md) → [ui-design-hud](../10-Library/notes/ui-design-hud.md) |
| 💰 Business | [Business](disciplines/Business.md) | [f2p-design-foundation](../10-Library/notes/f2p-design-foundation.md) → [monetization-models](../10-Library/notes/monetization-models.md) |

---

## Cross-Discipline Bridges

- [Mechanics across the canon](bridges/Mechanics%20across%20the%20canon.md) — Schell tetrad ↔ MDA mechanics ↔ Adams types ↔ Fullerton formal elements
- [Pleasures & Aesthetics](bridges/Pleasures%20%26%20Aesthetics.md) — LeBlanc 8 pleasures ≡ Schell 8 pleasures
- [Iteration & Playtesting](bridges/Iteration%20%26%20Playtesting.md) — Fullerton ↔ Adams ↔ Schell ch.7
- [Flow & Mental Models](bridges/Flow%20%26%20Mental%20Models.md) — Csikszentmihalyi ↔ Koster ↔ Sellers
- [Magic Circle & Play](bridges/Magic%20Circle%20%26%20Play.md) — Huizinga ↔ Salen & Zimmerman ↔ Sellers

---

## Project Space

- [_index](../40-HotPotato/_index.md) — Hot Potato design workspace
- [[../30-Analyses/games/]] — game teardowns
- [[../30-Analyses/genres/]] — genre analyses

---

## Library

- [[../10-Library/sources/]] — 17 source cards (s001–s017)
- [Schell Lenses by Chapter](../20-Reference/Schell%20Lenses%20by%20Chapter.md) — all 100 Schell lenses
- [[../50-Feed/]] — online intake

---

## Meta

- [[../meta/CLAUDE.md]] — operating manual
- [[../meta/index.md]] — full content catalog
- [[../meta/log.md]] — activity log
