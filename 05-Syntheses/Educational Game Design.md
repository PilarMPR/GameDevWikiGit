# Educational Game Design

> **What this is:** Everything the canon says about games as learning tools — Koster's games-as-teaching thesis, the edutainment trap, learning objectives vs. fun objectives, transfer of learning, scaffolded difficulty in educational contexts, age-appropriate design, and the B2B educational games context. Aggregated across s016, s014, s009, s005, s006.

---

## 1. Games Are Inherently Educational

**Koster** (s016) opens with what should be the founding principle of all educational game design:

> *"Games are teachers. Fun is just another word for learning. And we use the same parts of our brain to engage with games that we use for every other kind of learning."*

This is not a metaphor. It is a mechanistic claim:
1. The brain evolved as a pattern-recognition machine
2. When it successfully acquires a new pattern, it releases a pleasurable signal
3. Games are formal systems that present patterns for the brain to learn
4. Fun = the pleasure signal from successful pattern acquisition = learning

**The implication:** every good game teaches. The only question is *what* it teaches. A violent game teaches pattern-mastery within a violent context. A math game teaches pattern-mastery within a mathematical context. The learning mechanism is the same; the content differs.

**Corollary:** if a game stops teaching new patterns, it becomes boring. Boredom is the brain reporting that the learning signal has ceased. This means boring educational games fail not because they're educational but because they've stopped teaching (too easy, too repetitive) or because the learning is too hard to access (too opaque, too complex).

---

## 2. The Edutainment Trap

**The most common failure mode in educational game design:**

The designer starts with a learning objective (teach multiplication tables) and builds a game *around* it. The game is a delivery mechanism for the content; the fun is a sugar coating. This produces what the industry calls "chocolate-covered broccoli" — the educational content is the broccoli, the game mechanics are the chocolate, and players can taste the difference.

**Why this fails:**
- The game mechanics don't *embody* the learning content — they're separate from it
- Players learn to bypass the educational content and get to the "real game"
- The learning happens despite the game, not through it
- Intrinsic motivation for the learning content is zero; players are only there for the game wrapper

**The better approach** (s016; s009): design so that the game mechanics *are* the learning. To play is to learn; to learn is to play. The content is not separate from the fun — it is the fun.

**Examples of non-traps:**
- *Math Blaster* was a trap: shooting games with math problems interrupting the action
- *Minecraft* education editions are closer to non-traps: building with geometry, chemistry, history embedded in the building mechanic itself
- *Kerbal Space Program*: orbital mechanics are not a barrier to fun — they ARE the fun

---

## 3. Learning Objectives vs. Fun Objectives

**Macklin & Sharp** (s009, ch.1) introduce **design values** as the north star of iteration. In educational contexts, the design values must include *both* the learning objective AND the fun objective — and these must be genuinely compatible.

**The compatibility test:** can the learning objective and the fun objective be achieved through the same mechanic? If yes, you have a genuine educational game. If no, you have a game wrapper around educational content.

**Compatibility examples:**

| Learning objective | Compatible game mechanic | Result |
|---|---|---|
| Fraction division | Character progression system that divides resources | Fun AND learning from same mechanic |
| Historical decision-making | Grand strategy game with historical context | Fun AND learning from same mechanic |
| Grammar structure | Sentence-building puzzle mechanics | Potentially compatible |
| Multiplication tables | Shoot the correct answer | **Not compatible** — mechanics are unrelated to content |

**The design process for educational games:**
1. Define the learning objective precisely (not "teach math" but "teach understanding of how fractions scale")
2. Find a game mechanic whose operation naturally *requires* that understanding
3. Design the game around that mechanic
4. Only then add progression, narrative, and polish

---

## 4. Learning Science Applied to Game Design

**Hodent** (s014) provides the cognitive science layer that educational game designers need:

### Working Memory Constraints
- Working memory holds ~3–4 items simultaneously
- New learning competes with active gameplay for working memory
- If the game's cognitive demands fill working memory, there's no capacity for the learning content

