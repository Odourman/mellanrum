# MELLANRUM — GRAPHICS PR61 FINAL VISUAL POLISH (MAIN V)
## 28 November 2026 | SOURCE_ONLY DESIGN / NO PRODUCT EDIT

**Immutable base**: [Draft PR #61](https://github.com/Odourman/mellanrum/pull/61) commit `cc549ee106be4fe1ec801eedeb00c677ec5c37e1`. Standard NTSC Atari 2600 F6 ROM, 16,384 bytes, SHA256 **`ef23e846b6b5ed9ba120ffbced01670d1bd29cf7b8cb2d0dcce841820bb81bf8`**. The currently reviewed PR61 is a playtest candidate, **NOT a verified release**.

**Full output**: [MELLANRUM_GRAPHICS_PR61_FINAL_VISUAL_POLISH.zip on Google Drive](https://drive.google.com/file/d/1woDTOjsFVYDpRpcn3DCYuucXrYmmpk26/view), archive SHA256 **`989dca91ed05c9938fa1f8c3919f2e83ca268b492c1abe0da512c62a89495e20`** (1,812,351 B; 161 members; CRC PASS; 160/160 file checksums). The ZIP contains **26-page PDF**, Swedish 36K-character technical/art thesis, **actual PR61 source/video-derived 15 before images**, **15 source-only after previews** in normal and alt phases, colors, owl, marker, coda/title, presence, runnable offline Python renderer, full exact 15-room PF data, and original unmodified user-supplied review ZIP.

A portable extraction-and-replay test regenerated all fifteen before/after model rooms and palette/asset derivations; static mask checks (15 source rooms, 12 canonical owl frames, 4 marker states) PASS. This is **NOT actual ROM or emulator evidence**. Supplied original 34 ZIP entries CRC PASS and 33/33 source manifest SHA PASS.

## Critical artistic observations
- PR61 conifers can look like crosses or blocks, not obvious pointed trees. The strongest proposed **B** uses stepped crown PF0: `$20 → $60 → $F0`, with additional mid-crown PF1/PF2 masking, and would require a real new kernel timing proof. Lower-risk **A** uses 8×4 source-family mask and simple crown constants; it makes a smaller, more affordable visual difference. Both are **design alternatives**, NOT a mandate to replace trees.
- **Higher user decision**: on 2026-11-24 [Issue #40 comment 7127852893](https://github.com/Odourman/mellanrum/issues/40#issuecomment-7127852893) the user said further tree polishing should stop. The new MAIN V GRAPHICS research order can explore but **cannot silently cancel this accepted product appearance**. MAIN/user should decide on any future actual tree change.
- Luminance proxy from actual supplied PR61 recorded video: II-02 **1.07:1**, III-03 **1.33:1**, III-04 **1.33:1**, III-05 **1.24:1**. Digital two-dominant-color ratio, not a WCAG standard or calibrated NTSC CRT. This is the most consequential immediately testable contrast/readability finding.
- Proposed TIA NTSC graphics palette `BG A0 A0 F0 02 04`, `PF B6 B6 B8 B8 B8`, `OWL 0E 0E 0C 0E 0E`, `GLYPH 3A 3A 38 3A 3A`, five shared `act + phase` slots. **Synthetic RGB LUT cannot prove** this exact palette on actual Stella/Gopher. Existing code `(room & $06) XOR PalettePF` changes TIA luminance with room index; source review should isolate this risk before any replacement.
- MAIN V reported **522 large video-image changes** (Act I 237 / II 273 / III 12). Independent 20-frame start/exit excluded procedure reproduced **506** (235 / 267 / 4). These have different windows and do **not** demonstrate a ROM bug. Request same-SHA native register traces at video frames 61–82, 318–338 and 831–946; do not suppress intentional Presence animation.
- **U3 OWL MUST BE PRESERVED:** 4 directions × 3 wingmask, mirrored U3 with vertical beak. No repaint/rebytes. Rendering-only vertical sub-band-position concept: offsets 0/4/8/12/16, no gameplay step interpolation, implementation only after separate approval.
- Current **STONE S3-A** (two polarities) must remain. Exit is **user-approved orange RIGHT ARROW** top-down `08 0C 0E FF FF 0E 0C 08` as explicitly approved 2026-11-24 in [Issue #46 comment 7138111730](https://github.com/Odourman/mellanrum/issues/46#issuecomment-7138111730). Do not restore obsolete S3-B proposal.
- Cursor local M0+BL, while P0 HUD holds 8×8 status. New same-position 4-state two-column local negative-space sketches are in ZIP, shapes must be verified in real native 1×. Color alone cannot distinguish accepted/denied/intercept.
- Presence already has three PF2 visual states; no new monster sprite. Preserve coda gradual transformation, 15 room collision logic, all gameplay and real TIA sound.
- Main PR61 audio strict PCM byte-parity **FAIL** persists and cannot be cleared by new graphics studies.

## Feasibility classes
A: Palette & 32-byte crown family/marker table **ART_ONLY** concepts, lower risk but need native testing and design authorization.
B: 3-stage crown and vertical U3 movement, needs narrow ROMDEV kernel modification + worst-case scanline proof.
C: extra title subtitle pass, new localized 8×8 on playfield, significant feasibility risk.
D: reject 32KiB, new RAM/cart coprocessor, conventional monster or high-frequency flicker.

**Budget**: 128B RIOT, ~118 variable bytes, 2 protected reserve, 8 active stack bytes; critical Stem13 75/76 CPU cycles. F6 16,384 max. No assumed spare sprite or additional scanline.

## Requested MAIN V action
Review full PDF and 15 rooms, prioritize **contrast and four actual local marker appearances**; separately diagnose pulse cause; only then consider whether owl-Y interpolation warrants implementation; do not reopen tree appearance without explicit user choice given Issue #40. All scope decisions and actual ROM tests remain MAIN/ROMDEV/independent Verification.
 
**Classification**: GRAPHICS_SOURCE_ONLY_DELIVERED / PORTABLE_MODEL_PASS / PRODUCT_UNCHANGED / NEW_STELLA_NOT_RUN / NEW_GOPHER_NOT_RUN / PHYSICAL_NOT_RUN / INDEPENDENT_NOT_RUN / NO_RELEASE.

**Technical data**: [PF art-only tables](TREE_ART_ONLY_TIA_TABLES.inc), [candidate color/cursor JSON](PALETTE_AND_MARKER_ORACLE.json). All source-room data/PNG/model generator are in the pinned Drive ZIP. The older independent same-day exploratory branch `graphics/pr61-final-visual-polish-20261128` is **not** the source for the above ZIP; use this date- and hash-matched documentation record when reading that ZIP.