# GDD: Overview

**Última actualización:** 2026-06-01 · **Fase:** Pre-producción · **Motor:** UE5 · **Target:** Steam

---

## Game title

**Hot Potato** *(working title — ver Q14 en open-questions)*

---

## Game Concept

**Pilla pilla basado en patata caliente, con objetos de Mario Kart y parkour.**

Un jugador aleatorio empieza siendo **La Patata** — el perseguidor. Su objetivo es tocar a otro jugador para pasarle el rol. El que sea la Patata cuando acaben los 120 segundos **PIERDE**.

Los runners (todos los demás) no solo huyen — **compiten entre sí acumulando FAP (Fuck Around Points)**: puntos ganados trolelando, usando ítems, empujando y haciendo el caos. **El runner con más FAP GANA.**

> El momento que define el juego: **el troll gana**. El mejor jugador no es el más rápido sino el más creativo siendo cabrón. Alguien puede apenas haber huido y ganar la partida por haberse dedicado a destrozar la vida de los demás.

---

## UPS (Unique Selling Points)

1. **El troll gana** — el sistema FAP recompensa activamente la creatividad disruptiva; jugar pasivo no da puntos. Ningún otro party game incentiva el caos de esta manera.
2. **Parkour como expresión** — wave dash, vault, wall jump crean una capa de movimiento expresivo que ningún party game tiene; el skill ceiling existe y se nota.
3. **La derrota es el espectáculo** — la Patata llorando en el podio es el momento más gracioso y memorable de la sesión. Perder produce el mejor clip.
4. **Local y online idénticos desde día 1** — mismo caos, mismos momentos sociales en sofá o por Discord. No hay experiencia de segunda clase.
5. **La Patata escala dinámicamente** — anti-camp + escalado OP garantizan que el chasing loop siempre sea viable y que el juego nunca se estanque.

---

## Target audience

**Primario**: Grupos de amigos (4–8 personas), 16–30 años, que juegan tanto en sofá como online por Discord. Les gusta Fall Guys, Mario Kart, Gang Beasts — juegos donde la partida genera conversación.

**Secundario**: Streamers y viewers — el sistema FAP y los momentos de trolleo producen clips naturales y reacciones grupales observables.

**Contexto de uso ideal**: sesiones de 30–45 min, local o online con voice chat, entre personas que se conocen. También funciona en convenciones/eventos para demos cortas con grupos rotativos.

---

## Platforms

**Primaria:** PC (Steam)
**Futura:** Consolas TBD

Local + online **igualmente importantes desde el día 1** — no es una feature secundaria, es parte de la promesa del producto.

---

## Genre

**Party tag game con parkour.**

Híbrido de:
- Juego de pillar clásico (pilla-pilla / tag)
- Patata caliente (el rol que nadie quiere tener al final)
- Sistema de ítems tipo Mario Kart (caos y creatividad > destreza pura)
- Parkour fluido como capa de expresión y habilidad

**No es**: un brawler (no hay knockouts como mecánica principal), ni un battle royale, ni un juego de esports.

---

## Art and Audio style

**Arte**: Gang Beasts como base de referencia — física caótica, tono absurdo, sensación de cuerpos blandos y movimiento impredecible. *(Referencia visual adicional pendiente — actualizar cuando el equipo comparta la foto.)*

**Audio**: Sonido a todo — el audio es feedback crítico. Cada acción tiene respuesta sonora inmediata. Música que escala de intensidad (pitch/tempo) conforme baja el timer.

Momentos de audio clave ya definidos:
- Slot machine: alarma + Formula 1 horn al liberar la jaula
- Nuevo Patata: "You are Patata now" SFX
- @30s: música crece, timer UI se agranda
- @5s: beeps finales, humo sale de la Patata
- Fin de partida: fanfare top 3 / sad trombone para la Patata

---

## Game Pillars

Los 5 principios que guían todas las decisiones de diseño. Si una feature no sirve a al menos uno, no pertenece al juego.

### 1. El troll gana
El sistema FAP recompensa ser creativo y disruptivo, no solo sobrevivir. La victoria viene de acciones activas sobre los demás. Si tienes que elegir entre huir y trollear a alguien, el juego te recompensa por trollear.

### 2. Perder es el espectáculo
La Patata llorando en el podio es el momento más memorable de la sesión. La derrota produce el mejor clip, el mejor chiste, la mejor reacción. La derrota no puede ser traumática — tiene que ser graciosa.

### 3. El movimiento es el alma
El parkour y el wave dash crean una capa de expresión que ningún otro party game tiene. El skill ceiling existe y los jugadores habilidosos se distinguen visiblemente, pero el skill floor es accesible. Esta es la característica diferenciadora de género.

### 4. La Patata siempre tiene recursos
La Patata nunca está desamparada. Anti-camp, escalado dinámico (×1.2 a 25s, ×1.5 a 40s), ítems exclusivos y XRay garantizan que siempre haya un camino para pillar a alguien. Un chasing loop roto no es divertido para nadie.

### 5. Local y online idénticos
El mismo caos, los mismos momentos sociales — en sofá con mandos o online por Discord con voice chat. Ningún modo es de segunda clase. Las decisiones de diseño (legibilidad a 2m de TV, feedback visual claro) sirven a los dos contextos simultáneamente.

---

## Estructura de la partida

```
Invite code → vote mapa/modo → playground lobby (tutorial, 30s AFK timer)
→ Slot machine (10s) → asigna primera Patata → jaulas bajan
→ 3-2-1 → MATCH (120s)
   Runners: acumulan FAP por trolleo, ítems, push
   Patata: persigue; si no pilla en 15s → escala dinámicamente
   @30s: speed boost general + timer crece
   @5s: timer pulsa + humo + beeps finales
→ Freeze 5s → PODIUM
   Runners ordenados por FAP — Patata forzada al último (llorando)
→ Rematch / Exit
```

---

## Navegación del GDD

- [gdd-mechanics](gdd-mechanics.md) — FAP system completo, tagging, 13 ítems, escala Patata
- [gdd-movement](gdd-movement.md) — run, jump, slide, parkour, wave dash, push/interact
- [gdd-systems](gdd-systems.md) — core loop, match timer, lobby, potato assignment, leaderboard
- [gdd-gamemodes](gdd-gamemodes.md) — FFA, Infected, TDM/Ranked/Custom
- [decisions](../decisions.md) — decisiones tomadas con rationale
- [open-questions](../open-questions.md) — 18 preguntas abiertas por urgencia

## Links al wiki

- [[../wiki/analyses/among-us]] — referencia de asimetría de roles (potato ≈ impostor)
- [[../wiki/concepts/mechanics/multiplayer-systems]] — diseño de conflicto asimétrico 1vN
- [[../wiki/syntheses/applying-the-canon]] — MDA y Sellers loops aplicados a HP
- [[../wiki/design-reference/mechanics]] — Lenses de balance, triangularidad y recompensas