**Practical implication:** educational games must calibrate total cognitive load carefully. If the gameplay mechanics themselves require full working memory, the player cannot also encode the educational content. Simpler game mechanics = more working memory available for learning.

### Spaced Repetition
Information revisited at increasing intervals is retained longer. The most effective learning methodology:
- Encounter content
- Practice immediately
- Re-encounter after a day
- Re-encounter after a week
- Re-encounter after a month

Educational games can implement spaced repetition naturally through their progression structure: introduce concept, require use in early levels, return to concept in later levels with higher complexity.

### Context-Dependent Learning
People remember things better in the context where they learned them. Tutorial information delivered in a separate "tutorial mode" transfers poorly to gameplay contexts. Learning embedded in gameplay contexts transfers directly to gameplay performance.

**Design rule:** teach the educational content in the *same context* where the player will need to apply it. Don't teach fractions in a tutorial screen and then ask players to apply them in a different-looking game context.

### The Forgetting Curve
Information not revisited is lost rapidly. A one-shot exposure to any educational content will have near-zero retention within 24 hours. Educational games must repeat and reinforce content across many sessions.

---

## 5. Transfer of Learning

**The most important and hardest problem in educational game design:**

**Near transfer:** the student applies what they learned in a context very similar to the learning context. *Playing the educational game well → performing well on a test of the same content.*

**Far transfer:** the student applies what they learned in a very different context. *Playing the educational game → applying the underlying concepts in real-world situations.*

**The hard truth** (acknowledged in the educational game research literature): most games achieve near transfer at best. Far transfer is rare and difficult to design for.

**Conditions for better transfer** (s014; s016):
- The game mechanic must have the same *deep structure* as the real-world application (not just the same surface features)
- The learning should be explicitly connected to the real-world context at some point in the game
- Players should be given opportunities to apply the concept in varied contexts (variety of transfer targets within the game)

**Koster's transfer insight** (s016): games teach the *pattern* of the system. Transfer happens when the real world has a similar pattern. A game that teaches systemic thinking about resource flows in a game economy can transfer to economic reasoning in reality — because the *patterns* are the same even if the surface is different.

---

## 6. Age-Appropriate Design

**Adams** (s006, ch.4) and Schell (s005, ch.8) both provide age-group analysis. Educational game design requires calibration to cognitive development stage:

### Ages 4–6 (Preschool)
- Concrete, visual, immediate feedback
- Very simple rules (1–2 rules maximum at once)
- Cause-and-effect mechanics with instant, obvious consequences
- No failure states that produce frustration (forgiveness is essential)
- Content: colors, shapes, numbers up to 10, basic sounds/letters
- Session length: 5–10 minutes maximum

### Ages 7–9 (Early Elementary)
- Can handle 3–4 concurrent rules
- Beginning to read; text can supplement visuals
- Competitive play becomes interesting (vs. simple obstacles)
- Content: early math, reading comprehension, basic science concepts
- Session length: 15–20 minutes

### Ages 10–13 (Target B2B audience for Wild Alchemists)
- Can handle complex rule sets
- Abstract thinking emerging (can reason about things not present)
- Social play highly motivating (friend groups matter)
- Can engage with systems-level thinking (cause → complex effect chains)
- Content: curriculum-aligned math, science, history, language arts; age-appropriate complexity
- Session length: 20–40 minutes; class period compatibility critical

### Ages 13–18 (Teen)
- Full abstract reasoning
- Strong social identity motivation; peer context paramount
- Can engage with ethics, complexity, and ambiguity
- Content: advanced curriculum; civic/social content; creative/expressive content
- Session length: flexible; sustained engagement possible

---

## 7. The B2B Educational Context

The Wild Alchemists educational games studio context (UK/US curricula, ages 9–13):

**The B2B buyer is not the player:** the purchasing decision is made by:
- School administrators (procurement, budget, curriculum fit)
- Teachers (classroom usability, lesson plan integration)
- Parents (safety, educational credibility)

