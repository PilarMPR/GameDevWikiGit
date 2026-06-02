# Formal Elements of Games

The structural anatomy every game shares — the minimal set of components that make a game a game. Multiple authoritative sources converge here with slightly different lists. This is one of the strongest cross-source agreements in the wiki: all sources agree on what a game is *made of*, even if they disagree on emphasis or vocabulary.

---

## Why formal elements matter

Formal elements are the designer's vocabulary for decomposing a game into its constituent parts. Before you can design, balance, or analyze a game, you need a language for what it contains. The disagreements between lists reveal genuine theoretical disagreements about what is *structural* vs. what is *aesthetic* vs. what is *contextual*.

---

## The lists, side by side

### Fullerton — 8 formal + 5 dramatic elements (s008, ch.3)

Fullerton provides the most complete and widely-taught list:

**Formal elements** (the structural skeleton):
1. **Players** — who plays; how many; roles; interaction patterns
2. **Objectives** — what players are trying to achieve; the winning condition
3. **Procedures** — the actions players may take; the legal moves of the game
4. **Rules** — constraints on procedures; what is forbidden or required
5. **Resources** — things of value players control or acquire
6. **Conflict** — the opposition that makes objectives difficult (other players, environment, chance)
7. **Boundaries** — where the game world ends (the magic circle in structural terms)
8. **Outcome** — the terminal result; how the game resolves

**Dramatic elements** (the experiential layer, distinct from formal):
- Challenge (the felt difficulty)
- Play (the experiential quality)
- Premise (the narrative frame)
- Character (agents and roles)
- Story (how events are sequenced)

Fullerton's key move: **separating formal from dramatic**. The formal elements define *what* the game is structurally; the dramatic elements define *how it feels*. The same formal structure can carry different dramatic elements (chess has different dramatic feel as "war simulation" vs. as "pure abstract puzzle"). → [[../../narrative/story-and-games]]

### Macklin & Sharp — 6 basic elements (s009, ch.1)

A more streamlined list, focused on what is necessary and sufficient:

1. **Actions** — what the player does
2. **Goals** — what the player is trying to achieve
3. **Rules** — what constrains and enables actions
4. **Objects** — things in the game world that have meaning
5. **Playspace** — the world where the game occurs
6. **Players** — who plays

Macklin & Sharp collapse Fullerton's "procedures" + "conflict" + "resources" + "boundaries" into fewer categories. Their list is parsimonious — it's the minimum needed to define a game's formal identity.

### Salen & Zimmerman — core mechanic (s013, ch.23)

Rather than a list of elements, Salen & Zimmerman identify the **core mechanic** — the essential repeated action that defines the game's nature:

> "The core mechanic is the essential play activity players perform again and again in a game. It is the atom from which gameplay is built."

Every game has one repeated action that is more fundamental than any other — the swing in baseball, the movement in chess, the platformer jump, the inventory management in RPGs. This single repeated action, repeated thousands of times, is the game's formal identity.

Their approach is complementary to Fullerton's — the core mechanic is the central procedure in Fullerton's list. → [[../../mechanics/core-mechanics]]

### Schell — the elemental tetrad (s005, ch.4)

Schell takes a higher-level view, arguing that games have four elements that must reinforce each other:

- **Mechanics** — rules, goals, and the algorithms of the game
- **Story** — the sequence of events; the narrative
- **Aesthetics** — how the game looks, sounds, and feels
- **Technology** — the medium through which the game is implemented

The tetrad is not a decomposition of formal elements but a **design alignment tool**: for a game to succeed, all four must reinforce each other. A game where the aesthetic (dark horror) conflicts with the mechanics (brightly colored puzzle-solving) feels incoherent.

> ⭐ **Key distinction**: Schell's tetrad maps to MDA but is not identical. Schell's Mechanics ≈ MDA Mechanics. Schell's Aesthetics = the visual/audio *style*, not MDA's Aesthetics (emotional response). Schell's Technology is absent from MDA. → [[mda-framework]]

### Adams — challenges + actions (s006, ch.13–14)

Adams frames formal elements through the lens of **gameplay** — the player experience of engaging with the game:

- **Gameplay = challenges + actions**: what the player must accomplish (challenges) and what the player can do (actions)
- **Core mechanics** implement the challenges and actions through rules and algorithms

Adams' five types of core mechanics (the things that generate challenges):
1. Physics mechanics
2. Internal economy mechanics
3. Progression mechanics
4. Tactical maneuvering mechanics
5. Social interaction mechanics

