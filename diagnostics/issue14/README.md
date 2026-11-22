# Issue #14 — disposable integration feasibility ROM (NOT a product patch)

This directory is an isolated diagnostic derivative of the immutable product commit
`49eb168b17d0254d06cf50d87c60e8fb6016db6e`, game-code commit `6cb86247c668162b180e5d77377098941b9803b3`.
The production ROM `e9ea87d381bcf8da39ec055d7d6951ceff97b21d3a798addd10fbbe540c5e974`
MUST NOT be edited. This build produces a *distinct* diagnostic SHA.

## Noncanonical mask warning
The exact GRAPHICS symbol pair "Brytning/Kretsrest" masks were **not accessible** in the project files.
The two 9-byte symbols are **temporary MAIN-verified synthetic probes** from Issue #14,
comment 7087704443: `00 18 24 5A BD 5A 24 18 00` and `00 C3 81 A5 BD A5 81 C3 00`.
They are visually distinct but do not approve or implement final symbolism. Trees are genuine
source-derived V5.1 playfield geometry and Presence bitmasks; P0 owl is source original
`A5 5A 7E FF DB FF 7E 24 00` with full eight nonblank pixel rows.

## Diagnostic hardware allocation

- PF = original eight 20-scanline green tree rows with editable geometry and PF Presence shadow.
- P0 = original owl sprite (full 8-bit bitmap, dynamic owlX/Y).
- P1 = two different synthetic glyph bitmaps, one hardware channel, NUSIZ1=$04,
  sprite origins at stoneX=4 => approximately x71 and x135 (+64 copy);
  original exitX=8 visual origin x139 (about 4 TIA color clocks/pixels shift).
- M0 = logical player cursor, hardware position from source cursorX/Y; four status widths
  1,2,4,8 via NUSIZ0 bits 4–5. This **visually reduces** the 8x8 cursor artwork;
  acceptance of that compromise and gameplay states needs human/independent review.
- BL free; M1 disabled to avoid duplicate ghost objects.

All V5.1 `stone=[4,y]`, `exit=[8,y]`, scene geometry and gameplay logic are unchanged.

## Explicit isolation

The copied diagnostic `rom/src/main.asm`, `rom/src/data.inc` ONLY are changed.
The original product source and ROM in GitHub draft PR #4 are untouched.
The diagnostic contains a *diagnostic-only extra overscan WSYNC* to get 262 lines.
This is NOT a fix for separate production raster issue #12 (observed 261).

## Reproduce

```bash
cd diagnostics/issue14
mkdir -p build
dasm rom/src/main.asm -f3 -obuild/diag.bin -lbuild/diag.lst -sbuild/diag.sym
python3 scripts/assemble_check.py rom/src/main.asm -o build/subset.bin
cmp build/diag.bin build/subset.bin
python3 scripts/cycle_budget.py
# Pinned Gopher2600 from GH Actions, original upstream 74c544203378c1448a33c29bc8b4586079b050f4
python3 scripts/probe_15.py
python3 scripts/pixel_audit.py
# stock Stella 6.7+ under an Xvfb virtual display
xvfb-run --auto-servernum --server-args='-screen 0 1024x768x24' bash scripts/stella_diag.sh
```

The 15 room screenshots and user feedback/overlap probes use **test-only POKE** for room
and RAM state selection; these are NOT ordinary gameplay completions. A separate
ordinary title+FIRE real joystick smoke is captured and uses no POKE, but gameplay
rules and reachability are not independently verified by these integration tests.

## Known limitations
- Two symbols are synthetic, not canonical final GRAPHICS masks.
- The real-game cursor's 8x8 animated frame is reduced to hardware missile width,
  with four distinguishable statuses, subject to artistic acceptance and input testing.
- Two distinct glyphs must remain exactly 64 TIA pixels apart; exit glyph is shifted 4px
  relative to old exit anchor. Logical positions unchanged.
- Dedicated 262-line diagnostic VSYNC/overscan is not equivalent to production 261 raster fix.
- Stella screen and TIA output may differ; any failure must be reported as such.
- A single kernel/POC cannot certify the whole game; independent Verification separate.
