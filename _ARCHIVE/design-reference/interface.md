# Design Reference: Interface & UI

---

## Schell's Lenses (s005)

### Control & Interface (ch.13)
**Lens #53 — Control**
- When players use the interface, does it do what is expected?
- Is the interface intuitive or complex? Is that complexity justified?
- Do players feel they have strong influence over the outcome?

**Lens #54 — Physical Interface**
- What does the player pick up and touch? Is it physically satisfying?
- Does the mapping between physical input and game action feel natural?

**Lens #55 — Virtual Interface**
- Does the virtual interface give the player the information they need, when they need it?
- Does any part of the interface obscure the game world unnecessarily?
- Is the interface consistent — does the same action always produce the same result?
- Can the player learn the interface quickly, or is it confusing?

**Lens #56 — Transparency**
- Is the interface invisible when it's working well?
- When the player makes an error, does the interface communicate what went wrong clearly?
- Is the system state always visible to the player? Do they know what mode they're in?
- Are there any hidden states that would surprise the player?

**Lens #57 — Feedback**
(See feel-and-controls.md for full questions)
- Does every player action receive clear, immediate feedback?
- Is feedback informative (what happened) not just confirmatory (that something happened)?

**Lens #58 — Juiciness**
- Does every interaction with the interface feel satisfying and alive?

**Lens #59 — Channels and Dimensions**
- What information channels are available? (Visual, audio, haptic)
- Is critical information presented in at least two channels?
- Are any channels overloaded? Are any underused?

**Lens #60 — Modes**
- What modes does the interface have? Does the player always know which mode they're in?
- Is it easy to enter and exit each mode? Is the transition clear?
- Are there accidental mode transitions? How are they handled?

---

## Tips from Other Sources

### Norman: Six design principles for interfaces (s015)

**Affordances checklist:**
- Does every interactive element communicate that it can be interacted with?
- Are affordances visible? (Hidden affordances are wasted affordances)
- Are there anti-affordances (elements that clearly cannot be interacted with)?

**Signifiers checklist:**
- Does every interactive element communicate *how* to interact with it (not just *that* it can be interacted with)?
- Are signifiers consistent — does the same visual language mean the same thing throughout?
- Are signifiers appropriate to the platform? (Glows work on screen; physical affordances matter for controllers)

**Constraints checklist:**
- Do constraints prevent the player from making catastrophic errors?
- Are destructive actions (delete save, permanent choice) clearly differentiated?
- Do logical constraints flow naturally from the game's world rules?

**Mappings checklist:**
- Is there a natural mapping between input direction and effect direction?
- Are related actions grouped together on the controller/keyboard?
- Does the same input always perform the same function across contexts?

**Feedback checklist:**
- Does every action receive immediate confirmation?
- Is the system state always visible?
- When nothing happens (the player's action had no effect), is that communicated?

**Conceptual model checklist:**
- Can the player build an accurate mental model of the system from normal play?
- Are there any "gotchas" where the model breaks? (e.g., "I expected X but got Y")
- Is the system's behavior consistent enough to support a stable model?

### Hodent: Cognitive load management (s014)

**HUD design:**
- How many items does the HUD require the player to track simultaneously?
- Can less-critical information be hidden or faded until needed?
- Is critical information placed where the player's gaze is likely to be?
- Is there visual hierarchy — can the player tell at a glance which information is most important?

**Onboarding UI:**
- Is new information introduced one piece at a time?
- Does each tutorial element appear when the player first needs it, not before?
- Is information reinforced through repetition, or presented once and forgotten?
- Does the tutorial mirror the actual gameplay context?

**Menu design:**
- How many clicks/inputs are required to reach the most common actions?
- Is the current position in the menu hierarchy always clear?
- Are irreversible actions protected (confirmation dialogs, clear warnings)?

### Adams: Interface as player-centric communication (s006, ch.12)
- Does the interface communicate all information the player needs to make decisions?
- Is any critical information hidden or hard to find?
- Are UI elements scaled appropriately for the expected viewing distance?
- Does the interface design match the game's aesthetic tone?

### Kremers: Diegetic vs. non-diegetic decision (s012, ch.11)
- Would this information make more sense communicated through the game world (diegetic)?
- Does communicating this through the HUD (non-diegetic) break immersion in a way that matters for this game's tone?
- Is there a meta UI option (not in-world, but narratively justified) that would work better?

**For each HUD element:**
- Can the player play without this information visible?
- If yes, consider hiding it unless the player is in a state where it's relevant
- Is there a more immersive way to communicate the same information?
