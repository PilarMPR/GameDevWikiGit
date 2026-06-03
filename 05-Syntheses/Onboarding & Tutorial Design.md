# Onboarding & Tutorial Design

> **What this is:** Everything the canon says about getting players into a game — the first-time user experience, teaching through play vs. telling, progressive disclosure, cognitive load management, and the forgetting curve. Aggregated across s005, s012, s006, s014, s008, s017.

---

## 1. Why Onboarding Is Its Own Discipline

**The central problem** (s005, ch.7; s014):

Games teach players an entirely new set of rules, controls, and systems that don't exist in the real world. The player arrives knowing nothing. Every mechanic must be communicated, every control internalized, every system revealed — without frustrating the player, without breaking the fiction, and without breaking the momentum of the game.

Poor onboarding is one of the most common reasons good games fail commercially. The player's first session is the make-or-break moment:
- **Steam:** refund window after 2 hours means players who bounce in the first session are lost forever
- **F2P:** players who have invested zero money make their retention decision in the first session (s017)
- **Party games:** if the host can't explain the rules in 90 seconds at the party, the game doesn't get played

**Hodent** (s014, ch.5) frames the problem cognitively:
> *"New information enters through short-term memory (7±2 items) and working memory (3–4 active items). It only reaches long-term memory through repeated practice. Tutorial information that isn't immediately practiced is gone within minutes."*

The practical consequence: you can't *tell* players the rules and expect them to remember. They must *do* in order to learn.

---

## 2. The Forgetting Curve

**Ebbinghaus's forgetting curve** (s014, ch.5): information not revisited is lost rapidly. Without reinforcement:
- 20 minutes after learning: ~60% retained
- 1 hour after learning: ~45% retained
- 24 hours: ~30% retained
- 1 week: ~10% retained

**Design implication for tutorials:**
- A tutorial that introduces 10 mechanics in sequence produces a player who remembers the last 2–3 and has forgotten the first 7
- Tutorial information must be **practiced immediately** after introduction — not just shown
- Complex mechanics should be **re-introduced** at the moment they're first needed in real play, not front-loaded in a tutorial section

**Spaced repetition** (s014): the most effective learning technique involves revisiting information at increasing intervals. In game design terms: introduce a mechanic, let the player practice it in a safe context, increase the complexity, revisit in a harder context, let the player demonstrate mastery. Zelda dungeon design (s005, ch.12) implements this exactly: introduce the dungeon item in a simple context, then progressively require more sophisticated use.

---

## 3. Implicit vs. Explicit Tutorials

**The spectrum:**

| Approach | How it works | Advantages | Disadvantages |
|---|---|---|---|
| **Pure explicit** | Text screen explains controls and rules | Comprehensive; nothing missed | Cognitive overload; not practiced; skipped by experienced players |
| **Tutorial level** | Separate guided level teaching basics | Controlled; low stakes | Breaks immersion; forgotten by time real play begins |
| **Contextual prompts** | UI hints appear when relevant context occurs | Just-in-time; less forgetting | Can feel intrusive; fail if player's attention is elsewhere |
| **Teaching through design** | Level geometry and enemy placement teach without words | Immersive; practiced immediately | Requires more design effort; subtle mechanics may be missed |
| **"Let me fail" design** | Player learns by doing wrong and seeing consequences | Deep encoding; intrinsic motivation | Requires forgiving failure states; can be frustrating |

**The best onboarding combines methods:** explicit for critical information that can't be missed (control scheme, core objective), implicit/design-led for mechanics that can be discovered organically.

**Kremers** (s012, ch.2) on teaching through level design:

> *"Show before ask. The player encounters the mechanic at low stakes before being required to use it. The environment teaches through implication."*

**Methods:**
- **Show before ask** — player observes the mechanic working before they must execute it
- **Environmental storytelling** — a dead character next to an enemy teaches that enemy is dangerous
- **Signifiers** (Norman, s015) — glowing edges, button prompts, visual affordances that communicate what's interactable

---

## 4. Progressive Disclosure

**The principle** (s006, ch.12–13; s014): reveal information and complexity incrementally. Don't front-load everything; introduce each new mechanic only when the player needs it.

**Adams' challenge hierarchy** (s006, ch.13) provides the structure:
1. Core mechanic (the single thing that defines the game) — teach first
2. Basic challenge (the simplest expression of the core mechanic) — teach second
3. Compound challenges (combinations of core mechanics) — teach as player demonstrates readiness
4. Advanced challenges (expert expressions) — discover organically or through optional content

**Cognitive load stages** (s014, ch.6; Sweller):
- **New player state:** all working memory occupied by controls, rules, and spatial orientation. No capacity for strategic thinking.
- **Intermediate state:** controls approaching procedural LTM; some working memory freed for strategy.
- **Expert state:** all basics in LTM; full working memory available for high-level decision-making.

**Design rule:** don't introduce strategic depth until the player has proceduralized the controls. Teaching resource management before the player can aim creates overload. Timing of complexity introduction should match cognitive load capacity.

