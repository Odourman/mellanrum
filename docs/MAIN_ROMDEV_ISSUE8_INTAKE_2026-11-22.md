# MAIN – ROM DEVELOPMENT Issue #8 delivery intake / title and Presence

**Date:** 2026-11-22
**Disposition:** `DEV_REVISION_RECEIVED / NATIVE_ROM_SHA_VERIFIED / STELLA_VISUAL_EVIDENCE_SEEN / NOT_RELEASE_VERIFIED`.
**Project authority:** decision MEL-032 title; MEL-033 ambiguous Presence; MEL-037 future hardware A/B mode selection. No merge/release authorized.

## Identified deliveries and supersession

- [PR #4](https://github.com/Odourman/mellanrum/pull/4) HEAD `eea14339010306de635a8c6238e242b76b28cc64`, Draft, open, unmerged, checked by MAIN.
- Developer code commit `6f6319be31985ea9009b7c21988f2977f1509e46`; evidence/docs-only HEAD does not change production binary.
- **Final native DASM 4K NTSC ROM SHA256 `a9531d5bbbff033711fbe54f8688b8e0259640e0a9a284c8ab585eea415c0bd5`, size 4,096.**
- The developer's earlier `d1005a0a406b1a0def8a70964fb1c880d269cfe570b965957140dd0ee1eba87d` is an **intermediate**, not final. Old pre-visual `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed` belongs to prior source and Pachinko model-only results. No test result transfers to the new ROM by name alone.
- MAIN downloaded [native build artifact 14773519887](https://github.com/Odourman/mellanrum/actions/runs/45072844664/artifacts/14773519887). ZIP CRC good; extracted `mellanrum_ntsc.bin` measured 4,096 B and the final SHA above. Developer build CI [45072844664](https://github.com/Odourman/mellanrum/actions/runs/45072844664) was SUCCESS.
- MAIN downloaded [actual Stella evidence artifact 14774191179](https://github.com/Odourman/mellanrum/actions/runs/45073465951/artifacts/14774191179). ZIP CRC good, 193 entries; ROM therein also 4,096 B and final SHA. Real [Stella run 45073465951](https://github.com/Odourman/mellanrum/actions/runs/45073465951) SUCCESS at exact PR HEAD, original software screenshot files and test-only instrumented room ROMs separately identified.

## Visual inspection and scope limitations

- MAIN inspected real uninstrumented product-ROM title PNGs: nine characters **MELLANRUM** read across one line with no other words; two icon-like forms still switch selected brightness via SELECT. A first all-black boot snapshot `mellanrum_ntsc.png` is followed by correctly rendered title in `mellanrum_ntsc_1.png` and subsequent frames; don't mistake the first black frame for absence of title.
- MAIN inspected screenshot pairs of test-instrumented rooms III-03/04/05 from actual Stella. Jagged, symmetrical negative space visibly interrupts the center forest; no face/eyes or independent monster sprite. This supports visual manifestation for the renderer but **not** full ordinary-player reachability or timings in uninstrumented production ROM. In latest 450734 artifact, choose on/off comparison frames by **measured pixel difference**, not merely fixed suffix. The III05 active `_4` image can match `active.png` in this artifact; `_1` has a distinct image.
- Developer report: [ISSUE8_TEST_MATRIX_2026-11-22.md](https://github.com/Odourman/mellanrum/blob/eea14339010306de635a8c6238e242b76b28cc64/docs/ISSUE8_TEST_MATRIX_2026-11-22.md). 20/20 reference tests, 15/15 developer model room witness routes, 225 additional model runs, no new gameplay collision write, developer 262 NTSC-line timing. These are **developer reports/model checks**, not independent raster/video/gameplay certification.
- **Not run/verified:** 15/15 real joystick full campaign, full actual NTSC beam/cycle validation, real audio listening, independent Verification, physical Atari/RetroN hardware, PAL. The Presence's negative-space artifact is artistically provisional pending user review; passing pixel-difference thresholds is not psychological/aesthetic proof.

## Next user-approved dependency: A/B hardware-only mode selector

The user explicitly adopted **left physical Difficulty A = Campaign standard**, **B = FRI SKOG**. Only console hardware controls mode; joystick and SELECT cannot change it. FIRE starts whichever A/B position is active; title remains just MELLANRUM. Mechanical console's actual A/B switch position cannot be changed by ROM, therefore "standard campaign" means recommended/default when physically set to A, not that software overrides B.

MAIN issues a **separate post-#8 implementation order**: [MAIN_TO_ROMDEV_AB_HARDWARE_ONLY_2026-11-22.md](MAIN_TO_ROMDEV_AB_HARDWARE_ONLY_2026-11-22.md). Preserve previous work; modify no other canon. This yields **another new ROM SHA**. Pachinko 2.0 may build its CI harness on the `a953...` stable visual revision, but the **full final stress run must freeze the resulting A/B-updated ROM**. Verification remains independent; PR #4 remains Draft.

## Release verdict

`ARTIFACT_INTAKE_PASS / TITLE_REAL_STELLA_OBSERVED / PRESENCE_INSTRUMENTED_STELLA_OBSERVED / FULL_GAMEPLAY_PENDING / AB_REVISION_PENDING / NO_RELEASE_PASS`.
