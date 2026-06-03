# Accessibility & Inclusive Design

> **What this is:** Everything the canon says about designing games for diverse players — cognitive, motor, visual, and auditory accessibility; designing for casual/non-gamer audiences; difficulty modes and their tradeoffs; universal design principles; and the specific accessibility challenges of party games. Aggregated across s014, s015, s005, s006.

---

## 1. The Case for Accessibility

**Why accessibility matters beyond ethics** (s014; s006):

**Market size:** approximately 15% of the world's population has some form of disability. Cognitive differences (ADHD, dyslexia, autism spectrum) are present in roughly 10–15% of players. Color vision deficiency affects ~8% of males. Motor impairments range from mild (one-handed play) to significant (adaptive controller users).

**The overlap with party game design:** party games by definition serve the *widest possible skill and ability range* — from experienced gamers to people who haven't played a video game in years. Accessibility for party games is not a niche consideration; it's a core design requirement.

**The curb-cut effect:** features designed for accessibility often improve the experience for everyone. Subtitles were designed for deaf players; they're used by players watching TV with the sound down, players learning a second language, and players in noisy environments. Difficulty modes were designed for players with limited gaming time; they're used by experienced players who want a relaxed experience.

---

## 2. Cognitive Accessibility

**Hodent** (s014, ch.3–6) provides the most detailed cognitive accessibility framework in the canon:

### Working Memory Limitations

Working memory capacity is not fixed at exactly 3–4 items for everyone — it varies significantly across individuals and populations:
- Children have lower working memory capacity than adults
- ADHD is associated with working memory challenges
- Aging can reduce working memory capacity
- Cognitive fatigue reduces effective working memory