...not by the 9–13-year-old student who will actually play.

**This creates a dual-design challenge:**
- **For buyers:** evidence of learning outcomes; curriculum alignment; classroom management features (teacher dashboard, progress tracking); cost-per-student value; technical requirements (school device compatibility, network requirements)
- **For players:** fun; engagement; age-appropriate aesthetics; social features (if classroom multiplayer); appropriate challenge and pacing

**Classroom-specific design requirements:**
- Session length fits within a class period (40–50 minutes maximum, ideally 20–25 min for a lesson segment)
- Can start quickly without extended tutorial (teacher has limited onboarding time)
- Teacher override controls (pause, skip, advance, manage individual students)
- Progress is resumable across sessions (students don't restart each class)
- Report card / progress dashboard for teachers
- Clear connection to curriculum standards (labeled by grade level and standard)

**The buy-in problem:** educational games often die not because they're bad games or bad education — but because teachers don't adopt them. Teacher adoption requires:
- Minimal friction to integrate into lesson planning
- Visible student engagement during class (teacher can see it's working)
- Clear explanation of what standard/skill is being addressed
- Professional credibility (does not look like a toy)

---

## 8. Engagement Without Deception

A specific ethical concern in educational game design: some games claim to be educational as marketing but deliver minimal actual learning. The field calls this "learning theater."

**Learning theater indicators:**
- Educational content is separable from the game (remove the math problems, the game still works)
- Players can succeed in the game without engaging with the educational content
- The educational content produces no change in the game state
- There's no adaptive difficulty based on learning performance

**Genuine educational game indicators:**
- The educational content is load-bearing for game success (you cannot win without learning the content)
- The game adapts to the player's learning performance (gets harder as the student masters content, easier when they struggle)
- Players cannot progress without engaging with the learning content
- Post-game assessments show measurable learning gains

---

## 9. Schell on Transformation (s005, Lens #97)

> *"Does this game transform the player? Is that transformation positive? What would it take for this game to genuinely change someone?"*

Educational games are explicitly designed for transformation. The design question is always: *what is the transformation target?* And the success criterion is always: *does the player leave with more than they arrived?*

---

## 10. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| All games teach; the question is what | s016 |
| The edutainment trap: content separate from mechanics produces broccoli-chocolate | s016, s009 |
| Educational content must BE the mechanic, not be attached to it | s016 |
| Working memory constraints limit simultaneous cognitive demands | s014 |
| Spaced repetition produces far better retention than one-shot exposure | s014 |
| Context-dependent memory: teach in the context where the skill will be applied | s014 |
| B2B educational games have dual design requirements: buyers and players | practical synthesis |
| Teacher adoption is the critical bottleneck in school deployment | practical synthesis |
| Learning transfer requires shared deep structure between game and real-world application | s016, s014 |

---

## 11. Relevant to Wild Alchemists B2B Studio

| Design principle | Studio application |
|---|---|
| Curriculum alignment labels | Required for UK/US school procurement |
| Teacher dashboard | Session overview, student progress, pause/advance controls |
| Class-period session design | 20–25-minute self-contained lesson segments |
| Dual audience design | Fun for 9–13-year-olds; credible to teachers; reportable to administrators |
| Age-appropriate mechanics | Concrete for 9–10; emerging abstraction for 11–13 |
| Learning embedded in mechanics | Content must be load-bearing for game success |
| Adaptive difficulty | Adjusts to demonstrated learning performance |
| Evidence base | Document learning outcomes; prepare for efficacy questions in procurement |

**Sources:** s016 (Koster) · s014 (Hodent) · s009 (Macklin & Sharp) · s005 (Schell) · s006 (Adams)

**See also:** [[../10-Library/notes/fun-as-learning-koster]] · [[../10-Library/notes/player-motivation-maslow]] · [[../30-Analyses/genres/educational-games]] · [[../00-Atlas/disciplines/Production]]
