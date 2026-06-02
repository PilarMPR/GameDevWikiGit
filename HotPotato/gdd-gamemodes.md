# GDD: Game Modes

**Última actualización:** 2026-06-01

---

## Free for All (FFA) — modo principal

El modo core descrito en el resto del GDD. Un Patata, todos los demás runners, 120 segundos, FAP como sistema de puntuación.

- **Win condition runners**: más FAP al final
- **Win condition Patata**: no ser Patata cuando el timer llega a 0
- Todos los objetos disponibles (universales + rol-específicos)
- XRay de la Patata activo

---

## Infected

### Explicación

Un jugador empieza siendo Patata. Cuando pilla a otro runner, **ese runner también se convierte en Patata** (el rol se PROPAGA, no se transfiere). El objetivo:
- **Patatas**: infectar a todos los jugadores antes de que acabe el tiempo
- **Runners**: sobrevivir el tiempo límite (1.5 min*) sin que la Patata pille a nadie

Si la Patata no pilla a nadie en 1.5 min → la partida acaba y las Patatas PIERDEN.
Si se pilla a alguien → el pillado se transforma + el timer se REINICIA.
El proceso se repite hasta que todas las Patatas fallen (tiempo out) o hasta que todos sean infectados.

### Diferencias respecto a FFA

| Aspecto | Infected |
|---------|---------|
| Friendly fire | NO (ni entre jugadores, ni entre Patatas) |
| XRay | NO tiene |
| FAP system | Sigues ganando FAP por putear al bando contrario |
| Abilities (runners) | Speed boost (cooldown 10s*) + Super jump (cooldown 20s*) |
| Patata items | Baneados |
| Stun patata | Mata a la Patata → va al spawn tras cooldown |

### UI específica
- Contador de infectados y survivors
- Iconos de speed/super jump con cooldowns visibles

---

## Team Deathmatch

*(Sección vacía en el GDD origen — pendiente de diseño)*

---

## Ranked Mode

*(Sección vacía en el GDD origen — pendiente de diseño)*

---

## Custom Matches

*(Sección vacía en el GDD origen — pendiente de diseño)*

---

## Cross-links al wiki

- [[../wiki/concepts/mechanics/multiplayer-systems]] — diseño de modos con conflicto asimétrico
- [[../wiki/analyses/among-us]] — Infected es structuralmente similar al modo Impostor; la propagación del rol es el mechanic principal