**Design for cognitive accessibility:**
- Limit simultaneous demands (one new mechanic at a time during onboarding)
- Provide reminders for complex rule states (what's my current objective? what can I do?)
- Allow time pauses (games with no-pause mode lock out players who need thinking time)
- Avoid simultaneous high visual complexity + high rule complexity
- Reduce extraneous cognitive load (UI clutter, unnecessary visual complexity)

### Attention Differences

ADHD, executive function differences, and anxiety all affect how players allocate attention:
- Variable reward schedules designed for engagement can be especially difficult for impulsive players
- Games requiring sustained attention for long sessions may exclude players with attention differences
- Frequent short reward cycles are more accessible than infrequent large rewards

### Processing Speed

Some players process information more slowly — whether due to age, neurological differences, or disability. Design considerations:
- Tutorial text should not auto-advance; always provide "next" control
- Time-limited decisions should have optional extended time
- Fast-moving information (scrolling text, timed elements) should have pause or slow-down options

---

## 3. Motor Accessibility

**The spectrum of motor impairments:**
- Temporary (broken arm, RSI)
- Permanent one-handed play
- Limited finger mobility
- Controller-only (no mouse or keyboard)
- Adaptive controller users (eye tracking, sip-and-puff, switch controllers)

### Full Control Remapping

**The baseline requirement.** Every player has a different body, different hand size, different physical comfort zone. Preset control schemes are a starting point; full remapping is the minimum for genuine accessibility.

**Key elements of full remapping:**
- Every button assignable to any other button
- Swap left/right stick for players who prefer non-standard layouts
- PC: full keyboard rebinding, including modifier keys

### Hold vs. Toggle

Many games require the player to *hold* a button to maintain an action (hold to sprint, hold to crouch). For players with limited sustained grip strength, this is a significant barrier.

**Solution:** toggle option for all sustained inputs. Toggle sprint on/off instead of hold.

### Button Mashing and Rapid Input

Quick-time events, button-mashing mini-games, and input timing windows assume fine motor control and reaction speed that not all players have.

**Solutions:**
- Option to disable QTEs or replace them with slower alternatives
- Extended timing windows (accessibility mode)
- Auto-pass options for rhythm/timing sections

### Controller Support (PC)

On PC, many players use controllers due to motor impairments or preference. Any PC release should support:
- Full controller playability for all game functions
- Steam Input integration for maximum hardware compatibility
- Adaptive controller (Xbox) compatibility

---

## 4. Visual Accessibility

### Colorblindness

**The most common visual accessibility issue:** approximately 8% of males have red-green colorblindness (deuteranopia or protanopia). About 0.5% of females. Total colorblindness is rare (<0.01%) but complete red-green blindness affects millions of players.

**Design rules (s014, ch.4; s015):**
1. Never use color as the *only* differentiator for critical information
2. Always add a secondary signal: shape, icon, pattern, label, outline
3. Test all UI with colorblind simulation tools
4. Provide colorblind mode with remapped palette

### Low Vision

For players with reduced visual acuity (not full blindness but significantly impaired):
- Text scaling options (small/medium/large/extra-large)
- High-contrast mode (pure black/white UI option)
- Increased icon sizes
- Avoid relying on small visual details for critical information
- Avoid small text in UI elements the player is expected to read during gameplay

### Screen Distance

Console games are played at varying distances from the TV. Standard design rule for TV-facing games (s003, spatial design context): minimum 28pt font at expected viewing distance. Test UI readability at 3 meters with standard TV.

### Photosensitivity / Epilepsy

Flashing lights at 3–50 Hz can trigger photosensitive epilepsy (PSE). This affects approximately 1 in 4,000 people, with higher prevalence in the <35 age group.

**Requirements:**
- Photosensitive mode (reduces or eliminates flash effects)
- Warning screen at game start
- Flash frequency design review before launch (avoid sustained flicker in this frequency range)
- Industry standard: W3C's WCAG 2.1 guidance on flash and blink

---

## 5. Auditory Accessibility

### Subtitles and Captions

**The baseline requirement for all dialogue:**
- Subtitles for all story dialogue, NPC dialogue, and voiced instructions
- Closed captions for all important audio cues (not just speech): "[Footsteps behind you]", "[Enemy alert sound]", "[Door opening]"
- Adjustable subtitle size, background opacity, and font

### Audio Cue Visualization

Critical game information delivered through audio must have visual backup:
- Screen flash or icon when hit from off-screen
- Visual indicator when a warning sound plays
- Visual direction indicator for spatial audio cues
- No critical information carried by audio alone

### Music vs. Sound Effects

Separate volume controls for music, sound effects, and dialogue/voice. Many players with partial hearing loss can hear sound effects clearly but not dialogue, or vice versa.

---

## 6. Difficulty Accessibility

**The difficulty question is an accessibility question.** Games that offer only one difficulty level exclude players who lack the time, reflexes, or skill to complete at that level.

### Types of Difficulty Modes

**Preset difficulty levels** (Easy/Normal/Hard): the standard. Easy = reduced enemy damage/speed/HP; Normal = designed experience; Hard = increased challenge.

**Granular difficulty controls** (increasing adoption): separate sliders for enemy aggressiveness, player damage, timer speed, checkpoint spacing. Each player calibrates to their specific challenge tolerance.

**Assist modes** (*Celeste* model): options to enable invincibility, slow time, or skip individual sections — framed as "for everyone to experience the full game," not as "for people who can't play."

**The Celeste approach** is increasingly the industry standard for accessibility: don't hide the options, don't frame them as "cheating," frame them as tools that allow everyone to experience the game the designer made.

### When NOT to Have Difficulty Options

Some games are defined by their difficulty (Souls-likes). The challenge IS the game, and removing it removes the experience. This is a legitimate design choice — but requires the designer to accept that the game will be inaccessible to players who cannot meet that difficulty floor.

- Dynamic difficulty scaling (adjusts to player skill)
- "Training mode" with reduced player count or longer timers
- Chaos level selection (more/less random item spawn rate)
- No permanent exclusion from sessions — everyone can participate even if they struggle

---

## 7. Universal Design Principles

**Norman** (s015) frames universal design (design that works for the widest range of users) through his six principles applied broadly:

1. **Affordances** that communicate clearly without requiring reading, game literacy, or prior experience
2. **Signifiers** that work across visual, auditory, and tactile channels simultaneously
3. **Constraints** that prevent mistakes rather than punishing them
4. **Mappings** that are as natural as possible (reducing the translation required)
5. **Feedback** that is multi-channel (visual + audio + haptic) so no single channel is required
6. **Conceptual models** that match player expectations without requiring gaming vocabulary

**The broadest application:** design for your *least experienced* player first. If the most inexperienced player can participate, everyone else can. The reverse is not true: designing for the most experienced player first and then "dumbing it down" produces different — and worse — results.

---

## 8. Inclusive Representation

Beyond mechanical accessibility, inclusive design includes who is *represented* in the game:

**Character diversity:** games where all player-facing characters are young, male, or from one ethnicity implicitly communicate who the game is "for."

**Cultural accessibility:** idioms, cultural references, and humor calibrated to one cultural context exclude players from other contexts.

**Language accessibility:** full localization into target markets' languages, including UI, dialogue, and tooltips.

---

## 9. Cross-Source Synthesis

| Claim | Sources |
|---|---|
| ~15% of the global population has some disability; accessibility is a market opportunity | s014 |
| Color alone is never sufficient for critical information (8% of males colorblind) | s014 |
| Full control remapping is the baseline motor accessibility requirement | s015 |
| The curb-cut effect: accessibility features improve experience for all players | s014, s015 |
| Difficulty accessibility: Celeste's assist-mode model is the industry standard | practice |
| Cognitive accessibility: limit simultaneous demands; never advance without player confirmation | s014 |
| Party games specifically require wide skill/ability range accessibility | s005 |

---

