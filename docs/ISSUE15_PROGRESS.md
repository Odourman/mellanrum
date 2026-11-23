# MELLANRUM – Issue #15: user-authorized completion, developer candidate

This is a **new**, distinct production candidate. The immutable baseline draft PR #4 at `49eb168b17d0254d06cf50d87c60e8fb6016db6e` and reference ROM SHA-256 `e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974` remain unchanged.

## Integration source
- Source basis: frozen 15-room product ROM code, with the independently tested Issue #14 source-backed PF/dual-P1/M0 kernel copied into new candidate.
- U3: 3 real, original horizontally-mirrored U3 owl frames with vertical beak, exact latest user-approved masks B0/B1/B2, 72-frame beat animation (B1 6 → B2 6 → B1 6 → B0 54), animated rendering only; no AI/tick changes.
- S3-A and S3-B: exact preferred GRAPHICS/user masks top-down: A `18 24 42 24 18 24 5A 24`, B `42 66 3C 24 5A 3C 66 42`. Same P1 channel with `NUSIZ1=$04`, mid-scanline second `GRP1` write.
- Presence B: exact 3-state original `c_or/c_and/s_or/s_and` from `ANIMATIONS_DATA.json` branch `graphics/mel046-u3-s3-presence-animation-20261123`, scheduled 8 frames each during preserved 24 visible / 40 invisible window, using `moveTemp`/`workY`/`candidateD` scratch during display; identical actual collision data and Presence interaction rules.
- P0 U3 full bitmap, M0 1/2/4/8-wide cursor status, BL spare; green PF across all acts; TIA owl color linked to M0 cursor.
- Physical EXIT offset −4 TIA color clocks relative to E9EA; no logical room coordinate/physics change.
- NTSC overscan `WSYNC` correction from the *diagnostic only* Issue #14 isolated fix; actual E9EA 261 in Gopher is not rewritten.

## Source/reproducibility
`build_issue15.py` regenerates `rom/src/main.asm` and `rom/src/data.inc` from pinned Issue #14 diagnostic source snapshot in `diagnostics/issue14/rom/src/`; all artwork bytes are spelled out. Compare regenerated source and exact original GRAPHICS source arrays. Original `reference/rooms.json` is unchanged.

## Current test evidence
- Source check: 20/20 Python model unit tests, 15/15 room solver records.
- Local 6507 subset assembler generated a full 4096-byte ROM. **This is not native DASM** until actual GitHub Actions native DASM builds it and performs exact byte comparison.
- 15 native Gopher2600 real TIA original room screenshots with diagnostic room POKE: **2880/2880** U3-B1/S3-A/S3-B bits match the user masks; *not* 15 normally played rooms.
- Gopher2600 native continuous raster with 300 `STEP FRAME` commands, FIRE/SELECT/RESET: boot partial 20, **299/299 subsequent frames at 262 scanlines**.
- Actual game logic via original 6507 execution against reference oracle: 15/15 solutions and 225 extra seeded model sequences, 4352 ticks. This is a separate developer CPU test, not native emulator full-playback.
- The bespoke CPU/RIOT frame model counts 263 nominal lines while true native Gopher reports 262; developer model overcounts the old source by one line as well, so native TV FRAME is the raster acceptance evidence.

## Remaining tests / acceptance
- Native DASM CI and exact artifact hash: PENDING.
- Same-Y/different-Y final masks at all 15 in native Stella: PENDING.
- 15/15 normal real Gopher controller input-driven campaigns and coda: PENDING.
- FRI, A/B, cursor feedback actual input paths, sound WAV and human listening: PENDING.
- ROM timing worst-case per scanline independent beam/cycle trace, dynamic stack watermarks, hardware RetroN77, independent Verification: NOT_RUN.
- MAIN design-review of the real native screenshots, sprite overlap, +1 WSYNC and 4 color clock anchor shift: PENDING.

No merge, release or canon change is authorized by this document.

**Candidate local ROM SHA-256 (subject to native build):** `45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7`.


---

# ROM DEVELOPMENT completion evidence (2026-11-23) – SUPERCEDES the historical PENDING statuses above

**Developer candidate is implemented and cross-emulator gameplay-tested. This is NOT an independent Verification or release approval.**

