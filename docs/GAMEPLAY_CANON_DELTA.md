# MELLANRUM vNext – GAMEPLAY_CANON_DELTA (Issue #21)

**Development candidate; pending human acceptance and genuine controller/emulator validation.** Source base immutable PR #16 HEAD `56d70c316031bf55a5260e1fbbe0fe187c55f297`. This document records new, user-delegated design changes under MEL-054, not a claim of approved final canon.

## Why the mechanics changed
MAIN's real Stella/libretro test of prior SHA `45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7` reproduced 14/15 passive victories. The old exit triggered automatically when the autonomous owl reached it. A still-autonomous owl must now encounter a forest altered deliberately by the player.

## Resonance semantics
- The **exit glyph is a forest-resonance readout**, not a free win tile. The owl wins only when entering the exit **while one authored mirrored tree group is visibly absent** in live gameplay collision bits.
- This is a **specific editable tree** (not just any FIRE press); touching an incorrect tree or the stone alone does not open the resonator. No hit point, score, boss, or enemy.
- The edited tree is a real PF/collision change. Act I changes persist, Act II echoes reverse the edit after 3/5 beats, and Act III phase inversion and the Presence constrain timing. This is designed to create distinct timing consequences rather than arbitrary key presses.
- The gate can close again if an echo restores the target. Cursor teleposition does not set the gate. The owl cannot complete solely by waiting.
- This is an **initial implementation candidate**; target-tree clarity, deadlocks, and achievable true-joystick solutions remain to be demonstrated. Do not claim artistic final acceptance.

## New per-room physical forest changes
The five original base silhouettes are preserved as motifs, but Acts II/III each preclear one distinct physically mutable tree at `LoadRoom`. `ToggleTree` modifies both actual PF memory and collision bits, not just a printed map. Table indices are half-board group keys = `5*y+x` (reflected).

| Room | Gate group (must clear) | Precleared group on entry | Rhythm |
|---|---:|---:|---|
| I-01 | 12 | none | permanent tree, first lesson |
| I-02 | 21 | none | edge-tree resonance |
| I-03 | 22 | none | stone polarity |
| I-04 | 8 | none | elevated obstruction |
| I-05 | 12 | none | two reflected sides |
| II-01 | 12 | 17 | time-limited echo |
| II-02 | 21 | 12 | stone/echo |
| II-03 | 22 | 13 | two pending events |
| II-04 | 8 | 17 | denied/intercept feedback |
| II-05 | 12 | 18 | remembering |
| III-01 | 12 | 23 | phase-swapped traversal |
| III-02 | 21 | 27 | inverted clearings |
| III-03 | 22 | 28 | Presence interception |
| III-04 | 8 | 23 | polarity/phase disagreement |
| III-05 | 12 | 27 | all three systems |

Exact digital provenance: `rom/src/data.inc` arrays `RoomGateKey`/`RoomPatchKey`, `reference/rooms.py` `GATE`/`PATCH`, `reference/rooms.json`.

## Audio change
Title and Act I use native TIA AUDC $04 tonal channels with slow low AUDF values. The title explicitly uses index zero even after a late-act reset or coda. Presence warning/active changes AUDC1 to noisy $08 with intermittent eight-frame impulses and quieter spans. No PCM recording has been modified or inserted into the cartridge.

## Remaining non-negotiable tests
1. Native DASM exact artifact, <=16,384B, no changes to PR4/PR16.
2. Actual 15×600s real Stella **idle** (model-only 500 beats is *not* emulator evidence).
3. 15/15 normal real Stella and Gopher joystick/FIRE wins, with coda and input logs, no POKE.
4. Each room's correct-target success and wrong-target counterfactual with state/raster logs.
5. 262 NTSC frames and worst-case 76-cycle beam/RIOT stack, audio recordings and human listening review.
6. User review of how a player recognizes the resonant tree. Current design may be too cryptic; do not claim gameplay certification until resolved.

## Compatibility
ROM source currently remains a 4 KiB unbanked candidate; **no F6 banking has been implemented**. This is within the hard 16 KiB limit, but must not be called F6 in evidence. All 30 techniques are reviewed separately in `docs/TECHNIQUE_30_AUDIT.md`.
