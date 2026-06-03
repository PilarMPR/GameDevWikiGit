# Narrative, World & Characters

> **What this is:** Everything the canon says about storytelling in games — the story/game tension, embedded vs. emergent narrative, world-building principles, character design, and indirect control through narrative. Aggregated across s005, s013, s008, s002, s012, s010.

---

## 1. The Core Tension: Story vs. Game

**Schell** (s005, ch.15) opens with the wave-particle analogy:

> *"Story and gameplay, two age-old enterprises with very different sets of rules, show a strange duality. Storytellers are now faced with a medium where they cannot be certain what path their story will take."*

The fundamental conflict:
- **Stories** want predetermined meaning — the author controls what happens, in what order, to what emotional effect
- **Games** want player agency — the player's choices determine what happens

These are structurally opposed. Single-player computer games combined both for the first time, and the field has been working out the implications ever since.

**The myth of passive entertainment** (s005): non-interactive stories are not passive. A well-told story — whether read, watched, or played — compels the audience to predict, question, and feel. The difference is not *active vs. passive* but *can the audience act on their decisions?*

**Design implication:** game designers should learn from traditional storytelling. The principles of narrative structure (setup, conflict, escalation, climax, resolution), character motivation, thematic resonance, and interest curves all apply to games. Dismissing traditional storytelling as "not applicable" is a strategic error.

---

## 2. Three Narrative Approaches

### String of Pearls

A linear, authored story is presented, with gameplay as the string connecting story moments (pearls). The player has agency within gameplay sections but the narrative path is predetermined.

**Used by:** most cinematic action games — *Uncharted*, *The Last of Us*, *God of War*, *Spider-Man*.

**Advantages:**
- Strong narrative control; reliable pacing
- Cinematic quality; guaranteed emotional beats
- Works with the interest curve — designer controls timing

**Disadvantages:**
- Player choice has no narrative impact
- Replay reveals the strings (players feel the rails on second playthrough)

**The 99% solution** (s005): together with the story machine, this accounts for essentially all successful interactive narratives. Everything in between is a partially-solved problem.

### Story Machine

The game's mechanics generate narrative as a byproduct of play. No authored story exists; the player's actions produce story-like sequences that they narrate to themselves and others.

**Used by:** *Dwarf Fortress*, *RimWorld*, *Crusader Kings III*, *Minecraft*, *No Man's Sky*.

**Advantages:**
- Infinite narrative variety; each playthrough is unique
- Deep player investment — "their" story
- Scales without authoring cost

**Disadvantages:**
- No narrative coherence guaranteed; absurdity emerges
- The best emergent stories are often unrepeatable
- Requires systemic depth to generate meaningful events (not just noise)

**Lens #65 — Story Machine questions** (s005): Do players have choices about how to achieve goals that produce different stories? Can different types of conflict arise? Can players personalize characters and settings? Do the rules lead to stories with good interest curves? Is there someone to tell their story to who cares?

### Branching / Choice-Based

The player makes explicit choices that affect the story's direction. The designer authors multiple possible branches.

**Used by:** *Mass Effect*, *Disco Elysium*, *Planescape: Torment*, visual novels.

**Advantages:**
- Player agency feels directly narratively meaningful
- Choice moments create emotional investment

**Disadvantages:**
- Combinatorial explosion: 3 choices per decision × 10 decisions deep = 88,573 possible outcomes. At 20 deep: 5.2 billion. Impossible to author fully.
- The standard workaround — funneling branches back together — produces the "illusion of choice" problem. Players feel the seams.

### The five structural problems (Schell, s005, ch.15)

Why the "fully interactive story" dream hasn't arrived:

1. **Good stories have unity.** The wretchedness of Cinderella's situation is designed for her escape to be satisfying. A story with twenty endings doesn't have a beginning that's the perfect beginning for each.
2. **The combinatorial explosion.** The math is impossible at author-scale.
3. **Multiple endings, one beginning.** A perfect beginning creates one perfect ending.
4. **Game actions undermine story.** Players can die and retry; they can exploit mechanics; they can play a scene differently twice.
5. **Dramatic control is the storyteller's primary tool.** Games give that control to the player. More freedom = less dramatic control. This isn't solvable — it's the nature of the medium.

---

## 3. Embedded vs. Emergent Narrative (Salen & Zimmerman, s013)

**Embedded narrative:** the pre-authored story elements created by the designer — cutscenes, dialogue, environmental storytelling, worldbuilding. The designer controls this.

**Emergent narrative:** stories that arise from gameplay itself — the player's sequence of choices and experiences that form a narrative in their mind. The designer *enables* but does not *author* this.