**Exact product ROM:** real native DASM unbanked NTSC 4096 B, SHA-256 `45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7`. Native DASM byte agreement / full .lst + .sym: [Actions #45090981800](https://github.com/Odourman/mellanrum/actions/runs/45090981800), artifact `14781417357`. Baseline PR #4 still Draft at `49eb168b17d0254d06cf50d87c60e8fb6016db6e`, original E9EA SHA unchanged.

| Developer acceptance case | Actual status / source |
| --- | --- |
| Native DASM 4096B, all exact bytes matching independent assembler | **PASS**, artifact `14781417357` |
| Original reference, 15 solutions, CPU test witnesses | **PASS**, 20/20 + 15/15 +225 seeded model runs; not emulated full gameplay |
| Real Gopher 15 rooms and U3/S3 masks | **PASS**, 2880/2880 bitmap bits; forced-room diagnostic screenshot only; artifact `14780579153` |
| Real Gopher 262-frame with normal FIRE SELECT RESET | **PASS**, 299/299 steady frames (cold first frame 20); same artifact |
| TWO full Gopher controller-only real campaigns and coda | **PASS**: 15/15 room wins twice, 166/166 actual RAM checkpoints and 166/166 262-lines per run, 11,548 frames per run, NO POKE. [Actions #45090981800](https://github.com/Odourman/mellanrum/actions/runs/45090981800), artifacts `14781244035` & `14781407818` |
| Real stock Stella title & both S3 glyphs at original PF/P0 | **PASS** after right-glyph screenshot crop correction, original 320x228 images left=36 and right=52 positive signal pixels. [Actions #45091226339](https://github.com/Odourman/mellanrum/actions/runs/45091226339) artifact `14781640972` |
| TWO complete Stella/libretro 15-room full-game normal joystick runs | **PASS x2**: original scripted input and byte-exact replay, 15 identical win-frame positions, 11,420 frames/run, coda to title at frame 11,419, actual read-only RAM and Presence III-03/04/05, 86 original PNGs per run, same exact timeline. [Actions #45091957175](https://github.com/Odourman/mellanrum/actions/runs/45091957175) artifact `14781568322` |
| Genuine Stella TIA PCM WAV | **PASS**: two 900-frame native Stella recordings KAMPANJ and FRI SKOG 31,440 Hz stereo, nonzero samples [Actions #45091878941](https://github.com/Odourman/mellanrum/actions/runs/45091878941) artifact `14781408384`; full 15-room campaign stereo WAV 5,983,556 samples (circa 190 s) in full Stella artifact `14781568322`. **Listening/subjective audio quality not verified.** |
| Genuine Stella FRI SKOG adversarial and long stress | **PASS**: BOG, CLOG, TILT_FIRE 2,500 frames each, and seeded TILT_STONE 50,000 frames; total 57,500 actual core frames, read-only RAM remained mode4 in each post-start checkpoint, no crash or lost video callbacks. [Actions #45092117212](https://github.com/Odourman/mellanrum/actions/runs/45092117212) artifact `14781203467` |
| Native Gopher HEADLESS audio-only CLI WAV trial | **INCONCLUSIVE** tool capture failed, no WAV despite two live TIA register traces. [Actions #45091424233](https://github.com/Odourman/mellanrum/actions/runs/45091424233). Fixed by using REAL Stella/libretro PCM callbacks above instead of inventing audio. |
| Physical Atari, PAL, dynamic stack highwater, independent per-register beam-cycle trace, accessibility/human play & art approval | **NOT_RUN / INCONCLUSIVE**; final separate Verification and MAIN release authorization pending. |

**Binding art/data:** exact latest mirror U3 B0/B1/B2 9-byte glyphs, selected S3 pair, Presence B three mask states; originals pinned in `art_sources/`. 15 reference room coordinates/physics and A/B start remain unchanged, S3 exit only -4 visible colorclocks versus old, owl and marker share P0 hue, owl overlaps may obscure symbol pixels. Corrected 262 real Gopher frames do not represent a physical Atari measurement. The earlier 263 developer trace is a known +1 discrepancy from native Gopher, **not** proof the product is 263 lines.

**No merge, no release.** MAIN should commission independent VERIFICATION/PACHINKO targeting only the new ROM SHA above, request actual artwork/human play acceptance, then separately decide release. Full reproducible downloadable ZIP + SHA256 manifest supplied in ROM DEVELOPMENT chat.
