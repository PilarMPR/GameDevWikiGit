# Iteration, Playtesting & Production

> **What this is:** Everything the canon says about the design process — how games are made, how prototypes work, how to learn from playtesting, and how teams and studios function. Aggregated across s008, s005, s009, s001, s006.

---

## 1. The Core Principle

**The strongest methodological consensus across all design sources:**

> *"You cannot design a great game by thinking about it. You can only design one by making it and watching people play it."*

Games are interactive, dynamic systems whose quality can only be assessed in play. Unlike a book or painting (which the creator can evaluate), a game's quality depends on the player's *experience of it* — inaccessible until someone plays it.

This is not a philosophy — it's a structural constraint. The game is not the experience; it's the artifact that creates the experience (s005, ch.2). The only way to know if the experience is right is to watch someone have it.

---

## 2. The Four Frameworks

### Fullerton — Playcentric Design (s008)

The canonical formulation:

**Cycle:** Conceptualize → Prototype → Playtest → Evaluate → Revise → Repeat

**The playcentric mindset:** design centers entirely on the player's experience. The designer is the player's advocate. Design quality is *discovered through play*, not specified in advance.

Key rules:
- Move to the next cycle as fast as possible. A day of playtesting teaches more than a week of thinking.
- Physical prototypes (paper, cards, dice) are faster to build and modify than digital ones
- Prototypes are questions — each one should answer a specific design question
- Formal + dramatic + dynamic elements each require testing at different stages

### Schell — Rule of the Loop (s005, ch.7)

> *"The more times you test and improve your design, the better your game will be."*

Not a recommendation — an absolute truth with no exceptions. The danger of digital games: each loop is expensive, forcing fewer loops = more risk.

**Two questions to maximize loop quality and speed:**
1. How can I make every loop count? → Assess and mitigate risks
2. How can I loop as fast as possible? → Reduce prototype cost; use physical prototypes

**8 Prototyping tips** (s005):
1. Answer a question — every prototype has one specific question to answer
2. Forget quality — a prototype is not a product; don't polish what you're about to throw away
3. Don't get attached — "ideas are like paper cups, not fine china"
4. Prototype the hardest thing first — test the riskiest element when change is still cheap
5. Expect the unexpected — the most useful prototypes reveal surprises, not confirmations
6. Use physical prototypes when possible — faster to build, faster to modify
7. Build the toy first — make the core interaction feel good before adding game structure
8. Get it in front of people fast — designer intuition is unreliable; player behavior is real

**Cerny's Method** (cited s005): make a small, polished version of the core experience (2 "publishable levels"); pre-production ends when those are genuinely fun. Production then expands the proven design.

**Waterfall vs. spiral:** traditional waterfall (complete design → complete production → test at end) is catastrophically bad for games. Design can't be verified until playable. **Boehm's spiral model** (risk assessment + prototyping + looping) is the professional standard.

### Macklin & Sharp — Design Values (s009)

Their contribution: anchor iteration to explicit **design values** — statements of what the designer believes is important:

1. Define design values: what experiences and ideas is this game trying to create?
2. Prototype rapidly: generate multiple possible approaches; don't commit early
3. Playtest with intention: each test tests specific questions derived from design values
4. Reflect and revise: evaluate against design values — did this produce the intended experience?

**Why design values matter:** without them, every playtest suggestion gets incorporated. With them, suggestions are filtered through "does this serve the experience we're building?" Design values prevent feature creep and keep iteration purposeful.

**8 kinds of prototypes** (s009, ch.10): paper, physical, playable (digital vertical slice), art/sound, interface, code/tech, experience, and role-played. Each answers a different category of design question. Choose the prototype that answers the current uncertainty.

### Sellers — The Designer's Loop (s001, ch.7)

Sellers frames iteration as one of the **four principal loops** — the designer's loop wraps around the entire game+player system:

```
design → observe player experience → identify gap → change design → repeat
```

This is a **balancing loop** — the designer reduces the gap between intended and actual experience.

**Sellers' critical rule:** *Observe, don't explain.* When watching a playtest, resist the urge to explain why the design made a choice. Let the player encounter the design as it is. The game must explain itself through play. If a designer explains something, they've lost information about how the game can communicate it better.

