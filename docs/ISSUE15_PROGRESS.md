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
