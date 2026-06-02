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
