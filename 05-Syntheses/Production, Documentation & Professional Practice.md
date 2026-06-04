# Production, Documentation & Professional Practice

> **What this is:** Everything the canon says about the professional context of game making — team structure and roles, design documentation (GDD, concept docs, one-pagers), the production pipeline, pitching, and the discipline of finishing. Aggregated across s006, s005, s008, s001.

---

## 1. Games Are Made by Teams

**Sellers** (s001, ch.11):
> *"Games are nearly always made by teams. Teams are themselves systems — the same parts/loops/wholes model applies. Success depends on shared vision and understanding of functional, studio, and corporate roles."*

**The systemic view of teams:** a development team is a complex adaptive system with:
- **Parts:** individual contributors with specialized skills
- **Loops:** communication channels, feedback processes, review cycles
- **Wholes:** the emergent quality of the team's work — greater than the sum of individual contributions

Team problems are system problems: when communication breaks down, the loop is broken. When roles are unclear, parts are acting without proper relationships. When vision is absent, the whole has no coherent goal.

---

## 2. Core Production Roles

**Adams** (s006, ch.2) and **Kremers** (s012) provide the most detailed role taxonomy in the canon:

### Game Designer
Responsible for the game's systems, mechanics, rules, and player experience. May specialize in:
- **Lead Game Designer:** vision, overall design coherence, sign-off on all design decisions
- **Level Designer:** spatial design, encounter design, teaching through levels
- **Systems Designer:** economy, progression, balance, rules
- **Narrative Designer:** story, dialogue, worldbuilding, character

**The designer's primary output:** design documents that specify what the game is and how it works.

### Programmer / Engineer
Implements the designer's specifications. Key specializations:
- **Gameplay Programmer:** implements mechanics, tools, and gameplay systems
- **Engine/Technical Programmer:** rendering, physics, networking, platform integration
- **Tools Programmer:** builds tools that other disciplines use

**The designer-programmer relationship:** the designer specifies *what* the game does; the programmer determines *how* it can be technically realized. Successful collaboration requires designers who understand technical constraints and programmers who understand design intent.

### Artist
Responsible for all visual assets and the game's aesthetic. Specializations:
- **Concept Artist:** defines the visual language; creates reference for 3D/2D production
- **Character Artist:** models, rigs, and textures player characters and NPCs
- **Environment Artist:** builds the 3D world spaces
- **UI Artist:** designs and implements interface elements
- **Technical Artist:** bridges art and programming; handles shaders, optimization

### Producer / Project Manager
Responsible for the project's schedule, budget, and resource allocation. Not a decision-maker on creative content — a facilitator who ensures the creative team can work effectively.

**The producer's value:** tracking dependencies, managing blockers, preventing scope creep, communicating between the team and external stakeholders. In indie contexts, the designer often serves as their own producer.

### QA / Tester
Finds bugs, verifies feature completion, and provides structured feedback on game quality. QA ≠ playtesting (playtesting is a design activity; QA is a quality verification activity).

### Audio Designer / Composer
Creates and implements sound effects, music, and voice. Often contracted rather than full-time on indie teams.

---

## 3. The Production Pipeline

**Adams** (s006, ch.26) and **Sellers** (s001, ch.12) converge on the standard production phases:

### Concept Phase
**Goal:** determine if this game should be made.

**Key activities:**
- Define the design vision and target experience
- Write a concept document (high concept + key features + target audience)
- Assess technical feasibility
- Assess market viability
- Identify major risks

**Output:** green/red light decision; concept document.

**Duration:** typically 1–4 weeks for a small team.

### Pre-Production
**Goal:** prove the concept works before full commitment.

**Key activities:**
- Build a vertical slice (a small but polished section of the complete game)
- Prove the core mechanic is fun
- Identify all major technical risks and resolve them
- Establish the visual style with key art and prototype levels
- Build the production tool chain
- Create the full production plan

**Output:** vertical slice that demonstrates the game is worth making; production schedule.

**Duration:** 2–6 months for mid-size teams; shorter for small indie.

