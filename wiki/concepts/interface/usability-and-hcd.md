# Usability and Human-Centered Design

The discipline of designing systems that fit the cognitive capabilities and limitations of the people who use them. In games, usability is the foundation of playability: a mechanically excellent game is inaccessible if the player cannot figure out what to do, what happened, or what to try next.

**Primary source:** *The Design of Everyday Things* by Don Norman (s015) — the foundational text. Secondary: Hodent (s014), Adams (s006 ch.12), Swink (s007).

---

## Norman's six principles (s015)

Norman's six fundamental principles of good design:

### 1. Affordances
An **affordance** is a relationship between a physical object (or digital element) and an agent that enables a possible action. A button affords pressing; a slider affords dragging; a ledge at avatar-height affords grabbing.

Key insight: **affordances are relationships, not properties**. Whether an affordance exists depends on the capabilities of the agent and the properties of the object together. A staircase affords climbing to humans but not to dogs.

For designers: affordances exist whether or not they are perceivable. An unperceivable affordance (a lever hidden behind a wall) does not help the user. **Visibility is what makes affordances useful.**

### 2. Signifiers
Where affordances define what is possible, **signifiers** communicate what is possible and where action should happen. Signifiers are perceivable signals — visual, auditory, tactile.

Norman's critical distinction (revised in the 2013 edition): the word "affordance" had been misused to mean "signifier." He corrected this by introducing the term:
- **Affordance** = what can be done
- **Signifier** = where and how to do it

Examples in games:
- A glowing outline around an item → signifies it is collectible (communicates the affordance)
- A crumbling wall with a distinctive crack → signifies it can be broken (communicates the destructible affordance)
- Button prompts appearing above an enemy → signify available actions (communicate the execution affordance)

> "Signifiers are the most important addition to the new edition. Signifiers specify how people discover those possibilities: signifiers are signs, perceptible signals of what can be done." (s015)

### 3. Constraints
Constraints reduce the number of possible actions, guiding users toward correct behavior. Norman identifies four types:
- **Physical**: physical incompatibility prevents wrong actions (a key that only fits one lock)
- **Cultural**: conventions constrain interpretation (red means stop/danger across many contexts)
- **Semantic**: the meaning of the action constrains it (a game saving a village NPC — killing them makes no narrative sense)
- **Logical**: if all other pieces have clear places, only one option remains

In games: constraints guide the player toward intended interactions without explicit instruction. A door with a visible keyhole and no other hardware signifies it opens with a key and nothing else.

### 4. Mappings
A **mapping** describes the relationship between controls and their effects. Good mappings are **natural** — the control movement corresponds intuitively to the result.

Examples of good mappings:
- Moving a joystick left → character moves left
- Pushing a slider up → volume increases
- Moving the camera right → the view pans right

Natural mappings exploit spatial metaphors: steering wheels turn to control turning; throttle moves forward for acceleration. When mappings violate spatial intuition (e.g., inverted Y-axis controls), players must override their instincts and develop new reflexes.

