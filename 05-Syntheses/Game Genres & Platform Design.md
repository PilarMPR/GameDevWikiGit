# Game Genres & Platform Design

> **What this is:** Everything the canon says about how genre shapes player expectations and design constraints, genre-specific mechanics, platform affordances, and the technology element of the elemental tetrad. Aggregated across s006, s005, s009, s013.

---

## 1. What Genre Is and Why It Matters

**Genre is not a category — it is a contract with the player.** When a player buys an FPS, they arrive expecting first-person perspective, projectile weapons, spatial movement, and some form of enemy to shoot. These expectations were set by prior games. Violating them requires deliberate design and explicit communication — or the player feels cheated.

**Adams** (s006, ch.3):
> *"Genre sets a player's expectations about what kind of fun they will have, what skills they will need, and what the game will look like. Designers ignore genre expectations at their peril."*

**The design implications of genre:**

1. **Afforded mechanics:** genre narrows the useful design space. RTS players expect real-time unit control; removing it requires strong justification and marketing communication.
2. **Audience calibration:** genre predicts who will play the game, their experience level, their platform preference, and their tolerance for complexity.
3. **Feature expectations:** players expect genre conventions to be present (or deliberately subverted). Missing a convention without subverting it is a design gap.
4. **Commercial framing:** genre determines which games you compete with on storefronts and in review systems.

---

## 2. Major Game Genre Families

### Action Games
**Core challenge:** reflexes, spatial awareness, timing, and physical skill under pressure.

**Subtypes and mechanic signatures:**

| Subtype | Core mechanic | Spatial challenge | Primary skill |
|---|---|---|---|
| **FPS/TPS** | Aim + shoot | 3D navigation, cover | Aim, positioning, timing |
| **Fighting** | Combo inputs, reads | 2D/3D arena | Execution, pattern reading |
| **Platformer** | Jump, run, navigate | 2D/3D obstacle course | Timing, spatial reasoning |
| **Action-adventure** | Combat + exploration | Open or linear 3D | Multiple (blended) |
| **Bullet hell / shmup** | Dodge + shoot | 2D bullet patterns | Spatial memory, reflexes |
| **Beat 'em up** | Close combat, positioning | Side-scrolling arena | Rhythm, crowd management |

**Key design principles for action games (s006, ch.20–21):**
- Response time must be sub-100ms (player demands exact feedback on inputs)
- Enemy tells must telegraph attacks far enough ahead to be dodgeable
- Difficulty must calibrate to the player's current precision, not abstract "level"
- Camera must never obscure the player character or immediate threats

### Strategy Games
**Core challenge:** decision-making, resource management, planning, prediction.

**Subtypes:**

| Subtype | Time structure | Scope | Primary skill |
|---|---|---|---|
| **RTS** | Real-time | Multiple units, base, economy | Multitasking, macro/micro |
| **Turn-based strategy** | Alternating turns | Multiple units | Planning, probability |
| **4X** (eXplore, eXpand, eXploit, eXterminate) | Turn-based | Empire-scale | Long-term planning, diplomacy |
| **Tower defense** | Real-time | Fixed battlefield | Spatial optimization |
| **Grand strategy** | Flexible | Historical scale | Systems mastery |

**Key design principles for strategy games (s006, ch.24–26):**
- Information must be organized so it's accessible without being overwhelming (cognitive load is the enemy)
- Decision points must be meaningful — decisions where one option is clearly optimal are not real decisions
- Pacing must allow time for planning while maintaining engagement
- Feedback on the consequences of decisions must be clear and attributable

### Role-Playing Games (RPGs)
**Core challenge:** character growth, narrative choices, exploration, and system mastery.

**Character advancement** is the defining mechanic — the player character grows in capability over time, and this growth is the primary reward cycle.

**Key subtype distinction:**
- **Western RPG:** high player agency in story, open exploration, character customization. Example: *The Elder Scrolls*, *Disco Elysium*.
- **JRPG:** tighter narrative, linear progression, fixed or semi-fixed party. Example: *Final Fantasy*, *Persona*.
- **Action RPG:** blends RPG character advancement with action combat feel. Example: *Dark Souls*, *Diablo*.

**Key design principles for RPGs (s006, ch.27):**
- The advancement system must produce perceptible, satisfying power growth
- Narrative choices must feel consequential (even if they converge)
- World must reward exploration with meaningful content
- The "character build" should be expressive enough to support different playstyles

### Simulation Games
**Core challenge:** understanding and manipulating complex systems.

