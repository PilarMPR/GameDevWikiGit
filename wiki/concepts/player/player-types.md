# Player Types

Taxonomies of how different people engage with and find value in games. Player-type models are design tools for audience analysis and feature prioritization — not boxes to categorize individual players, but lenses for understanding the range of motivations a game must address.

---

## Bartle's four types (s005, ch.8)

Richard Bartle's taxonomy, originating from MUD (multi-user dungeon) research, identifies four archetypes based on two axes: **acting vs. interacting** and **world vs. players**.

| Type | Primary motivation | Card suit |
|------|-------------------|-----------|
| **Achievers** | Achieve the game's goals; accumulate points, items, and status | ♦ Diamonds |
| **Explorers** | Discover the breadth of the game; understand its workings | ♠ Spades |
| **Socializers** | Relationships with other players; the social dimension | ♥ Hearts |
| **Killers** | Compete with and defeat other players; dominate | ♣ Clubs |

Bartle's spatial representation (s005, ch.8):
- **Achievers** act on the world (collecting, completing, mastering)
- **Explorers** interact with the world (probing, discovering, understanding)
- **Socializers** interact with players (connecting, supporting, communicating)
- **Killers** act on players (competing, defeating, disrupting)

### Design implications of each type

**Achievers** need:
- Clear, granular goals (quests, achievements, missions)
- Quantifiable progress (experience bars, percentages, scoreboards)
- Meaningful rewards for completing goals (items, titles, trophies)
- Completionist content (collectibles, 100% completion states)

**Explorers** need:
- Hidden content and secrets to discover
- Systems deep enough to repay investigation
- Lore and worldbuilding
- Tools for understanding the game's mechanics (debug modes, wikis)

**Socializers** need:
- Communication tools (chat, voice, emotes)
- Cooperative mechanics (group content, shared objectives)
- Social visibility (who played what, who your friends are, guilds)
- Spaces for non-gameplay interaction

**Killers** need:
- Competitive systems with clear winners and losers
- Meaningful stakes (ranked modes, permanent consequences)
- Skill differentiation (so victory feels earned)
- Leaderboards and public rankings

> ⭐ **Bartle's warning**: these types are population tendencies, not fixed individual identities. Most players are mixtures. Bartle himself notes the taxonomy has gaps and should not be used to rigidly classify people. Schell adds: "Bartle's taxonomies have gaps, and when misused can gloss over important nuances." (s005, ch.8)

---

## LeBlanc's 8 aesthetics as a player taxonomy (s011)

MDA's 8 aesthetics can be read as 8 motivational profiles — players who come to a game for different primary experiences:

| Aesthetic | What draws this player |
|-----------|----------------------|
| **Sensation** | Sensory pleasure: visual, audio, haptic experience |
| **Fantasy** | Escapism, role-playing, being someone else |
| **Narrative** | Story, drama, character arcs |
| **Challenge** | Mastery, competition, difficulty |
| **Fellowship** | Social connection, team play |
| **Discovery** | Exploration, secrets, novelty |
| **Expression** | Customization, creativity, self-expression |
| **Submission** | Relaxation, time-passing, low-stakes engagement |

The 8 aesthetics framework is more granular than Bartle and avoids the acting/world axes. A single player might be motivated by both Challenge and Fellowship simultaneously. This is more useful for feature design than Bartle. → [[../../theory/mda-framework]]

---

## Demographics and psychographics (s005, ch.8; s006)

### Demographics
Observable characteristics of the audience:
- **Age**: affects complexity tolerance, theme preference, play session length
- **Gender**: affects genre preference, social motivation weight, aesthetic preference (with heavy caveats — gender is a spectrum and these are population-level tendencies)
- **Gaming experience**: core gamer vs. casual player vs. non-gamer; affects onboarding tolerance, mechanic complexity, jargon familiarity

Schell's principle: demographic categories are useful for audience research but dangerous if used as design constraints. "If you're designing for women, don't design what you *think* women want — find out what the actual women in your audience want." (s005, ch.8)

### Psychographics
Psychological characteristics: values, interests, lifestyle, motivations. Harder to measure than demographics but more predictive of player behavior. Includes:
- Attitude toward competition (loves / tolerates / avoids)
- Social play preference (solo / co-op / competitive)
- Narrative engagement (story-first / gameplay-first / emergent narrative)
- Completionism tendency (explores everything / follows main path)

---

## BrainHex (s005 adjacent)

A later taxonomy (Nacke et al.) motivated by neurological reward types:
- **Seeker**: exploration and curiosity reward
- **Survivor**: threat avoidance and tension relief
- **Daredevil**: thrill of risk-taking
- **Mastermind**: problem-solving and optimization
- **Conqueror**: overcoming challenges through skill
- **Socializer**: social reward and connection
- **Achiever**: completion and collection reward

BrainHex maps more directly to neurochemical reward systems but is less widely used in industry than Bartle.

---

## Player types and game design (s005, s011, s001)

### Designing for multiple types
Most games serve multiple player types simultaneously. The design question is weighting:
- A game heavy on Achievement content and light on Social content will retain Achievers but lose Socializers quickly
- A game with rich narrative and light competitive systems serves Fantasy/Narrative players but not Killers

Mapping your game's features to player-type needs reveals gaps. If your feature list has nothing for Explorers, you're not serving that motivation.

### Player type shifts over lifecycle
Players don't have fixed types — they shift as they become more skilled and experienced:
- New players tend toward **Achievers** (want clear goals and progress feedback to feel competent)
- Mid-game players often become more **Explorers** (starting to probe the system's depth)
- Long-term players shift toward **Killers** or **Socializers** (having mastered the game, they compete or build community)

Designing for the full player lifecycle requires serving different type emphases at different stages. (s001, ch.4)

### Player types and F2P retention (s017)
F2P games consciously design for all four types because retention depends on serving the full range of motivations:
- **Achievers**: daily missions, battle pass tiers, collection systems
- **Explorers**: seasonal content, story updates, hidden secrets
- **Socializers**: guild systems, co-op events, friend features
- **Killers**: ranked modes, leaderboards, PvP content

---

## Key concepts & cross-links

- [[motivation]] — the psychological foundations behind player-type preferences
- [[player-psychology]] — perception, attention, and emotional response across player types
- [[../../theory/mda-framework]] — 8 aesthetics as player motivation taxonomy
- [[../../mechanics/game-loops]] — different loop types serve different player types
- [[../../business/free-to-play-design]] — F2P lifecycle designed around player-type retention

## Sources

s005 ch.8 (Schell — Bartle's four types, demographic/psychographic analysis) · s011 (MDA — 8 aesthetics as player motivation taxonomy) · s001 ch.4 (Sellers — player motivation in the context of the interactive loop) · s006 ch.12 (Adams — audience analysis, player demographics)
