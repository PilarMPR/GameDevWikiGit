# Design Reference: Feel & Controls

---

## Schell's Lenses (s005)

### The Toy (ch.7)
**Lens #15 — The Toy**
- Is my game fun to play with, even without a goal? Would it make a good toy?
- If not, can I find a way to make the core interaction more toy-like?
- Does the player want to pick it up and manipulate it?

### Controls & Interface Feel (ch.13)
**Lens #53 — Control**
- When players use the interface, does it do what they expect? If not, why not?
- Is the interface intuitive and easy to master, or is it complex?
- Do players feel they have strong influence over the outcome?
- Do players feel powerful? Can they feel more powerful somehow?

**Lens #54 — Physical Interface**
- What does the player pick up and touch? Can this be made more pleasing?
- How does the physical input map to actions in the game world? Can the mapping be more direct?
- What metaphor is used when mapping inputs to the game world?
- How does the player see, hear, and touch the game world? Is there a way to make the world more real in the player's imagination?

**Lens #55 — Virtual Interface**
- Does the virtual interface give the player the information they need?
- Does the interface feel like a natural extension of the game world?
- Does the interface ever get in the way of the player's experience?
- Is there any information the player needs that isn't being communicated?

### Feedback & Juiciness (ch.13)
**Lens #57 — Feedback**
- Does the game give clear feedback for every player action?
- Is the feedback immediate enough that the player can connect it to the action?
- Is there feedback for partial progress, not just completion?
- Is there both positive and negative feedback?
- Could I add more feedback without overwhelming the player?

**Lens #58 — Juiciness**
- Is my game "juicy" — does every interaction feel satisfying and alive?
- Are there small touches that reward the player for interacting even incidentally?
- Could any more elements be added that would make the game feel more alive?
- Does every action have a visual and audio response?

**Lens #59 — Channels and Dimensions**
- What channels of information does the player have? (Visual, audio, haptic, etc.)
- Am I using these channels thoughtfully and well?
- Are any channels overloaded (too much information) or underused?
- Is any critical information conveyed through only one channel? Could I add redundancy?

**Lens #60 — Modes**
- What modes does my game have? Does the player understand what mode they're in?
- Are there too many modes? Do modes make the player feel confused?
- Is it clear how to enter and exit each mode?
- Is the player ever in an unexpected mode?

---

## Tips from Other Sources

### Swink: 3 Building Blocks of Game Feel (s007)
Ask for each building block in your game:

**Real-time control:**
- When the player provides input, does the game respond within 240ms?
- Is the input-response relationship clear? Does it feel like the player is doing what they intend?
- Is there unnecessary latency in the chain from input → game logic → visual output?
- Does the input curve (linear/exponential) match the desired feel?

**Simulated space:**
- Does the game world have convincing physical properties (gravity, momentum, collision)?
- Does the avatar feel like it occupies real space and has real mass?
- Does the space respond to the player's presence in believable ways?

**Polish:**
- Are there anticipation animations before key actions?
- Are there follow-through animations after key actions?
- Do particle effects, sound, and screen shake reinforce each action's impact?
- Are there squash and stretch effects that give objects life?

### Swink: 6 Measurable Game Feel Components (s007)
Use these as a diagnostic checklist:
1. **Input**: Is every input acknowledged? Is there an input deadzone, and is it appropriate?
2. **Response**: Does the response match the player's intention? Is the mapping curve correct?
3. **Context**: Does the environment correctly respond to the player's presence and actions?
4. **Polish**: Are there appropriate visual/audio/haptic embellishments that enhance the feel?
5. **Metaphor**: Does the game feel analogous to a real-world experience? Is that analogy clear?
6. **Rules**: Do the rules of the simulation feel consistent and physical?

### Swink: Identity extension test (s007)
- Can the player lose themselves in the character? Do they stop thinking "I am pressing a button" and start thinking "I am running"?
- What breaks the identity extension? Latency? Unexpected responses? Visual disconnection?

### Norman: Mapping design checklist (s015)
- Is there a natural mapping between the input and its effect? (Stick left → character moves left)
- Are there any anti-natural mappings (input direction opposite to expected effect)?
- Are there modes where the same input has different effects? Are those modes clearly communicated?
- Can the player predict what will happen before they act?

### Norman: Feedback checklist (s015)
- Does every action produce a perceptible response?
- Is the feedback immediate (within 500ms)?
- Is the feedback informative — does it tell the player *what* happened, not just *that* something happened?
- Is the feedback proportional — does a significant action produce a more significant response?

### Hourences: Feel through composition (s003)
- Do moving elements in the level (fans, pendulums, creatures) add life to the space?
- Does the environment react to the player's passage (footprints, disturbed foliage, lighting changes)?
- Does the audio environment change based on the player's actions and location?

### Hodent: Sensory feedback for learning (s014)
- Is there multi-channel feedback for critical events (visual + audio at minimum)?
- Are feedback events associated closely enough in time with the actions that caused them?
- Does feedback help the player build an accurate mental model of the system's rules?
