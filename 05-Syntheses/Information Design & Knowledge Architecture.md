# Information Design & Knowledge Architecture

> **What this is:** Everything the canon says about information as a primary design lever — who knows what, when, how information is revealed, hidden information mechanics, the hierarchy of knowers, and information asymmetry as a game mechanic. Aggregated across s013, s005, s015, s014.

---

## 1. Information as a Primary Design Mechanic

**Salen & Zimmerman** (s013, ch.16–17) position information design as equally fundamental to mechanic design:

> *"Information is not just the background of play — it is a mechanic. What information players have access to, and when they receive it, fundamentally shapes the strategies available and the experience of play."*

**The design insight:** you can transform a game without changing any rule, resource, or mechanic — simply by changing *who knows what.* Draw poker and stud poker use the same hands, the same betting, the same chips — but completely different strategic experiences arise from the difference in information visibility.

**Norman's parallel** (s015): information design at the game level mirrors the design of feedback and conceptual models at the interface level. The Gulf of Evaluation (not knowing what happened) and the Gulf of Execution (not knowing what to do) are both information design failures. At the game level, these become strategic information failures.

---

## 2. The Hierarchy of Knowers

**Schell** (s005, ch.10, Mechanic 2 — Objects/Attributes/States) introduces the concept of the **hierarchy of knowers:**

```
OMNISCIENT LAYER (God/the game system)
  ↓ knows everything
GAME LAYER (what the software tracks)
  ↓ reveals to...
ALL PLAYERS (shared public information)
  ↓ + each player's...
INDIVIDUAL LAYER (private per-player information)
  + a game's...
HIDDEN LAYER (information no player can directly access)
```

**At each layer, the designer makes choices:**
- What does the game track that no player ever sees? (Hidden simulation)
- What information is public to everyone? (Shared state)
- What information does each player know privately? (Hidden information mechanics)
- What information no one knows? (True randomness, unrevealed outcomes)

**Design question:** for every piece of information in your game, ask: who knows this, and when?

---

## 3. Information State Types

**Salen & Zimmerman** (s013, ch.17) define the spectrum of information states:

### Perfect Information
All game state is visible to all players. No hidden information.

**Examples:** Chess, Go, tic-tac-toe. Both players can see the entire board; strategy is entirely about prediction and planning, not information gathering.

**Design properties:**
- Pure skill competition (no luck from hidden information)
- High analytical depth (every position fully analyzable)
- Can be psychologically exhausting (no "I didn't know about that" excuse)
- Favored in abstract strategy games

### Imperfect Information (Shared Hidden)
Some game state is hidden from *all* players — typically determined by randomness yet to be revealed.

**Examples:** Shuffled deck (no one knows next card), dice yet to be rolled, randomized loot drops. Information exists but is hidden from everyone equally.

**Design properties:**
- Creates uncertainty without unfairness (all players equally ignorant)
- Requires probabilistic reasoning rather than perfect prediction
- Reduces the ceiling on analytical depth
- Widely used in card games, board games with dice

### Asymmetric Information (Private per Player)
Different players have different information about the game state.

