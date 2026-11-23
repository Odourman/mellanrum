# MELLANRUM / ROM DEVELOPMENT – Issue #8 implementation and evidence handoff

**Date:** 2026-11-22. **Status:** `NATIVE_DASM_BUILD_PASS` + `DEVELOPER_MODEL_PASS` + `STELLA_VISUAL_OBSERVED`. **Not:** independent Verification, complete real-emulator campaign PASS, hardware approval, merge or release.

## Authority, immutable code and build

- Binding authorization: [MAIN order](https://github.com/Odourman/mellanrum/blob/main/docs/MAIN_TO_ROMDEV_TITLE_AND_PRESENCE_2026-11-22.md) and [Issue #8](https://github.com/Odourman/mellanrum/issues/8).
- Base ROM: GitHub draft PR #4, source commit `8bdecde79a6bc1ecb804484d5d257f4f1a99b052`, SHA-256 `ec791333da37613ec99ea70b2a983ecc1666b4e576211ece41a8e40bd14cbaed`.
- Revised PRODUCT source code commit: `6f6319be31985ea9009b7c21988f2977f1509e46` on `romdev/fullgame-20261122`. Subsequent evidence/docs-only commits preserve the identical product bytes unless explicitly noted.
- Revised ROM: `rom/bin/mellanrum_ntsc.bin` / `build/mellanrum_ntsc.bin`; **4,096 bytes**, standard 4 KiB NTSC, **SHA-256 `a9531d5bbbff033711fbe54f8688b8e0259640e0a9a284c8ab585eea415c0bd5`**.
- [Native DASM and development tests](https://github.com/Odourman/mellanrum/actions/runs/45072844664): SUCCESS. The exact native DASM ROM was downloaded from artifact `14773519887`, ZIP CRC good, bytes matched local developer assembler ROM. Current source data generator and source geometry remain exact.
- [Existing static+native optional DASM CI](https://github.com/Odourman/mellanrum/actions/runs/45072844641): SUCCESS.
- [Existing Stella boot smoke](https://github.com/Odourman/mellanrum/actions/runs/45072844669): SUCCESS.
- [New real Stella multi-screenshot run](https://github.com/Odourman/mellanrum/actions/runs/45072837947): SUCCESS; artifact `14773997555` includes **145 PNG frames**, 11 explicitly instrumented room/beat variants, PNGs, assembler listings, ROM hashes, and raw Stella logs. Original ZIP CRC verified.

## Exact approved changes

A. The TITLE displays precisely one full word, **MELLANRUM**, on a single horizontal line, encoded as 40-bits per glyph row and drawn by real TIA left/right PF register updates. Existing SELECT toggles KAMPANJ/FRI SKOG and FIRE starts the selected mode. The game does **not** draw textual KAM/FRI words. Two non-text conifer/branch symbols are distinguished by selected bright vs dim color. Genuine Stella screenshots: `evidence/issue8/title_campaign.png`, `evidence/issue8/title_free_forest.png`, `evidence/issue8/STELLA_TITLE_TWO_MODES_CONTACT_SHEET.png`.

B. During V5.1 foreshadow and active Presence states, a *purely visual* 24-frame on/40-frame off interruption of PF2 sculpts a short-lived hollow, incomplete, eye-less gap between reflected conifer silhouettes. Warning uses only crowns, active uses crown+stem; release returns to normal. No new enemy sprite, TIA object, AI, hitbox, collision-map write, phase change, echo change, stone-state rule change, joystick change, exit rule or randomness. Live TIA PF register updates in actual Stella evidenced for **III-03, III-04, III-05**.

## Test matrix (source-derived / real-emulator distinctions)

| Test | Result | How checked / limitations |
|---|---|---|
| Original reference source unit tests | **PASS 20/20** | Python reference only; source `rooms.json` unchanged |
| Original 15 geometry and solution witnesses | **PASS 15/15** | CPU 6507 developer machine code vs Python oracle |
| Additional deterministic/randomized development tests | **PASS 225 runs / 4352 ticks** | Not real emulator button replays |
| Dynamic mirrored tree operations | **PASS 20** | `check_playfield.py`; actual `pfbuf` byte checks |
| Title exact word data | **PASS** | `check_title_presence.py` reconstructs all 40 PF bits / 9 glyphs; no extra title word tables |
| SELECT/FIRE/RESET and original two modes | **PASS** | Original developer `check_input.py`; SELECT mode changes also pictured in Stella; frame-exact real gameplay input not proven |
| Presence scheduled warning/active/release | **PASS** | `check_title_presence.py` cases for III-03/04/05, existing authoritative `UpdatePresence` unchanged |
| Presence renderer does not alter map or collision geometry | **PASS** | 48-byte `pfbuf`, 8-byte `mapRows` snapshot compare before/after `RenderPlay` |
| Title & 15 room developer raster | **PASS** | Developer 6502/RIOT/WSYNC model observed stable 262 NTSC scanlines; *not independent Stella raster analyzer* |
| Native production ROM, SHA, byte equality | **PASS** | Real DASM in Actions vs separate Python subset assembler; 4096 bytes |
| Actual Stella title, exactly one readable word | **OBSERVED PASS** | Uninstrumented production ROM screenshot, single horizontal `MELLANRUM` and no other on-screen words |
| Actual Stella menu selection | **OBSERVED PASS** | `xdotool F1` SELECT changes active visual icon, single word stays unchanged |
| Actual Stella Presence III-03/04/05 | **OBSERVED PASS** | Real TIA frames of *instrumented Reset-only room/tick variants*; paired active off/on at same room and tick plus after |
| Actual Stella visible pixel change | **PASS** | Central-forest on/off delta: III-03 **1616**, III-04 **1518**, III-05 **2022** pixels in identical game state; warning stage delta 680/582/662 |
| Actual Stella full 15-room campaign with real joystick replay | **NOT_RUN** | Separate Pachinko 2.0 and independent Verification required |
| Real emulator TIA scanline and collision-register analyzer | **NOT_RUN** | Only developer cycle model plus Stella observation, not pixel-accurate timing certification |
| Audition of actual Atari sound / WAV measurement | **NOT_RUN** | Audio logic was unchanged; no new audio evidence claimed |
| PAL / original physical Atari | **NOT_IMPLEMENTED / NOT_RUN** | NTSC candidate only |
| Independent VERIFICATION, artistic acceptance, release | **PENDING** | MAIN / Pachinko 2.0 / separate Verification |

## Reproducible visual method and important caveat

The `scripts/make_visual_evidence_rom.py` test generator takes the **same production assembler source** and creates a **separate instrumented Reset variant** for each targeted source room and logical tick. The variant initializes `room`, `mode`, `beat`, calls original `LoadRoom` and `UpdatePresence`, and holds normal owl beat countdown for the screenshot window. **Its code / hash differ from the ordinary product ROM**, but the original TIA raster code, original material geometry, and dynamic shadow renderer are unchanged. Real Stella 6.7+ running on Xvfb draws and saves the PNGs via F12; there is no fabricated graphics screenshot. Two frames from the same active tick prove the 24-on/40-off visual gate works. These variants are **not** proof that a complete player-run campaign navigated to those states.

The annotated contact sheets place labels *outside* the original 320×228 screenshots; the 16 individual source PNGs are byte-unchanged from Stella's artifact and include SHA-256 in `evidence/issue8/README.md`. `scripts/check_visual_captures.py` now requires substantial actual center-screen pixel differences for active + warning states, not just file existence.

## Artistic/technical deviations and outstanding gates

The silhouette is deliberately a central **geometric negative-space tear**, not a separate creature, face or eyes; reflection retains a formal symmetry. Whether it is disturbing and sufficiently incomplete is **MAIN's artistic decision**, not something Python can certify. No fourth material object appears, and no screen-flash. The title's two icons are nonverbal and do not explain their semantic meaning on-screen; external manual/packaging must document left=campaign, right=free forest. Title frame under developer model remains exactly 262 scanlines, though two blank boundary wraps occur in the visible-title routine.

**Do not merge or release without separate MAIN authorization.** The old full-system/Pachinko report applies only to original SHA and must be rerun against `a9531d5b...`, with independent Verification separately performed for the exact commit and ROM bytes.