**Cerny's rule** (cited s005, ch.7): pre-production ends when you have 2 "publishable" sections of the game — sections that are polished enough they could ship. Everything before that point is pre-production, regardless of time elapsed.

### Production
**Goal:** build the complete game.

**Key activities:**
- Execute the production plan
- Maintain the design vision through the full scope
- Respond to playtest findings with design iteration
- Balance scope against schedule
- Reach alpha (all features complete, not all content)

**Output:** alpha build.

**Duration:** the longest phase; typically 6 months to 2+ years for commercial games.

### Alpha
**Goal:** the game is feature-complete; all systems exist but may not be polished.

All core mechanics implemented. All intended levels/modes/characters present. Not necessarily bug-free or artistically complete.

**Alpha testing:** internal testing for bugs, balance, and feature completeness.

### Beta
**Goal:** the game is content-complete; polishing and bug-fixing only.

No new features after beta. All content present. Focus entirely on polish, bug-fixing, and optimization.

**Beta testing:** wider testing; may include external players; stress testing for online features.

### Launch
**Goal:** ship.

Gold master (the final release candidate) submitted to platform holders. Marketing assets complete. Launch infrastructure (servers, storefronts) ready.

### Post-Launch
**Goal:** support and grow the game's player base.

Patches, DLC, balance updates, community management, post-launch analytics. For live service games, this is the largest phase.

---

## 4. Design Documentation

**Adams** (s006, ch.2) and **Fullerton** (s008, ch.9) provide the documentation framework:

### The High Concept Document (1 page)
The minimum viable design document. Contains:
- **Tagline:** one sentence that captures the game's essence
- **Genre:** what kind of game this is
- **Player experience:** what emotions and activities the player will have
- **Core mechanic:** what the player does most of the time
- **Differentiator:** what makes this distinct from existing games

Purpose: pitching to potential partners, investors, or publishers. Must communicate the game's core value proposition in under 2 minutes of reading.

### The Game Design Document (GDD)
The comprehensive specification of the game's design. A living document that evolves with the game.

**Warning (Adams, s006):** large GDDs written early and rarely updated become misleading. The document should reflect the *current design*, not the original vision.

**Modern GDD structure (Adams, s006, ch.2):**

**Part 1 — Game Overview:**
- Game summary (2–3 paragraphs)
- Platform(s) and target audience
- Genre and comparable titles
- Player experience goals
- Unique selling points

**Part 2 — Game Mechanics:**
- Core mechanics and interactions
- Controls
- Camera
- All game systems (combat, economy, progression, etc.)
- Balancing parameters

**Part 3 — Player Experience:**
- Flow states and experience arc
- Onboarding design
- Pacing and difficulty curve

**Part 4 — Game Content:**
- World design overview
- Level list and descriptions
- Characters and NPCs
- Items, weapons, abilities (with stats)
- Enemy types (with behaviors)
- Narrative overview

**Part 5 — Technical and Production:**
- Technical requirements
- Asset list
- Art direction notes
- Audio direction notes

**Living document rule** (s001, ch.6; s008): the GDD is the touchstone for decisions. When the game changes (and it will), the GDD must change. A GDD that doesn't reflect the game is worse than no GDD — it misleads.

### Micro-Documents
For specific design problems, one-page documents:
- **Game rules document:** the complete rule set for a level/mode/mechanic
- **Encounter design spec:** the specification for a specific encounter
- **Character design spec:** complete stats and behavior for one character
- **Balance sheet:** spreadsheet tracking resource generation and consumption rates

### The One-Pager / Pitch Document
A designed marketing document for pitching the game to publishers, investors, or platform holders. Contains:
- Logline (one sentence)
- 3–5 key screenshots or concept art pieces
- Short gameplay description
- Target audience profile
- Business model
- Team credentials

---

## 5. Pitching

