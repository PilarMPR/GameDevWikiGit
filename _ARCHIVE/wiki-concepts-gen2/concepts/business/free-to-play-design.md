# Free-to-Play Design

Designing games that are free to download but generate revenue through in-game purchases, ads, or subscriptions. F2P is not a monetization strategy bolted onto a game — it is a **design philosophy that shapes every aspect of the experience**, from core mechanics through economy to social systems.

**Source:** s017 (F2P Handbook Part 1 of 4, blog) · s005 (Schell — player needs) · s011 (MDA — referenced by s017) · s007 (Swink — 3Cs) · s014 (Hodent — reward psychology)

---

## The core F2P principle (s017)

> "Fun first. Without a compelling core experience, no economy, retention loop, or monetization can survive." (s017, Conclusion)

Every F2P design failure traces back to a failure at this level. A game that is not inherently engaging cannot be made engaging through rewards, FOMO, or payment pressure. The F2P handbook explicitly positions good game design — fun mechanics, clear 3Cs, engaging systems, strong onboarding — as the **foundation without which nothing else works**. (s017)

This is the discipline of F2P design: building the full free experience as if it needed to stand alone, then finding ethical ways to monetize it.

---

## The 3Cs framework (s017, citing s007)

The F2P Handbook foregrounds the **3Cs** — Character, Camera, Controls — as the fundamental axis of core game feel:

- **Character**: how the player's avatar moves, responds, and exists in the world. The character's physicality is the player's primary point of contact with the game.
- **Camera**: how the player sees the world. Camera position, movement, and framing determine what information the player has and how the world is perceived.
- **Controls**: input mapping, responsiveness, and feedback. Controls are the player's agency — poorly designed controls make everything feel wrong regardless of content quality.

These three must work together. Bad controls feel wrong even in a beautiful game with great mechanics. A beautiful camera setup is undermined by a character whose movement is imprecise. 3Cs are the sensory foundation of game feel. → [[../../feel-and-controls/game-feel]], [[../../feel-and-controls/camera-design]]

---

## The four-stage F2P arc (s017)

The handbook describes F2P design as four interdependent stages:

### Stage 1: Core game design (covered in Part 1 / s017)
- **3Cs**: establish compelling moment-to-moment feel
- **Systems**: the game's mechanics, loops, and progression that make it worth playing
- **Onboarding**: the new player experience — what happens in the first 10 minutes determines retention
- **Feedback**: clear, immediate response to every player action; the player always knows what they did and what effect it had
- **Accessibility**: make the core experience reachable without payment; the free experience must be genuinely good

> **Data gap**: Stages 2–4 (Economy Design, Retention Loops, Monetization) are described by the handbook but the source (Parts 2–4) was not ingested. This is Part 1 only (s017 provenance note).

### Stage 2: Economy design
How resources flow through the game. An F2P economy must balance:
- **Earnable currency**: what players can earn through play (reinforces core loop)
- **Purchasable currency**: what players can buy (must not make earn-through-play feel pointless)
- **Sinks**: where currency exits the system (prevents inflation)
- **Price anchoring**: first prices seen become reference points (Weber-Fechner; Hodent s014)

### Stage 3: Retention loops
Mechanics specifically designed to bring players back on repeated sessions:
- **Daily missions**: daily login rewards and tasks create a reason to return every day
- **Session hooks**: each session should end with a compelling reason to return (unfinished content, cliffhanger, visible pending reward)
- **Social retention**: friends create mutual accountability; guild systems, competitive ladders, and cooperative events leverage social obligation
- **Content cadence**: regular content releases (events, seasons, expansions) give returning players something new

### Stage 4: Monetization
How the game generates revenue while maintaining player trust:
- **Value exchange**: players must feel they receive fair value for money spent
- **The undermining effect**: aggressive monetization of intrinsically rewarding activities destroys intrinsic motivation (s014, Hodent) — if players feel the game is asking them to pay for things that should be free, engagement collapses
- **IAP catalog**: cosmetic items > power items (pay-to-win destroys competitive balance and community trust)

---

## Retention loops and the F2P core loop (s017, s011)

The F2P Handbook explicitly builds on MDA (s011): the game's **mechanics generate dynamics** that create **aesthetic experiences** compelling enough to produce return visits. The core loop design is the primary driver of retention.

Key loop properties in F2P:
- **Short core loops** (seconds to minutes): immediate, satisfying, repeatable. The action that players do constantly must feel good.
- **Medium loops** (sessions, daily): session goals, daily quests, progression milestones — these are why players return each day
- **Long loops** (weeks, seasons): major progression milestones, seasonal content, battle passes — these are why players stay engaged for months

Each loop must produce a clear reward and a visible next goal. Players who complete a loop and see nothing to do next leave. → [[../../mechanics/game-loops]]

---

## Onboarding as F2P-critical (s017, s014)

In F2P, the new player experience is even more critical than in premium games: the player has invested zero money and is making the retention decision in the first session. Onboarding failures in F2P are catastrophic; they happen before the player has any sunk cost investment.

F2P onboarding requirements (s017):
- **Immediate value**: the player must experience something genuinely fun within the first 60 seconds
- **Progressive complexity**: introduce one system at a time; never overwhelm working memory (Hodent, s014)
- **Early win**: give the player an achievable, satisfying win in the first session — generates competence and autonomy (SDT, s014)
- **Hook investment**: give the player something to come back for before the session ends (a visible reward pending, an incomplete quest, a social prompt)

---

## Ethical design in F2P (s014, s017)

The most contested area of F2P: where does good retention design end and exploitative design begin?

Hodent's framework (s014):
- **The undermining effect** (overjustification): making players feel that intrinsically motivating activities are contingent on payment erodes intrinsic motivation. The player who loved the game starts to feel like they're working for rewards.
- **Variable ratio reinforcement**: intermittent variable rewards (loot boxes, gacha) produce maximum engagement through unpredictability — this is the "slot machine effect." Ethical design ensures the activity itself is rewarding, not just the reward structure.
- **Loss aversion exploitation**: making players feel they will *lose* something if they don't pay is more effective than promises of gain — but it generates resentment when players recognize the manipulation.

The design test (s017): if players would feel the game is treating them fairly upon reflection, the design is ethical. If they would feel manipulated, it isn't.

---

## Key concepts & cross-links

- [[monetization]] — specific monetization patterns (IAP, gacha, battle pass, cosmetics)
- [[../../mechanics/game-loops]] — loop architecture is the F2P retention engine
- [[../../feel-and-controls/game-feel]] — 3Cs as the foundation of F2P core experience
- [[../../player/player-psychology]] — reward schedules, undermining effect, loss aversion
- [[../../player/motivation]] — SDT: competence, autonomy, relatedness as retention foundations
- [[../../player/flow-channel]] — flow as the daily-loop target
- [[../../theory/mda-framework]] — F2P design builds explicitly on MDA

## Sources

s017 (F2P Handbook Part 1/4 — core stance, 3Cs, 4-stage arc, onboarding) · s014 (Hodent — reward schedules, undermining effect, loss aversion, cognitive load in onboarding) · s007 (Swink — 3Cs and game feel) · s011 (MDA — explicitly cited by s017) · s005 ch.9 (Schell — player needs as retention foundation)
