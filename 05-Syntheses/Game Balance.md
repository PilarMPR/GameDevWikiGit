# Game Balance

> **What this is:** Everything the canon says about balancing games — methods, structures, the 12 Schell balance types, difficulty design, and the relationship between balance and the flow channel. Aggregated across s005, s001, s011, s006, s014.

---

## 1. What Balance Is

**Sellers** (s001, ch.9):
> *"Balance is a property of the complete game+player system — not the game alone. It emerges from the relationships between parts: their attributes, values, and behaviors. A well-balanced game avoids dominant strategies, keeps players in the flow channel, and offers a probability space worth exploring. Balance is never 'done.' Build resilient systems, not perfect ones."*

**Schell** (s005, ch.11):
> *"Balancing a game is adjusting its elements until they generate exactly the experience you want."*

The culinary analogy: not just identifying the ingredients (mechanic design) but calibrating proportions and combinations. The most artisanal skill of design.

**MDA** (s011): balance is not experienced at the Mechanics level — it's experienced at the Dynamics level. The Monopoly flaw is a mechanics-level positive feedback loop that produces wrong Dynamics → wrong Aesthetics. Balance failures are Dynamics problems disguised as Mechanics problems.

---

## 2. Four Methods of Balance (Sellers, s001, ch.9)

| Method | What it is | When to use |
|---|---|---|
| **Designer-based** | Intuition and judgment from experience | First approximation; always present |
| **Player-based** | Observing real player behavior in playtests | Playtesting; behavioral data |
| **Analytical** | Data and analytics from the running game | Live games; post-launch tuning |
| **Mathematical** | Probabilities, models, expected values | Economy design; chance systems |

None alone is sufficient. The mathematical model informs the designer; playtesting with real players corrects both. In live games, analytical balance via player data is the primary post-launch tool.

**Schell's methodological rules** (s005, ch.11):
- **Double and halve:** when changing a value to balance, don't increment in small steps. Double or halve it to find the useful range quickly, then refine. William Blake: *"You never know what is enough unless you know what is more than enough."*
- **Problem before solution:** state the problem clearly before proposing a fix. Many cascading balance errors come from fixing symptoms while the root cause persists.
- **Playtest with a skill mix:** the development team is too expert; novices alone show only the entry experience. Mixed-skill playtesting reveals the full difficulty curve.

---

## 3. Structural Balance — Transitive vs. Intransitive

### Transitive systems (s001, s005)

Ordered power hierarchy: A > B > C > D. A clear ranking exists.

**The dominant strategy problem:** when one option is strictly better than all others in all situations, strategic depth collapses. Players who discover it stop making decisions — they just execute the dominant strategy.

> *"Once a dominant strategy is discovered, the game is no longer fun, because the puzzle of the game has been solved."* (s005, ch.11)

**Exploits are hidden dominant strategies.** When a developer removes an exploit, a novice designer panics — "now I can't beat the game." In reality, removing the dominant strategy is a depth *increase*: the game just gained a layer of strategic complexity.

**Balancing transitives:** assign numerical value to each attribute, sum per option, adjust until totals are comparable. Then validate with playtesting. The math informs the prototype; the prototype informs the math.

*Biplane Battle example* (s005): speed, maneuverability, firepower each scored; adjust until total scores are equivalent across aircraft types.

### Intransitive systems (s001, s005)

Cyclic relationships: A beats B, B beats C, C beats A. Rock-paper-scissors is the archetype.

**The structural advantage:** no option is universally superior. The "meta" cannot be solved with a single choice — context always determines which option is best.

**Applications:**
- Unit triads in strategy games: infantry > cavalry > archers > infantry
- Weapon triads in action games: close-range > mid-range > long-range > close-range
- Character triads in brawlers: grappler > zoner > rush-down > grappler

The intransitive relationship ensures all options have value. It creates the condition for genuine strategic decision-making — "which option is best *right now*, against *this opponent, in this situation?*"

---

## 4. The Twelve Balance Types (Schell, s005, ch.11)

Schell identifies 12 distinct dimensions that must each be examined:

### Type 1: Fairness
*Lens #30*

**Symmetric games** — all players start with identical resources. The only variable is skill. Problem: first-player advantage exists in many symmetric games.

**Asymmetric games** — players have different powers, resources, or win conditions. Legitimate reasons:
1. Simulate real-world situations (war, negotiation)
2. Let players explore different strategies
3. Personalize for player strengths
4. Level the field between skill-disparate players
5. Create tactically interesting situations

**Alien vs. Predator example** (s005): Predators have mechanical advantages. Players accept this because it's coherent with the fiction, and beating a Predator as an Alien becomes a prestige achievement. **Perceived fairness matters as much as mathematical fairness.**

### Type 2: Challenge vs. Success
*Lens #31*

