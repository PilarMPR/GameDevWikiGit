# Game Analysis: Hades (2020, Supergiant Games)

**Genre:** Roguelite action dungeon crawler · **Platform:** Multi · **Player count:** 1 · **Session length:** 30–90 min per run; 50–100+ hours total

**Why this game:** Hades is the definitive example of how to integrate narrative with a roguelite structure, and how to design meta-progression that feels rewarding without becoming mandatory. An essential reference for loop architecture and for how death/failure can be a narrative mechanic.

---

## Quick stats

| Property | Value | Relevance |
|----------|-------|-----------|
| Control complexity | Medium (weapon + dash + cast + call) | Combat feel reference |
| Session structure | 1 run = 30–90 min; fails gracefully | Loop architecture |
| Meta-progression | Permanent + run-specific; well-balanced | Progression systems |
| Narrative integration | Story progresses through *all* runs, including failed ones | Narrative through repetition |

---

## Formal Elements

| Element | Detail |
|---------|--------|
| **Players** | 1 |
| **Objectives** | Escape the Underworld; reach the surface; per-run: defeat 4 bosses |
| **Procedures** | Move, dash, attack, special, cast, summon; choose boons at shrines; spend resources |
| **Rules** | Death returns player to House of Hades; permanent progress (darkness, keys, gems) persists; boons reset each run |
| **Resources** | Darkness (permanent currency), keys (permanent unlocks), gems, diamonds (rare), boons (run-specific), heat (challenge modifier) |
| **Conflict** | Player vs. enemies (action combat); player vs. own improving skill |
| **Boundaries** | The Underworld levels (Tartarus, Asphodel, Elysium, Temple of Styx); the House of Hades as between-run hub |
| **Outcome** | Reach the surface (win condition); any run attempt progresses the narrative |

---

## MDA Analysis

### Mechanics
- **Roguelite run structure**: each run is a randomized sequence of rooms; death resets the run but not meta-progress
- **Boon system**: each run, Olympian gods offer boons that modify Zagreus's abilities. Boons create build diversity within a run; no boon carries over between runs.
- **Weapon variety**: 6 weapons with different move sets; each can be upgraded with different aspects (via story-unlocked upgrades). This creates lateral variety without vertical power tiers.
- **Pact of Punishment (Heat system)**: player-chosen difficulty modifiers that make runs harder for higher-tier rewards. Self-selected difficulty.
- **Keepsakes**: equippable items that confer run-starting bonuses; allow soft specialization toward preferred boon givers.

### Dynamics
- **The "last hit run" phenomenon**: many near-successful runs end at the final boss. The proximity to success (you almost escaped!) is itself a retention mechanism stronger than any explicit reward.
- **Build expression**: each run produces a different boon combination that creates a distinct playstyle. Players develop preferences and strategies for specific builds. This is meta-game knowledge that improves over time.
- **Narrative escalation across runs**: every conversation with NPCs in the House of Hades advances the story. Characters comment on your recent run, your progress, your relationship with them. The narrative is never locked behind success — it progresses through *engagement*, not *victory*.
- **The "Fated List" system**: optional objectives that give direction to runs and reward meta-knowledge (e.g., "escape using only Artemis boons").

### Aesthetics
- **Challenge** (primary): combat mastery; the improvement arc from first escape attempt to consistent clears
- **Narrative** (co-primary): character relationships, the Olympians' personalities, the story of Zagreus and his family — all delivered primarily through post-run conversations
- **Discovery** (strong): new boon combinations; story beats unlocked with characters; weapon aspects; hidden rooms
- **Expression** (secondary): the build-crafting dimension; choosing how to play each run

---

## Core loop diagram

```
Hub (House of Hades): conversations, upgrades, story
                    ↓
              Run begins
                    ↓
    [Room: enemies + optional shrine + choice boon]
                    ↓ (repeat ~30+ rooms)
              Boss encounter
                    ↓
    Success → next region → next boss → escape
    Death → return to Hub
                    ↓
    Conversation with NPCs (story advances regardless)
    Spend permanent resources (meta-progression)
                    ↓
    Next run begins (new boons, same permanent progress)
```

**Loop hierarchy:**
- Micro loop: room-to-room combat and choice (2–5 minutes)
- Session loop: full run (30–90 minutes)
- Meta loop: permanent character relationships and story arcs (50–100+ hours)

---

## Design highlights

### 1. Failure as narrative mechanism

Hades is the most elegant solution to the roguelite narrative problem: if the player dies and resets, how do you tell a coherent story?

