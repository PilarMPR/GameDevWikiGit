# Multiplayer Systems

The design of games where multiple players interact with each other — the mechanics, dynamics, and social structures that emerge when more than one human is in the system simultaneously. Multiplayer is not a "mode" added to a single-player game; it is a fundamentally different design problem.

---

## Why multiplayer is different (s013, s001)

In single-player games, the designer controls all variables except the player's input. In multiplayer games, other players are uncontrollable variables with their own goals, skills, and intentions. This produces:

- **Asymmetric information** (players have different knowledge of the game state)
- **Social dynamics** (trust, deception, coordination, competition) that no single-player mechanic can produce
- **Emergent behavior** at the human level, not just the mechanical level
- **Infinite replayability** through the combinatorial space of human behavior

The systems thinking framing (Sellers s001): in multiplayer, the game+player system becomes a game+multiple-players system. The coupling between players IS a game mechanic — arguably the most powerful one available.

---

## Conflict types in multiplayer (s008 Fullerton, s013)

Formal elements analysis identifies several distinct conflict structures:

### Direct conflict (competitive)
Players act against each other directly. One player's success reduces another's. Zero-sum or nearly zero-sum.

Examples: chess, fighting games, most shooters, battle royale, Smash Bros.

Design challenge: balance across players, fairness perception, skill gap management.

### Indirect conflict (comparative)
Players compete but don't act directly on each other. Success is comparative: who achieves the goal faster or better?

Examples: racing games, score-based games, leaderboards, Tetris 99.

Design advantage: reduces the emotional intensity of being attacked directly. Better for casual audiences.

### Cooperative conflict (players vs. system)
All players work together against the game system. Success is collective; failure is collective.

Examples: Left 4 Dead, Overcooked, Portal 2 co-op, Pandemic.

Design challenge: free-rider problem (one player can coast while others carry); failure attribution (blaming a teammate destroys the cooperative spirit).

### Asymmetric conflict (players with different roles/powers)
Players have different abilities, win conditions, or information. The conflict arises from the asymmetry.

Examples: Among Us (Impostors vs. Crewmates), Town of Salem, Dead by Daylight (one vs. many), Battletoads vs. enemies.

Design challenge: balance between radically different experience types; ensuring neither side has a trivially dominant strategy.

### Mixed conflict (competitive + cooperative)
Players cooperate against a shared threat but also compete against each other. Alliance formation and betrayal are mechanics.

Examples: diplomacy games, Betrayal at House on the Hill, Fall Guys team events, Mario Party.

Design advantage: the most socially rich conflict type. Produces the most emergent social behavior. Also the hardest to balance.

---

## The social dynamics problem

### King of the hill / leader targeting
In competitive multiplayer, the emergent social behavior of "gang up on the leader" is a balancing loop. Players naturally cooperate against whoever is winning, preventing runaway dominance.