Each type produces its own characteristic challenge type and formal element set. → [[../../mechanics/core-mechanics]]

### Anthropy & Clark — verbs and objects (s002)

The most minimal possible vocabulary:

- **Verbs** — what the player does (operative actions, the things the player can perform)
- **Objects** — things that exist in the game world (nouns that verbs act upon)

Anthropy & Clark argue these are the **atoms of game meaning**: every meaningful game action is a verb applied to an object. "Jump over the obstacle" (jump = verb, obstacle = object). "Collect the coins" (collect = verb, coins = object).

This vocabulary is particularly useful for **analyzing what a game is about** — the verbs of a game define its character. A game about "jumping, running, dodging" feels very different from a game about "managing, investing, trading" — even if their formal structures (objectives, rules, outcomes) could be identical.

---

## Synthesis: the convergent anatomy

Across all sources, a game contains:

| Component | Fullerton (s008) | Macklin & Sharp (s009) | Schell (s005) | Anthropy (s002) |
|-----------|------------------|------------------------|---------------|-----------------|
| Who plays | Players | Players | — | — |
| What to achieve | Objectives | Goals | Mechanics | — |
| Legal moves | Procedures | Actions | Mechanics | Verbs |
| Constraints | Rules | Rules | Mechanics | — |
| Things of value | Resources | Objects | — | Objects |
| Opposition | Conflict | — | — | — |
| Where | Boundaries | Playspace | Technology | — |
| Terminal state | Outcome | Goals | Mechanics | — |
| Experience layer | Dramatic elements | — | Story/Aesthetics | — |

**The irreducible core**: players act (verbs/procedures) on objects/resources, under rules, toward goals/outcomes, within boundaries. This is what every game shares.

---

## Formal elements and MDA (s011)

MDA's Mechanics layer = Fullerton's formal elements. The distinction:
- **MDA** gives the formal elements a causal role: mechanics → dynamics → aesthetics
- **Fullerton** gives the formal elements a design role: decompose the game into these parts to analyze, modify, and playtest each

They are complementary views of the same structural layer. → [[mda-framework]]

---

## Formal elements and game analysis (s010)

Fernández-Vara (s010) uses formal elements as a category in **game analysis** alongside representation (what the game depicts) and context (the social/cultural setting). Formal analysis of a game = cataloguing its formal elements and how they interact.

Game analysis that only addresses representation or context without addressing formal elements misses what makes games games — the mechanics, rules, and procedures are where the game's distinctive meaning is produced (procedural rhetoric). → [[meaningful-play]]

---

## Formal elements across game types

One value of having a formal elements vocabulary is comparing across game types:

| Game | Core mechanic | Key resource | Primary conflict |
|------|---------------|--------------|------------------|
| Chess | Move a piece | Control of squares | Opponent |
| Monopoly | Buy/rent property | Money | Opponent + chance |
| Tetris | Place a falling piece | Space/time | Environment |
| Minecraft | Place/remove blocks | Materials | Environment + creativity |
| Poker | Bet | Money/chips | Opponent + hidden information |

Same formal vocabulary; radically different experiences. The difference lies in how the formal elements are tuned — their values, interactions, and ratios — which is game design.

---

## Key concepts & cross-links

- [[mda-framework]] — MDA's Mechanics layer = formal elements
- [[systems-thinking]] — formal elements are the "parts" of the game system
- [[meaningful-play]] — formal elements are the structural prerequisites; meaningful play is what they produce
- [[magic-circle]] — the boundaries of the magic circle = formal element "boundaries"
- [[../../mechanics/core-mechanics]] — the design of formal elements in depth
- [[../../mechanics/game-balance]] — balancing = adjusting the formal elements until dynamics match aesthetic targets
- [[../../narrative/story-and-games]] — dramatic elements are the narrative layer atop the formal skeleton

## Sources

s008 ch.3 (Fullerton — 8 formal + 5 dramatic elements; playcentric design) · s009 ch.1 (Macklin & Sharp — 6 elements) · s005 ch.4 (Schell — elemental tetrad) · s006 ch.13–14 (Adams — challenges + actions + 5 mechanic types) · s002 (Anthropy & Clark — verbs and objects) · s013 ch.23 (Salen & Zimmerman — core mechanic) · s010 (Fernández-Vara — formal elements in game analysis) · s001 ch.8 (Sellers — parts/properties/behaviors/relationships)