Simulation games model real (or plausible) systems with enough fidelity that understanding the system produces mastery. The "fun" is Koster's pattern-mastery applied to a specific domain.

**Subtypes:** city builders (*SimCity*, *Cities: Skylines*), life simulations (*The Sims*), vehicle simulations (flight sims, racing), management sims (*Football Manager*).

**Key design principle:** simulation must be simplified enough to be learnable (not a true simulation) but complex enough that mastery is rewarding. The art is the **right level of abstraction** for the intended audience.

### Puzzle Games
**Core challenge:** finding the dominant strategy.

As established in the Puzzle & Challenge Design synthesis, puzzles are games with a knowable right answer. Pure puzzle games are sequences of these challenges with progressive difficulty. The retention challenge: once solved, they're used up. Good puzzle games have enough depth that solutions reveal new puzzles.

### Adventure Games
**Core challenge:** exploration, narrative, and inventory/knowledge puzzles.

Adventure games are primarily about exploration of a world and story, with puzzles as gating mechanisms. The core tension: puzzles must feel like organic parts of the world, not arbitrary locks (*The 7th Guest* problem).

**Key design principle (s005):** integrated puzzles only. Every solution must be motivated by the world's logic.

### Sports and Racing Games
**Core challenge:** competing against others (or your own previous performance) through physical simulation.

Design is heavily constrained by the real-world activity being simulated. The degree of simulation fidelity vs. accessibility is the primary design dial. *Rocket League* vs. *FIFA*: same general category, radically different fidelity/accessibility positions.

### Social/Party Games
**Core challenge:** shared experience, social dynamics, accessibility.

As detailed in the Multiplayer & Social Design synthesis. Party games prioritize observable play, short sessions, and wide skill range accessibility over depth or simulation fidelity.

### Casual/Mobile Games
**Core challenge:** accessible, session-flexible engagement for broad audiences.

**Key design principles for casual (s006, ch.3; s017):**
- One-session learning: new player to competent in under 5 minutes
- Session flexibility: can be played in 2 minutes or 20 minutes
- No penalty for interruption (mobile players are interrupted constantly)
- Broad aesthetic appeal (not genre-coded to any subculture)
- Retention through progression and social features, not mechanical depth

---

## 3. Genre Hybridization

Modern game design increasingly involves intentional genre hybridization — taking the core challenge of one genre and combining it with mechanics from another:

| Hybrid | Genre 1 | Genre 2 | Example |
|---|---|---|---|
| Action-RPG | Action (reflexes) | RPG (growth) | *Dark Souls*, *Diablo* |
| Roguelike-deckbuilder | Roguelike (procedural) | Strategy (deck management) | *Slay the Spire* |
| Battle royale | Survival | Shooter | *Fortnite*, *PUBG* |
| ARPG metroidvania | Action | Exploration-gated | *Hollow Knight* |
| Party-platformer | Platform | Party/social | *Fall Guys* |

**For Hot Potato:** the game hybridizes **tag/chase mechanics** (physical challenge) + **party game structure** (social, observable, short sessions) + **parkour platformer movement** (athletic expression). The genre conventions to respect: party game accessibility and social readability; the conventions to subvert: traditional tag games lack progression (FAP system) and individual expression.

**Schell's warning** (s005, ch.3): a hybrid game that doesn't clearly communicate what kind of fun it offers will confuse its audience. Genre hybridization requires communication clarity — the marketing, the screenshots, the store description must set the right expectations.

---

## 4. Genre Expectations vs. Genre Subversion

**Adams** (s006, ch.3): the designer can choose to:
1. **Follow conventions:** benefit from existing player expectations; risk of feeling derivative
2. **Subvert conventions:** create surprise and distinction; risk of alienating genre fans
3. **Ignore conventions:** neither benefit nor risk of genre expectations; risk of being invisible

