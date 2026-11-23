# U3 Vingkropp – lodrät näbb (GRAPHICS source-only, 2026-11-23)
**Status: GRAPHICS_DESIGN_PROPOSED / NEW_EMULATOR_NOT_RUN. No product ROM changes.**

User's direct correction: change U3 mouth from horizontal to vertical, i.e. a beak. All U3 2-frame and 3-frame variants retain identical wings, body outlines, head/eye positions and animation timing.

Exactly two 8-bit mask rows changed (top-down index 3,4): `FF E7` → `EF EF`. This makes a **one-pixel-wide, two-pixel-tall vertical negative-space beak**, slightly left of center (pixel x3), with both eyes unchanged (third top-down row `DB`). Other six rows unchanged.

## Three unique frames (8 bytes, top to bottom)
| Frame | 8 bytes |
|---|---|
| B0 resting (also A1) | `18 7E DB EF EF 7E 7E 24` |
| B1 middle (also A0) | `18 7E DB EF EF FF BD 24` |
| B2 wings out | `18 7E DB EF EF FF FF 24` |

The current 9-byte ROM table convention (bottom-up plus 00 blank) is in [ART_ONLY.inc](./ART_ONLY.inc). No new animation phase or memory cost versus the previous U3 proposal. S3, Presence, coordinate and gameplay source remain untouched.

### Exact pixel mask, B1
```text
...##...
.######.
##.##.##
###.####
###.####
########
#.####.#
..#..#..
```
`#` = opaque P0 owl pixel; `.` = background.

Compared to earlier mask `18 7E DB FF E7 FF BD 24`, this is a targeted **two-row mouth/beak edit only**. No emulators or hardware tests have been run for these new exact bytes. The previous Issue #14 test used other, noncanonical owl/sigil bytes and cannot verify this design.

**Frozen product unchanged:** `e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974` / Draft PR#4. No merge/release.