**The "build the toy first" principle** (s005, Lens #15): make the core interaction feel satisfying *before* adding any game structure. If the fundamental activity (jumping, shooting, driving) isn't immediately enjoyable as a toy, no progression system or tutorial will fix it.

---

## 5. The First Win

**Schell** (s005, ch.9): Maslow's hierarchy applied to onboarding — the player's first-session need is **competence**. They must feel effective before they'll engage further.

**The first win design principle:** engineer an early success that:
- Requires some real skill (so it feels earned, not given)
- Is achievable by almost everyone within 3–5 minutes
- Produces a strong positive feedback response (audio, visual, progress indicator)
- Sets up the desire to continue

**F2P onboarding requirements** (s017):
- **Immediate value:** genuinely fun within 60 seconds
- **Early win:** an achievable, satisfying win in the first session
- **Hook investment:** something to come back for before the session ends

**Schell's progressive difficulty principle** (s005, ch.11, Type 2 Challenge):
> *"The first level or two should be very simple — the player is already challenged trying to understand the controls and goals."*

Designing the tutorial as if the player is already competent produces instant frustration. The first challenge should be trivially easy by the standard of the game — its purpose is to give the player the *feeling* of competence while teaching the basic mechanic.

---

## 6. The 90-Second Rule (Party Games)

In a party context, onboarding has a hard time constraint. The host must explain the game out loud, to a mixed-skill group, while food is being eaten. The game is not played if this takes more than 90 seconds.

**Design principles for party game onboarding:**

1. **One-sentence rule** — the core mechanic must be communicable in a single sentence.
2. **Learn by dying** — the first session IS the tutorial; players learn by experiencing consequences
3. **Forgiving first round** — score doesn't count, or penalties are reduced, in round 1
4. **Controls self-teach** — button prompts visible in-game; controller layout displayed on screen; no manual required
5. **Spectators as teachers** — experienced players watching teach newcomers naturally; design so observation is educational

---

## 7. Tutorial Anti-Patterns

**Common failures and their fixes:**

### The Tutorial Wall
The game halts for a series of tutorial popups before the player can do anything. **Fix:** weave teaching into early gameplay — the player always has agency.

### The Info Dump
All mechanics are explained at once before the first challenge. **Fix:** just-in-time disclosure — introduce each mechanic only when the player first needs it.

### Tutorial ≠ Game
The tutorial uses different visuals, enemies, or contexts than real gameplay. Skills don't transfer. **Fix:** tutorial IS the first level of the game; contexts are identical.

### The Tutorial Prison
The player cannot skip or speed through the tutorial even on second playthrough. **Fix:** make tutorial skippable after first completion; store completion status.

### Popups During Action
Tutorial hints appear during intense gameplay moments when the player's attention is entirely consumed by avoiding death. (Hodent, s014, ch.6 — inattentional blindness). **Fix:** deliver tutorial information during calm/safe moments; never during high-action sequences.

### The Wall of Text
Tutorial information presented as paragraphs of text rather than interactive demonstration. **Fix:** one mechanic at a time; demonstrate immediately; require practice before moving on.

---

## 8. Schell's Scaffolding Principle (Pyramid Design)

**Lens #51 — The Pyramid** (s005, ch.12):
> *"Does challenge start simple and build to complexity? Is the difficulty curve gradual?"*

The scaffold structure:
1. Introduce mechanic in isolation (simple context, no distractions)
2. Introduce a complication to the mechanic (the mechanic must interact with something else)
3. Require the player to combine the mechanic with a previously learned mechanic
4. Require the mechanic in a high-pressure situation

Zelda dungeon design is the purest implementation: the dungeon item is introduced in a trivial context (solve a simple door), then required in a moderate context (navigate with the item), then required in a complex context (the boss fight requires mastery of the item).

This same scaffold applies to any mechanic: movement, combat, puzzle-solving, resource management, social interaction.

---

## 9. Accessibility in Onboarding

Onboarding must account for diverse player profiles:

**Variable prior knowledge:** experienced gamers skip over what's obvious; newcomers need everything explained. Solutions: skip buttons, contextual hints that appear only when a player seems stuck, difficulty modes that reduce complexity during onboarding.

**Variable cognitive load capacity:** some players have less working memory available due to age, disability, or cognitive differences. Solutions: extra time on information screens, audio narration alongside text, option to repeat tutorials, reduced simultaneous demands.

**Varied learning styles:** some players learn by reading, others by watching, others by doing. Solutions: multimodal tutorials (show + tell + do), optional extended tutorials for "show me everything" players.

---

## 10. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Tutorial information not immediately practiced is lost (forgetting curve) | s014 |
| Introduce mechanics only when immediately needed (progressive disclosure) | s006, s012, s014 |
| The first win must feel earned, not given — competence is the first-session need | s005, s014 |
| Show before ask — observe before execute | s012 |
| Never present tutorials during high-attention gameplay sequences | s014 |
| Party game onboarding must work in 90 seconds explained out loud | practical synthesis |
| The tutorial should be the first level of the game, not a separate space | s012, s008 |

---

