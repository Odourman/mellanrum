# MELLANRUM Issue26 – authentic 16,384-byte F6 bank map

**Scope:** New isolated PR #27, explicit MEL-055. Stock unmodified Atari 2600, NTSC, 6507/TIA/RIOT (128B RAM). Standard fixed F6 mapper: selecting physical cartridge ROM bytes at CPU-visible address $FFF6, $FFF7, $FFF8 or $FFF9 corresponds respectively to bank 0, 1, 2, 3 (6507's 13-bit bus mirrors to $1FF6–$1FF9). No Superchip RAM, custom ASIC, ARM or second CPU.

## Explicit file layout and live use

| Image offset | Mapped CPU window | File | Live content | Amount |
|---|---|---|---|---:|
| $0000-$0FFF | $F000-$FFFF bank0 | `rom/f6/bank0_score.asm` | Act I five *independent* 256-frame three-stream TIA compositions; banked 6502 score routine; reset/return selectors | 4096 B |
| $1000-$1FFF | $F000-$FFFF bank1 | `rom/f6/bank1_score.asm` | Act II five delayed-memory rhythm compositions, stronger dual-voice textures, own runtime and F6 return/reset | 4096 B |
| $2000-$2FFF | $F000-$FFFF bank2 | `rom/f6/bank2_score.asm` | Act III five phase/Presence oscillating and dissonant dual-voice compositions, runtime and F6 return/reset | 4096 B |
| $3000-$3FFF | $F000-$FFFF bank3 | `rom/src/main.asm`, `rom/src/data.inc` | Actual 15-room playable CPU/NTSC renderer, all 15 distinct authored PF maps and collision arrays, U3/S3 sprites, Presence PF, input/AI/echo/phase, title/coda | 4096 B |

**Not a padded 4K file:** the first three banks encode **15 × 256 × 3 = 11,520** byte-addressable real-time composition/control values. Every byte is consumed at runtime from its room bank by the real 6507 for `AUDC0/AUDC1/AUDF0/AUDF1/AUDV0/AUDV1` as every soundStep phase cycles; the score also modulates `COLUBK` with the second voice. This means all 15 rooms have separate audible and subtly visible rhythm identities instead of five 4K repeating sound presets. The remaining space in each bank houses actual 6502 interpreter, lookup, F6 hotspots, NMI/RESET/IRQ vectors, hardware-safety jump code and a little alignment between routines and vectors. It is **not** 12 KiB of non-executable empty padding; normal small unused areas around vectors exist.

## Real cross-bank call and return

Normal CPU executes the kernel in bank3. Each frame's `SetColorsSound` chooses act bank 0..2; the title selects bank0. At same-resident physical PC `$FF90`, `LDA $FFF6,X` selects chosen F6 bank. **Next PC $FF93 executes inside the new bank**, whose stub contains `JSR BankScorePlay`; it loads room modulo 5, three different 256-frame pages, writes both actual TIA channels plus background breath, plus Presence interference. At $FF96, `LDA $FFF9` selects game bank3 and the **same PC $FF99** runs its RTS, returning to normal game logic on the original stack.

Every bank also contains the same `$FF9A` emergency reset entry: `LDA $FFF9; JMP $F000`; bank0..2 vector reset at $FF9A so hardware reset from *any* active bank returns to game bank3 before executing game reset. Bank3 vectors directly to `Reset` at $F000. Authentic native DASM `rom/f6/build_f6.py` checks all four bank sizes, correct hotspot opcodes and vectors, and concatenates in bank0+1+2+3 order. Source+bank metadata outputs `ROM_16K_BUILD.json` and SHA256SUMS.

## Technical limitations and risk

F6 maps only one 4KiB window at a time; it does not add RAM, sound channels, graphics objects, scanline cycles, or vertical resolution. All banks execute only during VBLANK for audio; raster critical kernels continue in bank3, no bank switch in active visible scanline. Exact CPU cost of new audio interpreter must still fit vertical-blank budget and be independently beam measured on final ROM SHA. Bank-select writes are on ordinary ROM hotspots, no other cartridge requirements.

CI: `.github/workflows/issue26-native-f6.yml` strictly builds DASM and runs genuine Stella 15-room game; ancient Issue15 4K tests are version-gated and must not falsely rebuild Issue21/26 via `build_issue15.py`.
