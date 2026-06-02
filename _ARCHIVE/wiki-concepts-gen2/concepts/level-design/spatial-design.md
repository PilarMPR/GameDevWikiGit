# Spatial Design

The craft of organizing game space to support movement, navigation, discovery, and experience. Game spaces are not just aesthetic backdrops — they are **functional systems that shape player behavior and emotion through architecture, sightlines, layout, and indirect control**.

---

## Architecture as experience design (s005, ch.19)

Schell's foundational claim:

> "The primary purpose of architecture is to control a person's experience. Architects and game designers are close cousins. Both create structures that people must enter in order to use. Neither can create experiences directly — instead, both must rely on the use of indirect control to guide people into having the right kind of experience." (s005, ch.19)

Game spaces are not buildings, but they serve the same experiential purpose: create the conditions for the experiences you want the player to have. A claustrophobic corridor creates tension; an open vista creates awe; a hidden room creates discovery and reward.

The distinction game designers have over architects: **no physical constraints**. A game world can contain impossible spaces, spaces that violate physical laws, spaces that shift and change. This is both freedom (anything is possible) and burden (you must decide what to build, rather than what the materials allow). (s005, ch.19)

---

## Five ways to organize game space (s005, ch.19)

Schell identifies five organizing principles for game space, from most linear to most open:

### 1. Linear
The player can only move forward (and possibly back) along a single path. The designer has **maximum control** over pacing and experience order; the player has **minimum navigational freedom**.

Examples: Candy Land, Monopoly (board), Super Mario Bros. (world map), Guitar Hero, Crash Bandicoot. Many story-driven games are functionally linear even when they appear open.

Use when: narrative control is paramount; the designer needs to guarantee a specific experience sequence.

### 2. Grid
Space is organized on a grid. Easy for players to understand mentally (form a map); easy for computers to process; natural for top-down and strategy games.

The grid need not be squares — hexagons, isometric grids, and irregular tilings all work. The key property: players can build an accurate mental map, enabling strategic planning and memory.

Use when: navigational clarity and player planning are core gameplay elements.

### 3. Web
Spaces are connected by a graph of paths, forming a web of possible routes. The player has **real navigational choice**. Some paths may be shortcuts; some may be more dangerous; some may require keys or abilities to unlock.

Most action-adventure games use webs: a central hub with spokes to areas, or interconnecting dungeons. Web spaces support backtracking, exploration, and the satisfaction of finding shortcuts.

Use when: exploration and player agency in navigation are design goals.

### 4. Points-in-space
Several discrete locations exist in a larger field, with no required path between them. The player navigates the field freely to reach points. Open-world games are the extreme version: the world map is a field, and interesting locations are points.

Points-in-space requires good **landmark design**: players must be able to identify and navigate toward points they can see or have discovered. Without landmarks, free-field navigation produces confusion.

### 5. Divided spaces
The game space is divided into sub-spaces (rooms, zones, biomes) with controlled connections between them. Movement between divisions is gated (doors, portals, level loads). This is the default for almost all indoor games and many large games.

Divided spaces allow the designer to control **density** (lots happening in a small area) and **contrast** (tense combat space followed by quiet exploration space).

---

## Functional vs. experienced space (s005, ch.10 and ch.19)

Schell distinguishes two layers of space:

- **Functional space** (covered in ch.10, Mechanic 1: Space): the abstract topological structure — which spaces connect to which, what is accessible, what are the distances. Functional space is the game's "skeleton."
- **Experienced space** (ch.19): the fleshed-out space the player actually moves through — the visual environment, the sightlines, the sense of scale, the atmosphere. The same functional space can be experienced very differently depending on how it is realized visually and aurally.

Good level design starts with functional space (the floorplan) and then builds the experienced space around it, never the reverse. (s003, s012)

---

## Sightlines and visual direction (s003, s012, s005)

**A sightline is a line of sight from the player's viewpoint to something in the world.** Controlling sightlines is one of the most powerful spatial design tools:

### Guiding movement
> "One of the keys to good level design is that the player's eyes pull them through the level." (s005, ch.14)

The eye naturally moves toward:
- **Contrast**: light objects against dark backgrounds; bright areas at the end of dark corridors
- **Motion**: moving objects attract attention regardless of other visual noise
- **Unique forms**: distinct shapes in a repetitive environment (a red barrel, an unusual structure, a glowing item)
- **Openings**: doorways, gaps, and passages suggest traversable space

Placing targets, goals, and waypoints at the end of sightlines pulls the player forward without explicit instruction.

### Tactical information
In action games, sightlines determine tactical advantage: seeing enemies before they see you; covering a choke point; sniping across a wide space. Multiplayer levels particularly depend on balanced sightlines — a position with too many sightlines is unchallengeably dominant (s003, multiplayer floorplans).

### Creating mystery and anticipation
Blocking a sightline (with a corner, a wall, a fog bank) creates anticipation and tension: what is around the corner? A partial reveal — seeing a shadow, hearing a sound, glimpsing something through a window — combines blocking with suggestion to create curiosity.

---

## Landmarks and navigation (s003, s012)

A **landmark** is a distinctive visual element that players use as a navigational anchor. Landmarks:
- Help players orient in space ("I need to go toward the tower")
- Make spaces memorable and distinct (reducing the "all rooms look the same" problem)
- Provide exploration targets ("I want to get to that glowing structure")

Landmark density is a design choice:
- **Dense landmarks**: easy navigation; high readability; potentially cluttered visual experience
- **Sparse landmarks**: harder navigation; more exploration required; potentially confusing

