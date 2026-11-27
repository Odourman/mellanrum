# REPRODUCE AND LIMITATIONS – independent PACHINKO PR59, 2026-11-27

The authoritative entire raw file evidence is in the Drive ZIP (https://drive.google.com/file/d/1_D4YDhN55FoXc7WFatBFgKEgBIzUfNNI/view), SHA256 `cf321ec3c82f747b3ef9fc21da867416a902602237daaae939a30e734362d6d8`.

Original archive `00_START_HERE.md` lists every tool, script, input sequence and raw log. Own scripts `pachinko_save_starts.py` (SOURCE_GUIDED transport only), `pachinko_room_probe.py`, `pachinko_idle_chunk.py`, `pachinko_multi_fire.py`, `pachinko_recovery_combo.py`, `pachinko_gopher_raster.py`, `pachinko_fri_probe.py`, `pachinko_fri_first.py`.

All 15 true original Stella room-start savestates have source controller prefix RLE and SHA; each actual adversarial case saves its complete frame-indexed controller RLE and read-only state probes. Long tests have serialized 24000-frame continuations with original checksum chains; 9 consecutive chunks per chosen room. Both compared ROMs and actual core binaries are embedded in ZIP. User can verify result files, SHA manifest 720/720 and CRC.

**Critical limits:** single actor sampled positions cannot certify dynamic softlock graph, native 262 line totals cannot prove 76-cycles all-path, sampled SP=`F9` cannot prove global 8-byte max, a numeric PCM difference does not prove a human can hear it, and same-ROM FRI PCM nondeterminism means do not call individual samples a new exclusive bug. No RAM forcing/ROM mutation performed. Only three of fifteen planned one-hour idle tests were actually executed. Prior developer 15/15 full game wins were not counted as new Pachinko passes.

**No product edits.** Separate independent Verification and MAIN/user decision remain required for any release.