# Independent VERIFICATION #50 — RC1 final focused timing, stack and F6 addendum
Date 2026-11-24. MAIN IV order: https://github.com/Odourman/mellanrum/issues/50#issuecomment-7144993648. This is the independent verifier's **new** targeted work; earlier independent same-ROM build/full-game/idle tests are not rerun. PACHINKO #51 is a separate actor.

## Exact unchanged product
PR49 HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3` still Draft and unmerged at publication; product commit `7b400ad8678e8341a26f65cc757b1eb762654c83`, original 16,384-byte NTSC F6 ROM SHA-256 `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`. Product Git blob `afce29944cce726fa0f935ed3104abc954e7e6da`. **No product changes.**

## Fresh genuine native Gopher evidence, not reused developer/Pachinko results

Gopher pinned source `74c544203378c1448a33c29bc8b4586079b050f4`, ELF SHA256 `7b12dff57fcb73154122d2477f35d9c8ae8b344649bc0faa8ff6f5663c70470b`, native `unreleased` executable. DA​SM binary hash `cfb23732297a4fe1c8d4a78d44206037d97733aedb2772503bbf029a4aa91291`. Original Stella core `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`.

- **9 real single-frame Gopher instruction traces**: 38,365 CPU instruction records; 1,809 WSYNC opcode observations, 9/9 full 262 NTSC, 0 skipped visible WSYNC. Natural controller I-01 idle and FIRE, natural FRI, and separately labeled forced-RIOT diagnostics II-02 pending, III-03 Presence+FIRE/echo/phase, III-05.
- **8 native direct TIA bus-write captures**: 5,042 actual PF0/PF1/PF2/GRP0/GRP1/COLUP1/NUSIZ/REFP0/RESP0/VSYNC/VBLANK/WSYNC etc. accesses, 8/8 262. Unlike instruction-start TIA traces, actual `TRACE STRICT+ONTRACE` bus writes carry real colorclock. Reported CL is relative to HBlank exit; actual scanline colorclock=CL+68. WSYNC trace can represent post-stall position; instead WSYNC issue deadline is derived from opcode start +3 cycles.
- **23 additional HUD/beat/ack/polarity frames**, all 262: ten forced fireX0–9, beat frames 54/55/60/61/66/67/72, ackType0..3 and both polarities. Actual x9 `RESP0` bus write at **CL151 on scanline214**, `F9A3 STA WSYNC` instruction begins **CPU73**, adds three cycles to exactly **76/76**. **Zero extra timing margin but no observed 263-frame**.
- **8 additional Gopher same-row stone/arrow TIA bus captures** at II-02,II-04,III-02,III-05 × polarity0/1, all 262: in **each** room, 367/367 actual PF/GRP/COLUP1 bus **positions** on playfield scanlines51–210 matched. Two HUD PF writes on scanline212 legitimately shift 6 colorclocks; DO NOT claim entire visible HUD perfectly identical. These are **forced-polarity RAM diagnostics**.

## ROM/listing-derived cycle budget, exact limits

From the **unchanged native bank3 DASM listing/ROM bytes**, `F90C Stem13` ordinary X9..2 has sum **75 of 76 CPU cycles including next STA WSYNC**, **1-cycle margin**. Conditional proof: SpriteRowIndex for X2–9 produces Y0..7; all ordinary Owl/Glyph/Marker/Blank selector addresses remain in their original ROM page for these Y; no indexed page-cross penalty. Pointer sources are defined in original program and tables. If arbitrary corrupted pointer RAM is allowed, that assumption no longer holds.

`F948 StemLastFast` X1/terminal path spans intended WSYNC-separated raster lines. Native observed F948 at scanline211 CPU25 and F976 HUD preparation WSYNC scanline212 CPU5/7, all tested completed frames 262. Prior 84/86-cycle aggregate across lines is not automatically a scanline defect. **Global terminal branch/domain proof INCONCLUSIVE**.

`FA49 PrepareOwlFrame` references the same-page OwlFrameLo with valid index 0..11, followed by `F7D7 Top16`. Seven beat threshold cases give first Top16 STA WSYNC starts CPU48,54,54,59,59,58,58; greatest observed plus write cost = **62/76, ≥14 cycles**. `F7E6 NextRow` and crown/stem PF/GRP/COLUP writes were observed in fresh direct bus traces. All-path visible TIA register latch deadlines in every natural combined case remain **INCONCLUSIVE**.

Natural controller reached, **without RAM POKE**, **five nested JSR** in I-01 at frame124: break before `F4AE JSR DecodeKey`, SP=`F7`, then genuine **QUANTUM CLOCK CPU BUS DETAIL** showed **stack writes at physical aliases `$01F7←$F4` and `$01F6←$B0`**, final SP `$F5`, and `$01F5` retained `FE`. This provides actual max-depth stack-bus evidence beyond an SP-only watch. Earlier independent RC1 static call graph: 2541 reachable states, max5 JSR, no valid 6th / extra push; under valid data, RIOT variables $80–$F5 and ten stack bytes $F6–$FF do not overlap, **zero spare**. **PASS_CONDITIONAL**; not arbitrary corrupted RAM, future ROM modifications or physical hardware proof.

Four fresh actual score trampoline experiments: natural act I bank0 `$FFF6`, two forced-act-II bank1 `$FFF7`, forced-act-III bank2 `$FFF8`; each returned via bank3 at PC `$FF99`, **SP `$FB` unchanged** and `$01FA..FD` return-address bytes identical before and after. **PASS_BOUNDED**. Earlier independently verified real normal full campaign naturally exercised 4,711 bank1 selections and 18,190 matched score returns, not newly rerun here. Diagnostic forced bank1 is not a newly solved player run.

## Test-only marker correction
The older `independent_markers.py` compared its marker crop against **itself**, making its `different_from_neutral_pixel_count` always zero. Recalculating from the original independent genuine Stella 160×228 PNGs at ROI x32..47,y81..88, using marker0 as neutral, produces **0 / 14 / 30 / 28** changed pixels. Four distinct pixel ROI hashes; previous product / archive untouched. This is a test-script defect, not game ROM bug. Pachinko's four natural III-04 marker images are *Pachinko evidence*, not a new verifier-run natural scene.

## Explicit limits and disposition

| Gate | Result |
|---|---|
| Ordinary valid Stem13 indexed cycle budget 75/76 | **PASS_CONDITIONAL** |
| HUD x9 actual bus and last WSYNC at 76/76 | **PASS_BOUNDED**, zero spare |
| Terminal X1 / transition actual raster | **PASS_BOUNDED; global branch proof INCONCLUSIVE** |
| PrepareOwlFrame threshold/Top16/NextRow actual original native bus | **PASS_BOUNDED** |
| Presence/FIRE/echo/phase, same-row two polarities | **PASS_BOUNDED diagnostic; all natural combos INCONCLUSIVE** |
| Five JSR actual controller and stack BUS addresses | **PASS for witness / PASS_CONDITIONAL overall** |
| F6 bank1 two real return probes + bank0/2 references | **PASS_BOUNDED** |
| Corrected 4 marker numerical counts | **PASS_DIAGNOSTIC** |
| Complete all-reachable-codepath 76 cycles + TIA-write register deadlines | **INCONCLUSIVE** |
| New original Stella per-instruction bus trace, human cold-play/listening, original Atari/RetroN77 | **NOT_RUN** |
| New demonstrated RC1 release-blocking defect | **None reproduced** |

**Archive:** `MELLANRUM_RC1_FINAL_TIMING_VERIFICATION.zip`, **21,419,217 bytes**, SHA256 **`f53c5ea0c2550237ce53a4ec63d2fb7ff5ee3df7f73e440b6b6cb102915f8005`**, **202 unique ZIP members; 201/201 SHA256 manifest, ZIP CRC PASS**. Entire original raw logs, exact original ROM, native listing/symbols, new machine matrices, original emulator executable, actual debugger commands, corrected scripts and complete Swedish report are delivered *directly in the Verification conversation*; **no invented external ZIP URL or claim of Github ZIP upload**. The previous accepted Verification evidence archive and its SHA stay unchanged. No raw Pachinko archive was accessible in this chat; reports reviewed via live GitHub only.

**Final advice to MAIN IV:** Do **not** invent a ROM bug or mandate a speculative patch from zero marginal stack/HUD alone. This is the requested single risk-limited follow-up, now complete. **`INDEPENDENT_VERIFICATION_INCONCLUSIVE` globally** because full natural all-path timing remains unproven. Strong specific PASS can be retained; present residual risk explicitly to user. Unchanged RC1 may advance to **human cold-play and physical-original-hardware review** as a candidate only, not merge/release. Separate human/physical gates, strict PR44 PCM numerical FAIL and PACHINKO partial status remain intact. No unauthorized next work phase.