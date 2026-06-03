# Educational Games Design Guide

Designing games where learning is the intended outcome — and where the game is the mechanism, not the wrapper. This guide addresses the B2B educational games market (school and institutional contexts, UK/US curricula, ages 9–13).

**Directly relevant to:** B2B educational games studios

---

## The central premise

Raph Koster's theory (s016) provides the foundational argument: **fun is learning**. The brain produces the "fun signal" when it successfully acquires a new pattern. Games are formal systems stripped of real-world noise that present patterns for the brain to master. Educational games are not games with content strapped on — they are games where the patterns being learned happen to be academic skills.

The distinction that matters: a well-designed educational game uses the exact same psychological mechanisms that make commercial games engaging (flow channel, pattern acquisition, SDT, meaningful play). It simply *names* the skill being developed as "multiplication" or "reading comprehension" rather than "headshots" or "resource management."

**The pitch argument for B2B buyers:**
> "Our mechanics produce [learning objective] as the emergent outcome of skilled play. The game is fun because it is teaching. It is teaching because it is fun. These are not separate."

---

## Learning design fundamentals

### Bloom's taxonomy mapped to game mechanics

Bloom's taxonomy identifies six levels of learning, from surface to deep. Each level maps to a game mechanic type:

| Bloom level | Description | Game mechanic equivalent |
|-------------|-------------|------------------------|
| **Remember** | Recall facts | Flashcard-style recognition (quick, low-stakes) |
| **Understand** | Explain concepts | Multiple-choice with explanation; dialogue navigation |
| **Apply** | Use knowledge | Simulation; open-ended problem solving |
| **Analyze** | Examine relationships | Strategy games; causal chain analysis |
| **Evaluate** | Make judgments | Design challenges; argumentation games |
| **Create** | Produce something new | Open-world building; generative tools |

Most educational games target only Remember and Understand — the lowest Bloom levels — because they're easiest to design and assess. The commercial opportunity is at Apply and above.

### Koster applied: the learnable middle

Koster's "learnable middle" (s016) = the zone where the curriculum content is neither too trivial to engage nor too complex to access. This is identical to Csikszentmihalyi's flow channel (s005 ch.9) applied to learning:

- **Too easy**: students already know this; boredom exit
- **Too hard**: students can't engage with the patterns; frustration exit
- **Learnable middle**: students are acquiring new patterns, extending their mental models, building competence

