# GDD: Movement

**Última actualización:** 2026-06-01

El sistema de movimiento es uno de los pilares de Hot Potato. El objetivo es un movimiento que se sienta snappy, responsive y ligeramente cartoon pero grounded. Debe ser compatible con GASP (motion matching).

---

## Run

### Objetivo
Movimiento base: snappy, responsive, sensation real de movimiento. Toda la aceleración/deceleración usa curvas, no valores instantáneos.

### Reglas
- Siempre activo (no hay walk alternativo)
- Left stick / WASD en cualquier dirección
- No se puede correr a través de objetos ni por >45° de pendiente
- En parkour, dirección no cambia hasta terminar la acción
- Se puede push/catch mientras se corre

### Características clave
- **Curva de aceleración**: de idle → full sprint gradualmente
- **Curva de deceleración**: al soltar input, frenado suave (inertia)
- **Turn sharpness**: cambios de dirección limitados; sin pivot 180° instantáneo. A más velocidad → más snap de dirección (efecto "quiebro")
- **Slope response**: bajada = más velocidad; subida = menos velocidad
- **Input buffering**: pre-input de jump/slide/roll aceptado durante el run

### Game feel (VFX/SFX)
| Elemento | Tipo | Descripción |
|----------|------|-------------|
| Dust particles al correr | VFX | Polvo pequeño por paso al tocar suelo |
| Speed acceleration | Camera FOV | Al llegar a velocidad X, FOV se amplía ligeramente |
| Stepping sounds | SFX | Pasos; más graves y pesados al sprintar |
| Strong brake | VFX/SFX | Partículas de polvo en dirección del freno + sonido de zapato frenando |

### Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `MaxRunSpeed` | float | Velocidad máxima al esprintar |
| `RunAcceleration` | float | Tasa de aceleración hasta full speed |
| `RunDeceleration` | float | Tasa de deceleración al soltar input |
| `TurnRedirectionDelay` | float | Delay antes de permitir cambio de dirección completo |
| `MaxTurnAnglePerSecond` | float | Ángulo máximo de giro por segundo corriendo |
| `SlopeSpeedBoostMultiplier` | float | Multiplicador bajando pendiente |
| `SlopeSpeedPenaltyMultiplier` | float | Multiplicador subiendo pendiente |
| `RunInputBufferTime` | float | Ventana para aceptar input anticipado (jump/slide) |
| `RunAnimPlayRateScale` | float | Escala playback animación según velocidad real |
| `IsRunning` | bool | Estado actual |

### Attribute interactions
- Timer <30s → velocidad de todos sube (`SpeedBoostPerSecond` = 10 units/s²)
- Si "injured" (stunned) → velocidad baja durante X segundos + limp animation
- Speed boost item → velocidad se multiplica durante X segundos

---

## Jump

### Características
- **Variable height**: cuanto más se mantiene el botón, más alto salta (hasta JumpHoldTimeMax)
- **Speed scaling**: distancia de salto escala con velocidad al despegar
- **Auto-parkour**: al mantener jump cerca de ledge → vault automático
- **Wall jump**: al lado de una pared, pulsar jump de nuevo para kick off
- **VFX dust** al despegar

### Fast fall + Roll
- Si caes desde >1.5m y pulsas slide ANTES de aterrizar → landing roll en el contacto
- Roll cancela el stun de aterrizaje y da un pequeño speed boost
- Sin roll → limping animation (penalización)

### Wave dash combo
```
Cae desde altura → Pulsa Slide antes de aterrizar (roll) → Pulsa Jump mid-roll → WAVE DASH
```
- Intensidad del wave dash escala con la altura de caída
- Cancela la penalización de aterrizaje
- Ideal para encadenar movimiento mid-combat o platforming

### Variables

| Variable | Descripción |
|----------|-------------|
| `JumpHoldTimeMax` | Tiempo máximo para el salto más alto |
| `JumpSpeedMultiplier` | Modificador de distancia basado en velocidad |
| `MinFallHeightForRoll` | Altura mínima para activar landing roll (1.5m) |
| `AirControlPercent` | % de control de suelo en el aire |
| `AirRedirectionTime` | Duración del cambio de dirección mid-air |
| `AirRedirectionAngle` | Ángulo máximo de redirección en aire |
| `RollSpeedBoost` | Velocidad ganada desde roll |
| `RollAnimIFrames` | Tiempo de invulnerabilidad durante roll |
| `RollDistance` | Distancia de la animación de roll |
| `LandingWindow` | Ventana antes de aterrizaje para activar roll |
| `WaveDashSpeedBoost` | Speed adicional del wave dash |

