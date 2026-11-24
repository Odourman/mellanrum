# Issue26 – real TIA two-channel 16KiB soundtrack

**No PCM samples embedded, no modern sound processor.** Three F6 banks each contain five room-specific scored sequences of 256 video frames × 3 bytes/frame; each frame's 6507 interpreter reads all three bytes. This is a byte-efficient authored generative score, not empty padding.

| Score byte | Bits | Actual hardware effect |
|---|---|---|
| Stream 0 | low 5 bits | AUDF0 pitch (0..31), sustained low-pitch channel |
| Stream 0 | upper 3 bits | AUDV0 volume, including short deliberate silence |
| Stream 1 | upper 4 bits | AUDC0 tone/timbre control (mainly tonal 12, Act III sometimes 4) |
| Stream 1 | lower 4 bits | AUDC1 second timbre (tonal 4/12/6, occasional Act III 8/noise) |
| Stream 2 | low 5 bits | AUDF1 countervoice pitch (0..31) |
| Stream 2 | upper 3 bits | AUDV1 volume (including absence) and linked COLUBK background breath |

Each room's seed, mutable tree density by raster row, stone starting polarity, 64-frame phrase, two interlocking pulse counters and act phase contribute to its 768-byte loop. These are deterministic and source-reproducible; no POKE, no RAM buffers, no extra cart hardware. `soundStep` advances at 60 FPS and loops at 256; 15 room-specific pages are genuinely reachable throughout a 15-room campaign. Audio output is the true unaltered Stella TIA mixer callback (stereo WAV 31440 Hz).

The interpreter emits texture interruptions for `presence` warning and active states, suppressing second voice in quiet gaps and injecting short grainy pulses at intentional frames. Existing normal-vs-waiting audio is muted at room done/coda. The soundtrack is deliberately dark and low at start; human audition is an independent qualitative gate. A separate diagnostic alternate TIA source must be distinctly labelled as non-product and its own SHA if produced.

Audio proof: recompute SHA from original native DASM F6 .bin, run exact Stella/libretro core and record actual WAV and scene screenshots; compare act-specific clips with the previous PR23 baseline. Audio signal/PCM nonzero does NOT mean artistic audition passed.
