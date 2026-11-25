# Renderer comparison

| Option | Hardware | Status | Missing evidence |
|---|---|---|---|
| Compact asymmetric playfield font | Modify PF bits in upper HUD | NOT_RUN | Real 1x frame, digit readability, status combos, scanline bus, restore |
| P0/P1 sprite font | Reuse players in selected top rows | NOT_RUN | Sprite availability, HMOVE ghosts, authentic frame, timing |
| Hybrid/narrow font | Reduce rows/bytes with possible legibility cost | NOT_RUN | No kernel or visual evidence |

The existing upper 16 rows already carry phase, slots, Presence and owl setup. No space is declared free. No screenshots/video were created.
