# REPRODUCE - Issue #42 PR38 BFDEB P0 follow-up

Source HEAD: 6e9db179867234a19cce329c709170f2423ffbbb
ROM SHA256: bfdeb5308dcecc526e802cd95886b94e0ce4953628e7bc7190c5d49231deac06
ROM size: 16384 bytes, F6/NTSC 4 x 4096, unchanged.
Gopher executable source: 74c544203378c1448a33c29bc8b4586079b050f4, native unreleased build.

The standalone 82-member evidence ZIP is supplied to the user in this VERIFICATION chat (SHA256 72900c4b3000b928a95259579234aca3f18c8e5d465c850780705a2cc121f934; ZIP CRC passed). It is NOT attached to GitHub. Extract ZIP; retain its directory layout. On Linux, chmod +x previous/gopher/gopher2600 if needed. All required binary and native listing bytes are inside ZIP.

From extraction root:

```bash
sha256sum previous/grounded/MELLANRUM_16K_NTSC_F6.bin
python static_stack_cfg.py
python run_campaign_gopher.py
python analyze_campaign_allframe.py
python campaign_bank_input_alignment.py
python cycle_windows.py ACTIII_ROOM12_ACTIVE
python summarize_cycle_suite.py
python fri_gopher_allframe.py
python watch_stack_overflow.py
```

Outputs:
- static_cfg.json: 2486 context states, max JSR 5, four bank reset vectors.
- campaign_allframe_replay.txt and campaign_allframe_stdout.log: genuine controller trace, 19780 STEP FRAME + 20058 native TV reports, 20057 postboot 262-line frames and one 20-line partial startup.
- campaign_allframe_result.json and campaign_bank_input_alignment.json: 18190 complete F6 scorebank return pairs, 15/15 room windows, 73 FIRE rising edges.
- cycle_windows/*/stdout.log: 8 real Gopher instruction-step recordings, 31859 CPU instruction boundaries, 1608 WSYNC; ACTIII_REPLICATIONS/trial1.log and trial2.log reproduce late VBLANK WSYNC at F68C.
- fri_gopher_adjudication.json and stack_guard_result.json: 780 native FRI controller frames, zero writes to mirrored stack $01F5.
- SHA256SUMS + PACKAGE_MANIFEST.json: archive integrity. No product file modified.

SOURCE_GUIDED full-campaign commands reproduce a known developer input sequence in a fresh verifier-owned emulator process. Forced Presence states in cycle_windows are separately marked DIAGNOSTIC and may not be reinterpreted as independently solved gameplay.

The full technical report (linked next to this document) describes measured bounds, remaining INCONCLUSIVE global 76-cycle all-path gate, and NOT_RUN independent new Stella CPU trace / physical hardware.
