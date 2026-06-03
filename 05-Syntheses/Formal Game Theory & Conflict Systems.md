# Formal Game Theory & Conflict Systems

> **What this is:** Everything the canon says about the mathematics of strategic conflict — game theory applied to game design, dominant strategies, Nash equilibrium, mixed strategies, the types of conflict, zero-sum vs. non-zero-sum, and how formal analysis informs balance design. Aggregated across s013, s005, s001, s006.

---

## 1. Why Game Theory Matters to Game Designers

**Salen & Zimmerman** (s013, ch.19):
> *"Game theory provides a mathematical framework for analyzing strategic interaction. Understanding it gives designers a formal tool for predicting dominant strategies, identifying degenerate conditions, and designing games where multiple strategies are genuinely viable."*

**The practical payoff:** game theory explains *why* certain mechanics produce dominant strategies (and how to prevent them), why some games feel strategically deep (and how to design for that depth), and how randomness and information interact to create interesting decisions.

This is not academic theory for its own sake — it is a diagnostic tool for balance design.

---

## 2. The Core Framework

### What Game Theory Studies

Mathematical game theory (von Neumann, Nash) studies situations where:
- Multiple rational agents make decisions
- Each agent's outcome depends on the decisions of others
- Each agent tries to maximize their own outcome

Games in the game-design sense are a subset of this: they are formal systems where players make strategic decisions with defined rules and outcomes. The formal game theory framework gives us tools to analyze the strategy space.

### Strategic Form vs. Extensive Form

**Strategic form** (normal form): all strategies and outcomes represented as a matrix. Useful for analyzing simultaneous-decision situations.

**Extensive form**: the game represented as a decision tree, showing the sequence of moves. Useful for analyzing sequential-decision situations (turn-based games, dialogue trees).

Most video games are best analyzed in extensive form — decisions are sequential, not simultaneous.

---

## 3. Dominant Strategies — The Design Enemy

**A dominant strategy is a strategy that produces the best outcome regardless of what the opponent does.**

**Schell** (s005, ch.11):
> *"Once a dominant strategy is discovered, the game is no longer fun, because the puzzle of the game has been solved — there are no more meaningful choices to make."*

**Sellers** (s001, ch.9): dominant strategies emerge from transitive systems — when one option is strictly better than all others in all situations. This produces the "dominant strategy problem."

### Types of Dominance

**Strict dominance:** Strategy A produces strictly better outcomes than Strategy B in *every* situation. If a strictly dominant strategy exists, rational players will always choose it.

**Weak dominance:** Strategy A produces outcomes *at least as good* as Strategy B in every situation, and *strictly better* in some situations. Less certain to dominate, but creates a systematic preference.

**Design rule:** eliminate strictly dominant strategies. Weakly dominant strategies may be acceptable if they require skill to execute.

### Identifying Dominant Strategies in Design

For a simple two-choice game, construct a **payoff matrix:**

| | Opponent: Strategy X | Opponent: Strategy Y |
|---|---|---|
| **My Strategy A** | (a, b) | (c, d) |
| **My Strategy B** | (e, f) | (g, h) |

Strategy A dominates Strategy B if c ≥ e AND a ≥ e (A always does at least as well as B).

**In practice for game designers:** this doesn't require formal matrices. Ask: is there one approach that is *always* better, or does the best approach depend on context? If the former, you have a dominant strategy problem.

---

## 4. Nash Equilibrium — What "Balanced" Means Formally

**Nash equilibrium** (John Nash, 1950): a state where no player can improve their outcome by unilaterally changing their strategy, given that all other players maintain their strategies.

**In game design terms:** a Nash equilibrium is a state where the meta-game has stabilized — no player has reason to switch strategies because every strategy they could switch to would be worse (or no better) given the current environment.

**The ideal Nash equilibrium for competitive games:** a state where *multiple strategies are all viable* (the game has a "balanced meta"). No single dominant approach; different strategies excel in different contexts.

**The degenerate Nash equilibrium:** all players converge on the same dominant strategy. The game has a "solved" meta. Example: in the early *StarCraft* meta, certain builds were universally optimal — the game was technically at Nash equilibrium, but it was a degenerate one with no strategic diversity.

**Design tool:** ask whether the Nash equilibrium of your game's strategy space produces interesting variety or degenerate convergence.

---

## 5. Mixed Strategies — Introducing Unpredictability

**Mixed strategy:** instead of choosing a single strategy (pure strategy), a player randomizes between strategies according to a probability distribution.

**The rock-paper-scissors example:** in a game with rock-paper-scissors structure:
- Pure strategy (always play rock) → opponent adapts to always play paper → you always lose
- **Mixed strategy** (play each option with probability 1/3) → opponent cannot exploit you → expected outcome is neutral

**The value of randomization:** in zero-sum perfect-information games, players who are *predictable* can be exploited. Randomization makes you unexploitable.

