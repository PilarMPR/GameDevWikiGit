# Progression Systems

The mechanics that track player growth over time and reward advancement — experience points, levels, skill trees, unlock systems, and power curves. Progression systems are the structural backbone of long-term engagement: they answer the question "what am I working toward?" at every scale.

---

## What progression systems do (s006; s001; s017)

Progression serves multiple simultaneous design functions:

1. **Pacing long-term engagement**: divides the game into achievable milestones that sustain motivation across many hours
2. **Teaching mastery**: gates advanced content behind demonstrated competence (the player must have leveled up enough to survive the harder zone)
3. **Expressing player identity**: branching skill trees let the player specialize and define their playstyle
4. **Creating anticipation**: visible next-step rewards (a level-up 10 XP away) motivate continued play
5. **Communicating growth**: numerical stats make skill improvement explicit, reinforcing competence (SDT)

Adams identifies **progression mechanics** as one of his five core mechanic types: the systems that determine how a game advances, restricts, and unlocks content. (s006, ch.13–14) → [[core-mechanics]]

---

## The experience point loop (s006, s001)

The canonical progression mechanic: **actions → XP → levels → new content**.

**XP (experience points)**: numerical measure of accumulated accomplishment. The most common progression currency. XP is earned by performing the game's core actions (killing enemies, completing quests, discovering areas) and accumulates toward a threshold.

**Levels**: discrete thresholds where accumulated XP produces a step-change in the player's capabilities. Leveling up typically:
- Increases baseline stats (health, damage, speed)
- Unlocks new skills or abilities
- Signals readiness for the next tier of content

The XP → level curve is a fundamental design parameter:
- **Flat curve** (same XP per level): predictable, regular advancement. Simple to understand; can feel mechanical.
- **Exponential curve** (each level requires more XP): later levels take longer to achieve, implicitly making them more prestigious. Standard in RPGs; creates the "grinding" dynamic when the curve steepens too fast.
- **Adjustable curve**: some games allow the designer to tune when levels arrive to match intended pacing.

**The Weber-Fechner problem**: logarithmic perception means that +10 damage at level 1 feels enormous; +10 damage at level 50 feels negligible. Progression numbers must grow faster than linearly to maintain *felt* impact. (s014, Hodent — Weber-Fechner bias) → [[../../player/player-psychology]]

---

## Power curves and balance (s006, s001; s005 ch.11)

A **power curve** plots player capability against progression level. Calibrating the power curve is one of the core balance challenges of any progression game:

- **Player power curve**: how strong is the player at each level?
- **Enemy/challenge power curve**: how demanding are encounters at each level?
- **The target**: player curve and challenge curve should run roughly parallel — both should increase together, maintaining the flow channel.

**Runaway progression**: if the player grows faster than the challenge (via grinding or overpowered abilities), the game becomes trivially easy before content is exhausted. The flow channel's lower wall has been breached.

**Difficulty spike**: if the challenge curve suddenly jumps above the player curve (under-tuned progression or over-tuned content), the player exits the flow channel above — frustration or grinding required.

**Soft cap / hard cap**: many games implement maximum levels or diminishing returns to prevent players from grinding to a point where content becomes trivial. The cap forces engagement with designed content rather than grinding past it.

---

## Skill trees (s006; s005)

Skill trees add **branching** to progression: the player chooses which capabilities to develop, specializing their playstyle.

**Design properties of good skill trees**:
- Each node should feel meaningfully distinct (not just +5% to a stat, but a qualitative change in what the player can do)
- Branches should produce genuinely different playstyles, not just different stat distributions
- The tree structure should be readable: the player can understand the progression path before committing
- No node should be strictly mandatory (if all builds require the same three nodes, the branching is illusory)
- Each node should feel rewarding to unlock, independent of its position in the tree

**Skill tree anti-patterns**:
- **Mandatory funnel**: all builds require the same early nodes; the branching is delayed or cosmetic
- **Trap choices**: some branches are clearly inferior; informed players ignore them while new players invest in suboptimal paths
- **Analysis paralysis**: too many nodes, too early; the player cannot evaluate the options meaningfully
- **Stat bloat**: nodes offer only percentage increases with no narrative or mechanical flavor

---

## Meta-progression (s017; s001)