**Systems-level iteration:** when a playtest reveals a problem, the fix is not always adding a feature. Often the system needs restructuring. The designer's loop requires willingness to discard not just a mechanic but the architecture that produced it.

---

## 3. Playtesting in Depth

### The six playtest types (s009; s008)

| Type | Who | Value | Limitation |
|---|---|---|---|
| **Internal** | Design team | Fast, continuous, free | Team knows the design; blind to new-player problems |
| **Developer** | Other designers | Precise, actionable feedback | Designers play differently from audiences |
| **Friend/family** | Known people | Accessible, willing | Social dynamics may soften criticism |
| **Target audience** | Intended players who don't know the team | Closest to reality | Harder to access |
| **New player** | First-time players specifically | Tests onboarding and first impressions | Limited scope |
| **Experienced player** | Players with significant time in the game | Tests mid/late-game content | Doesn't reveal entry experience |

**Match playtester to stage:** rough paper prototype → developer feedback; near-final digital build → target audience. Using experienced designers for new-player testing produces false positives (they'll figure it out anyway).

### Data types (s008, ch.9)

**Qualitative:**
- **Think-aloud protocol** — ask players to narrate thoughts while playing. Reveals mental model formation, confusion points, decision-making
- **Post-session interviews** — open questions after play; players can reflect more clearly
- **Observation notes** — specific behaviors, reactions, events; continuous during session

**Quantitative:**
- Completion rates (what % reach each milestone?)
- Attrition points (where do players stop?)
- Time spent (too fast = trivial; too slow = stuck or boring)
- Retry rates (repeated attempts = frustrating but trying)
- Feature usage (which mechanics do players use; which do they ignore?)

**Behavioral:**
- *Lab behavior* — players sometimes do things that contradict what they say. **Trust behavior over stated preference.**
- Body language — leaning forward (engagement), slumping (disengagement), rapid inputs/sighing (frustration)

### The facilitator's discipline (s008; s001)

1. **Don't explain** anything the game doesn't explain itself. If the player is confused, that confusion is data — data about how the game communicates, not data about the player's intelligence.
2. **Don't lead** — "did you like the jump mechanic?" invites confirmation. "What did you think about the movement?" opens genuine response.
3. **Don't defend** — when players criticize design decisions, don't explain the rationale. Their experience is real; your explanation is irrelevant to the design problem.
4. **Don't help** — watching a player struggle is valuable. The moment you explain something, you've lost information about how the game can explain it better.

### Acting on playtest results (s009; s008)

1. Cluster observations by design area (onboarding / mechanics / pacing / etc.)
2. For each cluster: does this contradict a design value? If yes, it's a priority fix.
3. For each fix candidate: what is the **minimum change** that addresses the problem?
4. What can be **removed**? Playtesting problems often indicate that something should be cut, not added.

**Danger of over-reaction:** single-playtest observations are anecdotes; patterns across multiple playtesters are design signals. Don't restructure the game based on one person's experience.

### Playtesting across development stages

| Stage | What to test | Best playtesters |
|---|---|---|
| Concept (paper) | Core mechanic; fundamental fun hypothesis | Designers, colleagues |
| Early prototype | Onboarding, core loop, first pacing | Developer circle, gamers |
| Alpha | All mechanics, content pacing, difficulty curve | Target audience |
| Beta | Polish, edge cases, balance | Target audience + experienced players |
| Pre-ship | New player experience; regression testing | Fresh target audience |

---

## 4. Documentation

### Types of design documentation (s008; s006; s001)

**Concept document** (s001, ch.6):
- High concept (1–2 sentences)
- Product (core identity and audience)
- Detailed design (how the vision is implemented)
- **Purpose:** the touchstone for all development decisions. "Does this feature serve the concept document?" is the highest-level design filter.

**Game design document (GDD)** (s006, ch.2):
- Traditional: comprehensive specification of all game systems
- Problem: large GDDs become immediately outdated and stop being read
- **Better approach:** living documents that describe the current design, not the aspired design. Short, maintained, actively used.

**Design values document** (s009):
- 3–5 sentences describing what the game *must* feel like
- Used as evaluation criteria in every playtest
- Must be small enough to hold in working memory

**Playtest notes:**
- Observation (what happened) vs. interpretation (what it means) — keep these separated
- Patterns across playtesters vs. individual reactions
- Timestamped where possible

**The documentation rule** (Schell, Lens #90): documentation that doesn't reflect the current state is worse than no documentation — it misleads. Maintain documents actively or archive them.

---

## 5. Team and Culture

### Games are made by teams (s001, ch.11)

Teams are themselves systems — the same parts/loops/wholes model applies. Success depends on:
- **Shared vision** — the single practice most correlated with successful games (s001, ch.6). A clear, compelling, shared vision means every designer can make decisions aligned with the design without being asked.
- **Understanding roles** — functional roles (what you do), studio roles (your position in the team), corporate roles (your position in the organization)
- **Communication loops** — feedback between team members is a loop like any other; breakdowns in communication cascade into design problems

### The designer's listening (s005, ch.1)

Schell's most important skill for designers: **deep listening**. Five kinds:

1. **Team** — the team collectively may hold skills the individual designer lacks
2. **Audience** — know them better than they know themselves; don't just ask what they want
3. **Game** — the game "tells" you what it needs through playtesting
4. **Client** — hear what they really want (wants ≠ needs)
5. **Self** — often the hardest; the source of authentic vision

**The major gift over the minor gift** (s005): innate aptitude (the minor gift) is less valuable than *love of the work* (the major gift). Love drives practice; practice grows skill past innate talent. The only way to know if you have the major gift is to start down the path and see if it makes your heart sing.

### The design process in stages (s001, ch.12; s006; s005)

| Stage | Goal | Key output |
|---|---|---|
| **Concept** | Is there a game here? | High concept, core mechanic prototype |
| **Pre-production** | Can we make this game? | Vertical slice; proven core experience |
| **Production** | Make the game | Full content; all features |
| **Alpha** | Is the game complete? | All features working |
| **Beta** | Is the game good? | Playtested; balance tuned; bugs fixed |
| **Launch** | Ship | Release candidate |
| **Post-launch** | Is the game thriving? | Patches, DLC, live operations |

**The hardest part: finishing** (s001, ch.12). Most ideas never get prototyped. Most prototypes never get finished. The discipline of completing a project — stage-gating, scope management, committing to ship — is as important as any design skill.

---

## 6. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Quality is discovered through play, not specified in advance | s008, s005, s009 |
| More iteration loops = better game (no exceptions) | s005 |
| Observe don't explain in playtests | s001, s008 |
| Trust behavior over stated preference | s008, s009 |
| Physical prototypes first; digital last | s008, s005 |
| Design values anchor iteration and prevent feature creep | s009 |
| Shared vision is the single practice most correlated with game success | s001 |
| Minimum change is almost always the right fix | s009 |
| Cut more than you add when playtesting reveals problems | s008, s009 |

---

## 7. Hot Potato — Production Implications

| Decision | Rationale |
|---|---|
| 2 publishable levels before full production (Cerny's Method) | Prove the core loop (tag + FAP) is fun before building all maps/modes |
| Physical prototype first (index cards + dice) | Can test tag mechanics and FAP scoring without UE5 setup time |
| Short playtest sessions (10–15 min) | Matches intended session length; reveals natural stopping points |
| Watch, don't explain, in social playtests | Party game feel is destroyed if the designer has to explain mechanics |
| Test with non-gamers early | Hot Potato's target audience includes casual players; don't only test with game-literate people |
| Decisions log cites sources | Designer's loop discipline: every decision has a traceable basis; reversals are informed, not reactive |

**Sources:** s008 (Fullerton) · s005 (Schell) · s009 (Macklin & Sharp) · s001 (Sellers) · s006 (Adams)

**See also:** [[../10-Library/notes/iterative-design-process]] · [[../10-Library/notes/playtesting-methods]] · [[../10-Library/notes/design-vision-concept-document]] · [[../00-Atlas/disciplines/Production]]
