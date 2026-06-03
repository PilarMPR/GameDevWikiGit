# UI, Interface & Information Design

> **What this is:** Everything the canon says about designing the information layer between the player and the game — HUDs, menus, diegetic vs. non-diegetic UI, information hierarchy, cognitive load in interface design, and making the interface invisible when it works. Aggregated across s005, s014, s015, s006, s012.

---

## 1. What Game UI Is For

**Norman's fundamental principle** (s015, ch.2): every interface element exists to close one of two cognitive gaps:

- **Gulf of Execution:** the gap between wanting to do something and knowing how to do it. The player has intent but not action.
- **Gulf of Evaluation:** the gap between the system producing an output and the player understanding what happened.

Every UI element should close one of these gaps. An element that closes neither is clutter.

**The golden standard** (s005, ch.13; s014):
> *"The player always knows what is happening, what to do next, and how well they are doing — without being distracted from the game itself."*

This is both the goal and the tension: good UI delivers all of this while competing as little as possible with the player's attention to the actual gameplay.

---

## 2. Diegetic vs. Non-Diegetic vs. Meta UI

**The most fundamental categorization in game UI design:**

### Diegetic UI
Interface elements that exist within the game world. The character can see them; they have physical presence in the fiction.

**Examples:**
- *Dead Space* health indicator — displayed on the suit the character wears; no external HUD
- *Doom (2016)* ammo count — displayed on the weapon itself
- Wristwatch that shows the time in a game where your character would plausibly own a watch
- *Metro: Last Light* notebook that the character physically opens

