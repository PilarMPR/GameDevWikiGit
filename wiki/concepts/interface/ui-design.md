# UI Design

The design of the visual information layer between the player and the game system — HUDs, menus, minimaps, dialogue boxes, inventories, and every other interface element. Game UI is unique: unlike productivity software, good game UI is often invisible when it works and only noticed when it fails.

---

## The UI's contract with the player (s015, s014)

UI exists to **close Norman's gulfs of execution and evaluation** (s015):
- **Execution**: "what can I do?" — the UI must show available actions and how to take them
- **Evaluation**: "what happened?" — the UI must show the result of the player's actions and the current game state

Every UI element should answer one of these questions. An element that answers neither is clutter. (→ [[usability-and-hcd]])

The golden standard: **the player always knows what is happening, what to do next, and how well they are doing** — without being distracted from the game. This requires careful information prioritization.

---

## Diegetic vs. non-diegetic UI (s012, ch.11; s010)

A fundamental axis of UI design:

**Diegetic UI**: interface elements that exist within the game world. The character sees them; they have a physical presence in the fiction.
- Examples: a wristwatch in a game where the character checks the time; a health bar visualized as wounds on the character's body; a compass on the character's belt; Doom (2016)'s health numbers on the armor's chest piece

**Non-diegetic UI**: interface elements that exist outside the game world, overlaid on the screen. The character doesn't see them; they break the fourth wall.
- Examples: traditional health bars in the HUD, minimap in the corner, ammo counter, pause menu

**Meta UI** (a third category): elements that are not in the world but are explained in-universe. A screen-edge blood splatter when the player is hurt — the character wouldn't see it, but the game treats it as communicating real damage. Subtly diegetic.

The design tension:
- Non-diegetic UI provides the clearest, most efficient communication — easy to read, never ambiguous
- Diegetic UI maintains immersion and narrative consistency but can be harder to read and limits information density

Most games use non-diegetic UI for critical information (health, ammo, map) and diegetic elements for atmosphere. The choice should serve the game's tone: a horror game that breaks immersion for UI readability loses atmosphere; an action game that sacrifices readability for immersion becomes unplayable.

---

## HUD design principles (s014; s015; s006)

The Heads-Up Display is the persistent information layer during gameplay.

### Hierarchy: what needs to be seen when?

HUD elements categorized by attention demand:
1. **Constant critical info**: health/life count, ammo, active objectives — must always be readable at a glance
2. **Situational critical info**: alerts, combat indicators, low-resource warnings — must be unmissable when they appear
3. **Strategic reference info**: minimap, resource counts, skill cooldowns — consulted deliberately, not at a glance
4. **Optional info**: detailed stats, map notes, social info — accessed when the player chooses

Information in category 1 should be placed where the player's gaze already goes (near the center of the screen, or at screen edges for peripheral attention). Information in category 4 can be behind a menu. (s014)

### Visual hierarchy and readability
- High-contrast text and icons against variable backgrounds (use a shadow, outline, or background panel)
- Consistent typographic hierarchy (number sizes signal importance)
- Gestalt grouping: related information clusters together (health + armor in the same region; weapon info together)
- Color consistency: if red means danger in one context, it must mean danger everywhere

### Cognitive load minimization (s014)
Every HUD element competes for working memory. Too many elements = cognitive overload. Principles:
- Show only what the player needs right now (reveal advanced info as the player needs it)
- Fade or hide elements that aren't currently relevant
- Use spatial memory: put elements in consistent positions so the player doesn't need to search

### Dynamic HUDs
Many modern games fade out the HUD when not in combat or when the player is not actively using resources. This reduces clutter in calm moments and makes the reappearing UI feel more urgent. Requires that the player can always summon the HUD on demand. (s014)

---

## Menus and navigation (s015; s014)

Menus are the non-realtime interface — inventory, options, character sheets, map screens.

### Menu structure
- **Flat** (all options visible at once): fast access; overwhelming at scale
- **Hierarchical** (options nested in categories): scales to large option sets; adds navigation depth
- **Contextual** (options change based on context): efficient; requires player to learn context-specific vocabularies

### Menu usability principles (Norman, s015)
- **Consistent navigation**: back is always the same button; confirm is always the same button
- **Clear current state**: the player always knows where they are in the menu hierarchy
- **Reversible actions**: destructive actions (delete save, discard item) have confirmation steps
- **Minimal required inputs**: reducing the number of button presses to reach any goal reduces friction

### Inventory design
Inventory systems are among the most complex UI challenges in games:
- **Spatial inventories** (grid-based, like Diablo's): visual, tactile; limited by grid size; enjoyable to organize for some players
- **List inventories** (scrolling lists): unlimited scale; requires good filtering/sorting
- **Card inventories** (collectible card game style): visual representation; appropriate for certain game types

The core tension: inventory management can be a satisfying minigame (item organization, loadout optimization) or a frustrating chore (shuffling items to make space). The design must decide which and commit to it.

---

## Tutorials and onboarding UI (s014; s008; s005)

The onboarding interface is a usability problem distinct from the gameplay UI. Key principles:

### Don't teach everything at once
Working memory holds 3–4 items actively. Introducing more than 3 new concepts simultaneously guarantees some will be missed. Progressive disclosure: teach one mechanic, let the player use it, then teach the next. (s014)

### Contextual tutorials over front-loaded tutorials
Teaching through doing is more effective than showing a tutorial wall. A button prompt appearing when the relevant action is first needed teaches in context; a 5-minute tutorial before the game starts front-loads information the player isn't ready to use.

### Fail-state as teacher
If a player fails, the failure should reveal what they needed to know. "You need the fire spell to defeat this enemy" — shown by the enemy being fire-resistant — is better than pre-emptive tutorial text.

### Skip gracefully
Players with prior experience should be able to skip. Mandatory tutorials for experienced players are the most common first-player-experience complaint in sequels.

---

## Screen real estate and resolution considerations (s014; s006)

- **Safe zone**: TVs and monitors may cut the outer edges of the screen. Critical UI must be within the safe zone (typically 80–90% of screen width/height)
- **Foveal vs. peripheral placement**: information the player actively reads goes near the center; alerts that need to be noticed peripherally go at screen edges
- **Scale for distance**: console games viewed from a couch at 3m need larger text than PC games viewed from 60cm
- **Accessibility**: colorblind modes (distinguishing red/green feedback must have an alternative), scalable font sizes, subtitle support

---

## Key concepts & cross-links

- [[usability-and-hcd]] — Norman's foundational principles underlying all UI design
- [[../player/player-psychology]] — perception, attention, and working memory constraints
- [[feedback-systems]] — feedback is a core UI function
- [[../feel-and-controls/input-and-controls]] — controls and UI interact (button prompts, control mapping displays)
- [[../../level-design/level-design]] — the interface is the player's window into the level
- [[../../narrative/indirect-control]] — interface as indirect control method

## Sources

s014 (Hodent — cognitive load, working memory in UI, HUD design, onboarding) · s015 (Norman — affordances, signifiers, mappings, feedback in interface design) · s012 ch.11 (Kremers — diegetic vs. non-diegetic sound; applies to all media elements) · s010 (Fernández-Vara — diegetic/non-diegetic framework from game analysis) · s006 ch.12 (Adams — player-centric design, interface as experience layer)
