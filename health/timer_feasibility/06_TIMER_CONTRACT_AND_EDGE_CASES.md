# Timer contract and unresolved edges

A/FIRE from title + Difficulty A starts campaign at 00:00. Count mode1 and mode2, preparation, waits and transitions. SELECT/held SELECT, denied FIRE, phase, echo and Presence cannot pause/reset. Freeze visible value at first valid room14 win while underlying time continues if room14 is restarted before coda. At coda start lock definitive time and show it through the existing 720-frame coda if visually safe. RESET returns title; next campaign starts at zero. B/FIRE FRI has no timer and must preserve sound counters/seed. NTSC frames only; no wall clock. Saturate at 99:59 without wrap.

Unresolved semantic edge: if displayed time freezes at first win while underlying time continues during wait and SELECT replay, coda's later locked value may differ. MAIN/user must decide whether coda display updates to that later value or whether "frozen" locks the final value at first win. The authorized prompt recommends counting replay time; excluding it is a design deviation.

No timer implementation or oracle run exists. All timing edge cases are NOT_RUN.
