# MELLANRUM PR61 GRAPHICS – TARGETED MODEL CORRECTION V2
**Date: 2026-11-28 | GRAPHICS / SOURCE_ONLY | NO PRODUCT CODE / NO ROM BUILD**

## Authority and exact source
- MAIN V defect report: [Issue #60 / comment 7241822918](https://github.com/Odourman/mellanrum/issues/60#issuecomment-7241822918).
- PR61 product source commit `cc549ee106be4fe1ec801eedeb00c677ec5c37e1`; ROM SHA-256 `ef23e846b6b5ed9ba120ffbced01670d1bd29cf7b8cb2d0dcce841820bb81bf8`, standard F6 NTSC 16384 bytes.
- Prior source-only GRAPHICS ZIP V1 `MELLANRUM_GRAPHICS_PR61_FINAL_VISUAL_POLISH.zip` / SHA `989dca91ed05c9938fa1f8c3919f2e83ca268b492c1abe0da512c62a89495e20` had **defective synthetic full-frame comparisons**. Earlier visual A/B interpretations are **RETRACTED**.
- **Corrected V2**: [ZIP at Google Drive](https://drive.google.com/file/d/17inLzY4zBLPd9-oGyfOB5IfplbpkxluO/view), filename `MELLANRUM_GRAPHICS_PR61_MODEL_CORRECTED_V2_20261128.zip`; local archive SHA256 `622bb6b1644633033ebbead5c89c6f0d69df4761d69f6779333c3be09ddbd1c2`, **2,431,265 bytes, 185 entries, CRC PASS, 184/184 SHA256SUMS PASS**. Drive upload succeeded and file metadata can be re-read.

## Root cause and exact corrective patch
In `08_MODELL/generate_all_graphics.py`, `source_mask()` returns 8-bit unsigned values, which are **array indices**, not boolean pixels when used with NumPy. `~mask` also returned 254 or 255 rather than logical complement. Fixed **inside** `recolor_model()`, before *any* image/mask indexing:
```python
mask, _ = source_mask(i, variant, phase, presence, presence_frame)
mask = mask.astype(bool)
```
This is a change **only to offline model code**, not the Atari assembly. Also corrected the compositor to avoid recoloring the HUD and all source pixels outside y=30..189, and marked every newly produced synthetic preview `SOURCE_ONLY / SYNTHETIC / NOT_STELLA_EVIDENCE`.

## Independently reproduced V2 synthetic image differences
Same native-equivalent **15 × 160 × 160 = 384000 pixels**, before vs model B:
- V1 falsely reported: **0 / 384000**. V2 now **308007 / 384000 changed**.
- Model A vs B: V1 **0 / 384000**. V2 **31376 / 384000 changed**.
- **15/15** original vs B; **15/15** A vs B; **15/15** phase0 vs phase1: source-only PASS.
- 5/5 sampled Presence rooms have actual source-mask differences.
- All source-video color pixels not classified as BG/PF, **2158/2158**, were preserved byte-identically; **0 overwritten** (not a general guarantee for objects sharing BG/PF color).
- Reflected PF mask: source PF0 bit 4..7, PF1 7..0, PF2 0..7; mirror, 8 double-video pixels/bit, 8 bands × 20 scanlines from y=30. The normal source orientation matches **81.6–93.6%** of actual source-video BG/PF two-color pixels in 15 rooms. The residual is model/video alignment and other object uncertainty, NOT exact pixel-level TIA parity.
- In all 15 sampled PR61 rooms the most frequent game-area RGB was classified BG, second PF; swap gives worse fit. Qualifying distance `min(dBG², dPF²)<1200`; unclassified objects and y>=190 HUD unchanged.

**Important art review:** With real RGB replacement active, Act II proposed green PF contrasts strongly but abandons some original red/brown character; Act III proposed green becomes potentially **too bright**. The V2 preview proves different images, **not better artistic choices**. Local 2-column cursor examples remain difficult to distinguish at 1×; no hardware claim.

## Files and reproducibility
The **complete V2 ZIP** contains:
- Corrected `08_MODELL/generate_all_graphics.py` and `validate_corrected_v2.py`, `run_model.py`, the original unchanged review archive for local replay.
- Corrected 15 before/after B images and 15 A previews, 15 A/B triptychs, 3 full-act contact sheets, all phase and Presence images, one same-room/same-position 4-state marker study.
- `10_KORRIGERING_V2/MASK_ORIENTATION_COLOR_OBJECT_PROTECTION_TESTS.json`, per-room `.csv`, technical bug report, corrected main 17-page PDF, updated 42K-char full MD report, archive `SHA256SUMS.txt`, exact version lock.
Run from extracted ZIP root: `python 08_MODELL/run_model.py && python 08_MODELL/validate_corrected_v2.py`. Recompute original manifest on a **fresh extracted archive** prior to re-running because the scripts regenerate outputs.

The previous user decision to **stop conifer revisions** remains in force for actual product; the new study does not authorize a ROM edit. The 12 accepted U3 owl appearances, S3-A stone polarity, user-approved amber right-arrow exit `08 0C 0E FF FF 0E 0C 08`, original 15 room semantics, 3 Presence stages, title, FRI and coda unchanged.

**PASS:** offline artifact CRC/sha, bool mask fix, 15-room source-vs-synthetic and A/B checks, phase/presence, detectable object preservation, orientation/color classification.  
**NOT_RUN:** new native ROM, Stella/Gopher, cycle/stack, human playtest, independent Verification, hardware tests.  
**INCONCLUSIVE:** subjective art, whether color-identical object pixels were overwritten, pulse RCA.

### Next
**MAIN V** should review V2 synthetic art and real 1× cursor contrast. Do not merge any "graphics" docs branch into product. ROM DEVELOPMENT may later get a *separate explicitly authorized* narrow task for contrast, cursor and pulse diagnostics only if MAIN decides; no change is authorized by this publication.