# Game Analysis & Design Criticism

> **What this is:** Everything the canon says about *reading* games — Fernández-Vara's three-area analysis framework, procedural rhetoric, the three schemas, how formal analysis improves design, and the vocabulary of game criticism. The skill that makes you a better designer by understanding games you didn't make. Aggregated across s010, s013, s005, s002.

---

## 1. Why Designers Should Analyze Games

**The core argument** (s010, ch.1):

> *"Game analysis is the complement of game design. Where design teaches you to build, analysis teaches you to read. A designer who can read games critically understands not just what works but why — and can apply that understanding deliberately."*

**Practical benefits of developing analytical skills:**
- You can study games you didn't make and extract transferable design principles
- You can identify *why* a game succeeds or fails beyond "it just feels good/bad"
- You can communicate design decisions in terms other designers understand
- You can critically evaluate your own game against a structured framework
- You can identify when your game is making unintended arguments through its rules

**Schell** (s005, ch.2) makes the same point through the lens of the designer's practice:
> *"Dissect your feelings. It's not enough to know you like or dislike something — you must be able to state what and why. Put concrete words to abstract feelings so you can communicate the target experience to your team."*

Analysis is the discipline of knowing why you feel what you feel about a game.

---

## 2. Fernández-Vara's Three-Area Framework

**Clara Fernández-Vara** (*Introduction to Game Analysis*, s010) provides the most systematic analytical framework in the canon:

### Area 1: Context

*Everything outside the game itself that shapes its meaning.*

**Production context:**
- Development team (who made it, how large, what resources)
- Publication context (who funded/published, what genre market existed)
- Technology constraints and affordances (what the platform enabled or prevented)
- The studio's other games and how this fits their work

**Reception context:**
- Critical reception (how was it received at release)
- Player community response (what the community built around the game)
- Historical significance (how has its reputation changed over time)

**Socio-cultural context:**
- Ideological context (what cultural assumptions does it reflect)
- Representational choices (who is depicted; how; what assumptions does the representation carry)
- Influence (what games preceded it; what games it influenced)

**Why context matters for designers:** a mechanic that succeeded in its original context may fail in a different context. Understanding *why* something worked historically helps predict whether it will work now.

### Area 2: Game Overview

*What the game is as a designed object.*

**Players:** how many; what roles do they have; how do they interact?

**Rules and goals:** what are the rules; what constitutes success; are there victory conditions, scoring, or open-ended goals?

**Mechanics:** what can the player do; what is the core mechanic; what secondary mechanics exist?

**Spaces:** what is the physical/virtual space; how is it organized; what is the relationship between space and gameplay?

**Fictional world:** what story/setting frames the mechanics; how much does the fiction matter to the gameplay?

**Gameplay experience:** what emotional experience does playing produce; what's the tone; what's the moment-to-moment feel?

### Area 3: Formal Elements

*The deep structural analysis of how the game works as a system.*

**Rules of the world:** what are the physics and logic; what's possible vs. impossible; what are the constitutive rules vs. regulative rules?

**Diegetic vs. extradiegetic rules:** some rules exist in the game world (a monster has 100 HP); others exist only at the meta-level (players take turns). Both are rules but have different relationships to the fiction.

**Abstraction:** what has the game simplified or removed from reality; what has it kept; why?

**Procedural rhetoric** — see section 3 below.

**Dynamics:** what behaviors emerge when the system runs? What strategies emerge? What unintended interactions exist?

**Control schemes:** how does the physical interface relate to the game actions; what does the mapping communicate about the game's identity?

**Difficulty and balance:** how is challenge calibrated; is the difficulty fair; what skill does it require?

**Representation:** who is depicted; how are they depicted; what values does the representation communicate?

---

## 3. Procedural Rhetoric

**Ian Bogost** (via s010):

> *"Procedural rhetoric is the practice of using processes persuasively — making arguments through rules and procedures, not just through text or images."*