**Examples:** Poker (each player sees their own hand only), Among Us (Impostors know each other; Crewmates don't know who's an Impostor), trading games (you know your own resources but not others').

**Design properties:**
- Creates deception, bluffing, and information-gathering as mechanics
- The most socially complex information state
- Produces emergent narrative ("I suspected them from the beginning")
- The strategic challenge is *what to reveal, when, and how*

### Enchanted Information
A concept from Salen & Zimmerman (s013) — information that exists outside the game rules but which players must pretend not to know.

**Examples:** The "rules" of role-playing games that players know out-of-character but must not act on in-character. The meta-knowledge that "the final boss is always in the last room" — technically outside the game, but players know it.

**Design implication:** enchanted information represents the gap between what players know *as players* (metagame knowledge) and what their *characters* know. Games relying on suspension of this knowledge require trust and social contract.

---

## 4. Information Revelation as Mechanic Design

Information revelation is how the game controls *when* players learn things:

### Gradual Revelation
The game reveals information over time as players progress or explore.

**Purpose:** maintains curiosity and the desire to continue. Koster (s016) — information revelation sustains the pattern-learning signal. Each new piece of information is a new pattern to process.

**Applications:**
- Fog of war in strategy games (players explore to reveal)
- Story reveals (plot points withheld until earned)
- Mechanic reveals (later-game systems only accessible after mastering earlier ones)
- Skill trees (new options visible only after prerequisites)

### Partial Revelation
Players can see *that* something exists but not *what* it is until they interact with it.

**Examples:** unexplored rooms on a map (outline visible, contents hidden), locked items (item exists but type unknown), NPCs whose intentions are unclear.

**Purpose:** creates curiosity (s005, Lens #4) and risk/reward decisions (should I investigate this unknown thing?).

### Simultaneous Revelation
All players reveal information simultaneously, preventing any player from reacting to another's revelation.

**Examples:** Rock-paper-scissors reveal, simultaneous action in some board games, sealed bids in auctions.

**Purpose:** eliminates response timing advantages; creates dramatic tension of simultaneous reveal.

### Discovery Through Play
Information is never explicitly stated; players must infer it from behavioral patterns.

**Examples:** understanding enemy AI by watching its patterns, understanding economic supply/demand by experimenting with prices, understanding physics by testing the system.

**Purpose:** deepest form of learning (Koster, s016 — pattern acquisition through direct experience); creates the most satisfying "aha" moments; requires the most robust simulation.

---

## 5. Information Asymmetry as Core Mechanic

Games built around *information asymmetry* as their primary mechanic:

### Social Deduction (Among Us, Werewolf)
- Some players have private information others lack (who is the impostor/werewolf)
- Gameplay is entirely about information gathering (accusations, observations) and information protection (deception, misdirection)
- The fun = the social process of negotiating uncertain information under pressure
- Design requirement: the information asymmetry must create genuine uncertainty (if the informed players can always deceive perfectly, the game has no strategy; if the uninformed players can always detect deception, the same)

### Card Games with Private Hands (Poker, Bridge)
- Each player's hand is private; strategy involves inferring opponents' hands from their behavior
- Betting and bidding are information signals (you reveal something about your hand by how you bet)
- Bluffing = deliberate misinformation about your information state
- Design: the skill ceiling comes from reading information signals, not card mechanics alone

### Real-Time Strategy (Fog of War)
- The map exists but is only revealed as players explore
- Enemy positions are private to the enemy player
- Scouting is an explicit mechanic for gathering information
- Design: the information cost (time, units spent scouting) must be balanced against the information value (strategic advantage gained)

---

## 6. Information Overload and Cognitive Load

**Hodent** (s014, ch.6) and **Norman** (s015): the brain cannot process unlimited information simultaneously. Providing too much information is as bad as providing too little.

**Information overload symptoms:**
- Players focus on a subset of available information and ignore the rest
- Players make decisions based on incorrect or incomplete information
- Players feel overwhelmed and disengage
- Players ask "what should I be looking at?"

**Design principles for managing information:**
- **Priority hierarchy:** not all information is equally important; visually signal what matters most
- **Just-in-time delivery:** present information when the player needs it, not all at once
- **Progressive disclosure:** reveal information complexity as the player is ready for it
- **Redundancy for critical information:** critical state should be communicated in multiple channels (visual + audio + haptic)

---

## 7. Schell's States, Secrets, and Surprises

**Schell** (s005, ch.10, Lens #22 — Dynamic State):

> *"The question isn't just what information exists — it's what is known by the game only, all players, some players, or no one. Each of these is a design choice."*

**The grandmother who thinks the computer "cheats"** (s005): she feels cheated by AI card games that appear to know what cards are in her hand. She's experiencing **information asymmetry** — the AI has access to game-layer information that a human opponent would not. The designer must decide: is this the intended experience, or a fairness violation?

**Design question:** for every piece of information in the game: *should this be hidden, shared, or revealed? At what point? Under what conditions?*

**The drama of revelation** (s005, ch.10): making private information suddenly public creates drama. "The card is turned over" is one of the most emotionally powerful moments in card games — because the information that was private becomes public, changing everything.

---

## 8. Narrative Information Design

**Salen & Zimmerman** (s013, ch.25–26) on information in narrative:

**Embedded narrative** is revealed information — the designer controls when plot points, backstory, and character details are disclosed. Narrative information design asks:
- What does the player know at the start? (Establishes their knowledge baseline)
- What do they learn through play? (The revelation arc)
- What remains unknown at the end? (Deliberate ambiguity)
- What is the player NOT supposed to know until a specific moment? (The withhold)

**The withhold** — deliberately denying information the player wants — is the engine of narrative tension. Wanting to know what happens next is what drives engagement with narrative. Good information design withholds strategically, releasing information at moments of maximum impact.

---

## 9. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Information state is a design mechanic as powerful as resource design | s013 |
| Changing who knows what transforms a game without changing any rule | s013, s005 |
| Perfect information produces pure skill competition; asymmetric information adds social complexity | s013 |
| The hierarchy of knowers is an explicit design decision for every game state variable | s005 |
| Information overload is as bad as information deficit | s014, s015 |
| Revelation of information creates drama; withholding creates tension | s013, s005 |
| Discovery through play (inferred information) produces the deepest learning | s016 |

---

