# Open Design Questions

Lista viva de preguntas sin resolver. Las preguntas resueltas van a [decisions](decisions.md).

**Tiered por urgencia** — Tier 1 debe resolverse antes del primer prototipo jugable.

---

## 🔴 Tier 1 — Antes del prototipo

### Q1 — Duración del match: 120s es el target, ¿se confirma?
El GDD establece `MatchDuration: 120.0`. ¿Es esto correcto?
- 2 minutos puede ser muy corto para que el FAP system se sienta completo
- 3 minutos (180s) daría más tiempo para momentos sociales emergentes
- **Current**: 120s como punto de partida; testear en primer prototipo

### Q2 — ¿El anti-camp también se aplica a la Patata o solo a runners?
El GDD menciona anti-camp genéricamente. ¿Tiene sentido penalizar a la Patata por no moverse cuando puede estar esperando una oportunidad?
- **Implicación**: si la Patata hace camping en una zona, el sistema debería revelarla a todos

### Q3 — Número de items en la arena: ¿cuántos giftboxes spawnan simultáneamente?
El GDD define los ítems pero no la densidad de spawn en el mapa.
- Demasiados giftboxes: demasiado caos; todos siempre tienen ítems
- Muy pocos: el sistema de ítems se vuelve irrelevante para algunos players

### Q4 — Boomerang: ¿tiene contramedida la Patata?
El GDD establece que el boomerang no tiene contramedida para el target, EXCEPTO: super jump, dodgeball bien apuntado, slide bajo plataforma, o caer.
- La Patata está excluida de tener super jump y dodgeball
- ¿Puede la Patata usar slide o caer para evitar el boomerang?
- **Implicación en balance**: el boomerang podría ser demasiado OP contra la Patata

### Q5 — Wave dash timing window
¿Cuál es la `LandingWindow` correcta? El GDD sugiere 0.25s pero esto requiere calibración.
- Demasiado permisivo → wave dash deja de sentirse como skill
- Demasiado estricto → inaccessible para casual players en un party game

---

## 🟡 Tier 2 — Antes de alpha

### Q6 — ¿Cómo funciona el spawn inicial de players en el mapa?
El GDD menciona una "holding area" con jaulas. ¿Cuánto espacio hay? ¿Los players pueden interactuar entre sí durante la animación de slot machine?

### Q7 — ¿Qué pasa si la Patata cae fuera del mapa?
¿Respawn? ¿Penalización? ¿El rol se transfiere?

### Q8 — Loot box visibility: ¿son visibles en el minimapa/a través de paredes?
Importante para la decisión de correr hacia un ítem vs huir de la Patata.

### Q9 — ¿El Dummy ítem engaña a la XRay de la Patata?
El Dummy es una copia exacta del player. ¿La XRay lo detecta también? Si es así, no funciona como contramedida de la XRay.

### Q10 — Detalle de la mecánica "Patata Dive"
El GDD menciona que si la Patata mantiene presionado el botón de catch cuando está cerca → se lanza hacia el runner. ¿Cuál es exactamente el range de activación? ¿Cuánto tiempo hay que mantener el botón?

### Q11 — Infected: ¿cuánto tiempo dura el cooldown de respawn al morir?
El GDD dice "stunned Patata en Infected → muere y va al spawn tras cooldown" pero no define el cooldown.

### Q12 — ¿El Spray paint (ítem de Patata) afecta las cámaras/UI o solo la visión del mundo?
Comparado con el Squid Ink de MK, ¿cubre la pantalla completa o solo parte del mundo?

---

## 🟢 Tier 3 — Puede esperar a beta

### Q13 — Art style y dirección visual
El GDD no define el art style. ¿Cartoon? ¿Semi-realistic? ¿Referencias?

### Q14 — Nombre final del juego
"Hot Potato" es el working title. ¿Se queda?

### Q15 — 5º pilar de diseño
El pilar 5 está como TBD en el overview. Candidatos:
- "Steam party" (local + online equally first-class)
- "Cada derrota es un chiste, no un drama"
- "Legible desde el sofá" (todo feedback visible a 2m)

### Q16 — ¿Team Deathmatch / Ranked tienen FAP o un sistema diferente?
Los modos adicionales están vacíos en el GDD. ¿FAP sigue siendo la métrica o cada modo tiene su propia win condition?

### Q17 — Map Forest y otros mapas: ¿cuántos en lanzamiento?
El GDD menciona `Map_Forest` como ejemplo. ¿Cuántos mapas se planean para el lanzamiento?

### Q18 — ¿Cómo funciona el matchmaking online?
¿Solo lobby privado (invite code) o hay matchmaking público también?

---

*(Mover a [decisions](decisions.md) cuando estén resueltas)*
