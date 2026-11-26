# HEALTH V – minimal room-number implementation lab

This package records a bounded NO-GO for the requested decimal room number. It includes the exact LAB baseline, a clean native DASM rebuild, two isolated local footprint attempts, their bank-3 listings and build logs, the final report, and test matrix.

Rebuild the baseline from `baseline/source/rom/f6/build_f6.py` with the bundled project DASM on PATH:

```sh
PATH=/path/to/dasm:$PATH python3 baseline/source/rom/f6/build_f6.py --out build/healthv_baseline
```

Expected ROM SHA-256: `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`.

To reproduce either failed footprint build, use the same command from its `source/rom/f6/build_f6.py`. Both fail while assembling bank 3 with DASM `Origin Reverse-indexed`; there is intentionally no candidate ROM. Probe files are not functional renderers and no candidate gameplay or emulator test is claimed.

`baseline/` contains build metadata, listings/symbols and the unchanged ROM. `attempts/` contains the separate PF2 and sprite probe sources, partial bank outputs/listings and raw stdout/stderr. `01_HEALTHV_REPORT_SV.md` records PASS/FAIL/NOT_RUN explicitly.