Games make arguments through their mechanics. **What the rules reward and punish** is an implicit argument about what is good and bad.

### Examples

| Game mechanic | Implicit argument |
|---|---|
| All problems solvable by combat | Violence is always an option; fighting is valid |
| Economic growth always increases happiness | GDP growth = wellbeing (a specific economic ideology) |
| Ecological balance required for survival | Environmental stewardship matters |
| Failure always reversed by enough practice | Effort always produces mastery (meritocracy assumption) |
| Rich players accumulate faster (Monopoly) | Capitalism compounds advantage (satire of real estate) |
| Stealth is rewarded; direct conflict is punished | Caution and patience are more valuable than aggression |

### Intentional vs. Unintentional Arguments

Most designers do not consciously craft these arguments — they emerge from the rule system. The question is whether to recognize and engage with them deliberately.

**For educational game designers:** this is especially critical. What argument does your game make about the subject domain? A history game where war always solves problems makes an argument about history. A science game where data is always unambiguous makes an argument about scientific practice.

**For Hot Potato:** the procedural rhetoric of the game argues:
- Social connections and chaos are fun (fellowship and sensation as primary aesthetics)
- Passive play is penalized (anti-camp mechanic)
- Everyone is at risk, regardless of skill (chaos injection equalizes)
- Losing can be funny (comedic loss state)
- Aggression (trolling) is rewarded (FAP system)

---

## 4. Playing Critically vs. Playing Normally

**Fernández-Vara** (s010, ch.2) on the analytical mindset:

Normal play: immerse in the experience; let the game take you.
Critical play: *observe* the experience while having it. What choices am I making? What is the game asking me to do? What am I feeling and why? What rules are producing this?

**The dual-mode problem:** observing your own experience disturbs it. Being analytical breaks the immersion that produces the experience you're trying to analyze.

**Schell's four techniques** (s005, ch.2) for navigating this:
1. **Analyze memories** — play normally, then analyze afterward
2. **Two passes** — play once for experience, once analytically
3. **Sneak glances** — brief analytical checks ("Is this exciting? Yes/No") without breaking flow
4. **Observe silently** — a Zen-like split attention that takes practice

**Practical workflow for designers:** play through a game you want to study twice. First run: normal play. Second run: analytical notes. The first run produces the genuine emotional experience you need to understand; the second run produces the structural analysis.

---

## 5. The Three Schemas Applied (Salen & Zimmerman, s013)

Every game can be analyzed through the three schemas — and a complete analysis requires all three:

### Applying the Formal Schema (Rules)
Map the game's mechanics:
- What are all the verbs (actions the player can take)?
- What are all the objects (entities in the game world)?
- What are the rules governing interactions?
- What constitutes winning/losing/completing the game?
- What is the probability space (range of possible game states)?

### Applying the Experiential Schema (Play)
Ask what the game is *like* to play:
- What is the moment-to-moment emotional experience?
- Where does the flow channel sit? Where does it break?
- What is the relationship between player action and system outcome (meaningful play)?
- What are the most memorable moments, and why?
- What is the game's characteristic experience (its "feel")?

### Applying the Cultural Schema (Culture)
Ask what the game *means*:
- What does the game represent, and how?
- What arguments does the game make through its rules (procedural rhetoric)?
- What community has formed around it, and what does that community do?
- How does the game relate to its cultural context of creation?
- Is the game's representation of people/situations accurate, stereotyping, or harmful?

---

## 6. Genre Analysis

Understanding genre is both a design tool and an analytical tool:

**Genre as player expectation:** genre is not just a category — it is a set of player expectations. Players who buy an FPS expect certain mechanics (first-person perspective, projectile weapons, spatial movement). Violating those expectations requires deliberate design and effective communication.

**Genre as mechanical vocabulary:** genres have evolved because certain mechanic combinations work well together. The RTS mechanic set (real-time, top-down, unit control, resource management, base building) has been refined over 30 years. Designing within genre leverages that refinement.

