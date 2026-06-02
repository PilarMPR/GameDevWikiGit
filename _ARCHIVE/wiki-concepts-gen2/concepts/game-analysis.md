# Game Analysis

How to **study and write about** existing games rigorously — the reading counterpart to the writing of design. From Clara Fernández-Vara's *Introduction to Game Analysis* (s010), the most comprehensive framework for systematic game criticism.

Game analysis matters for designers: the ability to analyze games critically — not just play them — is what lets you extract transferable principles and apply them to your own work. Every analysis page in this wiki (`wiki/analyses/`) uses this framework.

---

## Games as texts (s010, ch.1)

Fernández-Vara's central premise: **games are texts** in the semiotic sense — systems of signs that can be analyzed for meaning, form, and cultural context. This doesn't reduce games to literature; it means games, like all texts, can be studied with the analytical tools developed for cultural criticism.

Treating games as texts enables:
- Comparative analysis (how does this game compare to others in the genre?)
- Contextual analysis (what cultural moment produced this game?)
- Formal analysis (how do the rules produce meaning?)
- Critical analysis (what arguments does this game make about the world?)

The key difference from purely mechanical analysis: **games produce meaning**, not just mechanics. The same rule set in different contexts produces different meanings. Pong and a military drone simulator might share a mechanic structure; they produce radically different meanings.

---

## The three areas of analysis (s010, ch.3–5)

### Area 1: Context
Everything external to the game that shapes how it is made and received:

- **Production context**: development studio, team composition, development history, budget
- **Technological context**: platform constraints, engine capabilities, what was technically possible when it was made
- **Genre context**: what genre conventions does it follow or subvert?
- **Socio-historical context**: what cultural moment produced this game? What anxieties, fantasies, or debates does it reflect?
- **Economic context**: business model, market position, target audience
- **Media relations**: how does this game relate to other media (films, books, toys, earlier games)?

Context explains *why* a game is the way it is. A game's formal features often only make sense in context: the limited color palette of early Game Boy games is a technological constraint, not an aesthetic choice. The prevalence of military FPS games in the early 2000s reflects both technological capability and post-9/11 cultural anxieties.

### Area 2: Game overview
A high-level description of what the game is:

- **Players**: how many, what roles, cooperative/competitive structure
- **Rules and goals**: what defines success? What is the win/loss condition?
- **Game modes**: how do rules change across modes?
- **Mechanics**: the core repeated actions
- **Spaces**: functional and experiential spaces; map structures
- **Fictional world**: setting, characters, tone, lore
- **Gameplay experience**: what does it feel like to play? What aesthetic experiences does it offer?
- **Communities**: how do players talk about this game? What communities has it produced?

The overview gives readers who haven't played the game enough to understand the analysis. It also reveals assumptions: what you include and exclude in an overview reveals your analytical frame.

### Area 3: Formal elements
The deepest level — analyzing how the game's specific rules, structures, and representations produce meaning:

**Rules analysis:**
- **Diegetic rules** — rules that exist within the game world (laws of physics in a simulation)
- **Extradiegetic rules** — rules that exist outside the game world (winning conditions, lives, continues)
- The relationship between diegetic and extradiegetic rules reveals the game's stance on realism vs. abstraction

**Procedural rhetoric** (following Ian Bogost; cited in s010):
Games make arguments through their *procedures* — their rules and mechanics. The argument isn't stated; it's enacted. 
- A game where violence always solves problems argues that violence solves problems
- A city-builder where higher taxes lead to declining growth argues for low-tax economics
- A medical game where faster diagnosis produces better outcomes argues for the value of clinical decision-making

**Procedural rhetoric examples:**
- *SimCity* argues that Robert Moses-style top-down urban planning is effective (through its mechanics)
- *Papers, Please* argues that bureaucracy dehumanizes (through its mechanics)
- *September 12th* argues that military counter-terrorism tactics produce more terrorism (through its mechanics — unavoidable civilian casualties in every attack radicalize bystanders)

**Dynamics**: how do the mechanics play out over time? What patterns of behavior emerge? (Connects directly to MDA → [[../theory/mda-framework]])

**Point of view**: from what perspective does the player experience the game? First-person, third-person, omniscient, limited? This is not only a camera question but an ideological one — who does the player *identify with*?

**Control schemes**: what actions can the player take? What *can't* they do? The limits of player agency are as meaningful as its extent.

