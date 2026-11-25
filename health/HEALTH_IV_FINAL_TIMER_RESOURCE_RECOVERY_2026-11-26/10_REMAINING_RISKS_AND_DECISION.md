# Remaining risks and final decision

## Confirmed findings

- A1 can reclaim `$C1` from `exitX` under source analysis and the sentinel-tested replay.
- A1 modifies CPU instruction timing and does not reproduce baseline framebuffer/PCM exactly.
- B1 pointer reuse, AB combined resources, and C2 input-edge bitpacking do not fit the fixed bank3 code window as actually assembled.
- A1+A+B do not reach the minimum persistent timer + mode2 snapshot budget. No font/decoder/gateway budget exists.
- coda/audio state limits alias choices. `codaHi` remains long-form soundtrack state during mode1/2; `codaLo` is used by the coda countdown.

## Unproven, not FAIL

No timer update code, fixed-point/60-frame counter, MM:SS conversion, final-time snapshot, renderer, timer/carry timing, timer-vs-LAB bus trace, Gopher timer test, global 262-line timer trace, timer stack high-water, T01–T24, human audio/readability, or hardware test was run. They are `NOT_RUN` because no candidate exists, not because an implementation was tested and shown to fail.

RLE's offline storage savings do not establish runtime feasibility. A runtime decoder and its cycle/RAM/score-write timing need a separate genuine build; this lab did not create one.

## Decision

`TIMER_NO_GO_WITHIN_TESTED_CONSTRAINTS` is appropriate: several direct practical paths were assembled/measured and could not provide the required persistent state and executable space while preserving all listed requirements. This is not universal impossibility proof. The practical recommendation is to leave the existing game without a campaign timer. No further open-ended research is recommended. Any future proposal to alter timer semantics, ROM size, mapper, audio, HUD or coda would need a separate explicit design decision and scope.
