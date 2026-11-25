# MELLANRUM – independent HEALTH LAB_STACK_INLINE_PADDED_B verification (2026-11-25)

**RESULT: `LAB_INDEPENDENT_DELTA_PASS_BOUNDED` / `GLOBAL_ALL_PATH_TIMING_INCONCLUSIVE`.** No new proven release-blocking product error in performed scope. Experiment **is not RC2**, no merge/release/production change. Frozen PR49 remains source reference.

## Original unmodified ROMs and source
- RC1 PR49 HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`, product commit `7b400ad8678e8341a26f65cc757b1eb762654c83`, SHA256 `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd`.
- HEALTH exact `LAB_STACK_INLINE_PADDED_B` experimental ROM SHA256 `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`.
- Two fresh genuine DASM builds per ROM (4 total), byte parity, all four banks and source-diff checked. The HEALTH documentation branch is **not** an experimental source commit. Exact source snapshot and original build logs are inside archive, with their own sha manifest.

## Independent assessment
- Valid-source CFG max nested JSR **5→4**, true native 6507 stack-bus natural witness at I-01 frame124, spare two bytes `$F6..$F7`; no RAM gain and only four free bank3 bytes remain.
- One branch loses one cycle if taken; 58 changed page-cross index sets, with three new +1 CPU-cycle classes in valid domain (title Y2/3, room GeoMapHi X1/2, RoomStoneY X4/5).
- **64 genuine title TIA bus writes +3 colorclocks** in lines84..99, yet ≥32 clocks remaining to the relevant right-side PF segment deadlines and no 160×228 Stella pixel difference. These are *real timing differences*, **not** timing identity.
- New genuine Stella **19,652/19,652 framebuffers** and **20,594,248/20,594,248 int16 PCM** identical RC1 repeat RC1 vs LAB_BEST; separate native Gopher **19,780 STEP FRAME, 15/15 rooms**, with 278 262-line TV samples.
- LAB-specific 540,000 idle frames; 15/15 causal omission, 15/15 SELECT-after-win, 15/15 alternative FIRE→SELECT→re-win, 50,010 FRI frames and 27,000 no-SELECT FRI frames with 255→0 beatwrap; natural four cursor states including III04 intercepted at global frame16637 in two independently cold-booted Stella processes, 12/12 U3 masks.
- Negative controls old PR47 and deliberately late-BCS yielded **263** scanlines at HUD x9, while RC1 and LAB_BEST yielded **262**. Five focused bus traces include differing *ignored WSYNC write-data*, with every meaningful register value and position matching.
- Overall reachable combined TIA/76-cycle all-path proof **INCONCLUSIVE**, physical Atari/RetroN77 and human cold-play/audio/art **NOT_RUN**. Full naturally instrumented bank1 bus trace **NOT_RUN** (bounded bank1 tests PASS).

## Reports, machine results and original evidence
- [Full Swedish independent report](INDEPENDENT_LAB_VERIFICATION_REPORT.md)
- [MAIN IV concise handoff](MAIN_IV_HANDOFF.md)
- [Separate prospective PACHINKO risks – not started](PACHINKO_RISK_HANDOFF.md)
- [Complete valid-domain relocation ledger (58 entries)](analysis/RELOCATION_DOMAIN_AUDIT.csv)
- [Machine-readable test matrix](analysis/TEST_MATRIX.csv)
- [CPU/TIA deadline summary](analysis/CYCLE_AND_TIA_DEADLINES.json)
- [Original source unified diff](analysis/EXACT_RC1_LAB_MAIN_ASM.diff)
- **[Full independent 1,048-member evidence ZIP in project Google Drive](https://drive.google.com/file/d/1pTfdnjhiBamHn406lcfSsdT5uEQgPB_x/view)**: 4,640,886 bytes, SHA256 `d4eca534a98cc5cb5222a05fed961cc05e6d3f5bd8fa472ad15df24229b4a599`, 1,047/1,047 SHA256 payloads/ZIP CRC PASS. This ZIP includes unchanged original ROMs and full independent raw Gopher/Stella CPU/beam/audio/pixel/controller outputs, all four fresh native assemblies, genuine original logs, tools, invalid test-harness evidence and corrected scripts.
- [HEALTH original source ZIP](https://drive.google.com/file/d/1GbegbPtjIseOp-p06-7KGrxq0DWsId_x/view) is developer reference only.

**Recommendation to MAIN IV:** independent stack benefit is credible within measured scope, and real relocation penalties are measured with no new output regression in tests. Keep RC1 frozen as product. User/MAIN can **separately** decide whether to authorize independent PACHINKO on **this exact experiment SHA** before any possible later RC2 decision. No automatic PACHINKO, ROM DEVELOPMENT, merge, tag, or release.