**Advantages:**
- Maintains immersion; the player and character share the same information
- Feels coherent within the fiction
- Often creates memorable, distinctive aesthetic (Dead Space's health bar is iconic)

**Disadvantages:**
- May be harder to read at a glance (must work as both in-world prop AND readable UI)
- Limits information density (can't have 20 elements on a suit's shoulder)
- Requires visual design to make in-world elements readable from the game camera distance

### Non-Diegetic UI
Interface elements that exist outside the game world. The character cannot see them; they overlay on screen.

**Examples:**
- Traditional health bar in the corner
- Minimap
- Ammo counter
- Pause menu
- Most mobile game interfaces

**Advantages:**
- Maximum readability and information density
- Easy to design and iterate
- Immediately clear to players via genre conventions

**Disadvantages:**
- Breaks the fourth wall
- Can clutter the screen
- Wrong for certain tonal contexts (horror games, immersion-first experiences)

### Meta UI
Elements that are technically non-diegetic but are given loose in-universe justification.

**Examples:**
- Screen-edge blood splatter when taking damage (character wouldn't see this, but it's "damage visualization")
- Screen effects like scanlines during hacking
- UI elements that "glitch" during hacker attacks in cyberpunk games

Meta UI provides the communication advantages of non-diegetic UI while maintaining the *feeling* of diegesis — it nods at the fiction without being bound by it.

### Spatial UI
World-space UI elements that exist in 3D space within the game world but aren't attached to props or characters.

**Examples:**
- Floating health bars above enemies
- Quest objective markers floating in world space
- Damage numbers that appear in 3D space above hit enemies

Spatial UI bridges diegetic and non-diegetic — it feels grounded in the world but isn't physically real.

---

## 3. HUD Information Hierarchy

**Four levels of HUD information** (s014, ch.6; s006, ch.12):

**Level 1 — Constant Critical Information**
Must always be readable at a glance. Players cannot perform deliberate lookup; this must register in peripheral vision or fast glances.
- Health/lives remaining
- Ammo count (for shooter)
- Active objective indicator
- Score (for score-driven games)

**Design rule:** place Level 1 information where the player's gaze already goes (near the action, or at primary screen edges). High contrast against variable backgrounds (shadow or outline essential).

**Level 2 — Situational Critical Information**
Must be unmissable when it appears, but isn't always present.
- Low health warning (triggered when threshold crossed)
- Enemy off-screen indicator
- Incoming projectile warning
- Objective complete notification

**Design rule:** these should interrupt peripheral attention. Motion (pulsing), brightness, sound, and screen position (outside safe area) all trigger exogenous attention capture.

**Level 3 — Strategic Reference Information**
Consulted deliberately, not at a glance.
- Minimap
- Resource counts
- Skill cooldowns
- Team status

**Design rule:** these can live at screen edges and be smaller. Player chooses to look at them. They should not compete with Level 1 and 2 information for attention bandwidth.

**Level 4 — Optional Information**
Accessed when the player chooses; never forced.
- Detailed stats
- Inventory details
- Map notes
- Social information

**Design rule:** behind a button press or in a dedicated menu. These are pull (player requests) not push (game delivers).

---

## 4. Cognitive Load and UI Design

**Sweller's cognitive load theory** (via s014, ch.6): every HUD element competes for working memory. The player's finite working memory (~3–4 items active at once) must be divided between:
- The game mechanics (what to do)
- The spatial situation (where to go)
- The opponent(s) (what they'll do)
- The UI (what am I looking at)

Each additional UI element is a tax on this budget. Too many elements = cognitive overload = player makes obvious errors and feels frustrated without knowing why.

**Practical rules:**
- Remove every UI element that doesn't actively help the player make better decisions
- If an element hasn't been looked at in 30 minutes of play, it probably doesn't need to be in the HUD
- When in doubt, cut — players can always go to menus for detailed information
- **Complexity budget:** every element added should either be essential OR explicitly replace an existing element

**The UI visibility test** (Schell, Lens #56 Transparency): when the interface is working well, players don't notice it. If players start talking about the UI — either because it helped or because it hindered — something is off. Good UI is invisible.

---

## 5. Menu Architecture

Menus are their own design discipline, separate from HUD design:

### Navigation Principles

**Depth vs. breadth tradeoff:**
- Deep menus (many levels, few options per level) require many clicks to reach options
- Broad menus (few levels, many options per level) overwhelm players with choices
- **Optimal:** 2–3 levels deep maximum; 5–7 options per level maximum

**The back button is sacred:** players must always be able to undo a navigation action. A menu trap (player cannot find their way back) is a usability failure that produces immediate frustration.

**Consistent mapping:** the same button should confirm, and the same button should cancel, across all menu contexts. Mode confusion (s005, Lens #60) in menus — where the function of a button changes unpredictably — produces errors.

**Shortcuts and favorites:** expert players want direct access. Provide quick-access options for frequently used features; don't bury them three levels deep.

### Menu Visual Design

**Visual hierarchy** (s014, Gestalt principles): related options cluster together; unrelated options have clear visual separation. Players shouldn't need to read every option to understand the menu's structure.

**Typography legibility:**
- Minimum font size for TV viewing distance: ~28pt
- Avoid all-caps for body text (legibility drops)
- High contrast text on all backgrounds (test on worst-case white text on pale background)
- Font choice should match game tone but prioritize legibility over style

---

## 6. Information Asymmetry as Design Tool

**Salen & Zimmerman** (s013, ch.17): changing *who knows what* is one of the most powerful levers in game design, and it is fundamentally a UI/information design decision.

| Information state | Design mechanism | Example |
|---|---|---|
| **Public to all** | Show on shared HUD, diegetic elements | Score in party game |
| **Private (per-player)** | Per-player UI, hidden on split screen | Hand of cards |
| **Hidden from all** | Removed from HUD, fog of war | Fog of war in RTS |
| **Asymmetric** | Different UI for different roles | Impostor's kill button in Among Us |
| **Delayed** | Information shown after the fact | Lag indicator in poker |

Changing a piece of information from public to private (or vice versa) can transform a game without changing any mechanic. *Draw poker* vs. *Texas Hold'em*: same hands, same betting, completely different strategic games because the information states differ.

**Design implication:** before finalizing a UI layout, ask: "Who should know this? When?" The answer may be different than the default (make everything visible to everyone).

---

## 7. Accessibility in UI Design

**Hodent** (s014, ch.3): UI must account for players with perceptual differences:

**Colorblindness:**
- ~8% of males have red-green colorblindness
- Never use color as the *only* differentiator for critical information
- Always add a secondary signal: shape, pattern, label, icon
- Colorblind mode: remapped palette is standard in AAA but should be accessible to indie developers via Unity/UE tools

**Visual acuity:**
- Provide text size options (at minimum: small/medium/large)
- UI elements that must be read at TV viewing distance need larger base sizes
- High-contrast mode option for players with low vision

**Motor accessibility:**
- Full control remapping (not just presets) is the baseline expectation
- Toggle vs. hold options for sustained inputs (hold a button = toggle it)
- Timing assistance options for timed inputs

**Cognitive accessibility:**
- Extended tutorial option
- Reduced simultaneous information demands
- Option to simplify HUD (show only Level 1 elements)

---

## 8. Schell's Interface Lenses (s005, ch.13, Lenses #53–60)

Schell dedicates a chapter and 8 lenses to interface design. Key principles:

**Lens #53 — Control:** when players use the interface, does it do what they expect? Do they feel in control?

**Lens #56 — Transparency:** is the interface invisible when working? Are there hidden states that ever surprise the player?

**Lens #57 — Feedback:** is feedback clear, immediate, and informative for every player action?

**Lens #58 — Juiciness:** is every interaction satisfying? Are there small touches that reward incidental interaction?

**Lens #59 — Channels and Dimensions:** am I using all available channels (visual/audio/haptic) thoughtfully? Are any overloaded?

**Lens #60 — Modes:** are modes clear? Is it always obvious which mode the player is in?

The through-line: **the interface is not the game, but a failure in the interface is a failure of the game.** A player who is confused, frustrated, or distracted by the UI is not playing the game — they're fighting the interface.

---

## 9. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| Every UI element closes the Gulf of Execution or Evaluation — or is clutter | s015 |
| Four levels of HUD information require different placement and attention strategies | s014, s006 |
| Good UI is invisible when working; noticed only when failing | s005 |
| Information state (who knows what, when) is a design lever as powerful as mechanics | s013 |
| Colorblindness affects ~8% of males; color alone is never sufficient for critical info | s014 |
| Cognitive load is finite; every HUD element taxes working memory | s014 |
| Mode confusion is a usability failure; consistent button mapping is non-negotiable | s005 |

---