Best narrative games work at both levels simultaneously:
- Strong embedded narrative gives context, motivation, and emotional stakes
- Strong emergent narrative makes player choices feel meaningful and personal
- Both levels reinforce each other: embedded story motivates the player to make choices that produce good emergent narratives

**Procedural rhetoric** (Fernández-Vara, s010, citing Bogost): games make arguments through their rules, not just their representations. A game where economic growth always brings happiness makes an implicit claim about economics. A game where ecological balance leads to prosperity argues something about environmental systems. Rules carry meaning — this is narrative operating at the mechanic level.

---

## 4. Theme — The Narrative Foundation

**Schell** (s005, ch.5) argues strongly that world design should be driven by **theme** — the core statement the game is making:

> *"Theme is not the story (what happens) but the meaning behind it (what it's about)."*

When theme drives world design, the world doesn't just *hold* the story — it *is* the argument the story is making. Players experience the theme spatially and procedurally, not just narratively.

**Two steps:**
1. Figure out your theme
2. Use every means possible to reinforce it — art, audio, mechanics, environment, characters, rules

**Theme as decision filter:** if an element reinforces the theme, it stays; if not, it goes. This turns every design decision from a debate into a check against a clear criterion.

**Most themes are experience-based** (s005): not "I want to say X about the world" but "I want players to feel Y." The *Pirates of the Caribbean* VR case — the theme was "the fantasy of *being* a pirate," and everything from the ship's-wheel controller to the AC vents blowing as sea breeze served that single experiential theme.

---

## 5. World-Building

### What a game world does (s005, ch.17; s012, ch.13)

A game world serves five simultaneous functions:
1. **Contextualizes mechanics** — a sword attack means something different in a medieval siege than in an abstract game
2. **Houses narrative** — story only works within a consistent world; inconsistencies break immersion
3. **Motivates exploration** — an interesting world gives the player reasons to go beyond the next corner
4. **Encodes theme** — the visual and structural design embodies the game's thematic argument spatially
5. **Enables imagination** — a well-designed world gives enough cues for players to fill in the rest themselves

### Consistency as foundation (s005, ch.17)

Players accept impossible worlds (dragons exist, magic works) without hesitation — but they are disturbed by inconsistencies *within* a world's own logic.

> *"The question is not 'is this realistic?' but 'does this follow the rules this world has established?'"*

Players build mental models of world-rules. Violations feel like betrayal. If fire is dangerous, fire must always be dangerous (or the exception must be explained). If locked doors can be picked, all locked doors should be pickable (or the exceptions clearly marked).

**Design rule:** before adding any world element, ask "does this fit the rules I've already established?" If not, either don't add it or revise the rules explicitly and communicate the change.

### Environmental storytelling (s012, ch.12; s005; s003)

The world tells story through props, damage, and layout — without dialogue or cutscenes:

- **What has happened** — damage, detritus, debris. A burned village says something about what preceded the player.
- **Who lives here** — a tidy, systematic arrangement of objects suggests one kind of character; a chaotic, defensive barricade suggests another.
- **What is valued** — most prominent elements signal values. A throne room tells you about power; a bare cell tells you about deprivation.
- **What is happening now** — active elements (fires still burning, enemies mid-patrol, machinery running) make the world feel independent of the player.

> *"The environment tells the story before the player arrives and after they leave."* (s012 paraphrased)

**Key principle:** don't interrupt play to deliver story. Environmental narrative keeps players in the magic circle while advancing the story. Tutorial popups and expositional cutscenes interrupt; environmental storytelling doesn't.

### World structure

| Structure | Description | Design challenge |
|---|---|---|
| **Closed world** | Bounded, fully authored | Make the bounded space feel alive and sufficient |
| **Open world** | Expansive, player-generated paths | Ensure density; avoid "empty world" syndrome |
| **Biome/region design** | Distinct areas with visual + mechanical identity | Navigational orientation + tonal + mechanical variety |
| **Vertical layers** | Sky/surface/underground conventions | Exploit convention-based indirect control |

---

## 6. Characters

### Player character: projection, not empathy (s005, ch.9)

In film and literature, audiences experience empathy — they feel *for* a character who is other. In games, the relationship is different:

> *"The player is not just watching the character — the player IS the character. The player is making the decisions. This projection is deeper than empathy; the player literally embodies the character's agency."*

Consequences:
- Player character deaths feel personal, not observational
- Player character failures feel shameful, not sympathetic
- Player character growth feels rewarding, not vicarious

**Design implication:** player characters must be designed not just as characters (with their own personality and arc) but as **avatars for player projection**. The more clearly the player can project themselves into the character, the stronger the engagement.

### Silent vs. voiced protagonist

| Approach | Characteristics | Best for |
|---|---|---|
| **Silent protagonist** (Link, Gordon Freeman) | Maximum projection; blank slate | Player-choice-centered narrative; long play sessions |
| **Voiced/characterized** (Geralt, Kratos, Ellie) | Rich narrative potential; specific personality | Story-driven games; authored emotional arcs |

