# Research & Inspiration

Scratchpad para referencias, análisis de competidores e inspiración directa para Hot Potato.

---

## Juegos de referencia directa

### Tag / Chase mechanics
**It (el juego de pillar)** — el core de HP es tag. Los mejores diseños de tag tienen:
- Tensión asimétrica: una persona vs. grupo
- La amenaza de la derrota permanente (estar "it" al final)
- Escalado dinámico para evitar stalemates

**Dead by Daylight** — asimetría 1 vs. 4; el Killer tiene XRay (Heartbeat mechanic que se parece exactamente al Terror Radius de HP). Reference para: terror radius design, escalado de Killer, anti-camp.

**Infected (modo en Halo/COD)** — la propagación de infección como mechanic. Reference para: modo Infected de HP; game feel de transformarse en el "bad team".

### Scoring basado en trolleo
**Among Us** → [[../wiki/analyses/among-us]] — FAP system tiene similitudes con el Impostor scoring social; el caos emergente del grupo.

**Gang Beasts** — ragdoll party chaos; los momentos más memorables vienen de interacciones físicas inesperadas. Reference para: el tone del juego, que morir sea gracioso.

### Parkour fluido
**Ghostrunner / Mirror's Edge** — parkour snappy y satisfactorio. Reference para: el feel del movimiento, no para la complejidad.

**Sunset Overdrive** — movimiento altamente mobile en contexto de party/chaos. Tono similar al que busca HP.

### Party games con items
**Mario Kart** — el sistema de items de HP está directamente inspirado en MK:
- Boomerang ≈ Red Shell (auto-tracking)
- Dodgeball ≈ Green Shell (disparo direccional)
- Spray paint ≈ Squid Ink
- Speed boost ≈ Mushroom
- Chewing gum ≈ Banana peel

**Fall Guys** → [[../wiki/analyses/jackbox]] — party game donde morir es gracioso, no traumático; pacing rápido.

---

## GDC talks relevantes

- **"Dead by Daylight: Designing Asymmetric Horror"** — diseño del terror radius, escalado del Killer, anti-camp. Muy aplicable a la Patata.
- **"Designing for Chaos: Party Game Systems"** — cualquier talk de Jackbox/Nintendo sobre party design
- **Masahiro Sakurai's YouTube** — especialmente episodios sobre party game design y fairness

---

## Análisis específico: ¿Por qué HP NO es un brawler?

El GDD de HP se auto-llama "party brawler" en algunos sitios pero el diseño real es diferente:

| Aspecto | Brawler (Smash) | Hot Potato |
|---------|----------------|-----------|
| Objeto de conflicto | Los players se atacan entre sí | Un player ES el objetivo (Patata) |
| Victoria | Más eliminations / último en pie | Más FAP / no ser Patata al final |
| Mecánica principal | Hit → knockback → ring out | Tag → transferencia de rol |
| Dirección de conflicto | Todo vs. todos IGUALMENTE | Patata vs. Todos (asimétrico) |

→ La referencia MÁS CERCANA a HP no es Smash — es **Dead by Daylight** (asimetría 1vN) + **Mario Kart** (items de caos) + **tag playground** (lógica de pillar)

---

## Variables clave a investigar antes del prototipo

1. **Dead by Daylight's terror radius** — cómo escala visualmente y auditivamente por proximidad (directamente aplicable a HP)
2. **Anti-camp systems en juegos de tag/asymétricos** — cómo otros juegos resuelven el problema del camping de la Patata
3. **Item economy en party games** — densidad de spawn, timing de reapparición, balance entre skill y luck
