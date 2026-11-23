# Source provenance / 2026-11-22

Authority: latest user full-game request; MAIN full-game GitHub order; verified V5.1 original rules/`reference/rooms.json`; final GRAPHICS V5.1; lower source only advisory.

| Source | Byte count | SHA-256 | Finding |
| --- | ---: | --- | --- |
| `MELLANRUM_GRAPHICS_V51_FINAL_TILL_MAIN_2026-11-22.zip` (user attachment) | 1,539,775 | `b9ae037d7e29602dc44ea7401e6739ba3cd606e03a90375ebc23ad3b06d5e419` | 117 archive entries, no invalid ZIP members, 116/116 SHA manifest files validated; 25 actual graphics sprite masks |
| `MELLANRUM_GRAPHICS_V5_1_OVERLAMNING_2026-11-22.zip` (user attachment) | 1,465,386 | `05e859233b8f514b1acf9f27224b75a02bc55d7a244f0de52607631f15767fe9` | 69 ZIP entries, testzip no bad member; includes original V5.1 as nested ZIP |
| Nested `ORIGINAL_V5_1_HUVUDPAKET.zip` | 570,796 | `7bb664dcd5a64e9dd8435aa83328827c72c345da5d9fb83b9d41bf70a34a3e5e` | 40 entries, no bad ZIP member. Original file by name was NOT separately mounted in this user message; byte identity to a separate unattainable copy is not asserted |
| Original `reference/rooms.json` | See versioned source | `ea80a4cc7d736db6b0b107560b37b064dc06399ee681d3c50ae3e042b05ada78` | 15 original candidate rooms; identical across nested V5.1 copy and final GRAPHICS `rooms_v51_original.json` |

The original nested ZIP's `LAS_MIG_FORST.md`, full paper, `reference/engine.py`, `test_engine.py`, model and room traces were inspected before generation. The final GRAPHICS archive's `STARTTEXT_TILL_MAIN.txt`, `00_GRAFIKAVHANDLING_FULLSTANDIG.md`, `01_GRAFISKT_MANIFEST_OCH_BESLUT.md`, `14_ARKIV_KALLOR_OCH_PROVENIENS.md`, `SHA256SUMS.txt`, `03_SPRITES_BITMATRISER/` and 15 room folders were inspected.

The historical synthetic **R01–R15 contact sheet** is from the G0 visual sketch and is **NOT** the canonical V5.1 room configuration. It is not used for ROM data.

Only source files needed for reproducible ROM building are vendored under `reference/`, `graphics/`, and `rom/src/data.inc`. Original sources are not silently modified by the generator. GRAPHICS 25 versus 23-mask mention is resolved by counting JSON records: **25 defined**; the conflicting 23 is a documentation inconsistency, not the actual data count.
