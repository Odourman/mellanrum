# Reproduction

Clean LAB source: BASELINE/LAB_BEST_SOURCE/main.asm and data.inc plus the pinned bank score sources/build_f6.py in BASELINE/PRIOR_HEALTH_EVIDENCE/MELLANRUM_HEALTH_OPTIMIZATION_LAB_EVIDENCE/BASELINE/SOURCE/rom/f6/. Run python3 build_f6.py --out <fresh-dir> from rom/f6/ using pinned TOOLS/dasm on PATH. Expect 16384 bytes, F6, SHA-256 8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b. Native .bin/.lst/.sym and ROM build JSON are under BASELINE/CLEAN_NATIVE_BUILD.

Allocation probe source is EXPERIMENTS/ALLOC3_RESERVATION_PROBE/SOURCE/rom/src/main.asm. It adds timerFrames, timerSeconds, timerMinutes before SEG code. bank3.sym shows $F6/$F7/$F8. Reject it as invalid due stack reserve/active stack conflict. Do not use its byte-identical ROM as timer build.

Prior evidence archives retain their own pins and manifests; they are not timer candidate evidence.
