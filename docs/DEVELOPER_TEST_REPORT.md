# ROM DEVELOPMENT / Developer-only verification / 2026-11-22

**Status:** SOURCE/MODEL + strict-subset-6502 binary execution checks performed; true DASM CI result must be read in GitHub Actions. DO NOT label this independent verification or a certified game release.

## Performed locally

| Test | Measured result | Evidence level |
| --- | --- | --- |
| Source ZIP integrity and manifest | Both ZIPs `testzip()=None`; GRAPHICS 116/116 file hashes match | SOURCE_PASS |
| Exact 15 rooms and mask count | 15/15 room JSON matched final GRAPHICS; 25 masks | SOURCE_PASS |
| V5.1 unchanged Python unit suite | 20/20 pass | SOURCE_MODEL_PASS |
| Original abstract solutions | 15/15 solver traces found | SOURCE_MODEL_PASS |
| Local strict subset 6502 assembler | Genuine 4,096-byte 6502 ROM image emitted; this is **not DASM** | DEVELOPER_ASSEMBLER_ONLY |
| Binary-instruction CPU vs Python oracle | 15/15 source witness sequences reach exit, 134 ticks; 225 seeded random runs, 4,352 ticks, full state parity (owl x/y/direction, stone, phase and phaseAge, beat, echo slots, 8x5 collision, success) | DEVELOPER_BINARY_MODEL_PASS |
| PF dynamic regeneration | 20 editable mirrored tree groups, all 48 PF RAM bytes after each update equal independently generated 6+14 PF bands | DEVELOPER_BINARY_MODEL_PASS |
| Joystick/console switches | Title SELECT once per press, start both menus, horizontal movement/repeat, per-room SELECT reset, RESET title, held FIRE one-shot | DEVELOPER_BINARY_MODEL_PASS |
| CPU/RIOT/WSYNC budget | 945 sampled **gameplay frames** across all 15 rooms, 262 scanlines in custom cycle/WSYNC model; deepest stack pointer `$F7` | DEVELOPER_TIMING_MODEL_ONLY |
| True DASM native assembly | NOT_RUN locally, requires CI on pull request | NOT_RUN |
| Stella, Gopher2600 pixel/raster captures | NOT_RUN | NOT_RUN |
| Actual CRT/RetroN77/Atari 2600 hardware | NOT_RUN | NOT_RUN |
| Two-channel audio subjective audition | NOT_RUN | NOT_RUN |
| PAL 312-line/50 Hz ROM | NOT_IMPLEMENTED | NOT_RUN |
| Independent verification by separate role | NOT_RUN | NOT_RUN |

## Deviations and approximations

1. V5.1 suggested 16KiB F6; actual implementation fits a **4KiB native cart**. No added RAM or emulator-only game state.
2. **Title** uses a vertically segmented `MEL` / `LAN` / `RUM` textmark and abbreviated `KAM` / `FRI` mode indicators. A full-width independent word font is not built.
3. **Graphics** uses true PF geometry and original OWL_E_IDLE + CURSOR mask family; secondary bird flaps, local negative PF Presence seam, optional M1 chisel and most transitional illustration are omitted under performance/complexity fallback. Presence retains its state, altered action meaning, and visual HUD warnings.
4. **FRI SKOG** has no exit and uses deterministic seeding from title-frame counter to choose one of four existing Act III geometries. It is not an unbounded procedural environment.
5. **Audio** uses a small group of TIA sound patches under the two-channel limit, polarity/echo shifts and subtle subtractive silence. Actual listener-audition, level and palette calibration have not happened.
6. Coda is 8-second statically simplified normal forest plus one polarity turn, **not** the final single-tree art concept. This is an intentional interim visual simplification and needs art review.
7. Input edge near beat boundary: frame-poll before `GameFrame`, one accepted pending fire carried into next `BeatTick`; if the fire arrives in the first frame following a tick it is processed at the following tick. No input queue of more than one edge, but held fire does not duplicate.
8. Sprite P0/P1 and missiles occupy per-row 14-line band; exact per-scanline overlap, HMOVE bars, television overscan/safe margins and transient TIA resource conflicts need Stella/Gopher observation. CPU simulation cannot certify them.
9. Some Python reference witness traces position the cursor instantly rather than exercising every joystick transition; frame-input tests are separate and no full 15-room **frame-exact joystick-human-route** reproduction was completed. Do not treat the abstract 15/15 result as that stronger test.

**Release gate remains OPEN** until native DASM compilation succeeds, emulator image and real gameplay tests across 15 rooms pass, and independent verification is completed. The requested game logic is implemented but hardware release quality is not established by local model checks.
