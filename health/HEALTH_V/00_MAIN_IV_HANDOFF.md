# MAIN IV handoff – HEALTH V room-number experiment

**Disposition:** `ROOM_NUMBER_NO_GO_WITHIN_TESTED_CONSTRAINTS`

HEALTH V used the exact `LAB_STACK_INLINE_PADDED_B` source and ROM named by the order. The source rebuilt with native DASM to the same 16,384-byte F6 ROM and the expected SHA-256. Two isolated bank-3 renderer footprint probes (3×5 PF2 and temporary P0/P1) were then assembled independently. Both hit DASM `Origin Reverse-indexed` when the added code crossed the fixed `$FF90` F6 trampoline. No candidate ROM was produced.

The baseline bank-gap record shows only one free byte before the trampoline and three after the coda in bank 3, separated by fixed structures. The PF probe reaches `$FFCA` before the `$FF90` origin (58 bytes beyond); the sprite probe reaches `$FFD2` (66 bytes beyond). These probes only estimate minimum code/data placement and do not claim to be complete renderers. A complete mode-gated renderer, row scheduling, two-digit handling for 10–15, TIA state restoration and transition logic would need additional bytes and raster work. On the tested layout, neither method is viable as a local insertion. A cross-bank renderer was not attempted because it would require a new bank-dispatch path during the visible kernel and could change its timing; that is not a small, bounded implementation.

**Actual PASS:** exact baseline source/ROM identification; clean native DASM baseline rebuild; all four banks assembled to 4,096 bytes; rebuilt ROM SHA matched the prescribed LAB SHA. **Actual FAIL:** both local footprint assemblies fail at the bank-3 fixed-origin overlap. **NOT_RUN:** every room-number function, candidate Stella/Gopher gameplay, candidate screenshots/video, timing/stack/audio comparisons, PR47 negative control, and candidate full-campaign regression. No candidate existed to run them against. Historical LAB emulator evidence is not counted as new HEALTH V testing.

No changes were made to PR49, `main`, the frozen product ROM or the LAB source. This experiment does not authorize promotion, merge, release, or resumption of any other work. Recommend retaining the verified LAB without a room number unless MAIN authorizes a separately scoped design/resource change.

## Identity

- Baseline source `main.asm`: `3246d67a40470454eb56c38f2f4c32fb34ccb4ff38ed796ccb10cf00a647d53e`
- Baseline 16K F6 ROM: `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`
- Baseline commit context: PR49 HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`; repository main/base observed `e1f70ccd7bab353fbe2232612c408683a41d937f`
- Native assembler: project-bundled DASM, binary SHA-256 `cfb23732297a4fe1c8d4a78d44206037d97733aedb2772503bbf029a4aa91291`; project build script identifies native DASM 6507. Tool output is retained in `baseline/` and `attempts/`.
