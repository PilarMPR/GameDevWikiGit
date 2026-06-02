# Applying the Canon

A practical guide for using this wiki's frameworks during actual design work. Not another theoretical summary — this page answers: **"I'm facing a design decision right now. Which framework do I reach for?"**

---

## Part 1: The Decision-Framework Map

A situation → tool mapping. Use the right framework for the problem in front of you.

| Design situation | Primary tool | Secondary tool | Wiki page |
|-----------------|-------------|----------------|-----------|
| Defining what the game is for | MDA: state the target aesthetics | Elemental Tetrad: align all four elements | [[../concepts/theory/mda-framework]] |
| A playtest felt wrong — diagnosing why | Gulf of execution (can't figure out what to do?) or evaluation (can't tell what happened?) | Flow exit analysis (boredom or anxiety?) | [[../concepts/interface/usability-and-hcd]], [[../concepts/player/flow-channel]] |
| Designing the core loop | Sellers' 4 principal loops | MDA Dynamics layer | [[../concepts/mechanics/game-loops]] |
| Calibrating difficulty | Flow channel + Adams difficulty curve | Koster's boredom analysis | [[../concepts/player/flow-channel]], [[../concepts/level-design/pacing-and-flow]] |
| Writing a GDD or one-pager | Design pillars + Macklin & Sharp's design values | Elemental Tetrad as structure | [[../concepts/production/documentation]] |
| Choosing player count / match structure | Formal Elements (conflict type) + Bartle types | MDA (Fellowship target = social mechanics needed) | [[../concepts/theory/formal-elements]], [[../concepts/player/player-types]] |
| Evaluating pacing of a level or session | Interest curve analysis | Tense-and-release macro structure | [[../concepts/level-design/pacing-and-flow]] |
| Designing a level | Teaching function (Kremers) + Indirect control (Schell) | Spatial organizing principle (Adams) | [[../concepts/level-design/level-design]], [[../concepts/level-design/spatial-design]] |
| Something feels unreadable or confusing | Norman's gulfs + signifier/affordance analysis | Hodent's cognitive load audit | [[../concepts/interface/usability-and-hcd]], [[../concepts/player/player-psychology]] |
| Choosing a monetization model | F2P principles + ethical monetization test | SDT (will rewards undermine intrinsic motivation?) | [[../concepts/business/free-to-play-design]], [[../concepts/business/monetization]] |
| Evaluating whether a mechanic belongs | Elemental Tetrad (does it reinforce the theme?) | Meaningful Play (does the action produce discernible, integrated outcomes?) | [[../concepts/theory/formal-elements]], [[../concepts/theory/meaningful-play]] |
| Something generates player frustration | Tell design (was the event telegraphed?) + feedback systems | Gulf of evaluation (was the outcome visible?) | [[../concepts/feel-and-controls/feedback-systems]], [[../concepts/interface/usability-and-hcd]] |
| The game isn't retaining players | Outer loop design + SDT (competence/autonomy/relatedness) | Koster: have patterns been exhausted? | [[../concepts/mechanics/game-loops]], [[../concepts/player/motivation]] |
| Characters / story aren't landing | Projection vs. empathy (are players inhabiting the character?) | Ludonarrative dissonance check | [[../concepts/narrative/characters]], [[../concepts/narrative/story-and-games]] |
| The team disagrees about a feature | Design values as arbitration | Lens #13 (Eight Filters) | [[../concepts/production/documentation]], [[../wiki/design-reference/production]] |
| Not sure whether to cut a feature | Lens #8 (Holographic Design): does every element serve the core experience? | Elemental Tetrad alignment check | [[../design-reference/theory]] |

---

## Part 2: Hot Potato Worked Example

Applying the wiki's full toolkit to Hot Potato (Wild Alchemists, party brawler, UE5, Steam 2027).

### Working MDA

**Target Aesthetics:**
- **Fellowship** (primary): the shared couch experience; laughter, shouting, group reactions; "did you see that?"
- **Challenge** (co-primary): skill expression matters; passing accuracy, positioning, reading the timer
- **Sensation** (supporting): the explosion, the sound of a hot potato, hit effects; physical satisfaction of passing

**Target Dynamics:**
- The potato creates continuous contested focus — no "waiting your turn"
- Passing under pressure produces clutch moments (high Sensation + Challenge)
- Explosion timing creates social blame moments ("you should have passed it!")
- Skill gap management keeps the game competitive across levels

