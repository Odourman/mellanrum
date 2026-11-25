# MELLANRUM: SKOGEN SOM LYSSNAR — FINAL TARGETED INDEPENDENT VERIFICATION

**2026-11-25 — VERIFICATION, MAIN IV order — frozen HEALTH `LAB_STACK_INLINE_PADDED_B` vs original RC1.**

**Disposition:** `FINAL_TARGETED_VERIFICATION_PASS_BOUNDED` for the *finite measured questions*, **`GLOBAL_ALL_PATH_TIMING_INCONCLUSIVE`**, **`FRI_RAW_PCM_STRICT_AB_INCONCLUSIVE`**, **`HUMAN_AND_PHYSICAL_NOT_RUN`**, **`NO_NEW_CONFIRMED_LAB_SPECIFIC_BLOCKER`**. This document is neither a release approval nor a decision to replace RC1. The local assembly/ROMs are unchanged. The campaign-wide clock concept mentioned by MAIN is not part of this verification and is not implemented here.

## 1. Object, authority and immutable bytes

The product reference is [Draft PR49](https://github.com/Odourman/mellanrum/pull/49) HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`, product commit `7b400ad8678e8341a26f65cc757b1eb762654c83`. The unchanged 16,384-byte standard NTSC/F6 ROM SHA256 is **`456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`**. Original source `rom/src/main.asm` SHA256 `758d5ad2eb14942d4b2ca6263aa2942ba61f927285291fa51bbedf4e8ff1f01d`, Git blob `6224bc13a17eb45d898118e72f6fc15a7586267c`.

The **experimental specimen**, not a new product commit, is `LAB_STACK_INLINE_PADDED_B`: **ROM SHA256 `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`**, exact `main.asm` SHA256 `3246d67a40470454eb56c38f2f4c32fb34ccb4ff38ed796ccb10cf00a647d53e`. Four banks ×4,096 bytes; banks0–2 byte-identical to RC1; bank3 relocates due to inlining DecodeKey in ToggleTree and six two-cycle NOPs. No new optimization, no product changes, no RC2 promotion.

Live [AGENTS.md](https://github.com/Odourman/mellanrum/blob/d013a0f82621d46ad12674a4a8e944bf005cd9c3/AGENTS.md), DECISIONS, SOURCE_REGISTRY and CURRENT_PROJECT_STATE read; the November22 status files are outdated relative to the later explicit user orders, actual ROM bytes, Issue48/PR49, HEALTH/VERIFICATION/PACHINKO handoffs. Project authority order respected. The three source ZIP archives independently downloaded, 100% CRC/manifest revalidated: HEALTH **3,318,898 B**, SHA `f8950badc9fed8495a7dfa5fbd7849dd8b5b252cfe9dfba125b041fe7e1289f1`, 1300/1299; previous independent VERIFICATION **4,640,886 B**, SHA `d4eca534a98cc5cb5222a05fed961cc05e6d3f5bd8fa472ad15df24229b4a599`, 1048/1047; PACHINKO **14,605,595 B**, SHA `f706afa7b934c87405a67898dfc48ca28753f3a140d26fc80fe87ac15728bd4e`, 515/514. All hashes of manifest **payload** entries match; root manifest itself correctly not counted as payload. `PROVENANCE/ARCHIVE_INTAKE.json` retains checks and complete original Drive URLs.

**Tools (real, hash verified):** native Gopher2600 pinned source `74c544203378c1448a33c29bc8b4586079b050f4`, ELF SHA `7b12dff57fcb73154122d2477f35d9c8ae8b344649bc0faa8ff6f5663c70470b`; native Stella libretro `8.0_pre 8dd5600` SHA `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`; prior original DASM 2.20.14.1 SHA `cfb23732297a4fe1c8d4a78d44206037d97733aedb2772503bbf029a4aa91291`. This complement reused four prior independently reproduced native builds/listings/syms, whose ROM SHA were rechecked; it **did not claim new DASM builds**. In original pin's Gopher logs CL is relative to the start of the visible window; scanline colorclock = CL +68. Bank-aware PC and CPU-bus events were captured, not inferred solely from PEEK/TV FRAME. Tool commands and SHA per raw log are preserved in the package.

## 2. P0-A — NEW, COMPLETE NATURAL bank1 F6 call, matched two-ROM test

The earlier Pachinko method timed out without one correct frame. This experiment instead replayed the **existing genuine source-guided controller sequence** with optimized frame breaks, without instruction-by-instruction tracing during the first ~5,880 frames. Validation pilot at 100 frames showed identical resulting CPU PC, room/mode and observed RAM to the conventional per-frame replay. At **frame5880, mode1, act II, room II-01** all below events are from *one continuous native Gopher2600 6507 quantum-clock CPU BUS trace per ROM*, from before caller JSR until after its RTS and through a complete 262-line frame. No POKE. Original: `EVIDENCE/BANK1_NATURAL/natural_bank1_{LAB,RC1}_raw.log` and matching script.

| Event | RC1 native PC | LAB native PC | SP or actual hardware bus |
|---|---:|---:|---|
| Before external `JSR $FF90` | `$F706` | `$F708` | SP `$FD`; all `$F5..$FF` actual read-only snapshots captured |
| Actual outer JSR | `$F708` next CPU | `$F70A` next CPU | writes `$01FD` = `$F7`; `$01FC` = `$08` RC1 / `$0A` LAB, then SP `$FB` |
| Bank3 trampoline entry | `$FF90` | `$FF90` | SP `$FB` |
| CPU *hotspot read* | `$FFF7` | `$FFF7` | true physical ROM bus read; F6 3→1, X=1 |
| Bank1 interpreter JSR | `$FF95` | `$FF95` | writes `$01FB` = `$FF`, `$01FA` = `$95`; minimum observed SP `$F9` |
| Interpreter RTS | bank1, via `$FF87` | same | physically reads `$01F9/$01FA/$01FB` as appropriate; restores SP `$FB` |
| CPU *hotspot read* | `$FFF9` | `$FFF9` | actual ROM bus; bank1→3; `$FF99` before outer RTS; duplicate debugger sample of same bus phase is **not another call** |
| Outer RTS | `$F709` | `$F70B` | SP `$FD`, correct version-specific caller return; active outer frame consumed |
| Following frame | native frame5880 | native frame5880 | 262 complete scanlines each |

Each log has **577 quantum-clock sample observations** and **182 de-duplicated actual bus-clock records**. No *actual CPU stack write* into `$01F5/$01F6/$01F7`; `$F5` guard remains `$FE`, LAB `$F6/$F7` remain `$00/$00`, while stale RC1 `$F6/$F7` show historical `$B0/$F4` after the earlier frame124 five-deep stack event. This difference is expected **inactive stack data**. The active outer return address legitimately overwrites old `$01FC/$01FD` and is subsequently popped, so the ten RAM bytes are **not required to be globally identical across all snapshots**. CPU bus writes and reads, return PCs and bankcontext, not simple hotspot-count parity, are the basis of this PASS.

**P0-A `PASS_BOUNDED`: one complete matching natural bank1 call in each ROM**, no stack-bank corruption found. **A second distinctly natural actII echo/phase case `NOT_RUN`**, and no claim that all bank1 paths are now exhaustively proven. Prior independent bounded bank0/bank2 tests and true full natural campaign remain prior results, not newly rerun here.

An invalid **first RC1 pilot** accidentally reused LAB relocated caller PC `$F708` rather than RC1 `$F706`. It was terminated and its invalid raw log preserved; source control comparison corrected, then valid paired native run completed. `FAIL_HARNESS_CORRECTED`, **not product failure**. CPU memory PEEK output is classified observer-only; do not confuse PEEK with a real CPU bus read.

## 3. P0-B — real stack reserve and conditional source bound

Prior independent per-ROM context-sensitive CFG (`2,541` RC1, `2,565` LAB source-valid control-flow states) yields **max five nested JSR vs four** and no additional valid-flow PHA/PHP/BRK stackpush. A previous naturally reached frame124 I-01 witness observed LAB minimum SP `$F7` and no `$01F6/$01F7` stack writes; RC1's fifth JSR reached SP `$F5` and wrote both reserved addresses. These are **PRIOR_INDEPENDENT_EVIDENCE**, not newly achieved in this complement. The new actII matched bank1 path has local **SP minimum `$F9`**; its actual bus accesses give an additional independent confirmation that no extra stack use is caused by actII bank switching. `$F6/$F7` are **unused reserve** under stated source-valid/ROM integrity/indirect pointer assumptions, not newly allocated game RAM. The two stack bytes (4 JSR ×2 bytes =8 stack bytes) are a meaningful improvement, but **zero margin above** the former RC1 stack allocation was a separate consideration and a universal all-path proof of arbitrary RAM corruption is not claimed. No newly observed stack violation.

## 4. P0-C1 — NEW complete natural OwlTryNext continuation, includes a material sound timing distinction

The naturally taken event originally found by Pachinko was reproduced **independently on the pinned Gopher native executable** with regular controller input, left Difficulty B, FIRE at frame18 and idle. At **FR=2142 in FRI SKOG (mode4, room12)**, bank3 `BCS OwlTryNext`, C=1:
- RC1 `$F4FC → $F567`: **4 CPU cycles**, page-cross.
- LAB `$F4FE → $F569`: **3 CPU cycles**, no page-cross. The `−1 CPU` / `−3 colorclock` delta is real.
- First `WaitVBlank` entrance both **SL18 CL−41**, first **real CPU `INTIM` read value `$14` (=20)** both; exit both **SL34 CL88**. True `VBLANK=0` bus write both **SL35 CL−53**. First subsequent visible PF0 write both **SL35 CL76** (then PF1 CL91 etc), identical data and positions; full image frame **262** for both. Thus the timing delta is **absorbed before** the common visible rendering boundary **in this natural event**. This is not a global validity proof.

**Important NEW bus finding, not visible in prior framehash comparisons:** An additional real native Gopher CPU/TIA **audio register bus trace** across **FR2100..2142 (43 actual frames)** captured **258 real TIA sound register writes per ROM** (6 each frame). In FR2100..2141, all 252 sound writes have identical register/data/scanline/colorclock in RC1 and LAB. At the *naturally taken* BCS in **FR2142, all six same-value writes occur 3 colorclocks earlier in LAB**:

| TIA register | RC1 scanline, CL | LAB scanline, CL | Data both |
|---|---|---|---|
| `AUDF0` | 8,151 | 8,148 | `$1B` |
| `AUDV0` | 9,−32 | 9,−35 | `$01` |
| `AUDC1` | 9,19 | 9,16 | `$04` |
| `AUDC0` | 9,58 | 9,55 | `$0C` |
| `AUDF1` | 9,109 | 9,106 | `$19` |
| `AUDV1` | 9,154 | 9,151 | `$02` |

**Disposition:** *real, valid-source, naturally reached LAB-specific audio bus-write timing change*. The saved cycle DOES propagate to the sound registers; it stops propagating before WaitVBlank and the observed visible PF writes. This difference is neither a missing scanline nor, on current evidence, a confirmed audible defect. No statement of exact TIA bus-time identity over all paths is valid. The PCM comparator is separately INCONCLUSIVE below. See `EVIDENCE/FRI_AUDIO/fri_tia_audio_registers_{RC1,LAB}.log` and `ANALYSIS/FRI_AUDIO_ORACLE.json`.

## 5. P0-C2/C3 — four formerly unresolved *natural* room-load timer consequences, complete matched evidence

Two fresh real controller-only Gopher processes replayed the same known 5,880-frame campaign prefix. At *the four natural transitions* already witnessed in Pachinko, inserted version-specific brief CPU and strict actual RIOT/TIA bus traces. Original commands and full logs in `EVIDENCE/ROOM_LOAD_TIMER`; machine results in `ANALYSIS/NATURAL_ROOMLOAD_A_B_TIMERS_AND_BUS.json` and CSV. **This is one underlying transport per ROM with four natural event checks, NOT eight independent full campaigns.**

| Room / frame | Indexed read X | Actual instruction timing | True `INTIM` at first WaitVB | First PF0 / total |
|---|---|---|---|---|
| I-02 / 964 | `GeoMapHi X1` | RC1 4, LAB 5 cycles | `$0C` at SL25 CL−29 both | SL35 CL70, 262 both |
| I-03 / 2497 | `GeoMapHi X2` | RC1 4, LAB 5 | `$0C` at SL25 CL−29 both | SL35 CL70, 262 both |
| I-05 / 4483 | `RoomStoneY X4` | RC1 4, LAB 5 | `$0C` at SL25 CL−29 both | SL35 CL70, 262 both |
| II-01 / 5872 | `RoomStoneY X5` | RC1 4, LAB 5 | `$0C` at SL25 CL−29 both | SL35 CL70, 262 both |

At all four: previous frame actual CPU `TIM64T` write of `$2B` at SL261 CL−20; new frame WaitVBlank entry `F05E` **SL25 CL−41** both, CPU first `INTIM` read of `$0C` **SL25 CL−29**, then wait exit at `F063` **SL34 CL88**; `VBLANK=0` CPU bus write **SL35 CL−53**, renderer starts same position and actual first PF0/PF1/PF2 positions **SL35 CL70 / SL35 CL85 / SL36 CL−65** with identical data and matching all traced PF access counts. The local **+1 CPU cycle** occurs earlier in LoadRoom, but the common RIOT timer waiting period absorbs it in all four real natural cases. Timer zero window was **not** missed in these tests; do **not** infer timer zero safety for all hypothetical unmeasured game states. **P0-C2/C3 `PASS_BOUNDED` each valid index.**

The indexed read domains are disjoint: GeoMapHi crosses at indices1/2, RoomStoneY at4/5; the two costs **do not accumulate** during the same LoadRoom. Prior 58 changed page-cross sets still comprise 55 outside source-valid index domains; prior valid TitleLeftPF2 Y2/3 +3-colorclock title changes with ≥32-clock PF segment deadline and no pixel delta remain prior independent evidence, not newly rerun.

## 6. P0-D — targeted worst-case, real beam and x9 sensitivity

A new real native Gopher run against LAB and RC1 with **actual locked `fireX=9`** (not merely cursorX9) completed **262** NTSC scanlines, with actual `RESP0` write **SL214 CL151** in both. The matched **PR47 negative-control ROM** (identical controller x9 input) gave **263** scanlines with RESP0 delayed to CL154: **detectable by this new instrumentation**. Debugger instruction-start PC samples are not treated as bus-write time. The existing source-valid HUD x9 WSYNC 76/76 is a conditional hard limit, zero spare cycle; ordinary Stem13 75/76, 1-cycle spare with verified valid Y7..0 (terminal X1 uses Y8 blank-byte and **separate** multi-row kernel); PrepareOwlFrame/Top16 previous bounded observed max 62/76; these latter analytical/observational claims are **PRIOR_INDEPENDENT_EVIDENCE**, not newly retested for global all-path.

A new **10-case LAB native Gopher risk matrix**, each containing an actual 262-line frame, two TV observations and true CPU/TIA bus traces, covered: natural locked fireX9, diagnostic cursor1/fireX9 distinction, ack accepted/denied, Presence interception, pending old target, pending denied next, Presence+echo+phase, owl beat54 and55. **1 natural controller-only; 9 explicitly `FORCED_RAM_DIAGNOSTIC`** after natural room prefix, not player-reachable evidence for those artificial combinations. All ten have RESP0 **SL214 CL151** and no extra scanline. A subset of forced RAM combinations could be impossible source-valid states; this is a *stress of the kernel's response*, not a proof of reachability or a global latch-deadline certificate. Prior two-polarity same-row and 12 owl masks, natural Presence interceptions and full campaign remain prior valid tests. **No new confirmed StemLastFast/Top16/GRP/PF bus deadline defect**, but no exhaustive terminal Presence/echo/beat/FIRE-state constraint proof either.

For a legitimate multi-scanline terminal segment, aggregate CPU cycles exceeding 76 over multiple WSYNC-delimited lines are *not* equivalent to a missed single-line deadline. `ANALYSIS/BEAM_DEADLINE_LEDGER.csv` records actual sampled RESP0 beam positions, raw command and class; missing analytic all-path limits are explicitly null/not proven, not zero. **Global all-path: `INCONCLUSIVE`.**

## 7. P1 — small, independent, four-process FRI audio comparator; why exact PCM A/B fails

A **new** controlled A/A2/B/B2 capture was actually run: four separate fresh Stella/libretro OS processes with pinned core, identical deterministic 2,400-frame B-Difficulty FRI `CLOG` input (402 RLE events, exact event *list* equal across ROMs; metadata source SHA differs), same seed241125, 2400 video callbacks each, **1,257,076 stereo PCM frames each, 31,440Hz, two channels = 2,514,152 int16 values per capture**. Original WAV and all callback/input/ROM metadata in `EVIDENCE/FRI_AUDIO`; independent comparator in `SCRIPTS/compare_fri_pcm_oracle.py`.

| Raw int16 comparison | Unequal of 2,514,152 values | Meaning |
|---|---:|---|
| RC1 run1 vs RC1 run2 | **694,036** | Same ROM: **strict PCM non-determinism** |
| LAB run1 vs LAB run2 | **752,110** | Same ROM: **strict PCM non-determinism** |
| RC1 run1 vs LAB run1 | 744,868 | Cannot attribute to LAB if control is unstable |
| RC1 run2 vs LAB run2 | 689,758 | Cannot attribute to LAB if control is unstable |

Video frame checkpoints are identical within each same-ROM pair in this capture. LAB raw 128-byte RAM sample checkpoints matched in its two runs; RC1 had **one differing raw RAM checkpoint at frame900 despite equal sampled framebuffer**, which may be stale scratch/stack etc, and is disclosed rather than silently ignored. The sample count/rate/video callbacks align. No unsupported automatic time alignment is used to turn distinct raw PCM into a PASS. The prior **20,594,248-int16** full-campaign strict A/A2/B parity is a *different deterministic scenario* and remains valid only within its original scope. A raw FRI WAV difference from this unstable comparator cannot be declared a LAB-specific new sound failure. The *independently observed six early sound register writes* are, however, a genuine internal TIA timing difference, and therefore neither unconditional identical sound nor a proven audible defect is claimed.

**FRI strict raw PCM A/B `INCONCLUSIVE`; real FRI sound-register bus timing delta `PASS` as a documented observation; no human hearing test / original physical TIA hardware execution.** This finite P1 is closed rather than endlessly repeating until PCM hashes happen to match.

## 8. Coverage accounting and harness exclusions

`ANALYSIS/TEST_MATRIX.csv` has **41 explicit rows** (including prior evidence references, controls, and NOT_RUN). New native 6507 evidence: two matched actual bank1 call chains (each 577 quantum samples, 182 dedup bus cycles); two independent full natural Owl branch/continuation traces; four distinct naturally reached load-index events per variant in **one 5,880-frame transport per ROM**; one matched x9 control per LAB/RC1 plus PR47 negative; ten **additional** one-frame LAB diagnostic HUD trials; 43 natural FRI audio-bus event frames per ROM (258 sound register writes each, 6 changed time); four separate 2,400-real-frame Stella FRI audio sessions (**9,600 genuinely new callback frames**). 43 extra FRI readouts / Gopher TV FRAME queries are *not* 43 new whole-game campaigns. CPU BUS quantum clock rows, TV FRAME observations, executed frame steps, separate natural controller scenarios and formal state coverage are distinguished.

The previous 15/15 campaign, 19,652/19,652 buffer-hash and 20,594,248 PCM int16 parity, 540,000 idle, 15 causal/recovery, 50,010 FRI, source-valid CFG and PACHINKO 105×2 profiles/3255 checkpoints remain **PRIOR_INDEPENDENT_EVIDENCE**/**PRIOR_PACHINKO_EVIDENCE**, not added as new samples here. First RC1 bank1 breakpoint (`F708` instead of `F706`) was a **`FAIL_HARNESS_CORRECTED` pilot**, explicitly preserved and replaced with a complete correct pair; initial room-load parser counted both test instruction prints rather than the relevant next PC, repaired and rerun against raw file. No product mistake inferred. All newly PASSED raw debugger processes returned exitcode 0. Both old frozen ROM bytes are rechecked at final packaging.

## 9. Remaining risks, severity and decision

| Question | Final status | What is known / not proven |
|---|---|---|
| Correct immutable bytes / source pins / 3 original ZIPs | **PASS** | Validated raw SHA, CRC, full manifests; prior builds used, not rerun |
| Natural bank1 FFF7/FFF9 and real stack bus / return | **PASS_BOUNDED** | Matched full pre/during/post both ROMs at actII; distinct second natural bank1 scenario NOT_RUN |
| Stack gain from max5→4 JSR | **PASS_CONDITIONAL** | Prior source-valid CFG+natural max witness, new bank1 min SP F9; does not allocate new RAM |
| OwlTryNext branch through visible output | **PASS_BOUNDED** | −1 cycle absorbed by wait boundary; **six audio writes −3 colorclocks** prior to wait |
| All four new genuine indexed page-cross loads to visible output | **PASS_BOUNDED** | All four natural A/B timer/INTIM/WSYNC/PF chains equal after wait |
| HUD x9 / 10 selected terminal risks | **PASS_BOUNDED** | True locked fireX9 and valid PR47 negative; nine forced-state stress cases not natural |
| Absolute all-source-valid combined timing/terminal latch proof | **INCONCLUSIVE** | Unmeasured naturally combined Presence/echo/terminal states; zero extra HUD x9 cycle margin |
| FRI PCM exact bit-for-bit A/B across processes | **INCONCLUSIVE** | Same-ROM comparator diverges, actual six shifted LAB sound bus writes verified |
| New demonstrable LAB-specific release blocker | **None reproduced** | No arbitrary guarantee of absence |
| Physical original Atari, RetroN77, human cold-play/art/audio | **NOT_RUN** | Separate authorization and human/hardware acceptance |

The 2-byte **valid control-flow stack reserve** is a real resilience improvement over RC1 with no extra declared RAM, at the cost of 2 extra bank3 ROM bytes and changed table/code timing. Four natural room load differentials are absorbed by timer; naturally taken Owl branch visibly resynchronizes but *actually shifts sound-register bus writes*. This measured difference is minor (one CPU cycle, values unchanged) yet should be transparently included in a future audio/physical review. There is no evidence currently warranting speculative ROM modification or treating the candidate as technically worse in gameplay than frozen RC1. Conversely a logically possible, never tested combined state could still expose a zero-margin HUD deadline. New random frame volume cannot prove all paths.

**Recommendation to MAIN IV / user:** Within bounded technical evidence, the **unchanged LAB experiment is reasonable to *select as a technical experiment base for a later separately ordered timer-feasibility study***, because the two bytes of real stack reserve are meaningful while no new functional, visible, bank or stack failure is demonstrated and local timing consequences are explicitly measured. **This is not RC2 promotion, release permission or timer implementation permission**. RC1 PR49 remains frozen and official until user chooses and an authorized later stage re-verifies changed SHA. Present the measured −3-colorclock sound-write shift and the `INCONCLUSIVE` global state/timing/FRI PCM caveats in the decision. If the user prefers minimal change instead, RC1 remains a valid conservative no-change baseline but retains the old zero extra stack margin. No further broad verification loop is requested. Human I-05 cold play, art/audio acceptance, physical original Atari and RetroN77 remain completely separate NOT_RUN gates.

## 10. Reproduction and artifact map

Read `04_REPRODUCE.md` for exact native emulator commands, tools and paths; `02_TEST_MATRIX.csv` for new/prior/invalid classification; `RESUME_STATE.json` for completion; `ANALYSIS/STACK_BANK_EVENT_LEDGER.csv`, `TIMER_VBLANK_LEDGER.csv`, `BEAM_DEADLINE_LEDGER.csv`, `RELOCATION_CONSEQUENCE_MATRIX.csv`, `FRI_AUDIO_ORACLE.json`. Unchanged original ROMs `ROMS/{RC1,LAB_BEST}.bin` accompany source snapshot and previously independent native bank3 .lst/.sym. Original raw debugger and WAV files are retained under `EVIDENCE/`. No product branch, GitHub PR, merge, release or downstream specialist phase was altered/started.