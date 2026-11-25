# Rejected and incomplete experiments

| ID | Hypothesis | Action | Result |
|---|---|---|---|
| E0 | Rebuild exact LAB first | Native DASM build of clean source composition | PASS, exact SHA 8a59...df03b |
| RAM-3 direct allocation | Three bytes after current variables fit | Added three DS declarations, built banks, inspected sym | FAIL: $F6-$F8 overlaps reserve/stack |
| Prior candidateD/workX alias | Reuse scratch | Prior HEALTH evidence preserved; not repeated | Rejected in prior lab for image/PCM differences |
| codaLo alias | Reuse one pre-coda byte | Source inspection | Incomplete: one byte and overwritten by StartCoda |
| codaHi/soundStep alias | Reuse audio state | Source inspection | Rejected: live soundtrack and FRI seed semantics |
| PF renderer | Fit timer in upper HUD | Not built | NOT_RUN |
| Sprite renderer | Reuse P0/P1 for digits | Not built | NOT_RUN |
| Integrated timer ROM | Add only timer to LAB | Not built | NOT_RUN; no playable ROM |

Allocation probe ROM equals LAB bytes and is not a timer ROM.