Good landmark design uses **hierarchical distinctiveness**: the most important landmarks (quest targets, level exits) are the most visually striking; secondary landmarks (neighborhood anchors) are moderately distinctive; background elements are visually coherent but not individually notable. (s003)

---

## Scale and spatial emotion (s005, s012)

Spatial scale communicates emotional state:
- **Small, low-ceiling spaces**: claustrophobia, intimacy, tension, vulnerability
- **Large, high-ceiling spaces**: awe, freedom, exposure, vulnerability from a different angle
- **Sudden scale change**: emerging from a tight tunnel into a vast cavern produces a strong emotional response — the "aha" moment of spatial revelation

Schell's principle: "controlling a person's experience" through architecture means using scale consciously. A boss arena should feel larger and more intimidating than the corridors leading to it. A safe rest area should feel enclosed and calm after an open, dangerous space. (s005, ch.19)

---

## Composition and visual readability (s003)

Hourences' visual design principles for level spaces:

### Composition basics
- **Rule of thirds and focal points**: the most important element of a space should dominate the visual composition — not compete with equal-weight elements
- **Framing**: use foreground elements (arches, walls, foliage) to frame important background elements and direct the eye
- **Depth cues**: overlapping elements, atmospheric perspective, and scale variation create a sense of 3D depth that helps players read distances

### Unity and connectivity
Spaces should have a coherent visual language. Mixing too many architectural styles, material types, or lighting conditions produces visual noise. "Unity" means the space reads as a single designed environment; "connectivity" means adjacent spaces feel like they belong to the same world. (s003)

### Moving geometry
Dynamic elements (rotating fans, swinging pendulums, flooding water) attract the eye reliably. They can direct attention to important areas, communicate danger, or mark the rhythm of a puzzle. The eye is drawn to motion — this is a biological fact exploited by level designers.

### Light as composition
Light is the most powerful compositional tool:
- **Bright areas** attract attention and suggest safety or reward
- **Dark areas** create tension, suggest danger, and hide information
- **Rim lighting** (light behind a silhouette) makes objects dramatically readable
- **Colored light** sets emotional tone: warm light feels welcoming; cold blue light feels threatening

The player unconsciously follows the light. A level designer who controls lighting controls movement. (s003; s014 perception principles) → [[../player/player-psychology]]

---

## Spatial flow and encounter rhythm (s003)

Spatial design and encounter design are inseparable. The physical arrangement of a space determines:
- **When** the player can see (and engage) an enemy
- **From where** flanking and retreat are possible
- **What resources** are available at what cost
- **The rhythm** of tension (combat space) and release (safe/exploration space)

Good spatial flow:
- Combat spaces have cover, verticality, and multiple approach routes
- Between combat spaces: transitional areas with lower tension (corridors, outdoor areas, quiet rooms)
- After major encounters: spaces with rewards, story beats, or visual payoffs
- Progression is implied spatially: larger, more complex, more visually intense spaces signal advancing challenge

The spatial rhythm of tension-and-release maps directly to the **interest curve** — the spatial implementation of pacing. (s005, ch.14) → [[pacing-and-flow]]

---

## Indirect control through space (s005, ch.16)

Schell's six methods of indirect control all have spatial implementations:

| Method | Spatial implementation |
|--------|----------------------|
| **Constraints** | Walls, locked doors, impassable terrain reduce choice to intended paths |
| **Goals** | Quest markers, glowing objects, and visible objectives pull movement |
| **Visual design** | Lighting, composition, and contrast guide the eye and then the body |
| **Interface** | Minimaps, waypoints, and compass roses extend spatial cognition |
| **Characters** | NPCs standing in corridors, pointing, looking toward objectives |
| **Music** | Ambient audio changes signal spatial transitions; directional audio guides toward sounds |

The key principle: **the designer does not have direct control over the player's movement, only indirect control**. The best spatial designs make the intended path so appealing — visually, tactically, narratively — that players choose it freely while believing they are exploring. (s005, ch.16)

---

## Spatial design across game types

| Game type | Primary spatial concern | Key spatial pattern |
|-----------|------------------------|---------------------|
| FPS | Sightlines, cover, flanking routes | T-junctions, asymmetric cover |
| Platformer | Obstacle readability, jump telegraphing | Clear foreground/background separation |
| RPG | World scale, fast travel, density | Hub-and-spoke, biome variety |
| Horror | Claustrophobia, limited information | Tight corridors, obscured sightlines |
| Exploration | Discovery, reward spacing, wonder | Points-in-space, surprise reveals |
| Puzzle | Clear problem boundaries, affordance | Single-room or segmented spaces |

---

## Key concepts & cross-links

- [[level-design]] — level design practice; teaching, goals, methodology
- [[pacing-and-flow]] — interest curves as the temporal counterpart to spatial design
- [[../feel-and-controls/camera-design]] — the camera determines what of the space the player sees
- [[../player/player-psychology]] — perception, attention, and visual guidance
- [[../interface/usability-and-hcd]] — readability, affordances, and spatial communication
- [[../mechanics/core-mechanics]] — Schell's Mechanic 1: Space (functional topology)
- [[../player/flow-channel]] — spatial design is the vehicle for maintaining flow

## Sources

s005 ch.10, ch.16, ch.19 (Schell — functional vs. experienced space, 5 organizational principles, indirect control, architecture analogy) · s003 (Hourences — composition, landmarks, visual design, lighting, spatial flow) · s012 (Kremers — floorplans, level design methodology, sightlines) · s006 ch.12 (Adams — camera and space) · s014 (Hodent — visual perception, attention, Gestalt principles) · s007 (Swink — simulated space as one of three building blocks of game feel)
