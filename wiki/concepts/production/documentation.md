# Documentation

The craft of capturing game design decisions in written, visual, and structured form — serving communication, alignment, and continuity throughout the development process. Documentation is not bureaucracy; it is the **shared language** that lets a team build toward a common vision.

---

## Why documentation matters (s009, ch.7; s005)

Games are made by teams over months or years. Without documentation:
- Different team members build toward different visions of the game
- Design decisions made early are forgotten and remade (or accidentally contradicted)
- New team members have no way to get up to speed on the game's direction
- Stakeholders (producers, publishers, investors) cannot evaluate what is being built

Documentation is the team's memory and communication channel. It is not a replacement for conversations — it is the record of their outcomes.

> "Documentation is the compass of the design process. It doesn't make the journey; it tells you where you are and where you're going." (s009 paraphrased)

---

## The game design document (GDD) (s009, ch.7; s005)

The GDD is the primary document describing what a game is. It serves two audiences:
- **Internal** (the team): shared understanding of vision, mechanics, and priorities
- **External** (stakeholders): communication of the game's concept, scope, and design rationale

### GDD structure (s009)

There is no universal GDD template, but effective GDDs typically cover:

**Game overview:**
- Logline: 1–2 sentences describing the game
- Genre, platform, target audience
- Core pillars: 3–5 principles that define what the game is and is not
- Design values: what experiences the game is trying to create

**Core mechanics:**
- The primary verbs (what can the player do?)
- The core loop (what does the player do repeatedly?)
- Progression systems (how does the game evolve?)

**Formal elements:**
- Full rule set
- Goals and win/loss conditions
- Resources and their relationships

**Game world:**
- Setting, premise, and tone
- Characters and their roles
- Level/environment overview

**Feature list:**
- Prioritized (must-have / should-have / nice-to-have)
- Each feature with a brief design rationale

**Appendices:**
- Reference art, competitive analysis, design inspiration

**What GDDs are not:** immutable contracts. A GDD at the start of development will not resemble the GDD at the end. It should be a living document, updated as the game evolves through iteration. (s008)

---

## One-pagers and pitches (s009; s005)

Before a GDD exists, and throughout development for stakeholder communication, shorter formats serve:

### The one-pager
A single page (or screen) describing the game concept. Intended to communicate what makes the game interesting and worth building, not how it works in detail.

Contents:
- Title and logline
- Core loop summary (what does the player do?)
- What makes this unique / the hook
- Target audience and genre
- Visual tone (a single reference image)

The one-pager is the pitch document. It must be compelling enough that someone who reads it wants to see more.

### The pitch deck
A presentation (5–15 slides) for structured stakeholder pitches. Expands the one-pager with:
- Market positioning
- Comparable titles ("X meets Y")
- Key features
- Business model and platform
- Team background
- Development timeline and budget

---

## Design documentation best practices (s009, s005, s001)

### Keep it alive
Documentation that isn't maintained becomes a liability — it misleads readers about the current state of the design. Assign ownership: someone is responsible for keeping each section current.

### Match detail to certainty
Don't document speculative features in exhaustive detail. Save deep documentation for settled design decisions. Speculative ideas belong in notes or a backlog, not the main GDD.

### Document decisions, not just decisions
Record not just what was decided but why. "The player has three lives because it tested better than infinite continues" is more useful than "the player has three lives." The rationale prevents accidental revisiting of already-settled debates.

### One source of truth
Avoid duplicate documentation in different places. When the game changes, one source of truth is updated; five sources all become outdated differently.

### Visual over verbal
Concept art, flow diagrams, and system diagrams communicate faster than prose. Where possible, use visuals to convey game feel, UI layout, and system relationships.

---

## Macklin & Sharp on documentation (s009, ch.7)

Key points from their coverage:
- **Prototype first, document second**: document what you've validated, not what you're hoping to build
- **Documentation as communication**: the primary audience for a document is the team; write for them
- **Pong design document as case study**: even a game as simple as Pong has enough design decisions to require documentation (paddle size, ball physics, score limit, serving rules) — documentation reveals the assumptions embedded in any design
- **Living documents**: all design documents should have version history and change logs

---

## Schell on documentation (s005, ch.24)

Schell frames documentation as a form of "listening" — the document is a communication with the future self and the team:
- Writing a design document forces clarity: "You can't document something you don't understand"
- Documents become the basis for team alignment; misalignment surfaces when the document is reviewed
- The process of writing reveals gaps in the design that weren't visible in prototype

---

## Key concepts & cross-links

- [[iterative-design]] — documentation captures the output of each iteration
- [[playtesting]] — playtest results should be documented
- [[team-and-culture]] — documentation serves team communication
- [[../../theory/formal-elements]] — GDD formal elements section captures the game's structural anatomy
- [[../../mechanics/core-mechanics]] — the core loop section of a GDD documents this

## Sources

s009 ch.7 (Macklin & Sharp — GDD structure, Pong case study, documentation principles) · s005 ch.24 (Schell — documentation as communication; design document as clarity tool) · s008 (Fullerton — living documents, documentation and prototyping relationship) · s001 ch.5 (Sellers — documenting system design decisions)
