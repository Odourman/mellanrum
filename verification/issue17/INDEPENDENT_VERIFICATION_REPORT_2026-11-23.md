# INDEPENDENT VERIFICATION — MELLANRUM PR #16 (2026-11-23)

**Overall verdict: INCOMPLETE — release blocked.** This is an independently executed, bounded verification run for [Issue #17](https://github.com/Odourman/mellanrum/issues/17), *not* a release approval, merge instruction, or substitution for PACHINKO #18.

## Exact identity
- Candidate: Draft PR #16, immutable source HEAD `56d70c316031bf55a5260e1fbbe0fe187c55f297`; branch untouched.
- Native-DASM-built **artifact originally produced by ROM DEVELOPMENT**: Actions artifact `14781417357`, binary `candidate.bin`, **4096 bytes**, independently recomputed SHA-256 `45d3422371d41bf896c0ac0076c57d93e600dcf7f4a1e51d4d352312fce8d7a7`.
- `candidate.bin` and sibling artifact `issue15_native/local_subset.bin` are byte-identical; this is not a separate native DASM rebuild.
- Runtime: independently launched Linux Gopher2600 HEADLESS from archived executable artifact `14780574047`, upstream pinned source `74c544203378c1448a33c29bc8b4586079b050f4`, executable SHA-256 `7b12dff57fcb73154122d2477f35d9c8ae8b344649bc0faa8ff6f5663c70470b`. Emulator's version command reports `unreleased`.

## Independently executed tests

| Test | Bounded outcome | Evidence |
|---|---|---|
| PR HEAD + ROM bytes + 4 KiB identity | **PASS** | Live PR metadata, independent downloaded-artifact SHA, cmp |
| Reset/IRQ vectors | **PASS** | ROM bytes resolve to `$F000` each |
| U3 B0/B1/B2 and S3 A/B bytes in ROM | **PASS (static)** | Independent byte search at symbols OwlB0/OwlB1/OwlB2/GlyphA/GlyphB |
| Original-room geometry arrays internally match checked-in ASM data | **PASS (bounded)** | ROM byte checks of act/stoneX/exitX/geom arrays; original external ZIP provenance separate |
| Own seed-23017 controller-only smoke | **PASS (bounded)** | 293 Gopher frame steps, FIRE/directions/SELECT/RESET, **27/27** 262-line TV samples |
| Difficulty A campaign/B FRI SKOG | **PASS** | Active RAM mode 1 vs 4; switching difficulty midgame did not change mode; RESET returned title |
| Normal full-campaign replay | **PASS (one known trace reproduced)** | Developer artifact `14781244035` controller commands re-executed in a fresh Gopher process; **11,548 frames**, **166/166** TV samples 262; independent RAM parser observes 0→14 room completion, coda mode 3, return to title mode 0; **NO POKE**. Does *not* establish a second independently devised solution route |
| Native screen visibility | **PASS (bounded)** | 15 original independent Gopher screenshots; none blank, green PF and both orange glyphs visible; same-Y room 0 and different-Y room 12 confirmed by pixel-region bounds |
| U3 animation rendering | **PARTIAL** | 25 new Gopher screenshots over 73 frames following intro; 3 stable B0/B1/B2 visual groups correlate to read-only `beatFrames`; initial transitional B1 sample differs, exact full-run pixel conformity not proven |
| Own randomized FRI SKOG stress | **PASS (bounded)** | seed `51723`; **10,000 real Gopher steps**, 40/40 native TV samples 262, 5 original PNGs, normal process exit, no POKE; SELECT, RESET, FIRE and directional combinations |
| Two active TIA audio channels | **PASS (register activity only)** | Own Gopher AUDIO outputs show nonzero channel control and volume; no independently captured PCM or human listening |

**Important:** The 262 scanline counts are **sampled native Gopher TV reports**, not a per-frame proof for every one of the 21,841+ frames advanced in all tests. Neither 76-cycle beam-budget trace nor maximum dynamic stack depth has been independently measured.

## Confirmed defect
- **P3 DOC mismatch:** `rom/README.md` at the exact candidate commit falsely states “Ingen gameplay-ROM finns ännu” despite the new game ROM. Recommend later controlled documentation correction; do **not** modify the SHA-pinned product as part of this verification.

## Not-run / unresolved
- **NOT_RUN:** clean independent native DASM assembly (DASM not installed in verifier's isolated environment), stock Stella/libretro execution (Stella unavailable), original V5.1/GRAPHICS ZIP raw-byte hash provenance (Mellanrum Drive folder empty / originals inaccessible), true Stella TIA PCM WAV capture and human listening, 76 cycles/line timing trace, high-water RIOT/stack, actual hardware and RetroN77, complete all-frame raster count, exhaustive same/other-Y bitmap comparisons and broad gameplay edge-case matrix.
- **INCONCLUSIVE / user-owned gate:** final S3/Presence B/art palette/legibility, 4-colorclock exit visual offset, sound-off accessibility and subjective audio/flicker safety. PAL is **NOT IMPLEMENTED**, not PASS.

**Recommendation:** Keep PR #16 draft/unmerged/unreleased. The independently re-executed Gopher evidence is positive, but does not satisfy all independent release gates. MAIN should route unresolved tools, source provenance, beam/stack, native Stella/audio and independent Pachinko #18 results before separate final authorization.

## Raw evidence retained
The verification run created 94-file downloadable evidence ZIP (independent Python test scripts, exact command streams, raw stdout, parsed RAM checkpoints, original screenshots for 15 rooms, raster samples, JSON reports, binary artifact, SHA256SUMS, and 15-room contact sheet). SHA-256 of evidence ZIP: `a8787178600aff57a3ae9f598b2cd1e8e39443b52f9a4163feed1a0dad1490ae`. The ZIP is supplied to the user in the Verification chat; it has **not** been uploaded to GitHub and must not be represented as a GitHub artifact. No changes to product ROM, PR #16, frozen PR #4, or gameplay canon were made.
