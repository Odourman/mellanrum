# MELLANRUM – Issue21 gameplay canon delta (developer proposal, not release canon)

Source: Issue21 explicit full production scope, base PR16 immutable HEAD `56d70c316031bf55a5260e1fbbe0fe187c55f297`. All 15 new room geometries, owl starts, stone/exit positions and source-model solutions are implemented on the separate vNext branch. Old PR16 and PR4 must not be altered.

## Root cause and actual rule change
Prior Stella experiment Issue19 shows 14/15 baseline rooms autonomously won under no input (827..3995 frames), a gameplay BLOCKER. New rooms are not mere waiting extensions: each is a different reflected forest arrangement, with owl/stone/exit reauthored and at least one specific necessary action witnessed in the deterministic source model. **New semantic change:** cursor hovering on a mutable tree no longer silently opens that cell for the owl; only accepted FIRE edits change it. This prevents opaque passive cursor routing and aligns input replay with the conceptual solver. Independent gameplay approval still outstanding.

## Room-by-room source differences (coordinates = logical 10×8)

| Room | Owl start old → new (x,y,d) | Stone old → new | Exit old → new | Trees/geometries | Source solution beats | Critical action omitted | Source 600-beat passive |
|---|---|---|---|---|---:|---|---|
| I-01 | 1,3,0 → 1,5,3 | 4,3 → 4,5 | 8,3 → 8,2 | revised, unique | 12 | beat 0, tree 21 | NO_WIN (source) |
| I-02 | 1,2,0 → 1,2,0 | 4,4 → 4,2 | 8,2 → 8,3 | revised, unique | 10 | beat 5, tree 8 | NO_WIN (source) |
| I-03 | 1,4,0 → 1,5,2 | 4,3 → 4,3 | 8,4 → 8,4 | revised, unique | 8 | beat 1, tree 22 | NO_WIN (source) |
| I-04 | 1,3,0 → 1,4,0 | 4,2 → 4,3 | 8,3 → 8,2 | revised, unique | 9 | beat 0, tree 22 | NO_WIN (source) |
| I-05 | 1,3,0 → 1,2,0 | 4,2 → 4,4 | 8,3 → 8,3 | revised, unique | 8 | beat 3, tree 19 | NO_WIN (source) |
| II-01 | 1,3,0 → 1,3,0 | 4,3 → 4,4 | 8,3 → 8,3 | revised, unique | 8 | beat 0, tree 17 | NO_WIN (source) |
| II-02 | 1,2,0 → 1,4,0 | 4,4 → 4,5 | 8,2 → 8,5 | revised, unique | 10 | beat 0, tree 22 | NO_WIN (source) |
| II-03 | 1,4,0 → 1,2,0 | 4,3 → 4,4 | 8,4 → 8,2 | revised, unique | 9 | beat 0, tree 12 | NO_WIN (source) |
| II-04 | 1,3,0 → 1,2,2 | 4,2 → 4,4 | 8,3 → 8,4 | revised, unique | 17 | beat 4, tree 22 | NO_WIN (source) |
| II-05 | 1,3,0 → 1,2,2 | 4,2 → 4,2 | 8,3 → 8,5 | revised, unique | 12 | beat 2, tree 8 | NO_WIN (source) |
| III-01 | 1,3,0 → 1,4,1 | 4,3 → 4,5 | 8,3 → 8,2 | revised, unique | 20 | beat 3, stone -1 | NO_WIN (source) |
| III-02 | 1,2,0 → 1,5,0 | 4,4 → 4,3 | 8,2 → 8,3 | revised, unique | 13 | beat 0, tree 27 | NO_WIN (source) |
| III-03 | 1,4,0 → 1,2,0 | 4,3 → 4,5 | 8,4 → 8,2 | revised, unique | 10 | beat 4, stone -1 | NO_WIN (source) |
| III-04 | 1,3,0 → 1,4,0 | 4,2 → 4,4 | 8,3 → 8,3 | revised, unique | 10 | beat 0, tree 23 | NO_WIN (source) |
| III-05 | 1,3,0 → 1,5,2 | 4,2 → 4,5 | 8,3 → 8,5 | revised, unique | 13 | beat 1, tree 28 | NO_WIN (source) |

## New audiovisual design
Title and Act I TIA low drone sources use `AUDC0=$0C` rather than crackly `$08`, with lower `AUDF0=$1C/$1D`. The title audio resets its sound-table selection instead of inheriting the previous act. Presence gains rare AUDC1 noise in warning and a short active pulse followed by silence. Changes are two-channel TIA hardware only; listening/art acceptance pending. U3 owl's 3 locked frames, PF green evergreen trees, 2 S3 symbols, negative Presence three-state animation, title and coda remain.

## Evidence discipline
- 15 unique source rooms and solution witnesses/600-beat passive/omission counterfactual are SOURCE_ONLY until native emulator reproduces them with controller-only input.
- Previous 4KiB PR16 SHA and successes are not vNext gameplay evidence.
- New exact ROM SHA and CI artifacts must be recorded after any final source edits.
- New rules and maps require independent Verification/Pachinko and MAIN/user final artistic/level acceptance; **NO MERGE OR RELEASE**.
