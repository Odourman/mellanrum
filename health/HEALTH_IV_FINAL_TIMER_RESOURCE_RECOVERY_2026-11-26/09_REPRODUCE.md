# Reproduction

## Baseline and tools

Use the pinned sources/tools in the previously validated HEALTH III archive (Drive file `1h-GH9l552CGNv0Rc2577zd4dOcQMUhtb`, SHA-256 `a3fd35f80ab424931dce2d74e273862f82475eb609038b031ff2fe9e563e8fa2`, 41,749,484 B; local CRC PASS). The clean LAB build expects DASM 2.20.14.1 SHA-256 `cfb23732297a4fe1c8d4a78d44206037d97733aedb2772503bbf029a4aa91291`.

For each buildable variant, from `EXPERIMENTS/<ID>/SOURCE/rom/f6`, run:

```sh
PATH=/absolute/path/to/pinned/TOOLS:$PATH python3 build_f6.py --out /absolute/path/to/EXPERIMENTS/<ID>/BUILD/native
```

Expected build ROM hashes:

- LAB clean baseline: `8a59b84eb5151f78d40e6943c854d7e42c166b531aee3d40432182d32dcdf03b`.
- A1: `68f945ade7441ea8c59b4ccdecf216af8a06d399e8b38e0162e7c6f788af0def`.
- A1C: `eb6689f62b1d7e0cc2609eab6c836c78a52ec78a02a9ea1a228fb09311cc1294`.
- A1 sentinel diagnostic only: `97f0377383934ce8dd9867b221c3b9ccccdcc2220b50dc2036ea041bf4c7268f`.

B1, AB and C2 are expected to fail DASM before a ROM is emitted, at `$FF9B`, `$FF97`, `$FF9F` respectively. Build logs are preserved.

## Stella replay

Pinned core: `TOOLS/stella_libretro.so` SHA-256 `2130ed1153cef66ef3f34bf9063f675f1f3342bc18320eb9ae5101743e3042df`. The exact saved frame-indexed replay is copied into `EXPERIMENTS/A1/TEST/controller_frame_events.json`. HEALTH's adapted A1 harness normalizes `exitX` as semantic constant 8 rather than requiring a variable symbol. Run `stella_full_campaign_digest_A1.py` with the same 295 input intervals, `--frames 21000 --audio-frames 21000 --screens`. Tool copy, command output, input, full frame hashes, timeline, PNGs, WAV and result JSON are retained. A1C uses its corresponding harness and input.

A1 sentinel test: `python3 EXPERIMENTS/A1_SENTINEL/TEST/check_sentinel.py --core <stella_libretro.so> --rom <sentinel-ROM> --replay <controller_frame_events.json> --out <output-dir>`.

R2: `python3 R2/pack_roundtrip.py`; expected 45 streams, 11,520 decoded bytes, packed 2,334, hash-exact roundtrip. C2 mapping model: `python3 R2/bitpack_exhaustive_model.py`; this checks 16 flag/action cases only and does not replace an emulator run.
