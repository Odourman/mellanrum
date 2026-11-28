# MELLANRUM GRAPHICS / PR61 FINAL VISUAL POLISH
**28 November 2026. SOURCE_ONLY / SYNTHETIC / NEW_EMULATOR_NOT_RUN.**  
**User task**: MAIN V → GRAPHICS final visual polish, *no product implementation*.  
**Product identity**: [Draft PR #61](https://github.com/Odourman/mellanrum/pull/61), commit `cc549ee106be4fe1ec801eedeb00c677ec5c37e1`, 16,384-byte NTSC F6 ROM SHA-256 `ef23e846b6b5ed9ba120ffbced01670d1bd29cf7b8cb2d0dcce841820bb81bf8`. PR61 not merged/released.

## Main findings (source-bound)
- The delivered H.264 images and PR61 main.asm/data.inc were read. A script-derived **reflected PF renderer reconstructed all 15 source room geometries**, matching 99.36–99.84% of classified PF pixels in 15 supplied H.264 starting screenshots (not a new emulator test).
- Low contrast H.264 sample: II-02 1.07:1, III-03/04 1.33:1, III-05 1.24:1. This is an **sRGB-video relative-luminance proxy**, not calibrated Atari CRT output.
- Baseline uses five palette entries indexed by `act+phase`, so cross-act phases share entries; **do not invent six independent palette slots**.
- Actual code `SetColorsSound` does `COLUPF = PalettePF[act+phase] XOR (room & $06)`. The XOR affects luminance bits and may make forest shapes near invisible. This is source-grounded. **It does not prove the cause of 522 large transient video changes**; short pulses ~frame 61–82 need exact emulator timing/register/video investigation.
- Recovered user decision in [Issue #40](https://github.com/Odourman/mellanrum/issues/40#issuecomment-7127852893) to stop endless conifer reworking; user's new explicit MAIN V brief **reopens a limited source-only exploration**, not an obligation to force an invasive tree replacement.
- The later user-approved **amber exit arrow** (Issue #46 comment 7138111730) supersedes older S3-B glyph in current game. Its **8-byte top-down mask is `08 0C 0E FF FF 0E 0C 08`**. Preserve. S3-A stone polarity mask and all **12 protected U3 owl masks** stay untouched.

## Ranked design recommendations / not implementation
**A1. Palette:** recommended `PaletteBG = A0 A0 F0 80 82`; `PalettePF = B6 B6 B6 B4 B6`, and remove source's per-room luminance XOR via `AND #$06` → `AND #$00`. This means uniform forest luminance per act/phase and reduces room-specific color variation, a documented design tradeoff. Estimated 0 additional cycles/bytes for an immediate operand swap; requires new ROM candidate and true emulator testing, **not implemented here**.

**A2. Minimal conifer crown taper:** source's mid-crown `PF1 & $7D` → `PF1 & $78` and `PF2 & $3E` → `PF2 & $3C`. Exactly two immediate bytes, no new PF writes, no extra RAM or cycles. Pixel-model effect is **moderate**, not magical. Alternative larger negative notches: `$74/$1E`. Avoid extra crown mid-scanline writes without beam margin; current Stem13 critical 75/76 cycles.

**A3. Preserve:** original U3 all directions/wing masks, S3-A and later amber exit arrow, three current Presence PF2 stages, coda transformation, 15 original PR61 rooms, original marker hardware plus 8×8 bottom HUD glyphs.

**B. Marker readability:** 4 hardware-different local M0/BL rails plus HUD P0 glyphs: neutral, accepted, denied, special Presence interception. Test a **same-position/same-background, actual 1× Stella 4-frame comparison** and overlaps before tuning durations; no free extra player sprite.

**B/C. Vertical owl flight:** developer PR61 still has 3 coarse intermediate appearances. A six-step pixel-motion design with offsets 0/4/8/12/16/20 scanlines is **illustrative**. Its real scanline placement requires new runtime timing and probably new code; cannot call it feasible from a model.

**C. Title subtitle:** "SKOGEN SOM LYSSNAR" only as separately costed alternate title pass; avoid degrading exact MELLANRUM and 262-line title. Preserve coda.

## Exact technical and evidentiary boundary
- PR61 main.asm original blob SHA `23ec5ebd952290ae07827fdc61010682f1211026`; data.inc `02db147d131447d7006e17ca177275259ffc1e80`.
- PR61 code: 118 declared RAM bytes, 8 byte stack budget, 2 protected reserves, constrained bank 3 and a reported 75/76 scanline path. Not empty resources to borrow.
- MAIN V reports strict PCM regression FAIL and nonfinal vertical flight. These are not cured by graphics design.
- All new before-after views, 15 room cards, alternate-phase renderings, source-collected 1× references, palette/JSON oracle, exact PF masks, animation, 19-page PDF, complete Markdown, generator and original-source ZIP are included in the **user-facing** `MELLANRUM_GRAPHICS_PR61_FINAL_VISUAL_POLISH.zip`. New design images are **SOURCE_ONLY / SYNTHETIC / NOT_STELLA_EVIDENCE**; old H264 and developer-Stella source images are separately labeled.
- User-facing ZIP has 84 files, 83/83 manifest hashes, CRC PASS, SHA-256 `61d2b78f6387b98af9423cdf4d73b905c2a5205f788a00f91c78c5025b0b0080`. Never claim this GitHub branch contains the binary ZIP.
- No production ROM built/changed; no CI/raster/ROM verification triggered; no merge/release.

**Next gate**: MAIN V reviews this source-only design, selects conservative A steps, authors a separate exact-scope ROM DEVELOPMENT task. ROMDEV then performs true Stella/Gopher raster, pixel/contrast, PCM regression, 15/15 game test on **new ROM SHA**, followed by independent Verification/Pachinko.