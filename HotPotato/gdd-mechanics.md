# GDD: Core Mechanics

**Última actualización:** 2026-06-01

---

## La mecánica central: el rol de Patata

El juego tiene **dos roles asimétricos**:

| Rol | Objetivo | Cómo gana |
|-----|----------|-----------|
| **Patata (Chaser)** | Pillar a un runner para pasarle el rol | No siendo Patata cuando el timer llega a 0 |
| **Runner** | Escapar y acumular FAP | Teniendo más FAP que todos los demás al final |

**La Patata siempre pierde puntos**: no puede ganar FAP mientras es Patata, y pierde FAP con el tiempo (decay). Esto garantiza que nadie quiera quedarse como Patata.

**El runner que más FAP tiene, GANA.** El que es Patata al final es forzado al último lugar en el podio.

---

## FAP — Fuck Around Points

El sistema de puntuación del juego. Todos los runners compiten entre sí por FAP, que se gana siendo disruptivo y creativo. El sistema tiene estas propiedades clave:

- **Servidor autoritativo**: todos los eventos FAP son validados server-side
- **La Patata no puede ganar FAP** mientras tenga el rol (flag `FAP_NoEarningWhilePotato`)
- **La Patata pierde FAP** con decay por tick (`FAP_PotatoDecayTick`, `FAP_PotatoDecayAmount`)
- **Anti-camping**: moverse poco durante `FAP_CampingThreshold` (8s) deduce puntos

### Tabla de puntuación FAP

| Acción | Puntos |
|--------|--------|
| Push a otro player | +5 |
| Push a la Patata | +20 |
| Usar ítem en otro player | +10 |
| Usar ítem contra la Patata | +15 |
| Guantes/slide contra la Patata | +25 |
| Dodgeball contra la Patata | +30 |
| Dodgeball contra player | +20 |
| Proximidad a Patata sin ser pillado | +1/5s |
| Salvar a player (empujar Patata lejos de él) | +25 |
| Activar trampa contra player | +15 |
| Activar trampa contra Patata | +20 |
| Slide contra player | +10 |
| Slide contra Patata | +25 |
| Emote cerca de la Patata | +10 |

### Multiplicadores

| Combo | Bonus |
|-------|-------|
| Knockover + push | +5 |
| Tagged after affected (tu stun ayuda a que la Patata pille) | +10 |
| Knocked out by trap | +5 |

### Deducciones FAP

| Acción penalizada | Puntos |
|------------------|--------|
| Ser stunned por push recibido | -5 |
| Ser pillado justo después de ser golpeado/stun | -10 |
| Ser knocked out por trampa | -5 |
| Camping (sin moverse `AntiCampThreshold` = 8s) | variable |

### Variables clave FAP

| Variable | Tipo | Valor ejemplo |
|----------|------|---------------|
| `FAP` | int | 0 |
| `BaseStartFAP` | int | 0 |
| `FAP_MaxCap` | int | — |
| `FAP_MinClamp` | int | — |
| `FAP_NoEarningWhilePotato` | bool | true |
| `FAP_PotatoDecayTick` | float | interval ticks |
| `FAP_PotatoDecayAmount` | int | puntos por tick |
| `FAP_CampingThreshold` | float | 8.0s |
| `FAP_CampingDeduction` | int | — |
| `FAP_ComboWindow` | float | — |
| `FAP_ComboBonus` | int | — |
| `FAP_StackCap` | int | max eventos iguales al mismo target |
| `FAP_SameVictimCooldown` | float | — |

---

## Tagging (pasar la patata)

La mecánica central de transferencia del rol.

### Cómo funciona

1. La Patata se acerca a un runner
2. Cuando el runner entra en `CatchRadius` (120u) → aparece outline azul sobre el runner + widget RT
3. La Patata presiona **RT** → animación de tag
4. Si es exitoso: runner recibe "You are Patata now" widget + smoke transition (1s) → runner ahora es Patata
5. Si falla: Patata hace animación de tropiezo (stun breve + wobble)

### Terror Radius (feedback al runner)

Cuando la Patata está dentro del radio de detección del runner → aparece un **streak rojo** en la dirección desde donde viene la Patata. A más proximidad, más brillante y grande.

### Patata Dive (habilidad especial)

Cuando la Patata está cerca de un runner, puede **mantener presionado el botón de catch** → se lanza hacia el runner.
- Si falla → stun + wobble + starts VFX

### Variables de tagging