**Schell** (s005, Lens #95 — The Pitch):
> *"What is the one-sentence description? Is it compelling? Does it accurately represent the game?"*

**The pitch elevator test:** you have 30 seconds in an elevator with someone who can fund your game. What do you say?

The pitch must be:
- **Clear:** the listener immediately understands what kind of game it is
- **Compelling:** they want to hear more
- **Memorable:** they remember it when you follow up

**Adams** (s006) on pitches to publishers:
- Publishers see hundreds of pitches annually
- The first 30 seconds determine if they read the rest
- The pitch must communicate uniqueness (why this game, not the 50 others that are similar)
- Market data (existing comparable titles, their sales performance) is expected, not optional

**The vertical slice as the ultimate pitch:** instead of explaining what the game will be, show what it already is. A polished vertical slice communicates design quality that no document can match.

**Upton** (s021) provides the most actionable pitch framework in the canon: every element of a pitch must answer exactly two questions — *"Is this game worth making?"* and *"Can this team make it?"* Everything that doesn't serve one of those questions actively hurts the pitch. His catalog of 30 failure modes all trace to the same root: forgetting that publishers are evaluating a **business investment and a team bet**, not aesthetics in isolation. The most common disqualifying errors: extensive backstory before the concept is explained; design pillars (internal compass for the team) presented as pitch hooks (audience-facing reasons to care); vague resource estimates; no assembled team; and unrealistic projections citing Minecraft or Among Us as baseline.

**Key distinction** (s021): design pillars define what the game *is* for the people making it; hooks attract players and publishers. A pitch deck filled with design pillars fails because the audience has no shared design context to make sense of them.

---

## 6. Finishing — The Hardest Part

**Sellers** (s001, ch.12):
> *"The hardest and most essential part of game development is finishing. Most ideas never get prototyped. Most prototypes never get finished."*

**Scope management:** the single most important production skill. Every game concept has infinite possible features. Production is the discipline of choosing what's essential and executing it completely.

**Stage-gating:** explicit checkpoints at each production phase. Advance to the next phase only when the current phase's criteria are met. Prevents the common failure mode: starting production without proving the concept, or starting beta without completing the content.

**The finishing discipline:**
- Lock features before beta (no new features after a defined point)
- Accept "good enough" for non-critical elements
- Cut features that aren't working rather than spending more time fixing them
- Treat "done" as the goal, not "perfect"

---

## 7. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Shared vision is the single practice most correlated with successful games | s001 |
| GDDs must reflect the current design, not the original vision | s006, s008 |
| Pre-production ends when the core mechanic is proven fun (Cerny's rule) | s005 |
| Finishing requires scope management and explicit feature locks | s001, s006 |
| The pitch must be clear, compelling, and memorable in under 30 seconds | s005 |
| Every pitch element must answer "is this worth making?" or "can this team make it?" | s021 |
| Design pillars (internal) and pitch hooks (external) are different things for different audiences | s021 |
| Teams are systems; communication breakdowns are loop failures | s001 |
| A game that isn't fun until 3 months from ship is not an anomaly — Thief: TDP survived this | s025 |
| Staffing up before technology matures and creating content before design is stable are production failure patterns | s025 |

---

## 8. Hot Potato — Production Implications

| Decision | Rationale |
|---|---|
| Concept document: "Hot Potato party brawler where not being the Potato wins" | One sentence captures the core; filters all feature decisions |
| Vertical slice target: one arena + core tag + FAP system — all working and polished | Cerny's rule applied; prove the core before building all maps/modes |
| GDD as living document in Obsidian vault | Knowledge management integrated with production; decisions log tracks all changes |
| Feature lock at beta: no new mechanics after alpha | Scope management for a small team; finish > expand |
| Pre-production success criterion: is playing the prototype better than explaining it? | Fullerton's playcentric test; if you need to explain, it's not ready |

**Sources:** s006 (Adams) · s005 (Schell) · s008 (Fullerton) · s001 (Sellers) · s021 (Upton) · s025 (Smith & Stellmach, Thief postmortem)

**See also:** [iterative-design-process](../10-Library/notes/iterative-design-process.md) · [design-vision-concept-document](../10-Library/notes/design-vision-concept-document.md) · [playtesting-methods](../10-Library/notes/playtesting-methods.md) · [decisions](../40-HotPotato/decisions.md) · [Production](../00-Atlas/disciplines/Production.md)