This is a free mechanic that designers get without building it — but it requires:
- Visible score/standing (players must know who the leader is)
- Accessible ability to target the leader
- Individual incentive to be the last to attack (don't attack too early; let others weaken the leader)

For Hot Potato: the player with the most points is a natural target. Design the stage and mechanic to support — not prevent — this social targeting.

### Trust and betrayal
In cooperative games, the free-rider problem and the possibility of betrayal (Among Us) create a social layer that mechanical challenge cannot replicate. Betrayal is only possible when trust is real — which requires actual cooperative stakes.

Designing for the trust-and-betrayal dynamic: ensure that genuine cooperation is required (neither player can succeed without the other) AND that betrayal is mechanically possible (even if unintended).

### Social pressure and blame
Multiplayer games create contexts where social pressure affects player behavior. "Don't mess up" in a co-op game produces performance anxiety that single-player cannot. "You were holding it" in Hot Potato creates good-natured blame that is the social punchline of the mechanic.

Design for appropriate blame: clear attribution of outcomes ("you were holding it when it exploded" is clear; "the potato glitched" is not) produces social moments. Unclear attribution produces frustration.

---

## Party game specific patterns

### The observable play requirement
In party games (4+ players, local play, shared screen), every player and spectator needs to be able to follow the game state without dedicated attention. This is a design constraint unique to party contexts.

Observable play requirements:
- **Single shared focal point**: all attention should converge on one thing at a time (the potato; the ball; the leader's position)
- **Player identification**: distinct colors, silhouettes, or markers so all players are always distinguishable even in chaos
- **State readability at distance**: health, score, and danger states visible from 2+ meters on a TV
- **Score and standings always visible**: spectators and waiting players must be able to follow without playing

### The short session requirement
Party games are embedded in social events — they must fit around conversations, food, drinks, and other activities. Sessions longer than 20–30 minutes (including onboarding) risk social rejection.

The design constraint: the game must provide a complete emotional arc within 15–20 minutes of actual play. This maps directly to pacing-and-flow's interest curve requirement: hook, build, climax, resolution, all within a socially acceptable time window.

### The asymmetric skill range
A casual party will have players with 100:1 skill ratios. A game that is skill-transparent (better players consistently win) will fail at a party unless there are explicit mechanisms to manage the gap.

Primary skill-gap solutions (see [[../../genres/party-brawler]] for full treatment):
1. **Catch-up mechanics**: advantages for trailing players
2. **Chaos injection**: items, environmental hazards, and random events that create variance no player can fully control
3. **Short rounds**: frequent resets prevent any single player's advantage from compounding
4. **The punchline mechanic**: when the loser's outcome is funny rather than merely punishing, the emotional stakes feel lower even if the game is competitive

---

## Technical considerations for networked multiplayer

### Input latency and game feel
Swink's 240ms boundary (s007) is the design target for single-player feel. Networked multiplayer adds latency on top of hardware latency:

- **Local area network (same room/router)**: 1–5ms additional latency; negligible for most games
- **Internet (competitive online)**: 30–100ms typical; significant for precision games; brawlers and party games are more tolerant than fighting games
- **Steam multiplayer**: Valve's Steam SDK provides matchmaking and P2P networking; peer-to-peer introduces variable latency depending on player locations

For Hot Potato on Steam:
- Aim for 16ms local latency (60fps tick rate minimum)
- Design netcode with input prediction and rollback for acceptable feel at 80–100ms
- Consider whether competitive online play is a design priority (local party is the core use case)

### UE5 multiplayer architecture
For Hot Potato specifically:
- Unreal's built-in replication system handles most of the networking
- The physics-based potato pass is the highest-risk networked element (physics replication is expensive)
- Consider a server-authoritative model for the potato's position to prevent desyncs
- Fast Replication (UE5.1+) reduces per-frame bandwidth for common objects

---

## Multiplayer design checklist

**For party games:**
- [ ] Is the game state observable by spectators without explanation?
- [ ] Can a novice player contribute meaningfully within 2 minutes?
- [ ] Does a skilled player's advantage cap out before the game becomes unfun for novices?
- [ ] Is the social punchline moment visible to all players simultaneously?
- [ ] Does the session fit in 20 minutes including onboarding?

**For competitive games:**
- [ ] Is the conflict type (direct/indirect/asymmetric) clear to all players?
- [ ] Is there a legible leader indicator so king-of-the-hill dynamics can emerge?
- [ ] Is the skill ceiling high enough that expert players stay engaged?
- [ ] Is the skill floor low enough that novices have genuine wins early?

**For cooperative games:**
- [ ] Is genuine cooperation required (not just parallel individual play)?
- [ ] Is the free-rider problem addressed?
- [ ] Is blame attribution clear when things go wrong?

---

## Key concepts & cross-links

- [[../../genres/party-brawler]] — party brawler specific patterns (skill gap, catch-up, observable play)
- [[../../analyses/smash-bros]] — asymmetric characters in competitive party play
- [[../../analyses/among-us]] — emergence from asymmetric information
- [[../../analyses/jackbox]] — social play with minimal mechanics
- [[../../concepts/player/player-types]] — managing Achievers/Socializers/Killers simultaneously
- [[../../concepts/mechanics/emergence]] — social dynamics as the highest form of emergence
- [[../../concepts/feel-and-controls/feedback-systems]] — feedback must serve all players simultaneously
- [[../../concepts/level-design/spatial-design]] — stage design for multiplayer conflict (sightlines, flanking routes)

## Sources

s013 ch.20 (Salen & Zimmerman — multiplayer game structures) · s008 (Fullerton — conflict types in formal elements) · s005 ch.11 (Schell — competitive, cooperative, competition vs. cooperation Lenses) · s001 ch.4 (Sellers — multiple players in the interactive loop) · s007 (Swink — input latency and networked feel) · s017 (F2P handbook — social retention mechanics)