**Target Mechanics** (derived backward from aesthetics):
- A timer-based shared object that creates continuous urgency
- A pass mechanic that rewards skill (accuracy, timing) without being inaccessible to novices
- A hold-time score economy that creates a tension decision (hold for points vs. pass for safety)
- Respawn-fast mechanics that keep everyone in play
- Character differences that create variety without power tiers

### Formal Elements Breakdown

| Element | Hot Potato design |
|---------|-----------------|
| **Players** | 2–6; symmetric win condition; asymmetric character abilities |
| **Objectives** | Accumulate score; avoid holding potato when it explodes |
| **Procedures** | Move, dash, attack (brawler layer), pass potato (object layer) |
| **Rules** | Holding potato when timer fires = score loss; passing before = safe; higher hold time = higher potential score but higher risk |
| **Resources** | The potato (single shared); player health/lives (optional); score |
| **Conflict** | Direct (brawler) + Indirect (compete for the potato) — hybrid conflict type |
| **Boundaries** | The stage; blast zones (brawler) |
| **Outcome** | Most points at end of X rounds wins; round-by-round score tracking |

### Core Loop (Sellers' 4 Loops Applied)

**Game model loop** (the system):
→ Round start → Potato spawns → Players contest it → Holder manages timer → Pass or explode → Score update → Next potato

**Interactive loop** (player ↔ game, second-to-second):
→ Player inputs (move/dash/pass) → Game responds (character moves, potato transfers) → Feedback (timer audio/visual escalation) → Player decides (hold longer? pass now?) → Repeat

