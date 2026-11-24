# Issue #43: Gate A - isolated COLUP1 stone-only feasibility probe

**Status:** SOURCE-ONLY FEASIBILITY / EMULATOR NOT YET RUN. This is NOT a final approval and is not based on a Stella screenshot.
Baseline: PR #38 exact HEAD `6e9db179867234a19cce329c709170f2423ffbbb`, untouched original ROM SHA256 `bfdeb5308dcecc526e802cd95886b94e0ce4953628e7bc7190c5d49231deac06`.

## Shared P1 problem

Actual original `Stem13` writes `GRP1` twice each scanline, left S3-A and right S3-B, separated horizontally by 64 TIA pixels from `NUSIZ1=$04`. Global `COLUP1` cannot be set red for the full line without recoloring S3-B in room indices 6,8,11,14 (II-02, II-04, III-02, III-05).

## Minimal diagnostic candidate

1. Preserve exact original `GlyphA`, `GlyphB`, U3 and all 15 room playfield and map *values*. Every original top playfield row is the same six bytes `F0 FF FF 60 66 66`; remove its 15 repeated copies and reconstruct the entire exact 48-byte `pfbuf` with 42 individual room bytes and six shared ROM constants during `LoadRoom`. This compression frees more than the added executable code in the 4096-byte bank-3 window without changing pixels.
2. Reuse existing `attempt` and `workKey` scratch bytes only after `GameFrame` and `SetColorsSound` game-state handling: store per-frame stone tint (old `PaletteGlyph` for polarity=0, provisional NTSC red `$46` for polarity=1), and original exit amber `PaletteGlyph` in the latter. No new RAM and no additional JSR nesting.
3. Original four mark bitmap arrays unchanged; preselect either original marker pointer or zero `BlankSprite` pointer on fifth crown line, retaining exact same per-scanline two-rail enable values but reducing the hot-loop mask work.
4. On each normal hot scanline: write stone `COLUP1` after WSYNC and before the left P1 copy, change `COLUP1` to original amber after its eight horizontal pixels and before the right copy. This is a horizontal within-scanline color split, not shared red.

## Preliminary instruction cycles (normal stem loop X = 9..2, including STA WSYNC)

| Event | Baseline latest completed cycle | Diagnostic completed cycle |
|---|---:|---:|
| WSYNC latch + color-left | 3 | 3 (WSYNC) + 3 (COLUP1) |
| First GRP1 load | 20 | 23 |
| M0 ENAM0 write | 35 | 35 |
| BL ENABL write | 48 | 48 |
| Color change to original amber | n/a | 54 |
| Second GRP1 load | 60 | 62 |
| DEX and taken BNE | 68 incl next WSYNC | 73 incl next WSYNC |

**Preliminary estimate**: normal loop 68/76 original, **73/76 diagnostic**, theoretical margin three CPU cycles. Final X=1 branch early-exits and has different PF bookkeeping; it is NOT included in this result and requires emulator/beam audit. The exact second P1 horizontal color latch is NOT proven by cycles alone. Even a 262-line frame does not prove untouched glyph appearance.

## Non-negotiable gates before new PR

- Native DASM 4*4096 and stock F6 vectors/hotspots, no new RIOT allocation/stack.
- First screenshot 1x II-02 and III-05 (initial polarity=1, then real selected polarity=0), both S3-A and S3-B on same y; glyph shapes, positions, output and adjacent PF pixels compared against original.
- Original `PaletteGlyph` for S3-B, actual legal NTSC red visual assessment for stone.
- Real STL/Gopher 262 raster sampled and worst exercised critical scanline cycle measurement incl last iteration, then 15/15, idle, causality, TIA audio if feasible.
- If any original copy's pixels/colors or timing changes unexpectedly: **FEASIBILITY_FAIL**; do not open approval PR.

All statements here are Gate A **hypotheses/test design**, not PASS for a new ROM.
