# GDD: Systems

**Última actualización:** 2026-06-01

---

## Core loop (macro)

```
[LOBBY] Invite code → vote mapa/modo → playground (30s AFK timer)
  ↓
[ASSIGNMENT] Slot machine (10s) → asigna primera Patata → jaulas bajan
  ↓
[MATCH] 120 segundos
  ↓ (loop interno)
  Chasing loop ~15s:
    Patata persigue → tag exitoso → nuevo runner se convierte en Patata
    Si no hay tag en 15s → Patata escala (Tier 1 @ 25s, Tier 2 @ 40s)
  ↓
  Runners acumulan FAP por acciones disruptivas en paralelo
  ↓
[ENDGAME] @30s: timer crece, speed boost general
  @5s: timer pulsa, humo Patata, beeps
  @0s: freeze 5s → LEADERBOARD
  ↓
[POSTMATCH] Podium FAP (Patata forzada última) → Rematch / Exit
```

---

## Match timer

| Variable | Tipo | Valor |
|----------|------|-------|
| `MatchDuration` | float | 120.0s |
| `Phase30sThreshold` | float | 30.0s |
| `Phase5sThreshold` | float | 5.0s |
| `MusicPitchCurve` | Curve | RemainingTime/Phase30s → pitch hasta ×1.2 |
| `SpeedBoostPerSecond` | float | 10.0 (units/s²) cuando <30s |
| `FinalBeepInterval` | float | 1.0s (cuando ≤5s) |
| `EndFreezeDuration` | float | 5.0s antes del leaderboard |

### Visual/Audio feedback del timer
- **@30s**: Timer UI crece (center pivot)
- **@5s**: Timer pulsa + smoke sale de la Patata + beeps cada segundo
- Música: pitch sube linealmente conforme queda menos tiempo

---

## Lobby y match setup

### Flujo de lobby
1. Host genera código (ej. "AB12CD")
2. Players se unen por código o invite
3. Vote de mapa/modo en pre-lobby
4. **Playground lobby**: zona interactiva donde los players practican controles
   - Hay widgets y art signs con los controles y mecánicas
   - En convenciones: checklist de todos los movimientos posibles a completar antes de poder dar ready
   - Si players no dan ready en 30s → countdown de 10s para forzar inicio
   - Ready button se llena visualmente cuando todos dan ready
5. Todos ready → countdown 3-2-1 → match start

| Variable | Tipo | Valor |
|----------|------|-------|
| `MaxPlayers` | int | 8 |
| `InviteCode` | string | "AB12CD" |
| `CountdownTimeLobby` | float | 10.0s |
| `ReadyGracePeriod` | float | 5.0s |
| `LobbyAuthority` | enum | Host |
| `AssetSyncTimeout` | float | 8.0s |

---

## Potato assignment (inicio de partida)

### Flujo
1. Todos los players spawnan en una holding area
2. **Slot machine animation** (10s): widget con imagen de la Patata rebota entre las cabezas de los players
3. Concurrent: **jaulas bajan** (beams de metal bajan + alarma sound + Formula 1 horn cuando la jaula está completamente abajo)
4. La animación desacelera → aterriza en el player elegido → "poof" smokebomb + el player se transforma en Patata
5. La jaula libera a todos simultáneamente
6. `bAssignmentInProgress` → bloquea input hasta que termine la secuencia

| Variable | Tipo | Valor |
|----------|------|-------|
| `AssignmentDuration` | float | 10.0s |
| `InitialBounceInterval` | float | 0.1s |
| `FinalBounceInterval` | float | 0.5s |
| `IntervalDecelerationCurve` | Curve | Ease-Out |
| `MaxConsecutivePotatoes` | int | 2 (max veces consecutivas el mismo player) |
| `CageLiftHeight` | float | 500.0 uu |
| `CageLiftDuration` | float | 1.0s |
| `bAssignmentInProgress` | bool | bloquea tag/input |

---

## Leaderboard en tiempo real

| Variable | Tipo |
|----------|------|
| `LiveLeaderboardUI` | Widget (bottom-left, top 3) |
| `TopTrollVFX` | VFX al líder FAP actual |
| `FAP_LeaderboardSlots` | int (top N in-match) |

### Anuncio mid-match de nuevo Patata
- Cuando un runner es pillado:
  - Widget small en lower-left: "New Potato!"
  - Nuevo Patata: "You are Patata now" widget

---

## End-of-match podium

| Posición | Layout |
|---------|--------|
| 1st | Centro-top |
| 2nd | Flank izquierdo |
| 3rd | Flank derecho |
| 4th+ | Listados verticalmente encima del podio |
| Patata | Forzado al último, con animación de lloros y bounce |

**Audio:**
- Top 3: Fanfare triunfante
- Patata: Sad trombone / circus "wah-wah"

**Botones:** Rematch / Exit to Lobby, greys hasta `RematchCooldown` (2.0s)

---

## Loop hierarchy (Sellers framework)

→ Ver [[../wiki/concepts/mechanics/game-loops]] para la teoría

**Interactive loop** (~segundo a segundo):
Player input → character responde → game state changes → feedback → nueva decisión

**Core gameplay loop** (chasing loop, ~15s):
Patata persigue → intenta tag → éxito/fallo → FAP events → nueva posición → new chase

**Round loop** (90-120s match):
Assignment → chase loops → escalado Patata → endgame tension → podium

**Session loop** (varias partidas):
Match → podium → rematch vote → nueva assignment → siguiente match

---

## Anti-camp system

- Si un player (Patata o runner) permanece sin moverse durante `AntiCampThreshold` (8s)
- Se activa: horn/arrow indica su posición a todos + deducción FAP (`FAP_CampingDeduction`)
- Indicador visible `AntiCampIndicatorDuration` (2.5s)

---

## Cross-links al wiki

- [[../wiki/concepts/mechanics/game-loops]] — loop architecture y Sellers' 4 loops
- [[../wiki/concepts/level-design/pacing-and-flow]] — interest curve del match (hook → build @30s → climax @5s → resolution)
- [[../wiki/concepts/player/flow-channel]] — el match timer como mecanismo de escalado de tensión
- [[../wiki/concepts/player/motivation]] — reward schedules, loss aversion (FAP decay de Patata)
