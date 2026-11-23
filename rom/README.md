# MELLANRUM – current new Issue #21 developer cartridge (Draft PR #22)

The older default-branch placeholder stating "no gameplay ROM exists" is outdated **for this dedicated development branch**. Issue #21 explicitly authorized new development without mutating frozen PR #4 or PR #16.

## Native NTSC ROM and source

- **New playable 4KiB unbanked NTSC cartridge:** `mellanrum_vnext.bin`.
- **Exact SHA-256:** `18163c0435347695ee1cff5a4b6b19c80d280ec255eeb7f9b98711471ccde11c`.
- **Authoritative source in this PR:** [main ASM](../rom/src/main.asm), [data.inc](../rom/src/data.inc), [authored rooms](../reference/rooms.json), [reference model](../reference/engine.py).
- **Reproducible native DASM command from repo root:**
  ```bash
  mkdir -p build/issue21
  dasm rom/src/main.asm -f3 -obuild/issue21/mellanrum_vnext.bin -lbuild/issue21/mellanrum_vnext.lst -sbuild/issue21/mellanrum_vnext.sym
  sha256sum build/issue21/mellanrum_vnext.bin
  ```
- Native build, ROM, .lst and .sym downloadable as [GitHub Actions developer artifact](https://github.com/Odourman/mellanrum/actions/runs/45146265215). The artifact is a native DASM build, not a fake/approximated emulator output.

**Warning:** `rom/bin/mellanrum_ntsc.bin` inherited on this branch belongs to the earlier frozen PR16 source; it is NOT the new Issue21 cartridge. Do not overwrite it, re-label it, or run the old `build_issue15.py` against vNext sources; the former would regenerate the wrong game from pinned earlier sources. To play the new game, build the new binary from the ASM above or download the exact new SHA cartridge delivered to MAIN.

The game is 4096 bytes and therefore fits normal unmodified Atari 2600 hardware; **F6 bank switching is not needed and not used**. No extra cart RAM, DPC, ARM, Superchip or helper chipset. Actual physical Atari validation remains NOT_RUN.

## Quality gates
Read [full Issue21 developer handoff](../docs/ISSUE21_DEVELOPER_HANDOFF.md), [rules/design delta](../docs/GAMEPLAY_CANON_DELTA.md), and [30 techniques](../docs/TECHNIQUE_30_AUDIT.md). PR #22 remains Draft. Independent Verification, Pachinko and MAIN user acceptance pending. **Do not merge or release.**