**Game design applications:**
- Enemy AI that randomizes attack patterns (preventing the player from finding a single guaranteed counter)
- Procedural content generation (varying the game state so "solved" approaches don't guarantee success)
- Random events that prevent any single strategy from dominating across all possible game states

---

## 6. Zero-Sum vs. Non-Zero-Sum

### Zero-Sum Games
One player's gain is exactly another's loss. The total "value" in the system is constant.

**Examples:** Chess (one wins, one loses — exactly), poker (money won = money lost by others), *Street Fighter* match (zero-sum win/loss).

**Design properties:**
- Perfect competition context: someone must lose for someone to win
- No possibility of mutually beneficial exchange
- All strategies are in opposition
- Creates adversarial dynamics

### Non-Zero-Sum Games
Players can all gain, or all lose. Total value is not constant.

**Examples:** cooperative games (all players win together), trading games (both parties gain from a fair trade), *Minecraft* creative mode (no win condition; all players can "win").

**Design properties:**
- Cooperation can be genuinely beneficial
- Mutually beneficial strategies exist
- Alliance formation is rational
- Creates collaborative dynamics

### Constant-Sum vs. Variable-Sum

A more precise distinction:
- **Constant-sum (zero-sum):** total payoff is fixed regardless of strategies chosen
- **Variable-sum:** total payoff varies based on strategies (cooperation can increase total value; mutual defection can decrease it)

**The Prisoner's Dilemma** (classic variable-sum game): two players each choose to cooperate or defect. Mutual cooperation > mutual defection, but defection dominates cooperation individually. Produces social dilemmas relevant to trust mechanics in games.

---

## 7. Conflict Type Analysis (Salen & Zimmerman)

**Salen & Zimmerman** (s013, ch.20) map the types of conflict games contain:

### Conflict by Scope

| Scope | Description | Examples |
|---|---|---|
| **Single player vs. game** | Player faces system challenge only | Puzzle games, single-player action |
| **One vs. one** | Two players directly opposed | Chess, fighting games, 1v1 FPS |
| **One vs. many** | One player against multiple opponents | Asymmetric multiplayer (Dead by Daylight) |
| **Many vs. many** | Teams competing | Team sports, team FPS |
| **All vs. all (FFA)** | Every player competes independently | Battle royale, Hot Potato |
| **All vs. the game** | All players cooperate against system | Co-op games (Left 4 Dead) |

### Conflict Resolution Mechanisms

| Mechanism | How it works | Examples |
|---|---|---|
| **Pure skill** | Better execution wins | Fighting game mechanical execution |
| **Strategy** | Better planning and decision-making wins | Chess, RTS macro |
| **Chance** | Random outcomes determine results | Dice roll, loot drop |
| **Social negotiation** | Persuasion and alliance determines outcomes | Diplomacy, social deduction |
| **Endurance** | Persistence determines outcomes | Survival games, marathon-style challenges |
| **Mixed** | Combination of mechanisms | Most complex games |

---

## 8. Degenerate Strategies and Their Prevention

**Degenerate strategies** (Salen & Zimmerman, s013, ch.21): strategies that undermine the intended game experience, even if they're technically legal.

**Types:**
- **Dominant strategies** (covered above): one approach always wins
- **Griefing strategies**: optimize for ruining others' experience without advancing your own win condition
- **Stalling**: playing to draw/delay rather than win
- **Camping**: exploiting a safe position to eliminate risk entirely

**Design solutions:**

| Degenerate strategy | Prevention mechanisms |
|---|---|
| Dominant strategy | Intransitive design; cost asymmetry; context-dependent effectiveness |
| Griefing | Social systems (reporting, muting); mechanical cost to griefing |
| Stalling | Time limits; score-based victory; activity requirements |
| Camping | Anti-camp mechanics; area hazards; timer pressure; FAP system (Hot Potato) |

---

## 9. Applying Formal Analysis to Real Game Design

**The designer's toolkit from game theory:**

1. **Build a simplified payoff matrix** for key strategic decisions: what do players gain and lose in each matchup? Does any strategy dominate?

2. **Test for Nash equilibrium:** if all players converged on the same strategy, would the game still be interesting? If no, you have a degenerate equilibrium problem.

3. **Check zero/non-zero sum:** is your game structured as zero-sum (adversarial) or variable-sum (cooperative potential)? Does the structure match your intended experience?

4. **Identify degenerate strategies** in playtest: ask "what is the optimal strategy?" If playtests consistently produce the same answer, you have a dominant strategy problem.

5. **Use randomization to break dominance:** if a dominant strategy exists that you can't break structurally, introduce uncertainty that prevents the strategy from guaranteeing superior outcomes.

---

## 10. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Dominant strategies end meaningful strategic choice; they must be designed out | s005, s013, s001 |
| Nash equilibrium is the formal definition of "balanced meta" | s013 |
| Mixed strategies (randomization) prevent pure strategy exploitation | s013 |
| Zero-sum design creates adversarial dynamics; variable-sum enables cooperation | s013 |
| Degenerate strategies must be specifically anticipated and designed against | s013, s005 |
| Payoff matrices are a practical tool for analyzing strategy space | s013 |

---

## 11. Hot Potato — Game Theory Analysis

| Strategic element | Analysis |
|---|---|
| Running from Potato (dominant?) | Running is strictly better than standing still → this is intentional; challenge comes from Potato scaling catching up |
| Trolling for FAP (dominant?) | Any troll action that's always best would be dominant; intransitive item design prevents this |
| Tag timing | No single "always best" moment to tag → context-dependent (proximity, timer, FAP standing) → no dominant strategy |
| King-of-hill targeting | Emergent Nash equilibrium behavior: all players target the leader → self-correcting |
| Zero-sum structure | FAP competition is non-zero-sum (all can earn FAP) but Potato loss is zero-sum (exactly one loser) → mixed |

**Sources:** s013 (Salen & Zimmerman) · s005 (Schell) · s001 (Sellers) · s006 (Adams)

**See also:** [transitive-vs-intransitive-systems](../10-Library/notes/transitive-vs-intransitive-systems.md) · [game-balance-overview](../10-Library/notes/game-balance-overview.md) · [meaningful-choices-triangularity](../10-Library/notes/meaningful-choices-triangularity.md) · [Mechanics](../00-Atlas/disciplines/Mechanics.md)
