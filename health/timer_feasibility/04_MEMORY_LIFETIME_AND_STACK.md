# Memory lifetime and stack assessment

LAB declares $80..$F5 (118 bytes); $F6..$F7 are protected stack reserve and $F8..$FF is the stated maximum eight-byte active stack area. Exact symbols are in BASELINE/CLEAN_NATIVE_BUILD.

A simple frame-phase timer needs three simultaneously live bytes (phase 0..59 plus two MM:SS bytes); a 24-bit frame counter also needs three. Actual allocation probe symbols are timerFrames=$F6, timerSeconds=$F7, timerMinutes=$F8. Static reserve gate rejects these. DS declarations emit no ROM bytes, so the diagnostic image hash is identical to LAB and is not a candidate.

Source liveness cautions: codaHi participates in soundStep carry and soundtrack state; soundStep affects FRI seed; waitFrames supports encounter/win wait; introFrames/beatFrames are reinitialized and used per room; candidate/work/move/index/pointer values are used by gameplay/rendering; codaLo has possible pre-coda availability but is one byte and StartCoda overwrites it. Previous candidateD/workX alias was rejected in prior HEALTH evidence for observed image/PCM differences. No complete new all-path alias proof exists.

No timer calls were added. The stack reserve remains intact in valid LAB. The allocation probe fails because its RAM symbols intrude into stack addresses. Dynamic timer stack measurement is NOT_RUN.