The answer: **failure is diegetically motivated**. Zagreus is literally trying to escape the Underworld — and the Underworld pulls you back. Death is not a game mechanic overlaid on the narrative; it IS the narrative. Every return to the House of Hades advances the story. Characters have more to say. Relationships develop. The narrative progression is decoupled from run success.

> "The roguelite loop IS the story. Zagreus dies and comes back. That's the point." (Supergiant design intent)

This is the highest example of [[../../concepts/narrative/story-and-games]]' meaningful play principle: the game's core mechanic (die and return) is integrated into the narrative rather than contradicting it.

### 2. Meta-progression that feels rewarding without becoming mandatory

Hades balances two opposing risks:
- **Too much meta-progression**: new players feel weak; old players feel the game is solved
- **Too little meta-progression**: no sense of long-term improvement; the grinding feels pointless

The solution: meta-progression unlocks **options** (new weapons, new boon possibilities, new starting advantages) rather than **power** (strictly better stats). A player who has unlocked all meta-progression doesn't win more easily — they win more *interestingly*, with more build diversity available.

The Pact of Punishment (Heat system) ensures that advanced players who would otherwise have outgrown the challenge can always make it harder. The floor of difficulty doesn't rise with progression; the ceiling of difficulty is always available.

→ [[../../concepts/mechanics/progression-systems]] (unlock systems vs. power systems)

### 3. The boon system as run-level expression

Within a single run, Zagreus acquires boons that define his build. No two runs produce the same combination. The boon system creates lateral variety (many possible builds) without vertical variety (no build is strictly better — different builds excel in different situations).

This is asymmetric design without power tiers. The choice of boons is a meaningful decision (which god's powers to prioritize?) without a dominant strategy (any build can clear the game). This produces the Discovery aesthetic through mechanical exploration.

→ [[../../concepts/mechanics/core-mechanics]] (asymmetric design) · [[../../concepts/mechanics/game-balance]] (intransitive relationships)

### 4. The relationship system as retention engine

Hades has a relationship system with every NPC in the House of Hades. Gifting nectar and asphodels builds relationship levels; maxed relationships unlock "favor" quests that advance personal story arcs. Each relationship is a mini-narrative that progresses over many runs.

This system does what F2P retention loops often try to do through external rewards (daily missions, currencies): it gives players a reason to return *that emerges naturally from the game's content*. You return to find out what Thanatos will say. You return to complete Nyx's favor. The motivation is intrinsic (you care about these characters) rather than extrinsic (you need the daily reward).

→ [[../../concepts/player/motivation]] (intrinsic vs. extrinsic; SDT Relatedness) · [[../../concepts/mechanics/game-loops]] (relationship loops as outer loop)

### 5. Voice acting volume and session variability

Hades has over 21,000 lines of voiced dialogue, more than most RPGs three times its scope. The purpose is not to fill content — it is to ensure that each room transition in each run can have fresh dialogue that responds to the current run state (which weapon you're using, what bosses you've defeated, how long your current run has gone).

This means: in 50+ hours of play, you rarely hear the same dialogue twice. The game feels alive and responsive at a scale far beyond what its small team should be able to achieve — because the dialogue system is designed to be context-sensitive, not sequential.

---

## What Hades does well (extractable principles)

1. **Failure is the mechanic**: make death diegetically motivated; the game's structure IS the story
2. **Narrative advances through engagement, not victory**: don't gate story behind success
3. **Progression unlocks options, not power**: give players more to choose from, not stronger starting positions
4. **Self-selected difficulty**: the Heat system lets players choose their own challenge curve
5. **Intrinsic retention through character relationships**: players return for story, not daily rewards
6. **Lateral variety over vertical variety**: many builds, each viable — depth without dominant strategies

---

## Relevance to Hot Potato

- **Failure as fun**: Hades shows how death/failure can feel like part of the experience, not against it. The explosion in Hot Potato should feel like Hades' death — funny, consequence-bearing, but not punishing.
- **Run structure as session loop**: Hot Potato's best-of-5 structure is a micro version of Hades' run structure — each round resets, but the session builds toward a final result.
- **Lateral variety**: hot potato characters with different strengths (one holds longer, one passes faster, one explodes more dramatically) without power tiers mirror Hades' weapon variety.

---

## Related analyses

- [[celeste]] — difficulty and accessibility design
- [[smash-bros]] — character variety without power tiers
- [[portal-2]] — narrative through environment

## Sources

s001 ch.4, ch.7 (Sellers — loop hierarchy; outer loops) · s011 (MDA — aesthetics) · s005 ch.14 (Schell — interest curves; run as interest curve) · s016 (Koster — replayability through unexplored patterns) · s014 (Hodent — reward schedules; intrinsic motivation)
