# Rejected, invalid, or bounded-only experiments

| ID | Class | Result | Why |
|---|---|---|---|
| Prior ALLOC3 | Invalid allocation/layout probe | Rejected | `DS` mapped timer symbols to `$F6-$F8`; no executable timer code. It remains historical, not a new test. |
| A1 | Resource-only ROM | Built; bounded Stella playthrough PASS; output delta | `$C1` is live-independent under tested source and dynamic sentinel, but the changed compare cycles/layout produce 19,220 differing frame hashes and 28 PCM bytes. Not accepted as timing/audio-parity baseline. |
| A1C | Resource-only ROM | Built; screenshot/fullframe parity PASS; PCM parity FAIL | Two-cycle NOP is not an exact one-cycle compensation. 1,935,416 PCM bytes differ. |
| A1_SENTINEL | Diagnostic-only ROM | 19,652-frame RAM witness PASS | Explicitly writes `$A5`; validates RAM liveness only, not normal game semantics or timer. |
| B1 | Source patch | Native BUILD_FAIL | Shared `pfPtr` recompute patch ends at `$FF9B`; fixed `$FF90` overrun by 11 B. No ROM/emulator test. |
| AB | Source patch | Native BUILD_FAIL | A1+B1 ends at `$FF97`; fixed `$FF90` overrun by 7 B. No ROM/emulator test. |
| C2 | Source patch | Native BUILD_FAIL | Packed `prevFire/prevSelect`, with reserved former `$D1` slot to preserve later RAM addresses, ends at `$FF9F`; overrun 15 B. Model-only exhaustive finite-state test is separate. |
| R2 RLE | Offline reversible data transform | 45/45 streams roundtrip PASS | No runtime decoder, ROM placement, RAM state, cycle budget, TIA timing or audio parity. 9,186 B offline reduction is not counted as recovered runtime ROM. |

No experiment overwrote the LAB baseline, RC1, main, PR49, previous HEALTH/VERIFICATION/PACHINKO evidence, or another specialist branch.