**Game-specific mapping challenges**: complex games with many actions must map them to a limited set of inputs (controller buttons, keyboard keys). Good mapping clusters related actions, uses consistent patterns (the same button confirms across all contexts), and minimizes mode confusion (the player always knows which mode they're in and what each input does).

### 5. Feedback
**Feedback** is the communication of what happened in response to an action. Without feedback, the player cannot know whether their action succeeded, failed, or had an unintended effect.

Feedback properties:
- **Immediate**: feedback must occur quickly enough to be associated with the action that caused it. Delayed feedback breaks the causal link.
- **Informative**: feedback must communicate *what* happened, not just *that* something happened. A screen flash tells the player something happened; a health bar dropping tells the player they took damage.
- **Proportional**: the strength of the feedback should match the significance of the action.

Forms of feedback in games:
- Visual: animations, particle effects, UI changes, color shifts
- Audio: sound effects, voice lines, music changes
- Haptic: controller vibration, force feedback
- Diegetic: character reactions, world changes

→ [[feedback-systems]] for full treatment

### 6. Conceptual models
The **conceptual model** is the player's mental model of how the system works — their understanding of the rules, cause-effect relationships, and internal mechanics.

A **good conceptual model** is one that matches the actual system behavior closely enough that the player can predict what will happen before they act. This is the foundation of strategic decision-making.

**Model misalignment** is the root cause of most usability failures: the player does something that makes sense according to their model, but the system behaves differently because the model is wrong. The result is confusion, frustration, and the perception of unfairness.

Design for good conceptual models by:
- Making internal system logic externally visible (show how the economy works, show enemy health, show resources)
- Being consistent: if similar actions produce similar effects in one context, they should in all contexts
- Using familiar metaphors: leveraging existing mental models from reality or other games reduces learning time

---

## The gulfs of execution and evaluation (s015)

Norman's model of human interaction with systems involves crossing two gulfs:

### Gulf of execution
The gap between the user's intention and their ability to act on it. The user wants to do something but doesn't know what to do.

Occurs when:
- Available actions are not visible or signified
- The mapping between intention and action is non-obvious
- The player doesn't know what inputs are possible

### Gulf of evaluation
The gap between what the system produces and the user's ability to understand that output. The user does something but doesn't know what happened.

Occurs when:
- Feedback is absent, delayed, or unclear
- The outcome doesn't match the conceptual model (player doesn't understand why)
- System state is opaque (player can't tell what the current state is)

A well-designed system minimizes both gulfs: the player always knows what to do (execution) and always knows what their action produced (evaluation). Most usability problems in games trace to one of these two gulfs. (s015, ch.2)

---

## Human-Centered Design (HCD) process (s015)

Norman's HCD framework:
1. **Observe**: watch real users interact with the system. Don't assume; observe.
2. **Generate ideas**: use observations to generate design ideas
3. **Prototype**: build rapidly and cheaply
4. **Test**: get real users to test; watch what happens, don't ask what they think
5. **Iterate**: repeat from observe until the gulfs are closed

The HCD principle: "avoid specifying the problem as long as possible." The real problem is often different from what the designer assumes. Observations reveal the real problem; premature solutions miss it. (s015, ch.6)

This aligns with Fullerton's playcentric design (s008) and Schell's Rule of the Loop (s005) — iterative, observation-driven design is independently discovered across multiple domains.

---

## Hodent's game UX extension (s014)

Hodent extends Norman's principles with cognitive science specifically for games:
- **Perception constraints**: the player can only perceive what is in their visual field and what passes the brain's filtering. Design must work with, not against, visual attention.
- **Memory constraints**: new information must be presented within working memory limits; onboarding must use spaced repetition.
- **Mental model alignment**: the player's conceptual model is built from first experience. Early interactions define the model; contradictions later produce confusion disproportionate to their severity.
- **Learnability**: how quickly can a new player build an accurate mental model? Learnability is the usability metric most specific to games. (s014, ch.3–5)

---

## Usability in games vs. other software (s015, s014)

Games have unique usability properties:
- **Deliberate difficulty is acceptable**: a puzzle that's hard to solve is not a usability failure — it is the product. The question is whether the player can perceive the puzzle and attempt it, not whether they can solve it instantly.
- **Voluntary effort is expected**: game players expect to invest effort; other software users generally do not. What would be a usability failure in a banking app (requiring the user to figure out how to transfer money) may be a feature in an adventure game (requiring the player to figure out how to open the safe).
- **Engagement is a usability metric**: a game that is technically usable but not engaging has still failed. Usability in games includes emotional usability — does the interface feel good to use?

---

## Key concepts & cross-links

- [[ui-design]] — the specific practice of game UI: HUD, menus, information hierarchy
- [[feedback-systems]] — Norman's feedback principle expanded to full game feedback design
- [[../player/player-psychology]] — perception, memory, and attention as the cognitive substrate
- [[../../level-design/level-design]] — level design as spatial usability design
- [[../../narrative/indirect-control]] — affordances and signifiers as indirect control tools
- [[../../feel-and-controls/game-feel]] — the feel of controls as an embodied usability experience

## Sources

s015 (Norman — The Design of Everyday Things: 6 principles, gulfs of execution/evaluation, HCD process) · s014 (Hodent — cognitive science extended to game UX; perception/memory/attention constraints) · s005 ch.9 (Schell — mental models in the context of the four cognitive abilities) · s007 (Swink — game feel as sensory usability) · s006 ch.12 (Adams — player-centric design; camera and spatial navigation usability)