**Fernández-Vara** (s010, ch.3): genre analysis asks:
- What genre conventions does this game follow?
- Which conventions does it subvert? Why?
- Is the subversion successful? What does the success or failure tell us?

**For Hot Potato:** the game straddles genres (party brawler, tag game, platformer) and this creates design questions about which conventions to follow and which to subvert.

---

## 7. Applying Analysis to Design Improvement

The analytical toolkit is most valuable when used *on your own game in development*:

### The Self-Analysis Checklist

**Formal analysis of your game:**
- Can you list all the operative actions? Are there too many/few?
- Is the probability space wide enough to generate meaningful variety?
- Are there unintended dominant strategies in the rule set?

**Experiential analysis of your game:**
- Where does the flow channel break? (playtest observations)
- Are player actions discernible? Integrated?
- What is the characteristic moment of the game — the moment players most remember?

**Cultural analysis of your game:**
- What argument does your game make through its rules?
- Is that the argument you intend to make?
- Who is represented; how; does it reflect your values?

### Comparative Analysis

Study 3–5 games in your target genre or player audience:
- What do they all do? (Genre conventions worth following)
- What does your game do differently? (Your distinct value)
- Where do the comparables fail or underwhelm? (Your opportunity)

---

## 8. The Vocabulary of Criticism

**Anthropy & Clark** (s002) argue that better vocabulary produces better design thinking. Key analytical vocabulary:

| Term | Definition | Source |
|---|---|---|
| **Core mechanic** | The essential repeated action defining the game | s013 |
| **Emergent narrative** | Stories arising from gameplay, not authored | s013 |
| **Procedural rhetoric** | Arguments made through rules | s010 |
| **Ludonarrative dissonance** | Conflict between story and mechanics | practice |
| **Magic circle** | The bounded space of play | s013, s004 |
| **Meaningful play** | Discernible + integrated outcomes | s013 |
| **Dominant strategy** | The one best approach that eliminates choice | s005 |
| **Flow channel** | The zone where challenge = skill | s005 |
| **Affordance** | A relationship enabling action | s015 |
| **Diegetic** | Existing within the game world | s012 |
| **Operative action** | A designed player action | s005 |
| **Resultant action** | An emergent behavior from operative combinations | s005 |

---

## 9. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Analysis and design are complementary skills; each improves the other | s010 |
| Complete analysis requires formal + experiential + cultural schemas | s013, s010 |
| Games make arguments through their rules whether designers intend them to or not | s010 |
| Genre is a set of player expectations as much as a mechanical category | s006, s010 |
| Critical vocabulary precision produces better design decisions | s002 |
| The analytical mindset requires deliberate practice (playing while observing is hard) | s005 |

---

## 10. Hot Potato — Analysis Tools Application

**Formal analysis:**
- Core mechanic: tag (transferring the Potato role by physical contact)
- Operative actions: move, jump, tag, use item, interact with environment
- Resultant actions: escape routes, choke points, item combos, alliance formation

**Experiential analysis:**
- Target emotional experience: chaotic fun, good-natured blame, social laughter
- Flow channel target: sessions where even losing players are entertained
- Characteristic moment: the moment of receiving the Potato (panic) and passing it (relief/triumph)

**Cultural analysis:**
- Procedural rhetoric: chaos and social interaction are inherently fun; everyone is at risk; passive play is punished; losing can be funny
- Representation: party setting with diverse human characters; no gender/race stereotyping; inclusive fantasy

**Sources:** s010 (Fernández-Vara) · s013 (Salen & Zimmerman) · s005 (Schell) · s002 (Anthropy & Clark)

**See also:** [meaningful-play-definition](../10-Library/notes/meaningful-play-definition.md) · [game-as-system](../10-Library/notes/game-as-system.md) · [game-analysis-framework](../10-Library/notes/game-analysis-framework.md) · [[../30-Analyses/games/]] · [Theory](../00-Atlas/disciplines/Theory.md)
