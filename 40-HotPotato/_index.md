# Hot Potato — Project Design Space

**Studio:** Wild Alchemists · **Genre:** Party tag game con parkour · **Motor:** UE5 · **Target:** Steam · **Players:** 2–8

> 🖥️ **Command Center (live dashboard):** [HotPotato_CommandCenter](https://wildalchemists.github.io/HotPotato_CommandCenter/)
> Health score · Financial projections · Sprint board · Bug tracker · Marketing · Launch countdown

---

## Concepto en una línea

Un jugador es la Patata (el chaser). El resto son runners que ganan FAP (Fuck Around Points) trolelando a todos. El que sea la Patata al acabar el tiempo PIERDE.

---

## GDD (diseño actual)

- [gdd-overview](gdd/gdd-overview.md) — logline, UPS, target audience, plataformas, género, art/audio style, pillars
- [gdd-mechanics](gdd/gdd-mechanics.md) — mecánica de Patata, FAP system (tabla completa), tagging, items
- [gdd-movement](gdd/gdd-movement.md) — run, jump, slide, parkour, wave dash, push/interact
- [gdd-systems](gdd/gdd-systems.md) — core loop, match timer, lobby, potato assignment, leaderboard, anti-camp
- [gdd-gamemodes](gdd/gdd-gamemodes.md) — FFA, Infected, TDM/Ranked/Custom

## Producción y finanzas

- [production](production.md) — sprint activo, backlog, milestones y log de producción
- [finance](finance.md) — presupuesto, gastos e ingresos del proyecto

## Documentos de trabajo

- [decisions](decisions.md) — log de decisiones de diseño (append-only; cada entrada lleva **Basis:** con fuentes)
- [open-questions](open-questions.md) — preguntas abiertas por tier de urgencia
- [research](research.md) — referentes, análisis de competidores
- [hot-potato-design](hot-potato-design.md) — síntesis de teoría aplicada a HP (de wiki/syntheses/)

## Scratchpad y prompts

- [brainstorming](scratchpad/brainstorming.md) — ideas en bruto
- [[prompts/]] — prompt library de Claude para HP

---

## Library references for Hot Potato

All library notes tagged `hp: true`. Use this view during GDD sessions.

```dataview
TABLE disciplines, sources, status FROM "10-Library/notes"
WHERE hp = true
SORT disciplines ASC, title ASC
```

---

## Lens quick-review for Hot Potato

Schell lenses relevant to HP (for design review sessions):

```dataview
TABLE lens FROM "10-Library/notes"
WHERE hp = true AND lens >= 1 AND lens <= 100
SORT lens ASC
```
