# MELLANRUM VERIFICATION #42 - P0 follow-up, 2026-11-24

**Independent VERIFICATION. Status: INCOMPLETE for release.** Response to MAIN III's Issue #42 comment #7130612270. Product ROM and all production sources are unchanged.

Source HEAD: 6e9db179867234a19cce329c709170f2423ffbbb
Product commit: 9293c46eb323f47197046e07e1178279d6c7f525
ROM: rom/bin/MELLANRUM_16K_NTSC_F6.bin (standard NTSC F6 4x4096; 16384 bytes)
ROM SHA-256: bfdeb5308dcecc526e802cd95886b94e0ce4953628e7bc7190c5d49231deac06
Immutable Draft PR #38: https://github.com/Odourman/mellanrum/pull/38

## P0a - global reachable stack bound: PASS for valid codeflow

Independent purpose-built context-sensitive static analyzer, verified against exact original native DASM assembly listings and four actual ROM banks, traversed **2486 (bank, PC, call stack) states**, **34 distinct JSR sites**, both branch outcomes, JMP/RTS edges, all four reset vectors and F6 hotspot transitions. Deepest call depth **5 nested JSR**; no sixth call, unexpected jump, bad return, stack-underflow, reachable BRK/RTI/PHA/PHP/CLI. Only TXS is Reset (SEI, LDX #FF, TXS). Five JSR = 10 return-address bytes.

Game variable RAM is $80..$F5, physical stack free addresses $F6..$FF. Stack $01FF..$01F6 mirrors physical RIOT $FF..$F6; minimum SP $F5. Hardware 6507 lacks external IRQ/NMI pins. Reset starts bank 0-2 at $FF9A trampoline to bank 3 $F000, or directly bank 3 $F000. F6 score-bank transitions are shallower than Frame -> GameFrame -> BeatTick -> CommitFire -> ToggleTree -> DecodeKey. All indirect pointer accesses in traversed paths are reads, with no indirect JMP. Normal source-derived bank index X is 0, 1 or 2.

Dynamic confirmation: earlier independent CPU trace attained SP $F5 with no overlap. New strict native Gopher2600 WRITE watch at $01F5 over 780 controller-operated real FRI frames: **0 hits**; verified $01F5/$01F6 are mirrors of $00F5/$00F6.

**Conclusion:** 5 is the bound for this exact ROM's valid reachable program flow. Zero extra headroom does NOT establish an existing stack corruption. Proof assumes normal ROM/code/data integrity, ROM-derived valid act/score bank index; not arbitrary pre-corrupted RAM, unexpected hardware, or later code changes.

## P0b - native full campaign per-frame 262 NTSC: PASS (bounded); global CPU 76c: INCONCLUSIVE

New independent actual native Gopher2600 (unreleased, upstream source commit 74c544203378c1448a33c29bc8b4586079b050f4, executable SHA256 7b12dff57fcb73154122d2477f35d9c8ae8b344649bc0faa8ff6f5663c70470b) process replayed **19,780 genuine STEP FRAME controller frames** across 15 rooms, coda and title. Input reused a known solution witness, explicitly **SOURCE_GUIDED**, with joystick/FIRE, **NO POKE**. Process exit 0.

**20,058 native TV FRAME reports** (at least one after each step, plus 278 checkpoints): **20,057 reports at 262 lines**; one *initial incomplete boot frame* at 20 lines. Thus **20,057 / 20,057 postboot frame reports = 262 lines**. Separate seed-operated FRI test: 780 actual Gopher frames, 779/779 postboot at 262, initial incomplete boot 20 lines.

Additional instruction stepping using QUANTUM INSTRUCTION, ONSTEP TV,TIA,CPU: **8 real single-frame scenarios**, **31,859 instruction boundary records**, **1608 WSYNC observations**, 8/8 complete frames at 262. Act I FIRE/tick; Act II; Act III Presence inactive, warning, active plus variation; FRI; coda. Source-forced Presence tests with RAM POKE are explicitly DIAGNOSTIC, not controller-guided campaign evidence.

**Reproduced timing finding 2/2:** Act III active Presence, bank 3 PC $F68C executes STA WSYNC on scanline 6 at CL=157 (CPU cycle 75); next instruction begins scanline 8 instead of 7, hence one consumed **VBLANK-only** line. Frame stays 262; no proven visible kernel corruption. **Overall worst-case 76 cycles over every possible path remains INCONCLUSIVE**, since eight single-frame instruction runs are not an exhaustive all-path cycle proof. New independent Stella per-scanline/cycle instrumentation was NOT_RUN (prior same-SHA Stella independent gameplay exists, not a new CPU trace).

## P0c - F6 under entire genuinely controlled campaign: PASS for executed route

Same 19,780-frame native Gopher source-guided campaign, TRACE STRICT of all four real F6 hotspots:

- bank 0 through $FFF6: **5600**.
- bank 1 through $FFF7: **4711**.
- bank 2 through $FFF8: **7879**.
- total completed score bank call/return pairs: **18190**.
- bank 3 via $FFF9: **18191**, including one startup Reset trampoline.
- **zero wrong selected bank and zero unmatched score return**, correct PC mapping ($FF93 score, $FF99 return, $FF9D startup); observed hotspot SP $FB during score, $FD startup, never below $F5.

Independent analysis aligned the F6 trace to **15/15 controller-reached room windows**, 0 wrong act-bank selections, and 73 observed FIRE rising edges during the full input trace. These are observed input edges, not claims each FIRE invokes one score bank. The known campaign route is NOT a newly invented solution, and alternative edge branches are not exhaustively covered.

## Evidence, exact methods, limits

- Previous independent native DASM 4-bank exact byte parity: https://github.com/Odourman/mellanrum/actions/runs/45381991878 .
- Previous independent Stella/libretro core 8.0_pre 8dd5600, 15/15 source-guided, 15x36000 idle and authentic PCM retained on exactly the same product SHA; not newly rerun in this P0 follow-up.
- Original source blob comparisons matched PR38 product commit.
- New full source scripts, actual Gopher binary, unchanged BFDEB-ROM, original native ASM listings, exact replay commands, full Gopher stdout, eight native instruction-trace logs, strict stack write watch, JSON outcomes, package SHA256SUMS and complete Swedish report are packaged in an **82-member 18,811,913-byte ZIP**, SHA256 **72900c4b3000b928a95259579234aca3f18c8e5d465c850780705a2cc121f934**. ZIP CRC PASS, 80/80 manifest entries PASS. The ZIP is linked to the user in VERIFICATION chat and is **not uploaded to GitHub**.

| Gate | Classification |
| --- | --- |
| Exact ROM identity, independent DASM previous result | PASS |
| Reachable JSR depth <= 5, RIOT stack alias under normal program flow | PASS with enumerated preconditions |
| Full source-guided campaign per-frame Gopher raster postboot | PASS 20057/20057 |
| F6 all score-bank transitions during actual campaign | PASS 18190 pairs |
| FRI 780-frame stack-write strict watch | PASS bounded, 0 hits |
| Selected instruction/WSYNC cycle traces | PASS for 8 sampled frames, VBLANK late-WSYNC observed |
| Global worst-case 76-cycle scanline over all game paths | **INCONCLUSIVE** |
| New independent Stella instruction/line-level timing, physical Atari / RetroN77 | **NOT_RUN** |
| Human cold play, art, music, release authorization | **NOT_RUN** |

**Recommendation to MAIN III:** Do not demand a speculative stack patch on the basis of zero spare bytes alone for BFDEB; tested static reachability + dynamic alias watch support exactly five JSR. Accept measured postboot raster and F6 only for this actual source-guided campaign. Global worst-case cycle proof remains open. Keep Draft PR38 unmerged; no release or product changes. A future changed ROM requires a new hash and independent re-verification.
