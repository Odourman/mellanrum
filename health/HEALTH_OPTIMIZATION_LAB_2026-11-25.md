# MELLANRUM HEALTH optimization lab — 2026-11-25

This is an isolated, documentation-only handoff for MAIN IV. The branch is based on frozen PR49 HEAD `d013a0f82621d46ad12674a4a8e944bf005cd9c3`. It does not modify RC1 or PR49 and carries no merge, tag, release, or implementation authorization.

## Outcome

Best experiment: `LAB_STACK_INLINE_PADDED_B`, ROM SHA-256 `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`. The candidate inlines DecodeKey and uses six NOPs to retain the removed JSR+RTS 12-cycle envelope. The conservative whole-valid-call-graph analysis reports RC1 depth 5 and candidate depth 4, zero candidate analysis errors, 2,565 reachable candidate context states. A Gopher high-water watch independently shows the fifth JSR writes the baseline stack boundary and the candidate does not.

A native-opcode differential checked 983,040 cases across all 40 valid keys, status bytes with D clear, four A/X/Y seeds and three SP seeds. A/X/Y/P/SP, scratch outputs, continuation behavior and cycle totals matched. Same-input Stella campaign: 19,652/19,652 framebuffer hashes equal and 20,594,248/20,594,248 PCM samples equal. Gopher and Stella each completed 15/15 rooms, coda and title return.

This is measured experiment evidence, not product acceptance. Independent Verification/Pachinko, extended idle/countertests, human/physical play and release acceptance remain NOT_RUN.

## Files

- [Complete evidence ZIP](https://drive.google.com/file/d/1GbegbPtjIseOp-p06-7KGrxq0DWsId_x/view)
- [Full technical report](https://docs.google.com/document/d/1Z2vxdNNppzlC3f-61oOq8nYThyJ4pe5B/edit)
- [MAIN IV handoff](https://docs.google.com/document/d/1Y8JZPQYeJFJP7B_d7N9UXGvn1Mfi8ahL/edit)
- [Experiment ROM](https://drive.google.com/file/d/1G6UR3vednL9GybvZ3ZsLQ18_ppIYohYA/view)
- [ZIP SHA-256 file](https://drive.google.com/file/d/1x6EK86VymH-WgjLBLT5iSn8lfkhhHXQm/view)

The ZIP includes exact source diff, full assembler source, native DASM logs/listings/symbols, per-bank hashes, full Stella/Gopher evidence, PCM/image comparisons, stack analysis and dynamic watches, all attempted/failed/rejected experiment records, reproducibility tools, SHA-256 manifest and verified ZIP CRC.

## Frozen product identity

RC1 SHA-256: `456005ed691860b32c44b79f2a71666f622b005f5a798eadf9b549c59cff13bd` (16,384-byte standard F6 NTSC). Candidate bank 0–2 hashes equal RC1; bank 3 changes. See `SHA256SUMS.txt` on this branch.

