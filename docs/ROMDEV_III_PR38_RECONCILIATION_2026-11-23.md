# ROM DEVELOPMENT III – PR38 reconciliering efter anslutningsavbrott (2026-11-23)

**Status: Developer emulator candidate, artistically incomplete. No merge/release.**

- Original exact tested source: `2c70bf7468fc33eed198246281a8ffd0a7cc9252`.
- Subsequent source HEAD `1e6e6e55cb1afe99e4765fdef483bc92d9bf6a84` changes six legacy Issue15-only 4KiB Actions guards only; **ROM bytes unchanged**.
- Pinned 16,384 byte standard F6 NTSC ROM SHA-256: `7e5add7d2580e7ebb3e871a79c13d7ba5680e71354946c941fe79b826e158134`.
- ROM blob: `87371e9cbbe584e21a85d855062e50e13721ef17`.
- Real Stella 15/15 & authentic TIA PCM: https://github.com/Odourman/mellanrum/actions/runs/45264527061
- Real Gopher 15/15, full coda, 278 checked 262-NTSC raster samples: https://github.com/Odourman/mellanrum/actions/runs/45264527051
- Real Stella 15 × 36,000 idle frames, all 15 jobs PASS: https://github.com/Odourman/mellanrum/actions/runs/45264527111
- Real Stella selected necessary FIRE omission 15/15 local PASS (bounded to original win frame +360, not proof of all routes); supplementary SELECT after unexpected FIRE from 15 controller-reached starts PASS 15/15, separate recovery JSON and script.
- Two new original Stella MP4s (campaign 327.517s, FRI 199.984s), both H264/AAC at 320×228 with exact ROM-SHA above; local render paths, original audio WAV and decodes in downloadable handoff ZIP. **Do not use old 4921f723... video for 7e5add7d...**.
- Original TIA hardware is mono with two sound voices, not native stereo; libretro PCM used duplicated L/R channels.
- New user-facing handoff ZIP: `MELLANRUM_PR38_7E5ADD_VERIFIED_HANDOFF_2026-11-23.zip`, 33 SHA-256 manifest records and CRC test, provided in this chat.

### CI failures
Historical `game.yml` and `title-presence-stella.yml` failed because they execute Issue15 4KiB regeneration or variants against a 16KiB F6 candidate. They must stay visible as historical FAIL. The six legacy workflows are guarded on this branch; future SKIPPED is **not** PASS. New native workflows are true 16KiB acceptance checks.

### Still open
- Most campaign tree silhouettes remain T-/cross-shaped at 1× in the audited actual ROM, despite minor five-family crown variations. Fifteen rooms remain too visually similar, owl/marker small. **MAIN aesthetic concerns not fully satisfied.**
- Alternative-player strategies and permanent softlocks not exhaustively tested, and one missed FIRE per room is only a bounded necessity check.
- Full 76 CPU cycles per scanline worst-case, bank fuzz, stack/RAM high-water, native all-frame beam timing NOT_RUN/INCONCLUSIVE; 278 Gopher samples insufficient.
- New exact-ROM 4-marker same-scene proof and comprehensive owl collision/phase visual audit NOT_RUN.
- Human cold-play and human artistic TIA listening NOT_RUN.
- New independent Verification and Pachinko and physical NTSC Atari/RetroN77 NOT_RUN.
- Project Sources proposal at https://drive.google.com/file/d/1owkqh8N-dWjKzs8QNiYcqgvKLB3fsIDZ/view is **proposal only**, no direct canon/main or ChatGPT Project Settings changes, and requires final-state update by MAIN II.
- Protected PR37/36/33/27/23/16/4 unchanged.

**Recommendation to MAIN II:** do not mark ROM DEVELOPMENT complete. Next priority: materially improve campaign conifer silhouettes and level-by-level interaction visibility before final SHA freeze, then reproduce all changed-ROM tests. No merge or release.