The flow channel applied to difficulty design. Techniques:
- Increase difficulty with each success (build player toward their personal ceiling)
- Let skilled players skip trivial sections (speed/efficiency rewards)
- Layer challenge tiers (C/B/A/S completion grades — different players find their own threshold)
- Never forget: just learning the controls is the first challenge

> *"The first level or two should be very simple — the player is already challenged trying to understand the controls and goals."* (s005)

### Type 3: Meaningful Choices
*Lenses #32–33*

Choices = Desires → freedom. Choices > Desires → overwhelmed. Choices < Desires → frustrated.

**Not quantity but quality.** Fifty vehicles with identical handling = zero meaningful choices. Two weapons that genuinely play differently = two meaningful choices.

**Triangularity** (Lens #33): the most compelling choice structure — safe/low-reward vs. risky/high-reward. *Space Invaders* mystery saucer: normal aliens are safe and give few points; the saucer requires exposing yourself but gives 100–300 points. The "do I go for it?" decision recurs throughout the session without losing tension.

**Expected value calibration** (Lens #28): for triangularity to work, risky paths must have roughly comparable expected value to safe paths. (*Qix* example: slow encircle = double points + harder, fast encircle = fewer points + easier; probabilities calibrated to equal expected value.)

> *"About 8 out of 10 times someone asks for help on a prototype that 'just isn't fun,' the game is missing this kind of meaningful choice."* (Schell)

### Type 4: Skill vs. Chance
*Lens #34*

More chance → relaxed, casual, less-fair measure of skill. More skill → competitive, serious, measure of excellence.

**Alternation pattern:** dealing cards is chance; playing them is skill. Rolling dice is chance; moving the piece is skill. This alternation between chance and skill creates pleasurable tension and release rhythms.

Preference varies by audience, age, culture (German-style board games minimize chance vs. American-style).

### Type 5: Head vs. Hands
*Lens #35*

Physical skill (reflexes, speed, accuracy, coordination) vs. cognitive skill (strategy, planning, memory, pattern recognition).

Both can coexist — boss fights often require *understanding* the pattern AND executing it with precision simultaneously. The critical rule: **communicate which type of challenge the game offers**. *Pac-Man 2* failed because the box implied action; the game was psychological puzzles. Players of both types were deceived.

### Type 6–7: Competition vs. Cooperation
*Lenses #36–38*

Two fundamental human drives:
- **Competition** — establish status, demonstrate mastery
- **Cooperation** — amplify collective capability, build social bonds

Options:
- Pure competitive (chess, fighting games)
- Pure cooperative (Pandemic, Left 4 Dead)
- Mixed (*Joust* — players compete for points but can coordinate for mutual survival, with dedicated "Team Waves" and "Gladiator Waves" that incentivize each mode alternately)
- Team competitive: combines both simultaneously

The mixed/team format produces the richest social dynamics — the tension between competing and cooperating is itself the gameplay.

### Type 8: Short vs. Long
*Lens #39*

Duration determines: depth of strategy possible, narrative arc achievable, target audience, social context.

**Tools for controlling duration:**
- Win/loss conditions (the only thing that actually ends the game)
- Initial invulnerability period (*Spy Hunter*: first 90s are invulnerable — novices learn before deaths matter)
- Elegant deadlines (*Minotaur*: at 20 minutes, all survivors teleport to a small room full of monsters — guaranteed sub-25-minute sessions with dramatic finales)

> *"Leave them wanting more."* (old vaudevillian adage, cited s005)

### Type 9: Rewards
*Lens #40*

Eight reward types (s005, ch.11):

| Type | Description | Example |
|---|---|---|
| **Praise** | Game tells you "well done" | Nintendo jingles, "Perfect!" |
| **Points** | Quantifiable measure; visible to others | Leaderboards |
| **Prolonged play** | Extra time or lives | Extra life in pinball |
| **Portal** | Access to new content | New level, unlocked area |
| **Spectacle** | Music, special animation | Pac-Man intermission |
| **Expression** | Personalization capacity | Skins, custom characters |
| **Power** | New or enhanced capabilities | Mushroom in Mario |
| **Resources** | Valuable in-game objects | Ammo, HP, virtual currency |
| **Completeness** | Closure of having finished everything | 100%, end credits |

**Variable rewards sustain engagement longer than fixed rewards.** The same average points distributed randomly maintain anticipation where fixed rewards quickly become routine (Skinner + variable ratio schedule).

### Type 10: Punishments
*Lens #41*

Paradoxically, well-designed punishment **increases** enjoyment by creating stakes and making success feel earned.

Six punishment types and a case study (*Toontown Online* post-death penalties calibrated after extensive playtesting):
1. Shame (character bows head)
2. Loss of points (rare; perceived value lower)
3. Shortened play (lose a life)
4. Game over
5. Setback (checkpoint/restart; placement is critical)
6. Resource depletion (items, powers, money)

**The golden rule:** convert punishments into rewards wherever possible. *Diablo's* food system originally penalized not eating (stats dropped). Blizzard inverted it: eating gives a temporary power boost. Players experience it as positive. Same mechanic, opposite framing.

> *"It is crucial that all punishment is for things the player can understand and prevent. When punishment feels random and unstoppable, the player labels the game 'unfair.'"* (s005)

### Type 11: Simple vs. Complex
*Lenses #42–43*

**Innate complexity** — the rules themselves are complex. Keywords: "unless," "except," "but if." Can simulate reality but burdens the player.

**Emergent complexity** — simple rules produce complex situations. Chess's pawn rules (move forward, capture diagonal, en passant, promotion) are innately complex — but they generate emergent complexity far larger than the rule set suggests.

**The ideal: elegance.** Measure it: how many purposes does each element serve? Points in Pac-Man serve 5 simultaneously: short-term goal, long-term goal, triangularity (big dots slow you), success metric, and extra life currency. That's elegance.

**Character vs. elegance** — necessary opposites. Pure elegance produces something perfect but soulless. Monopoly's boot and top hat have nothing to do with real estate — but they're beloved. The "lovable flaws" of a game are its character.

### Type 12: Detail vs. Imagination
*Lens #45*

Players' imaginations are richer than most productions can match. Don't detail what you can't do well. The **binoculars effect**: a close-up first establishes the image; imagination sustains it for the rest of the game.

Principle: give enough detail to seed imagination, then step back and let players fill the rest. Text adventures relied entirely on this — and for certain audiences, they produced richer worlds than photorealistic 3D.

---

## 5. Power Curves and Progression Balance (s001, s006)

**The fundamental principle** (s001, ch.9): *every benefit has a cost, and the two are inextricably linked*. The delay in paying higher costs is what paces the game while the player feels they are growing.

**Power curve:** plots player capability against progression level. The player curve and challenge curve must run roughly parallel:

```
Power/
Challenge
    |    /─── Challenge (designed)
    |  ─/─── Player power (actual)
    | /
    |/
    └──────────────────── Time/Level
```

**Runaway progression** (player grows faster than challenge): game becomes trivially easy; flow channel's lower wall is breached → boredom.

**Difficulty spike** (challenge suddenly jumps above player curve): player exits the channel upward → frustration + grinding.

**Soft/hard caps:** many games implement maximum levels or diminishing returns to prevent grinding past content trivialization.

---

## 6. Balance in Live Games

For games that ship and continue receiving players, balance is an **operational discipline**, not a design milestone:

- Analytical balance (player behavioral data) is the primary tool
- Every significant update may re-introduce imbalances
- Player communities discover dominant strategies faster than internal teams
- Meta-game balance (the community's optimal strategies) evolves independently of patch notes
- Patch notes themselves are a trust mechanism — transparency about balance changes preserves community trust

**The resilience principle** (s001): never aim for perfect balance. Any player can find new imbalances in any sufficiently complex system. Design *resilient* systems — ones that remain broadly playable even when local imbalances exist, and that don't catastrophically collapse when a dominant strategy is found.

---

## 7. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Balance is a property of game+player, not game alone | s001 |
| Dominant strategies end the game's interesting decisions | s005 |
| Intransitive design prevents dominant strategies structurally | s001, s005 |
| Variable rewards sustain engagement better than fixed | s014, s005 |
| Punishments well-designed increase enjoyment by creating stakes | s005 |
| Elegant mechanics serve multiple purposes simultaneously | s005 |
| Balance failures are Dynamics problems, not Mechanics problems | s011 |
| Double and halve to find design space quickly | s005 |
| Live game balance never ends | s001, s017 |

---

## 8. Hot Potato — Balance Implications

| Decision | Rationale |
|---|---|
| Dynamic Potato scaling (×1.2/×1.5) | Balancing loop on dominant "just run away" strategy; prevents catch-up failure |
| FAP caps/anti-camping mechanics | Prevents dominant passive strategy from dominating |
| Intransitive item design (counters between items) | Rock-paper-scissors triads prevent single-item dominance |
| Short rounds | Prevents reinforcing loops from running to full dominance; resets advantage |
| Mixed competition/cooperation | Richest balance structure for party play (Types 6–7) |
| Triangularity in FAP actions | High-risk trolling earns more FAP; safe play earns less — classic triangle |

**Sources:** s005 (Schell) · s001 (Sellers) · s011 (MDA) · s006 (Adams) · s014 (Hodent)

**See also:** [game-balance-overview](../10-Library/notes/game-balance-overview.md) · [transitive-vs-intransitive-systems](../10-Library/notes/transitive-vs-intransitive-systems.md) · [meaningful-choices-triangularity](../10-Library/notes/meaningful-choices-triangularity.md) · [game-balance-methods](../10-Library/notes/game-balance-methods.md) · [reinforcing-vs-balancing-loops](../10-Library/notes/reinforcing-vs-balancing-loops.md) · [Mechanics](../00-Atlas/disciplines/Mechanics.md)