The ZPD (Vygotsky's Zone of Proximal Development) from educational theory is the same concept. The flow channel is the game design term; the ZPD is the learning science term. Designing a game that keeps students in their ZPD is the same problem as keeping players in the flow channel.

**Design question for every curriculum level**: at what difficulty level is this content learnable for the target age and prior knowledge? That difficulty level is the starting point for the challenge curve.

### SDT in educational contexts

Self-Determination Theory (s014) maps directly:

- **Competence**: students feel they are genuinely learning and improving at the subject matter — not just at the game. If the game skill is disconnected from the learning skill, SDT is not being served.
- **Autonomy**: students choose their path through the content, their character, their approach. Not all students have the same learning style; autonomy allows the game to serve multiple approaches.
- **Relatedness**: connection to characters, to classmates, to a larger narrative that makes the learning matter. This is where the "why are we learning this?" question is answered.

The F2P undermining effect (s014) applies here: if the game uses extrinsic rewards (points, badges, leaderboards) to motivate learning, and students learn the game primarily to get rewards rather than because the content is interesting, the intrinsic curiosity about the subject is being undermined. **Design learning as the game, not the gate to rewards.**

---

## MDA for educational games

### Target aesthetics

For ages 9–13, UK/US curricula context:

- **Challenge** (primary): mastery of the curriculum content through play — the same satisfaction as mastering a hard level applies to mastering a hard math concept
- **Discovery** (strong): the curriculum content as a world to explore, not a list to memorize — finding connections between concepts, discovering applications
- **Narrative** (supporting): a story frame that contextualizes why the learning matters and that the student cares about continuing

Avoid aesthetics that educators will distrust:
- **Submission** (passive entertainment): a game that entertains without teaching produces no outcomes teachers can defend to administrators
- **Sensation** (pure sensory reward): visual/audio spectacle without connection to learning content is perceived as distraction

### MDA design process for educational games

1. Define the **learning objective** first (the curriculum anchor)
2. Define the **Aesthetic target**: what emotional experience should mastering this objective produce? (Pride in competence? Wonder at discovery? Excitement at application?)
3. Design **Dynamics** that produce that aesthetic through engagement with the curriculum content
4. Design **Mechanics** that create those dynamics — where the mechanic IS the learning activity

**Example — fractions for ages 10–12:**
- Learning objective: understand fraction equivalence and addition with unlike denominators
- Aesthetic target: competence (mastery pride); discovery (seeing how fractions connect to real quantities)
- Dynamic: the player must correctly calculate fractional amounts to solve a resource management problem; wrong fractions produce bad outcomes; correct ones produce satisfying resource outputs
- Mechanic: crafting economy where recipes require fractional quantities; visual feedback on fraction values through portion-filling graphics

---

## Design patterns that work in educational games

### 1. The simulation pattern
The game *is* the subject matter. The simulation produces the learning as a natural outcome of engaging with the system.

- **SimCity**: urban planning is not taught; it is experienced
- **Oregon Trail**: historical decisions produce historical consequences
- **Foldit** (protein folding): real research problems as gameplay

Best for: high Bloom levels (Apply, Analyze, Evaluate); subjects with inherent systemic structure (economics, ecology, history, biology)

### 2. The challenge pattern
The curriculum content provides the tools for solving the game's challenges. The game presents problems; the content is the solution.

- **DragonBox** (algebra): abstract algebra rules are the game mechanics; the student "solves puzzles" while learning algebra
- **Math-heavy strategy games**: resource calculations are the game; the math is the skill

Best for: procedural skills (arithmetic, grammar rules, coding); when correct application produces visible game success

### 3. The narrative framing pattern
The curriculum content is embedded in a story context where it matters. Students learn because the story requires it, not because the game requires it.

- **80 Days** (geography, history): accurate knowledge of world geography and history produces better narrative outcomes
- **Assassin's Creed Discovery Tours** (history): historical accuracy as exploration reward

Best for: knowledge content (history, science facts, cultural literacy); when the student can feel the story consequences of learning

### 4. The hidden mechanic pattern
The assessment is invisible to the student; the learning is the game. The teacher sees the outcomes; the student sees play.

- A math game where difficulty adapts based on demonstrated competence without ever showing a difficulty level
- A reading comprehension game where the story questions adapt to individual reading level
- An analytics dashboard for teachers that shows content mastery, not just play time

Best for: formative assessment (ongoing, not final-exam-style); adaptive learning; when teacher buy-in requires measurable outcomes

### 5. The failure-safe environment pattern
Educational contexts require high psychological safety for experimentation — students who fear failure stop trying. Game design can create a context where:
- Failure is expected and instructive ("you got 6/10 — here's what you missed")
- Multiple attempts are normal and rewarded
- Progress is visible even when mastery isn't complete
- Comparison to peers is opt-in, not default

---

## B2B market realities

### Who buys and what they care about

**The decision chain:**
1. **Teacher** (primary influencer): cares about curriculum alignment, ease of use in class, and whether students actually engage
2. **Department head / curriculum coordinator** (decision maker): cares about alignment to national/state standards, evidence of effectiveness, budget
3. **IT administrator** (technical gate): cares about compatibility, security, data privacy (COPPA, FERPA, GDPR), deployment simplicity
4. **School business manager / procurement** (final approval): cares about price, licensing model, invoicing requirements

**Buyer priorities in order:**
1. Curriculum alignment — maps to standards they're assessed on
2. Ease of deployment — runs on existing devices; no IT complexity; works offline if needed
3. Evidence of effectiveness — pilot data, published research, case studies
4. Teacher control dashboard — assign content, monitor progress, export grades
5. Price — per-student licensing is most legible; district licenses for larger commitments

### Standards alignment (UK/US)

**UK National Curriculum** — key stages and subject statements are published by the Department for Education. Every design decision must be mappable to a specific key stage statement to pass procurement scrutiny.

**US Common Core State Standards** (adopted by most states) — ELA and Math standards with grade-level expectations. Supplemented by Next Generation Science Standards (NGSS) for science content.

**Practical implication**: before designing a single mechanic, identify the specific standard code(s) you're addressing. This becomes the pitch's first slide.

### Technical requirements for B2B

- **SCORM or xAPI (Tin Can API)**: the technical standards that allow your game to report learning outcomes to a Learning Management System (LMS). Most schools use Canvas, Schoology, Moodle, or Google Classroom. Without LMS integration, teachers can't see outcomes.
- **COPPA (US) / GDPR (EU/UK)**: children's data privacy. Cannot collect personal data from under-13 players without explicit parental consent. Design must avoid unnecessary data collection.
- **Device compatibility**: UK/US schools typically have Chromebooks, shared iPads, or Windows desktops. Mobile-first design or HTML5/WebGL deployment is usually more practical than native apps.
- **Bandwidth**: many schools have poor bandwidth. Heavy-asset games (large textures, streaming audio) fail in the real deployment context.

### Pricing models

| Model | How it works | Best for |
|-------|-------------|----------|
| **Per-student license** | Price × number of enrolled students per year | Individual teachers buying; most legible |
| **Class license** | Fixed price per classroom per year | Small school or pilot scale |
| **Site license** | One price for the whole school | Budget-holder buy-in; school-wide deployment |
| **District license** | One price for an entire school district | Largest scale; requires district procurement |
| **Freemium** | Core content free; expanded content paid | Viral adoption; individual teacher buy-in before institutional |

### The pilot model

Most educational game purchases start with a pilot — a free or heavily discounted first engagement with one teacher or one school. Pilot success is the primary conversion mechanism.

What a successful pilot requires:
1. One champion teacher who believes in the product
2. A measurable outcome that both teacher and you agree to assess
3. Minimal setup friction (if setup takes more than 20 minutes, the pilot won't start)
4. A debrief and case study documented at the end

The goal of a pilot is not to earn revenue — it is to earn a case study and a reference customer.

---

## The design checklist for educational games

- [ ] Is the curriculum standard explicitly named and mapped to a specific mechanic?
- [ ] Is the learning happening *through* play, not *despite* play?
- [ ] Can a teacher assign specific content and see student outcomes without playing the game themselves?
- [ ] Does the game run on Chromebooks and shared iPads without installation?
- [ ] Is there LMS integration (SCORM or xAPI) or a simple teacher dashboard?
- [ ] Does the onboarding take < 5 minutes for a student with no prior game experience?
- [ ] Is the difficulty adaptive to student performance (not a fixed difficulty)?
- [ ] Is failure safe — does incorrect play produce learning, not shame?
- [ ] Would a student play this voluntarily? (If no, the game is a test with graphics)
- [ ] Would a teacher show this to their department head with confidence? (If no, the presentation layer needs work)

---

## Reference case studies

- **Quest to Learn (NYC)**: a full school built on game-based learning principles; founded by Katie Salen. Not a product but a proof of concept for the philosophy. → [katie-salen-eric-zimmerman](../../10-Library/notes/katie-salen-eric-zimmerman.md)
- **DragonBox**: algebra for ages 5+; purely mechanic-driven learning with no explicit math notation early. Commercial success.
- **Duolingo**: language learning as gamified habit loop. Not a curriculum product but demonstrates the retention power of well-designed learning loops.
- **Minecraft Education Edition**: Microsoft's educational adaptation; demonstrates that a commercial game can become a curriculum tool with teacher tools and standards alignment.

---

## Key concepts & cross-links

- [theory-of-fun](../../10-Library/notes/fun-as-learning-koster.md) — Koster's theoretical foundation: fun = learning
- [motivation](../../10-Library/notes/player-motivation-maslow.md) — SDT; intrinsic motivation; the undermining effect
- [flow-channel](../../10-Library/notes/flow-channel-definition.md) — the flow channel = the Zone of Proximal Development
- [mda-framework](../../10-Library/notes/mda-framework-overview.md) — designing toward learning outcomes via MDA
- [playtesting](../../10-Library/notes/playtesting-methods.md) — playtesting with classroom populations
- [among-us](../games/among-us.md) — social deduction as educational content
- [katie-salen-eric-zimmerman](../../10-Library/notes/katie-salen-eric-zimmerman.md) — Quest to Learn precedent
- [raph-koster](../../10-Library/notes/raph-koster.md) — the theoretical bridge

## Sources

s016 (Koster — fun = learning; theoretical foundation) · s014 (Hodent — SDT; intrinsic motivation; undermining effect) · s005 ch.9 (Schell — flow channel; ZPD analogy) · s011 (MDA — aesthetics for educational targeting) · s008 (Fullerton — playcentric design applied to classroom contexts) · s013 (Salen & Zimmerman — Quest to Learn context; meaningful play in educational settings)