**The subversion discipline:** when subverting a genre convention, the subversion must be:
- *Deliberate* (not an accident)
- *Legible* (the player understands what you're doing)
- *Worthwhile* (the subversion produces a better experience than the convention)

*Portal* subverted the shooter genre: there are no weapons, enemies can't be killed, and the "gun" creates portals. The subversion is deliberate, legible (the game makes it clear from the start), and worthwhile (it produces a novel spatial puzzle experience).

---

## 5. Platform Design — The Technology Element

**Schell** (s005, ch.4): Technology is one of the four tetrad elements. The medium of implementation is not a separate concern — it is a design element that constrains and affords the other three elements.

### Platform Affordances and Constraints

| Platform | Input method | Session context | Social context | Typical constraints |
|---|---|---|---|---|
| **PC** | Keyboard + mouse / controller | Desk, focused | Solo or online | High complexity tolerance; competitive potential |
| **Console (TV)** | Controller | Couch, casual-to-focused | Local multiplayer viable | UI must read at TV distance; couch co-op possible |
| **Mobile** | Touchscreen | Anywhere, interrupted | Predominantly solo | Short sessions; interrupt-safe; no precision input |
| **Handheld (Switch)** | Controller + touch | Anywhere, focused | Hybrid local/online | Both portable and TV; session flexibility |
| **VR** | Motion controllers + head tracking | Stationary, isolated | Predominantly solo | Physical fatigue; motion sickness; no text input |
| **Arcade** | Dedicated cabinet | Standing, public | Watching/competing | Short sessions; no save state; spectator appeal |

**For Hot Potato (Steam PC + potential console):**
- PC: controller support essential for couch play; keyboard/mouse secondary
- Console: UI must read at TV distance; local party play is primary use case
- Platform-specific features: Steam achievements, leaderboards, lobby system should be integrated from day 1

### Control Scheme Design by Platform

**Adams** (s006, ch.12): the interaction model (how the player controls the avatar) and camera model must be matched to the platform's input capabilities.

- Mouse: high-precision pointing; ideal for aiming (FPS), RTS, and navigation
- Analog stick: lower precision; compensate with aim assist for shooters; better for free movement
- Touch: no physical feedback; gestures replace buttons; hold/swipe/tap as primitive inputs
- Motion controllers (VR): full spatial input; natural for physical gestures but fatiguing

**The platform-mechanic alignment principle:** design mechanics that feel *at home* on the platform's input method. An RTS designed for mouse control but ported to controller requires a redesigned UI system, not just remapped buttons.

---

## 6. Genre and Audience Intersection

Different genres strongly correlate with different audience profiles (s006, ch.3–4):

| Genre | Typical age range | Male/female skew | Gaming experience | Session length |
|---|---|---|---|---|
| Core FPS/competitive | 16–30 | Male-skewed | High | Long |
| JRPG | 15–30 | Balanced | Medium-high | Long |
| Casual/mobile | All ages | Female-skewed | Low-medium | Short |
| Party/couch | All ages | Balanced | Low-high | Short-medium |
| Strategy/4X | 20–40 | Male-skewed | High | Very long |
| Narrative adventure | 18–35 | Balanced | Medium | Medium |
| Social simulation | All ages | Female-skewed | Low-medium | Medium |

**Caveat (s005, ch.8; s006, ch.4):** these are population-level tendencies, not individual rules. Never use them to design for an individual; use them to calibrate the *default experience* for the most common player profile, then test against the actual audience.

---

## 7. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Genre is a player contract, not just a category | s006 |
| Violating genre conventions requires deliberate communication | s005, s006 |
| Platform input method shapes mechanic design fundamentally | s006, s005 |
| UI must be calibrated to platform viewing distance and context | s006 |
| Genre hybridization requires clarity about what kind of fun is offered | s005 |
| Casual games require session flexibility and interrupt safety | s006, s017 |

---

## 8. Hot Potato — Genre and Platform Implications

| Decision | Rationale |
|---|---|
| Party game genre conventions followed: short sessions, wide skill range, observable play | Genre contract; players who pick up a party game have these expectations |
| Tag/parkour mechanic as genre subversion of standard party games | Most party games are turn-based or minigame collections; real-time parkour tag is the distinctive subversion |
| Primary platform: Steam (PC) + controller, with console port planned | Party game context = couch play = controller; Steam as primary distribution |
| UI tested at TV viewing distance from day 1 | Console port means TV distance readability is a baseline requirement |
| Session design: 3–5 min per match | Party game session contract; must complete before social attention wanders |

**Sources:** s006 (Adams) · s005 (Schell) · s009 (Macklin & Sharp) · s013 (Salen & Zimmerman)

**See also:** [game-feel-definition](../10-Library/notes/game-feel-definition.md) · [party-game-design-patterns](../10-Library/notes/party-game-design-patterns.md) · [multiplayer-conflict-types](../10-Library/notes/multiplayer-conflict-types.md) · [party-brawler](../30-Analyses/genres/party-brawler.md) · [Mechanics](../00-Atlas/disciplines/Mechanics.md)
