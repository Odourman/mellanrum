# Renderer budget and image evidence

**Timer renderer:** `NOT_RUN`. No real font, playfield/sprite path, row selection, TIA restore, timer readout, cycle budget, or timer screenshot exists. Existing HUD rows and P0/P1/M0/BL/PF uses are still occupied. A concept or pseudo-kernel would not establish net code/data placement.

**A1 resource-only replay (not timer output):** real Stella/libretro 8.0_pre, 320×228, 19,652 frame callbacks, 295 recorded input intervals; all 15 room wins, coda, title return. Baseline and A1 used the same saved frame-indexed input intervals. Candidate A1 had 19,220 full-frame framebuffer hashes differ from baseline. At saved frame 17, 8 pixels differed at x=60..63, y=40 and y=180. The image diff is retained in the experiment archive.

**A1C rejected cycle-padding replay:** 19,652/19,652 framebuffer hashes matched baseline, but PCM differed in 1,935,416 bytes. A1's unpadded change differed in 28 PCM bytes. No human listening test was performed; no audible PASS is claimed. The diagnostic `$A5` sentinel build is not a graphics/audio candidate.

The full Stella WAVs and images for A1 baseline/candidate are retained under `EXPERIMENTS/A1/TEST`; A1C images/audio are retained under `EXPERIMENTS/A1C/TEST`. No video was generated because no integrated timer ROM exists.
