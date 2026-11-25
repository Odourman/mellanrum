# Timer contract and independent oracle plan

The contract retained from HEALTH III is: A/FIRE + Difficulty A starts at 00:00; count campaign frames through modes 1 and 2, waits and transitions; SELECT and denied actions never reset/pause; freeze the visible snapshot at first valid room 15 win while underlying time continues if the player replays the final room; lock the definitive value at coda entry; show through the existing 720-frame coda if legible; RESET clears the attempt; Difficulty B/FRI has no timer; frame time comes from NTSC emulated frames; saturate display at 99:59 without affecting play.

Independent oracle required for a future candidate: count actual emulator frame callbacks between title FIRE frame `N0` and accepted final-win frame `Nwin`, using one documented full-frame interval convention; expected displayed seconds are floor of completed intervals / chosen NTSC conversion. It must not read the ROM timer to compute expected values. Check frame 0/1, 59/60/61, 599/600, 5999/6000, saturation, SELECT replay, RESET, mode2 waits, FRI, coda, and long-run monotonicity.

No timer bytes, timer update instruction, timer display, or timer candidate exists in this lab. Therefore no oracle execution, timebase selection, carry/overflow cycle measurement, start/stop frame proof, or displayed-digit test is claimed. All T01–T24 are `NOT_RUN` on a timer ROM.