**Difficulty and balance**: how does the game calibrate challenge? Who can play it, and at what cost?

**Representation and identity**: how does the game represent gender, race, class, disability, and other identity categories? Are these representations consistent with the game's mechanics or in tension with them?

**Levels and choice design**: how is the game structured into levels or chapters? What choices does the player have, and what are the consequences of those choices?

---

## Methodology (s010, ch.2)

### Preparation
- **Source critically**: understand how and why you obtained the game (pirated? purchased? museum archive?)
- **Play critically**: play multiple times, with different strategies, attempting to find the boundaries of the system
- **Maintain critical distance**: enjoy the game, but also observe yourself enjoying it
- **Define "finished"**: a 100-hour RPG cannot be "fully analyzed" in one playthrough; define the scope of the analysis in advance

### The analysis itself
- **Document as you play**: take notes, screenshots, video captures
- **Play with specific analytical questions in mind** rather than playing to finish
- **Look for friction** — moments where the game's systems conflict with its fiction, or where the game's representation conflicts with its mechanics
- **Compare to similar games** — meaning emerges from contrast

### Writing
- **Be specific**: cite specific game states, specific design choices, specific mechanics — not vague impressions
- **Separate description from analysis**: first describe what the game does, then analyze what it means
- **Use the vocabulary**: procedural rhetoric, diegetic/extradiegetic, formal elements, MDA — this vocabulary exists to enable precise communication

---

## Procedural rhetoric in practice (s010; Bogost)

The most powerful concept in game analysis for designers — because it is the reverse of design:

**In design**: you choose mechanics; those mechanics create behaviors; those behaviors produce meanings.
**In analysis**: you observe meanings; you trace them back to behaviors; you identify the mechanics that produce them.

This bidirectionality means that procedural rhetoric is both an analytic tool (for studying existing games) and a design tool (for making games that argue something).

**The designer's use**: before finalizing mechanics, ask — what argument does this mechanic make? Is that the argument I want to make? Does it conflict with the narrative argument?

If your combat mechanic makes violence feel satisfying and consequence-free, your game is arguing that violence is satisfying and consequence-free — regardless of what the cutscenes say.

---

## Diegetic vs. extradiegetic rules (s010, s012)

This distinction applies to more than just rules — it applies to **all game elements**:

| Element | Diegetic | Extradiegetic |
|---------|----------|---------------|
| Rules | Laws of the game world (gravity, limited speech, social norms) | Win conditions, lives, continues, scoring |
| Sound | In-world sound (dialogue, ambient, footsteps) | Soundtrack, UI sounds |
| UI | Health represented as wounds on body, compass in world | Health bar, minimap in corner |
| Characters | NPCs, enemies | Tutorial guide who "breaks the fourth wall" |

The *ratio* of diegetic to extradiegetic elements is a design choice with aesthetic and meaning implications. Games with high diegetic ratios (Dwarf Fortress, detailed military simulations) feel more "serious" and simulation-like. Games with high extradiegetic ratios (classic arcade games, casual games) feel more "gamey" and abstracted. → [[../interface/ui-design]] (diegetic vs. non-diegetic UI)

---

## Game analysis and game design (across sources)

Game analysis is not just for critics — it is an essential designer skill:

- **Learning from others' designs**: systematic analysis extracts transferable principles; casual "played this" does not
- **Competitive analysis**: analyzing competitors reveals their design choices, and by extension, the players they're targeting and the experiences they're promising
- **Self-analysis**: applying the analytical framework to your own game reveals assumptions you didn't know you had

Schell's process of using lenses is a form of micro-analysis: each lens is an analytical question applied to a design-in-progress. Fullerton's playtesting analysis uses the formal elements framework to diagnose problems. MDA is an analytical framework applied both to existing games (analysis) and to new games (design).

---

## Related

[[../theory/formal-elements]] · [[../theory/meaningful-play]] · [[../theory/mda-framework]] · [[play-and-culture]] · [[../analyses/_index]]

## Sources

s010 (Fernández-Vara — Introduction to Game Analysis: games as texts; three-area framework; procedural rhetoric; diegetic/extradiegetic; methodology) · s013 (Salen & Zimmerman — formal/experiential/cultural schemas; games as systems) · s002 (Anthropy & Clark — verbs as meaningful; games as expressive medium) · s005 (Schell — Lenses as analytical tools) · s008 (Fullerton — formal elements as analytical vocabulary)