---

## Slide

### Características
- **Hereda velocidad de running** al iniciarse
- Bajando pendiente → aceleración extra
- Permite pasar por huecos y tight spaces (crouch height)
- Si se bloquea → transición automática a crouch
- Cadena: Slide → Roll → Jump → Wave dash

### Falling slide to roll
Si pulsas slide justo antes de tocar el suelo desde cierta altura → landing roll, previene limping/stun.

### Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `SlideBaseSpeed` | float | Velocidad mínima si se inicia desde idle |
| `SlideSpeedMultiplier` | float | Multiplicador aplicado a velocidad actual al iniciar |
| `DownhillAccelerationMultiplier` | float | Boost en pendiente descendente |
| `SlideDuration` | float | Tiempo que dura sin interrupción |
| `SlideStopFriction` | float | Resistencia que frena el slide |
| `CanSlideInAir` | bool | Permite slide mid-air (para fast fall) |
| `MinFallHeightForRoll` | float | Altura mínima para roll al slidear en aire |
| `WaveDashIntensityMultiplier` | float | Modificador de wave dash basado en altura de caída |
| `SlideToCrouchTrigger` | bool | Activa crouch si el slide se bloquea |
| `SlideChainBufferWindow` | float | Ventana para pulsar jump después de slide → wave dash |

---

## Parkour

### Auto-vault & Ledge grabs
- Corriendo hacia un ledge + **hold jump** → vault automático
- Si momentum es alto y el ledge es más alto (1.5m) → grab y hop up automático
- Sin hold jump → no sube

### Wall kick / Wall jump
- En el aire cerca de una pared → pulsar jump → kick off de la pared
- Preserva momentum, tiene air control parcial
- Útil para recovery o platforming avanzado

---

## Wave dash (detalle técnico)

```
Altura caída (mín: WaveDashMinFallHeight)
→ Pulsa Slide antes de aterrizar (roll)
→ Dentro de WaveDashWindow (0.3s): Pulsa Jump
→ WAVE DASH
```

Intensidad = `WaveDashBaseSpeed` + (`vertical fall speed` × `WaveDashSpeedFromFallMultiplier`)

### Variables

| Variable | Tipo | Descripción |
|----------|------|-------------|
| `WaveDashMinFallHeight` | float | Altura mínima para calificar (ej. 100cm) |
| `WaveDashWindow` | float | Ventana tras roll para pulsar jump (0.3s) |
| `WaveDashBaseSpeed` | float | Velocidad base añadida al momentum |
| `WaveDashSpeedFromFallMultiplier` | float | % de velocidad vertical convertida en horizontal |
| `WaveDashMaxRedirectAngle` | float | Ángulo máximo de cambio de dirección |
| `WaveDashCooldown` | float | Cooldown anti-spam (0.8s) |

---

## Push / Interact

### Descripción
Permite empujar o agarrar a otro player para alterar su trayectoria. FAP source principal para los runners.

### Controls
- **Push**: Left click / RT
- **Pull**: Right mouse / RB

### Mecánica
- En range (`InteractionRange` = 200u) → runner target tiene outline azul
- Push → burst de partículas + fuerza aplicada (10% de ground force)
- Pull → VFX beam entre ambos players hasta soltar
- Cooldown entre interacciones

| Variable | Tipo | Valor ejemplo |
|----------|------|---------------|
| `bCanInteract` | bool | true |
| `InteractionRange` | float | 200.0 |
| `PushForce` | float | 0.1 (10% ground) |
| `GrabForce` | float | 0.1 |
| `RedirectTime` | float | 0.25s |
| `MaxRedirectAngle` | float | 45.0° |
| `InteractionCooldown` | float | — |

---

## Air control

- Cuando está airborne (jump o caída): control parcial de dirección
- Redirección limitada y suave (no instantánea como en suelo)

---

## Cross-links al wiki

- [[../wiki/concepts/feel-and-controls/game-feel]] — 3Cs; identity extension; el movimiento debe sentirse como "yo soy el personaje"
- [[../wiki/concepts/feel-and-controls/input-and-controls]] — 240ms boundary; input buffering; deadzone
- [[../wiki/concepts/feel-and-controls/feedback-systems]] — feedback de cada acción de movimiento
- [[../wiki/concepts/player/flow-channel]] — movement depth como skill ceiling que mantiene el flow channel
