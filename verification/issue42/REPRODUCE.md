# Reproduce Verification #42 on immutable PR #38 BFDEB

Use source commit `6e9db179867234a19cce329c709170f2423ffbbb` and confirm exact original ROM SHA-256 `bfdeb5308dcecc526e802cd95886b94e0ce4953628e7bc7190c5d49231deac06` before running any case. No changes to production ROM or mapper are permitted. Original Git blob `51dc00b5ce8170b289acd0b4d997e0c6080b8f54`.

## Native source→bank→ROM check

Independent GH Actions workflow [run #45381991878](https://github.com/Odourman/mellanrum/actions/runs/45381991878), artifact ID `14913109392`. Workflow source: [verification42-independent-build.yml](https://github.com/Odourman/mellanrum/blob/verification/issue42-pr38-bfdeb-20261124/.github/workflows/verification42-independent-build.yml).

```bash
dasm rom/f6/bank0_score.asm -f3 -obank0.bin -lbank0.lst -sbank0.sym
dasm rom/f6/bank1_score.asm -f3 -obank1.bin -lbank1.lst -sbank1.sym
dasm rom/f6/bank2_score.asm -f3 -obank2.bin -lbank2.lst -sbank2.sym
dasm rom/src/main.asm -f3 -obank3.bin -lbank3.lst -sbank3.sym
cat bank0.bin bank1.bin bank2.bin bank3.bin > independent_16k.bin
sha256sum independent_16k.bin
cmp independent_16k.bin rom/bin/MELLANRUM_16K_NTSC_F6.bin
```

Native DASM tested: Ubuntu24.04 apt package `2.20.15~20201109+really2.20.14.1-2`. Expected 16,384 bytes and exact BFDEB SHA.

## Real emulator instructions

Unzip evidence ZIP from Verification chat **into a directory preserving all relative paths**. ROM: `grounded/MELLANRUM_16K_NTSC_F6.bin`; original libretro Stella core: `grounded/stella_libretro.so`; original Linux Gopher: `gopher/gopher2600`. Python 3 dependencies: ctypes, json, PIL/Pillow, hashlib. Original libretro device-adapter source is `source/tests/issue15/libretro_stella_capture.py`, while all independent PASS decisions derive from independent Verification Python.

```bash
python stella_verify.py                    # Stella 15/15 SOURCE_GUIDED, 19,652 frames
python stella_idle.py 0                    # index selected room as supported by script
python stella_counterfactual.py 0          # index selected room as supported by script
python stella_fri50k.py                   # 50,010 actual free-forest frames
python stella_beat_wrap.py                # 26,000 consecutive frames, beat rollover
python stella_telemetry.py                # full per-frame RAM observation
python presence_intercept_controller.py   # actual controller-driven ActIII interception
python stella_marker_compare.py           # separate, forced-RAM renderer diagnostic
python gopher_bank_probe.py               # forced-room bank diagnostics, see script
python gopher_raster_diagnostic.py        # 312-frame ActII and ActIII POKE diagnostics
python stack_probe.py                     # ActI actual CPU/SP trace, first 215 frames
python gopher_stack_actIII_diagnostic.py  # separately forced-room ActIII CPU/SP
```

Check each script's exact CLI arguments; some take batch/room parameters. Inspect `result.json` and corresponding raw `stdout.log` for **actual** frame, memory and CPU findings. `independent_gopher_campaign/stdout.log` is a terminated **partial** replay, not a 15/15 completion. Native screenshots and WAV are actual source-ROM outputs; the same-scene 4-form test explicitly uses forced RAM diagnostic states and cannot be described as four normal user-reachable action sequences.

The source-guided frame-indexed control inputs come from **developer witness**, and this has been preserved as a provenance classification: it is independently reexecuted, not independently solved. Individual 15×36,000 idle and 15 critical FIRE omission results are new Verification emulator executions.

Full status and remaining P0 blockers: [INDEPENDENT_VERIFICATION report](https://github.com/Odourman/mellanrum/blob/verification/issue42-pr38-bfdeb-20261124/verification/issue42/INDEPENDENT_VERIFICATION_PR38_BFDEB_2026-11-24.md).
