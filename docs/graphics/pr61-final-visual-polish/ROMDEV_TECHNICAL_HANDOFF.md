# PR61 GRAPHICS - art-only technical handoff to ROM DEVELOPMENT
**Source commit:** `cc549ee106be4fe1ec801eedeb00c677ec5c37e1` — **ROM** `ef23e846b6b5ed9ba120ffbced01670d1bd29cf7b8cb2d0dcce841820bb81bf8` — **NO CODE CHANGED IN THIS GRAPHICS TASK.**

## Data-only and byte-minimal deltas (proposal, not code)
Current `experiments/global_hold_final_polish/rom/src/data.inc`:
```asm
PaletteBG: dc.b $A0,$A0,$F0,$82,$84
PalettePF: dc.b $B6,$B6,$46,$B4,$B6
PaletteOwl: dc.b $0E,$0E,$0C,$0E,$0E
PaletteGlyph: dc.b $3A,$3A,$38,$36,$3A
```
Recommend **same 5-slot shared index structure**:
```asm
PaletteBG: dc.b $A0,$A0,$F0,$80,$82
PalettePF: dc.b $B6,$B6,$B6,$B4,$B6
```
Same existing source `SetColorsSound`: replace `AND #$06` with `AND #$00` **only where it applies to room-derived COLUPF variation**; verify source context so no gameplay AND changes. Do not blindly run global replacements. Preserves opcode length/cycles but removes room-based luminance variation.

Current crown masks in active ROM source `main.asm`:
- first mid crown: `PF1 AND #$7D` → `#$78`.
- first mid crown: `PF2 AND #$3E` → `#$3C`.
These are source-only modifications suggested to future ROMDEV; exactly 2 immediate-value changes, no new TIA writes or RAM. The result is **modest**; don't overstate silhouette gains.

Fallback crown-B: `#$74` / `#$1E`, but visual shape less consistent. Crown-C requires new raster writes and fails *automatic* feasibility because current heavy Stem13 path is reported 75/76 CPU cycles.

## Protect exact art data
- U3 all four directions × 3 wing phases: read actual PR61 `OwlSprite0..11` source; **no modification authorized** under this task. No blinking, vertical beak.
- S3-A stone glyph preserved. **CURRENT exit glyph is user-approved arrow** `08 0C 0E FF FF 0E 0C 08` top-down (Issue #46); do not replace with older S3-B.
- Cursor local draws two real narrow rails from M0+BL; HUD uses separate P0 source bitmap. True 8×8 local forms not supported by current object map without raster redesign; don't confuse sources with rendered behavior.
- Presence PF2 OR/AND masks already have 3 source stages; preserve activity/visibility timing and causal rules.
- Keep source room data, collision maps, difficulty, title, coda and full TIA audio unchanged except separate authorized task.

## Pulse diagnostic request
Around supplied H.264 frames **61–82**, large changes alternate back and forth: 20k+ pixels cross >12 RGB difference in the user CSV for several frames, while no pixels cross >50 at the same sample. This points to a moderate **global brightness pulse** in the *video* but does not prove an unintended TIA register flicker. Ask ROMDEV to replay same full PR61 SHA, instrument per frame exact `COLUBK/COLUPF`, `Score` dispatch/fase, `VBLANK/VSYNC` and video capture RGB, freeze same room/phase/input, compare raw native framebuffer vs encoded H.264. Never globally suppress Presence negative-space effect as speculative fix.

## Suggested independent same-SHA acceptance
- 15 rooms, both phase states, full 1× original video frames and synthetic oracle references; measure BG/PF sRGB indicator but inspect human readability.
- Same scene/context, neutral/accepted/denied/intercept: four **actually captured** local marker+HUD states plus actual owl overlap; external P0/P1/M0/BL timing.
- 4 directions × 3 U3 frames unmodified, vertical movement natural controller reached in actual Stella/Gopher, no fake POKE frames.
- 262 NTSC line and 76 cycle per scanline in worst-case, RAM/stack highwater, F6 bank/trampoline integrity; no extra RAM.
- Copy input/raster/test logs and post-build ROM hash, include genuine video/PCM, ensure strict PCM regression addressed separately rather than waived.
- New independent Verification and Pachinko once candidate frozen.

**Ordering priority:** contrast/luminance > optional modest crown mask > marker read and vertical flight feasibility > no invasive title/pulse until root cause. This is graphics advice, not software authorization.