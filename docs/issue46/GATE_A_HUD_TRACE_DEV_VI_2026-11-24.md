# Issue #46: ROM DEVELOPMENT VI Gate A targeted HUD trace — 2026-11-24

**DEVELOPER_DIAGNOSTIC_PASS_BOUNDED; MAIN receipt/review pending; no Gate B product integration.** No product files modified.

Pinned PR44 HEAD 5b98c8c14d5c38232fee30a3609e939818b61e8b, source eaa6b97f9313cb0c49f39b3f4d301da601df638d, ROM SHA256 07970f492ca9c8aa2f0445b00ce6a046624176db6ebaa7917d7392b7f6b43c2c (16384 bytes). Native Gopher executable SHA256 7b12dff57fcb73154122d2477f35d9c8ae8b344649bc0faa8ff6f5663c70470b, source 74c544203378c1448a33c29bc8b4586079b050f4, original artifact 14780574047, archive SHA256 662ebc5e3af35e8af8710cd91722328c58f1959f088450cdfe323d6e5b3101b7.

Ten actual native Gopher instruction traces: rooms zero-based 6,8,11,14 with both polarities, room12 with forced active Presence and both polarities. Room/polarity/Presence POKEs are explicitly diagnostic. 42,504 observed CPU instruction boundaries, 1,900 visible WSYNC observations, 0 skipped visible WSYNC, all 10 complete frames 262 scanlines. VBLANK off/on writes at SL35/227 in all 10. Five pairs of authentic Gopher display-scaled 1026x700 screenshots differ only at the stone and expected HUD polarity indicator; no exit or other changes. These are not 1x Stella images. Native trace coordinates use visible color clock CL=0; HBLANK begins CL=-68.

| Event | Polarity0 | Polarity1 |
|---|---|---|
| final blank WSYNC F93D | SL210 CL145 | same |
| next instruction F93F | SL211 CL-68 | same |
| PF0 store F96A | SL211 CL118, next CL127 | same |
| PF2 store F976 | SL211 CL151, next SL212 CL-68 | SL211 CL157, next SL212 CL-62 |
| PF1 store F97A | SL212 CL-62, next CL-53 | SL212 CL-56, next CL-47 |
| HUD WSYNC F97C | SL212 CL-53 | SL212 CL-47 |
| HUD prep F97E | SL213 CL-68 | same |

The 84/86-cycle span crosses naturally into HUD's first line; PF1 has settled before CL=0, PF2 before its visible region. No extra visible WSYNC skip or observed polarity-dependent artifact outside intended pixels. PF0 changes late on the preceding line in both cases; it is existing baseline timing, not a new shift. Recommend **no speculative correction**. Full all-path raster and physical hardware remain INCONCLUSIVE/NOT_RUN. Prior developer static max-five-JSR and ordinary Stem13 page-safety are unchanged; this is not independent Verification.

## Separate preparation (SOURCE_ONLY)

12/12 corrected approved masks mathematically checked against original ROM; DOWN B2 top-down ends 7C per subsequent MAIN IV prompt. All 15 compressed GeoPF data arrays reconstructed byte-identically: common 6-byte top + 36 unique bytes + common 6-byte bottom. 90 gross saved, 54 rotated-mask bytes added, net gross 36 before code, alignment, pointers. No runtime build or integration claim. Proposed use existing geom storage $BB as actual successful render direction (all source accesses audited; old test harness reads geom, update contract; retain mapPtr for LatchFire). Move wing selection into a budgeted top HUD line, use REFP0 only for left and clear it in HUD prep; don't add Stem13 cycles. Actual layout, page-cross, timing and RAM behavior must be rechecked after integration.

**MAIN IV:** please receive the new targeted Gate A evidence before Gate B product work, as required by the current user-authorized prompt. Archive and raw logs provided in developer conversation. PR38/44 protected. No merge/release.
