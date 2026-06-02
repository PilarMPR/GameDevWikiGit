# 05-Syntheses — Cross-Source Topic Compendiums

Deep, multi-source treatments of practical design topics. Each document aggregates everything the full canon says about a subject — organized by sub-topic, not by book. The goal: read one document and know everything the library knows about that topic.

These are the layer above atomic notes and MOCs. Where atomic notes = one idea, and MOCs = navigation, **syntheses = working knowledge**.

---

## Documents

### Core Design (original 8)

| Document | Topics covered | HP relevance |
|---|---|---|
| [[Movement, Controls & Game Feel]] | Game feel, 3Cs, input mapping, movement physics, camera models, polish/juice, proprioception, tuning | Critical |
| [[Game Loops & Systems]] | Systems thinking, four loops, core/outer loops, mechanics taxonomy, emergence, feedback loops, MDA | Critical |
| [[Player Psychology, Motivation & Flow]] | Perception, memory, attention, fun theory, flow channel, Maslow, SDT, reward schedules, player types | Critical |
| [[Game Balance]] | Methods, transitive/intransitive, 12 Schell balance types, power curves, live balance | Critical |
| [[Level Design, Pacing & Indirect Control]] | Teaching through levels, spatial organization, sightlines, interest curves, tense/release, indirect control | High |
| [[Narrative, World & Characters]] | Story/game tension, embedded/emergent narrative, theme, world-building, character design | Medium |
| [[Iteration, Playtesting & Production]] | Iteration process, prototyping, playtest types, data collection, facilitation, documentation | High |
| [[Monetization, Retention & F2P]] | Revenue models, F2P arc, retention loops, pay-to-win vs. cosmetic, ethics | Medium |

### Expanded Coverage (12 additional)

| Document | Topics covered | HP relevance |
|---|---|---|
| [[Multiplayer & Social Design]] | Conflict architectures, party game patterns, competitive design, cooperative mechanics, social emergence, skill gap | Critical |
| [[Onboarding & Tutorial Design]] | FTUE, progressive disclosure, forgetting curve, first-win, implicit vs. explicit tutorials, 90-second party rule | Critical |
| [[Sound, Music & Audio Design]] | Audio as fastest feedback channel, music as indirect control, adaptive music, diegetic/non-diegetic, sound timing | Critical |
| [[UI, Interface & Information Design]] | Diegetic vs. non-diegetic UI, HUD hierarchy, menus, information asymmetry, cognitive load in UI | High |
| [[Visual & Aesthetic Design]] | Art direction, visual readability, color theory, lighting, animation principles, silhouette, accessibility | High |
| [[Economy & Resource Design]] | Sinks/sources, resource types, economic loops, inflation/deflation, zero-sum vs. positive-sum, F2P currencies | High |
| [[Puzzle & Challenge Design]] | Puzzle vs. game definition, Schell's 10 principles, Adams' challenge hierarchy, integrated vs. explicit puzzles | Medium |
| [[Character Design & Player Projection]] | Projection vs. empathy, avatar design, NPC functions, character arcs, interpersonal circumplex | Medium |
| [[The Philosophy & Theory of Play]] | Huizinga, Caillois, Suits' lusory attitude, meaningful play, three schemas, magic circle, procedural rhetoric | Medium |
| [[Educational Game Design]] | Games as teaching, edutainment trap, learning objectives vs. fun, transfer, B2B context, age-appropriate design | B2B Studio |
| [[Game Analysis & Design Criticism]] | Fernández-Vara's 3-area framework, procedural rhetoric, three schemas, genre analysis, critical vocabulary | General |
| [[Accessibility & Inclusive Design]] | Cognitive/motor/visual/auditory accessibility, difficulty modes, universal design, diverse representation | High |

---

## How to use these

**For design work:** open the relevant synthesis before making a design decision. These tell you what all 17 sources say on the topic before reasoning from scratch.

**For Hot Potato:** Movement + Loops + Psychology + Balance should be open during GDD sessions. The "HP implications" section at the end of each synthesis is the direct application.

**For learning:** read in order (loops → balance → psychology → feel → level design) to build a complete mental model.

**These are living documents.** When new sources are ingested or new insights emerge, update the relevant synthesis.

---

## Relationship to other layers

```
05-Syntheses/          <- working knowledge on a topic (READ THIS)
    |
10-Library/notes/      <- one idea per note; atomic; citeable
    |
10-Library/sources/    <- 17 source cards; provenance
    |
raw/                   <- 17 PDFs (git-ignored)
```