**Meta-progression** operates above the single-playthrough level: capabilities or resources earned in one run carry over to subsequent runs, accumulating across sessions.

Examples:
- Roguelikes: permanent unlocks (new items, character classes, modifiers) earned in failed runs that make future runs more capable
- F2P games: permanent character upgrades that persist across all sessions
- Battle passes: season-level progression that operates on a timeline independent of individual sessions

Meta-progression is the **outer loop** in F2P game architecture: the motivational frame that makes players return across many sessions. (s017) → [[game-loops]]

**Design tension**: meta-progression can undermine the challenge of individual sessions if permanent upgrades stack too much power. Roguelikes navigate this by keeping per-run progression randomized and challenging regardless of meta-unlocks. F2P games navigate this with pay-to-win concerns (see [[../../business/monetization]]).

---

## Unlock systems (s006; s017)

**Unlock systems** gate content behind completion criteria. Unlike XP curves (continuous accumulation → threshold), unlocks can be tied to:
- **Achievement**: "defeat the boss without taking damage"
- **Discovery**: "explore this area"
- **Completion**: "complete all missions in Chapter 3"
- **Real-time progression**: "reach level 10 in the battle pass"
- **Purchase**: "buy this character in the shop"

Unlock pacing is a narrative design choice: unlocks should arrive at moments that feel meaningful rather than arbitrary. A character unlocked after a significant in-game event (you defeated the villain) feels earned; a character unlocked arbitrarily at level 14 feels like filler.

**Sequencing**: unlock order implicitly tells the player what to prioritize. First unlocks should address the most common player needs; late unlocks can be specialized or prestige items.

---

## Progression and motivation (s014; s001)

Progression systems primarily satisfy **competence** (SDT) — the player feels effective and growing. The level-up moment, the skill tree choice, and the new ability unlock all provide direct evidence of growth. (s014, ch.7) → [[../../player/motivation]]

**The treadmill problem**: if XP and levels become the *goal* rather than a byproduct of intrinsic engagement, the game becomes a Skinner box. Players who "need" to reach the next level before stopping are extrinsically motivated — the activity itself is no longer the reward. This undermines the long-term engagement the system was meant to support.

Good progression design: leveling up *reflects* genuine mastery development and *enables* new meaningful play, rather than being an arbitrary time-gate.

**Visible progress**: at all times, the player should be able to see their distance from the next milestone. Progress bars, level counters, and quest trackers are all implementations of Schell's Puzzle Principle #3 (sense of progress) applied at the game scale. → [[puzzles]]

---

## Progression across game types

| Game type | Primary progression mechanic | Key design concern |
|-----------|------------------------------|-------------------|
| RPG | XP → levels → skill trees | Curve calibration; meaningful branching |
| Action RPG | Character levels + gear tiers | Power curve vs. content difficulty |
| Roguelike | Per-run + meta-progression | Balancing meta-power vs. per-run challenge |
| F2P | Season/battle pass + permanent upgrades | Retention without pay-to-win |
| Puzzle/platformer | World/level unlocks | Clear completion criteria; momentum |
| Fighting game | Character unlocks + skill mastery | Mechanical depth as the "progression" |
| Sports | Season records, team ratings | Progression as representation, not power |

---

## Key concepts & cross-links

- [[core-mechanics]] — Adams' 5 mechanic types include Progression Mechanics
- [[game-balance]] — power curve calibration is a balance problem
- [[game-loops]] — progression is the outer loop that frames the core loop
- [[../../player/motivation]] — competence, extrinsic vs. intrinsic, undermining effect
- [[../../player/player-psychology]] — Weber-Fechner logarithmic perception affects progression feel
- [[../../player/flow-channel]] — progression must maintain the player in the flow channel
- [[../../business/free-to-play-design]] — progression as a retention mechanism

## Sources

s006 ch.13–14 (Adams — Progression Mechanics as mechanic type; entities, attributes, states in progression context) · s001 ch.4, ch.7 (Sellers — outer loop as progression; engagement through growth) · s005 ch.11 (Schell — game balance and power curves; chapter on balance) · s014 (Hodent — Weber-Fechner perception and stat scaling; competence from SDT) · s017 (F2P Handbook — battle pass, meta-progression in live-service context) · s016 (Koster — progression as teaching new patterns; boredom at mastery)
