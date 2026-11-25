# HEALTH IV – handoff to MAIN IV

**Game/role:** MELLANRUM: SKOGEN SOM LYSSNAR / HEALTH, final bounded timer-resource lab  
**Status:** `TIMER_NO_GO_WITHIN_TESTED_CONSTRAINTS`  
**Date:** 2026-11-26  
**Product/release:** No product change, no timer ROM, no PR, merge, tag, or release.

## Decision

No safe playable timer candidate was produced. The strongest new RAM witness is one byte at `$C1` after replacing `exitX` with the verified constant 8. A diagnostic sentinel retained `$A5` at `$C1` through a 19,652-frame real Stella replay covering all 15 rooms, modes 0–3, and coda. The playable A1 source built as standard F6 and reached all 15 wins/coda/title, but its framebuffer hashes and a small number of PCM bytes differed from the LAB baseline. It is resource evidence, not a timer candidate.

The best tested pointer-recompute patch (B1) did not assemble: code reached `$FF9B`, 11 bytes beyond the fixed `$FF90` F6 trampoline. Combining A1's four-byte code reduction with B1 still reached `$FF97`, seven bytes beyond the boundary, before any timer routine, font, or gateway. Packing two input-edge flags saved one RAM byte in source but exceeded the same boundary by 15 bytes. A pre-coda snapshot also needs two bytes while the live timer needs three; `codaHi` remains part of long-form score timing outside coda.

An offline lossless RLE roundtrip covers all 11,520 soundtrack bytes and packs to 2,334 bytes. This does not supply a runtime decoder: the bank score routines end at `$FF86/$FF8A`, leaving 10/6 bytes before `$FF90`, and no spare persistent decoder state was proven. No compressed ROM was built.

**Recommendation:** abandon the campaign timer under the present 16 KiB F6, RAM, audio, display, and behavior constraints. Keep the frozen RC1/product path untouched. This is a bounded practical NO-GO, not a mathematical proof that no different design could ever work.

## Evidence and limits

- LAB source `main.asm` SHA-256 `3246d67a40470454eb56c38f2f4c32fb34ccb4ff38ed796ccb10cf00a647d53e`; clean native LAB ROM SHA-256 `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`.
- A1 ROM SHA-256 `68f945ade7441ea8c59b4ccdecf216af8a06d399e8b38e0162e7c6f788af0def`, 16,384 B, F6. Stella core SHA `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`.
- A1 retained the recorded 295-interval input replay: same 15 room wins and frame indices, coda, and title return. Of 19,652 full-frame hashes, 19,220 differ from the baseline run. At a saved checkpoint, eight pixels differ at `(60–63,40)` and `(60–63,180)`. PCM files have equal format/length; 28 of 41,188,496 bytes differ. Human audibility was not assessed.
- A1C adds two NOPs to restore the one-cycle-per-compare change. Its 19,652 frame hashes match baseline, but PCM differs in 1,935,416 bytes; rejected.
- A1 sentinel diagnostic ROM SHA `97f0377383934ce8dd9867b221c3b9ccccdcc2220b50dc2036ea041bf4c7268f`; read-only RAM showed `$C1==$A5` on every frame across all rooms and modes 0–3. It is diagnostic only.
- Timer core, visible renderer, independent timer oracle, Gopher timer run, timer raster/stack proof, and T01–T24 on a timer candidate: `NOT_RUN` because no candidate exists.

See `01_FINAL_RESOURCE_RECOVERY_REPORT_SV.md`, ledgers, test matrix, and experiment folders. Existing HEALTH III archive is referenced by its verified Drive ID and hash in the full report; it is not duplicated here.