Neither is universally superior. Silent = broader projection, weaker narrative arc. Voiced = richer story, narrower identification. Align the choice with the game's narrative goals.

### NPC design principles (s005, ch.18; s006)

NPCs serve four functions:
1. **Narrative delivery** — quests, backstory, worldbuilding, exposition
2. **Indirect control** — guiding player attention and movement (s005, ch.16)
3. **Emotional texture** — making the world feel inhabited; players respond emotionally to characters they encounter repeatedly
4. **Mechanical challenge** — enemy AI as gameplay mechanic

**Believability, not realism** (s005): NPCs don't need to simulate fully — they need to be consistent with the world's logic and emotionally resonant. The threshold is set by genre conventions.

**Consistency over complexity** (s005, ch.18): an NPC who always behaves consistently within their defined character is more believable than one with many behaviors that occasionally contradict each other. Simpler but consistent beats complex but contradictory.

### The empathy mechanism (s005, ch.9)

Humans project personality onto any agent perceived to have intentions — even abstract shapes (Heider & Simmel experiment). In games:

- **Large eyes** → vulnerability → protective instinct (babies, Pikmin, Yoshi)
- **Symmetrical faces** → trustworthiness and health
- **Expressive animation** → communicates emotional state instantly, often overriding verbal content
- **Consistent motivation** → makes agents feel like they have goals, not like props

> *"We can project emotional life onto any agent we perceive to have intentions. The cost of creating a relatable character is lower than intuition suggests."* (s005, ch.9 paraphrased)

---

## 7. Story and Game Design Integration

### Five principles for integration (s005; s012)

1. **Theme before story** — establish the emotional/thematic core first; let story and mechanics both serve it
2. **Show story through play** — deliver narrative through gameplay moments, not just cutscenes. Story *felt* through interaction resonates more deeply than story *watched*.
3. **Match mechanical stakes to narrative stakes** — if the story says something is at risk, the mechanics should make the player feel that risk
4. **Never interrupt play for story** — deliver story beats through natural pauses (level completion, safe rooms, exploration) not during active gameplay
5. **Give the player narrative ownership** — let them feel their choices shaped the story, even when major beats are authored

### Ludonarrative dissonance

The conflict when mechanics and narrative contradict each other:

- *Bioshock:* story says "you have no choice"; mechanics give full agency
- Many violent games: story frames protagonist as reluctant hero; mechanics reward gratuitous violence

Ludonarrative dissonance breaks engagement by exposing the constructed nature of the experience. **Fix:** ensure the game's mechanics reinforce rather than contradict its narrative claims. A story that says the protagonist is fragile should make cautious play rewarding and reckless play costly.

---

## 8. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Story and game are structurally opposed; design manages the tension | s005, s013 |
| Traditional storytelling techniques fully apply to games | s005 |
| Emergent and embedded narrative should reinforce each other | s013 |
| Theme is the most powerful decision filter in design | s005 |
| World consistency is non-negotiable; players notice and are disturbed by violations | s005 |
| Environmental storytelling keeps players in the magic circle while advancing the story | s012, s005, s003 |
| Player characters require projection space, not just personality | s005 |
| NPC consistency beats complexity | s005 |
| Rules carry meaning — games make arguments through mechanics | s010, s002 |

---

## 9. Hot Potato — Narrative Implications

| Decision | Rationale |
|---|---|
| Strong visual character identity per player | Projection + readability; players need to feel they're a specific person, not an avatar |
| "Party chaos" theme drives all design | Theme as decision filter: does this mechanic reinforce chaotic, social, funny? |
| Tag mechanics have narrative weight | Becoming the Potato = narrative moment; losing = comedic, not tragic |
| Anti-camp mechanics coherent with theme | A game about chaos and trolling should mechanically punish passive play |
| Loss state as punchline, not punishment | Narrative framing of loss: the Potato cries. Funny failure keeps players in mood. |
| Environmental storytelling in arenas | Arenas should visually tell you "this is a playground for chaos" — bright, readable, toylike |

**Sources:** s005 (Schell) · s013 (Salen & Zimmerman) · s008 (Fullerton) · s002 (Anthropy & Clark) · s012 (Kremers) · s010 (Fernández-Vara)

**See also:** [story-narrative-approaches](../10-Library/notes/story-narrative-approaches.md) · [indirect-control-methods](../10-Library/notes/indirect-control-methods.md) · [world-building-principles](../10-Library/notes/world-building-principles.md) · [character-design-projection](../10-Library/notes/character-design-projection.md) · [Narrative](../00-Atlas/disciplines/Narrative.md)
