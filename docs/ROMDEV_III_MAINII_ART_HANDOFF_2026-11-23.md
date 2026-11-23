# ROM DEVELOPMENT III → MAIN II: Issue32 art revision, 2026-11-23
Status: **DEVELOPER_BUILD_AND_CAMPAIGN_PASS / ART_REVIEW_OPEN / NOT_RELEASE**.

## Identity
- Branch: `romdev/mainii-art-final-20261123`; Draft [PR #37](https://github.com/Odourman/mellanrum/pull/37), from frozen PR36 HEAD `bc5ad4a118f8909be131163529325055d4e0413e`.
- Implementation source CI commit before pin: `3367a5f1ffbaaf29cfb050c3a2998fb7675f1c3d`. Pinned ROM commit `da7119899635a5b63a74f6ffa158a8e2265f3606` (subsequent evidence docs do not modify ROM).
- Native 16,384-byte F6 NTSC ROM SHA-256 **`d3754d78ec6c435b4641d4fc281f95a79acff0126c0ad3370db8156c8465853a`**; checked-in `rom/bin/MELLANRUM_16K_NTSC_F6.bin`, Git blob `a7d09eb8250c863ad981732479a7b7c303767230`.
- No changes made to protected PR #36, #33, #27, #23, #16 or #4. No merge, tag or release.

## Implemented against MAIN II video-audit
- First 24 title frames: electrical TIA disturbance without automatic start; hardware left A/B + FIRE remain in control.
- Dark, neutral-gray Act III background instead of persistent cobalt blue, retained visible green forest.
- Room-/phase-responsive forest color and changed negative-space Presence pattern.
- Conifer top raster narrowed for two scanlines, broader branches restored below; real 6507/TIA kernel, original U3 and S3 untouched.
- 12-second ambiguous coda, full title return.
- Separate real native campaign and *genuine* left-Difficulty B FRI SKOG controller replay. Both H.264/AAC versions in user handoff archive, 30fps, 320x228.
- Still aesthetically open: trees can remain too T-like, owl/markers small, 15 rooms not all qualitatively redesigned by this revision. Do NOT call artistic final acceptance.

## Same-ROM native developer evidence
- [Native DASM + Stella 15/15, 19,652 frames, 720f coda, 12,000f genuine FRI SKOG, authentic stereo TIA WAV, artifact](https://github.com/Odourman/mellanrum/actions/runs/45247959885), same source bytes reproduced on [run 45248173350](https://github.com/Odourman/mellanrum/actions/runs/45248173350).
- [True Gopher2600 native controller 15/15, full coda, 19,780 frames, 278/278 sampled 262-line NTSC frames](https://github.com/Odourman/mellanrum/actions/runs/45248173545).
- [Guarded source→ROM pin and genuine Stella 15/15 run](https://github.com/Odourman/mellanrum/actions/runs/45250828064).
- Locally reproduced from genuine controller-reached libretro Stella savestates, RAM PEEK only, 15 × 36,000 no-input frames = 540,000 frames, 0 idle wins; 15 bounded critical-FIRE omission replays, 15 PASS, original win frame +360 horizon. Original scripts/JSON and same SHA provided in downloadable handoff ZIP, not yet uploaded as a dedicated Actions job.
- Core Stella `8.0_pre 8dd5600`, SO SHA-256 `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`.

## OPEN / NOT_RUN / INCONCLUSIVE
- 76-cycle per-line worst-case beam, RAM/stack high-water, full F6 fuzz / stress not exhaustively tested. 278 sampled Gopher 262-line frames do not close these gates.
- Human cold-play, professional audio judgement, alternative paths and softlock matrix, full 4-same-scene cursor/overlap audit for *new* SHA: NOT_RUN/INCONCLUSIVE.
- Physical Atari2600/RetroN77 and independent final SHA Verification/Pachinko: NOT_RUN. Old Issues #28/#29 tied to old PR27 SHA.
- This is a working engineering candidate, **not** a claimed fully polished artistic end-state or release.

MAIN II should review the actual 2 videos and source/trace bundle for game-feel, graphical legibility and causal variety, and only commission independent Verification/Pachinko when art/code freezes on an exact final SHA.