**Player mental loop** (player's internal model):
→ "Where is the potato? Who has it? How hot is it? Can I grab it safely? Who is closest to me when I need to pass?"

**Designer's loop** (iteration):
→ Playtest observation → Identify flow exits (boredom: potato drama isn't tense; anxiety: too-fast timer) → Revise timer curve / score economy / pass mechanics → Repeat

### Flow Channel Design Questions for Hot Potato

The party brawler has a 10× skill range at a typical party. The flow channel must be maintained for all players simultaneously.

**The calibration question:** At what hold-time value does the skill-vs-luck balance tip?
- If the timer is very short (< 3 seconds): luck dominates; skilled players can't meaningfully manage the potato; Achievers lose interest
- If the timer is very long (> 10 seconds): skill dominates; novices get stuck holding and take repeated losses; Socializers and beginners lose interest
- Target range: **5–7 seconds** with an escalating feedback curve that makes the last 2 seconds feel urgent regardless of skill level

**The catch-up question:** What happens when one player is significantly ahead in score?
- Pure skill → dominant players crush novices → Socializers leave
- Rubber banding → skilled players feel unrewarded → Achievers leave
- Best solution: **item chaos + stage hazards** that provide variance without explicit rubber banding; skilled players navigate chaos better but can't fully control it

### Round Interest Curve

Each 90-second round should follow this interest curve (Schell ch.14):
- **(A) Initial interest**: potato appears; tension begins immediately
- **(B) Hook**: first pass under pressure — teaches the core mechanic fast
- **(C) Build**: successive exchanges; timer escalating on each hold
- **(D) Peak 1**: first explosion — punchline + score update; everyone reacts
- **(E) Valley**: brief reset; new potato spawns; tension resets
- **(F) Build again**: exchanges with more player awareness (they know the mechanic now)
- **(G) Climax**: final potato of the round; highest stakes; everyone knows what's coming
- **(H) Resolution**: round-end score reveal; who won? social moment

**Fractal structure**: each individual potato hold is a micro interest curve (calm → tension → decision → pass or explosion). The round is the medium curve. The session (best of 5) is the macro curve.

### Schell Lenses most applicable to Hot Potato

From [[../design-reference/mechanics]] and [[../design-reference/feel-and-controls]]:

- **#27 Skill**: Is there a meaningful skill gap? Can skilled players express skill without dominating completely?
- **#28 Expected Value**: What is the expected value of holding vs. passing at each timer state? Is the decision interesting?
- **#31 Challenge**: Are challenges appropriate for the full skill range? Can experts and novices both engage?
- **#33 Triangularity**: Is there a risk-reward gradient in holding the potato? Does the risk feel real?
- **#37 Cooperation**: Does the gang-up dynamic emerge naturally (everyone targets the leader)?
- **#40 Reward**: What are the rewards? When do they arrive? Are they satisfying?
- **#53 Control**: Does passing feel responsive? Do players feel in control of their fate?
- **#57 Feedback**: Does the timer's escalation communicate urgency clearly at every moment?
- **#58 Juiciness**: Is every interaction — pass, explosion, near-miss — satisfying and alive?
- **#61 Interest Curve**: Draw the interest curve for a single round. Is there a hook, a climax, a resolution?

---

## Part 3: Educational Games Studio Application

Applying the canon to pitch and design for the B2B educational studio (UK/US curricula, ages 9–13).

### The theoretical bridge (Koster → Learning Science)

Koster's theory (s016) provides the philosophical foundation: **fun is learning**. This is not a metaphor — it is a mechanistic claim. The brain produces the "fun signal" when it successfully acquires a new pattern. Educational games are not games that happen to have content — they are games where the patterns being learned happen to be academic skills.

The implication for pitching to schools: **you don't need to argue that educational games are as fun as commercial games**. You argue that a well-designed educational game uses exactly the same mechanisms that make commercial games engaging — the flow channel, pattern acquisition, competence development — and those mechanisms also happen to produce learning.

The B2B pitch argument:
> "The mechanics are [curriculum-relevant challenge]: students engage in [solving X problems], which creates dynamics of [skill progression and pattern recognition], which produces the aesthetic experience of competence and discovery — while simultaneously developing the targeted [learning objective]. The game is not a wrapper around educational content; the educational content IS the game's skill system."

### SDT and learning design

Self-Determination Theory (s014) maps directly to learning research:
- **Competence** = students feel they are getting better at the subject (not just at the game)
- **Autonomy** = students feel their choices matter in the game world (and in their learning path)
- **Relatedness** = students feel connected to characters, classmates, or a broader mission

Educational games that fail do so by delivering Competence (skill feedback) in a vacuum without Autonomy or Relatedness. The game feels like a test, not an experience.

### MDA for educational games

Target aesthetics for ages 9–13 (UK/US curricula context):
- **Challenge** (primary): mastery and growth; the same aesthetic that makes Celeste compelling applies to math challenges
- **Discovery** (strong secondary): the curriculum content as a world to explore, not a list to memorize
- **Narrative** (supporting): a story frame that contextualizes the learning objective
- **Fellowship** (optional, powerful): multiplayer or asynchronous comparison creates motivation without pay-to-win

Avoid aesthetics that conflict with the educational context:
- **Submission** (pastime/mindless): educators will reject games that feel like passive entertainment
- **Sensation** (pure sensory pleasure): without connection to learning, considered a distraction by teachers

### The hidden mechanic pattern

The most effective educational games embed the learning objective as a game mechanic that the player experiences as play, not as a test:

- *Math skills* → resource economy mechanics where arithmetic is required to make strategic decisions
- *Reading comprehension* → dialogue-based puzzle mechanics where reading carefully is the operative action
- *Scientific method* → experiment-design mechanics where hypothesis and observation are the gameplay

The teacher sees the assessment; the student sees the game. The design problem is making these inseparable — if the educational content can be skipped or ignored while still making progress, the design has failed.

### B2B pitch structure

The typical B2B educational game pitch deck (based on [[../concepts/production/documentation]]):

1. **Problem statement** — what academic challenge this addresses (cite curriculum standards: UK National Curriculum / Common Core)
2. **Learning objectives** — what students will demonstrably be able to do after engaging with the game
3. **The game** — one paragraph or visual; MDA framing ("mechanics are X, which creates Y, which delivers Z")
4. **Evidence/theory** — Koster's fun=learning; SDT; any pilot data
5. **Technical specs** — platform, LMS integration, xAPI/SCORM compliance, teacher dashboard
6. **Pricing model** — per-student license / site license / district license
7. **Pilot offer** — a free or reduced-cost pilot for one classroom or school

**What B2B buyers actually care about** (in order):
1. Curriculum alignment — does it match the standards they're assessed on?
2. Ease of deployment — does it run on the devices they already have? Does it work without IT?
3. Evidence of effectiveness — any data showing learning outcomes?
4. Teacher control — can teachers assign, monitor, and assess through the tool?
5. Price — per-student licensing is more legible than site licenses for budget justification

---

## Sources

This page synthesizes the full wiki. Primary frameworks: s011 (MDA) · s005 (Schell — Formal Elements, Lenses) · s001 (Sellers — 4 loops) · s013 (Salen & Zimmerman — formal elements) · s014 (Hodent — SDT) · s016 (Koster — fun = learning) · s008 (Fullerton — playcentric) · s009 (Macklin & Sharp — design values). Hot Potato application: [[../genres/party-brawler]], [[../analyses/smash-bros]], [[../analyses/jackbox]].
