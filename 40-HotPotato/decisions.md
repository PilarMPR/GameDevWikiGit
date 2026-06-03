# Design Decisions Log

Append-only, cronológico. Ver [open-questions](open-questions.md) para las preguntas sin resolver.

---

## 2026-06-01 — La Patata es el chaser (tag game, no objeto físico)

**Status:** Locked

**Decisión:** Hot Potato es un juego de pillar (tag), NO un brawler donde pasas un objeto físico. El término "patata" se refiere al ROL del player que persigue — quien tiene el rol de Patata es el chaser. El rol se transfiere con el tag.

**Rationale:** Esta estructura crea dinámicas sociales más ricas que un objeto físico: el horror de convertirte en Patata, la satisfacción de pasar el rol, y la motivación constante de los runners para huir Y trollear simultáneamente.

**Basis:** (s011) [mda-feedback-dynamics](../10-Library/notes/mda-feedback-dynamics.md) — tag mechanic creates a balancing loop; (s005) [lens-38-competition-vs-cooperation](../10-Library/notes/lens-38-competition-vs-cooperation.md) — mixed competition/cooperation structure; [party-game-design-patterns](../10-Library/notes/party-game-design-patterns.md) — social punchline mechanic.

---

## 2026-06-01 — FAP (Fuck Around Points) como sistema de victoria de runners

**Status:** Locked

**Decisión:** Los runners no ganan simplemente sobreviviendo — ganan acumulando FAP a través de acciones disruptivas. El runner con más FAP al final del match gana.

**Rationale:** Sin un sistema activo de scoring, los runners solo tienen un incentivo (escapar) y el juego se vuelve pasivo. FAP garantiza que TODOS los players tengan decisiones interesantes constantemente — incluso mientras no son la Patata. Es también la fuente de los momentos sociales más memorables.

**Opciones descartadas:**
- Ganar solo por sobrevivir (demasiado pasivo; incentiva esconderse)
- Ganar por ser pillado menos veces (penaliza en vez de incentivar acción)

**Basis:** (s005) [meaningful-choices-triangularity](../10-Library/notes/meaningful-choices-triangularity.md) — FAP creates safe/risky choice triangularity; (s005, ch.11) [lens-32-meaningful-choices](../10-Library/notes/lens-32-meaningful-choices.md) — without FAP, runners have no interesting decisions; [multiplayer-conflict-types](../10-Library/notes/multiplayer-conflict-types.md) — active scoring converts indirect conflict to mixed conflict.

---

## 2026-06-01 — La Patata pierde al final (no win condition de la Patata)

**Status:** Locked

**Decisión:** El player que ES la Patata cuando el timer llega a 0 PIERDE — es forzado al último lugar en el podio con animación de lloros.

**Rationale:** La amenaza de la derrota permanente (no solo "pasar el rol") crea tensión genuina. El "chiste" del podio (Patata llorando) hace que la derrota sea funny rather than punishing — in line con el pilar "morir es el chiste".

---

## 2026-06-01 — Patata escala dinámicamente si no pilla en 15s

**Status:** Provisional (tiempos y multiplicadores a testear)

**Decisión:** Si la Patata no pilla a nadie en 15 segundos, recibe escalado de stats en tiers:
- Tier 1 (25s sin pillar): ×1.2 speed y jump
- Tier 2 (40s sin pillar): ×1.5 speed y jump (no acumulativo)

**Rationale:** Previene turtling y garantiza que el chasing loop sea siempre ~15s. Sin escalado, los runners con items y habilidades de evasión podrían trollear indefinidamente a una Patata débil.

**Revisit if:** Playtesting muestra que el Tier 2 es demasiado disruptivo o que la escalada es demasiado lenta para producir tags.

---

## 2026-06-01 — 2 slots de ítems; el segundo reemplaza al nuevo pickup

**Status:** Locked

**Decisión:** Cada player tiene 2 slots. Al recoger un tercer ítem, el ítem en Slot 2 se reemplaza.

**Rationale:** 1 slot es demasiado restrictivo y produce demasiada presión de decisión. 3+ slots rompe la economía. 2 slots con replace forzado del Slot 2 crea decisiones interesantes sin overhead cognitivo excesivo.

---

## 2026-06-01 — Movimiento: run siempre activo, no hay walking

**Status:** Locked

**Decisión:** Los players siempre corren. No hay toggle walk.

**Rationale:** La velocidad constante hace el juego más dinámico y reduce el cognitive overhead de "¿camino o corro?". Consistente con el ritmo de un party game activo.

---

## 2026-06-01 — Wave dash como movimiento avanzado opt-in

**Status:** Locked (mecánica existe; tuning pendiente)

**Decisión:** El wave dash existe como movimiento avanzado que requiere timing preciso (fall → slide before landing → jump mid-roll). No es necesario para jugar pero crea skill ceiling.

**Rationale:** Los party games exitosos tienen un "floor accesible" (cualquiera puede jugar sin wave dash) pero un "ceiling expresable" (jugadores habilidosos tienen tools adicionales). El wave dash cumple ese rol.

---

## 2026-06-01 — Los 5 pilares de diseño (validados por equipo)

**Status:** Locked

**Decisión:** Los 5 pilares son:
1. El troll gana
2. Perder es el espectáculo
3. El movimiento es el alma
4. La Patata siempre tiene recursos
5. Local y online idénticos

**Rationale:** Validados en sesión de alineación. El pilar 3 fue elegido explícitamente como diferenciador de género — lo que HP tiene que ningún otro party game tiene.

---

## 2026-06-01 — Logline oficial

**Status:** Locked

**Decisión:** "Pilla pilla basado en patata caliente con objetos de Mario Kart y parkour."

**Rationale:** Simple, referenciable, captura los 3 ejes del juego.

---

## 2026-06-01 — Local y online igualmente importantes desde día 1

**Status:** Locked

**Implicaciones de diseño:** Legibilidad a 2m en TV, feedback sonoro claro, UI funcional en los dos contextos. No se puede diseñar solo para mouse+teclado ni solo para sofá.

---

## 2026-06-01 — Arte base: Gang Beasts

**Status:** Provisional (referencia adicional pendiente — foto del equipo)

**Decisión:** Gang Beasts como referencia visual base. Referencia adicional a confirmar.

---

*(Añadir nuevas decisiones con formato: `## YYYY-MM-DD — [título]` + Status + Decisión + Rationale)*