| Variable | Tipo | Valor |
|----------|------|-------|
| `bIsPotato` | bool | — |
| `CatchRadius` | float | 120.0 |
| `CatchWindow` | float | 0.2s |
| `CatchCooldown` | float | 0.8s |
| `ChaserGroundSpeedMultiplier` | float | 0.95 |
| `PotatoXRayRange` | float | 1500.0 |
| `XRayPingInterval` | float | 1.5s |

### Condiciones de activación del tag

- Player DEBE ser Patata
- Runner DEBE estar en CatchRadius
- Patata NO debe estar stunned
- Player NO debe tener IFrames activos
- Game timer > 0

### Prioridades

- Si un player está stunned mientras le pillan → el stun del catch tiene prioridad
- No se puede pillar a otra Patata (en modo FFA)

---

## Escala dinámica de la Patata (anti-turtle)

Si la Patata no pilla a nadie durante 15 segundos, empieza a escalar:

| Tiempo sin pillar | Efecto |
|------------------|--------|
| 25s | Tier 1: ×1.2 speed y jump |
| 40s | Tier 2: ×1.5 speed y jump (no acumulativo) |

Esto garantiza que el tiempo de un chasing loop típico sea ~15s y que la Patata nunca sea inútil.

---

## Sistema de objetos

### Slots

Cada player tiene **2 slots de ítems**:
- **Slot 1**: Equipado (se usa con el botón de ítem)
- **Slot 2**: Almacenado

Al coger un giftbox:
- Si Slot 1 vacío → va a Slot 1
- Si Slot 1 lleno, Slot 2 vacío → va a Slot 2
- Si ambos llenos → reemplaza Slot 2 (el ítem anterior desaparece)

| Variable | Tipo | Valor |
|----------|------|-------|
| `CurrentItem` | enum | None + IDs |
| `StoredItem` | enum | None + IDs |
| `MaxHeldItems` | int | 2 |
| `ItemPickupCooldown` | float | 0.2s |
| `bCanPickupItem` | bool | — |

### Tabla completa de ítems

#### Universales (Patata + Runners)

| Ítem | Descripción |
|------|-------------|
| **Smoke bomb** | VFX cloud circular alrededor del que lo lanza |
| **Super jump** | Multiplica altura de salto; caída más flotante; mantiene air control |
| **Boomerang** | Se dirige automáticamente al player más cercano; no tiene contramedida excepto super jump, dodgeball bien apuntado, slide bajo plataforma, o caer |
| **Speed boost** | Speed boost breve; speed lines VFX; cámara se aleja ligeramente |
| **Dodgeball** | Green shell estilo Mario Kart pero dispara donde miras; KO players |

#### Solo Runners

| Ítem | Descripción |
|------|-------------|
| **Boxing gloves** | KO a otros players (incluyendo Patata); outline azul en range; stunned victim orbita estrellas + walk cómico + vignette |
| **Dummy** | Copia exacta del player que la lanza, corre por un spline predefinido para distraer |
| **Baseball bat** | Players hit ragdolean en dirección del swing (ángulo basado en cámara); si el player yeeted choca con otros, los tumba también |
| **Widowmaker hook** | Gancho que viaja en dirección del look; agarra ledges altos o viaja grandes distancias |
| **Chewing gum** | Trampa de suelo; cualquier player (incluida Patata) que lo pise se ralentiza durante X segundos |

#### Solo Patata

| Ítem | Descripción |
|------|-------------|
| **Double dash** | Dos dashes rápidos disponibles cuando la Patata quiera |
| **Tag magnet** | Radio que atrae a los players cercanos hacia la Patata e impide que se alejen |
| **Spray paint** | Squid ink de Mario Kart; afecta a todos menos a la Patata; se disuelve en X segundos |

---

## Leaderboard en tiempo real

- **Mini leaderboard in-game**: esquina inferior izquierda, Top 3 players con FAP actual
- **Efecto TopTrollVFX** al líder actual
- **End-of-Match podium**: 
  - 1st centro-top, 2nd y 3rd flanqueando
  - 4th+ listados verticalmente
  - Patata forzada al último con animación de lloros
  - Fanfare para top 3, sad trombone para Patata
  - Botón rematch disponible tras `RematchCooldown` (2.0s)

---

## Cross-links al wiki

- [[../wiki/concepts/mechanics/multiplayer-systems]] — conflicto asimétrico y roles
- [[../wiki/concepts/mechanics/game-loops]] — loop architecture (chase loop ~15s)
- [[../wiki/concepts/player/player-types]] — Achievers (FAP), Killers (trolleo), Socializers (momentos grupales)
- [[../wiki/concepts/player/motivation]] — reward schedules; loss aversion (patata pierde FAP)
- [[../wiki/analyses/among-us]] — referencia más cercana: rol asimétrico (potato ≈ impostor)
