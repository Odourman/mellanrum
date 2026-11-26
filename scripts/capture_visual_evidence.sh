#!/usr/bin/env bash
# Actual Stella / real 6507+TIA software emulator, Xvfb. Capture multiple frames
# per room so intermittent 24-on/40-off rendering is demonstrably observable.
set -euo pipefail
mkdir -p build/visual/shots build/visual/variants
export SDL_AUDIODRIVER=dummy
export SDL_VIDEODRIVER=x11
export DISPLAY="${DISPLAY:-:99}"

capture_one() {
  local file="$1" label="$2" with_select="${3:-0}"
  echo "RUN_REAL_STELLA $label $file"
  stella -video software -fullscreen 0 -tia.zoom 3 -sssingle 0 -ss1x 1 \
      -snapsavedir "${PWD}/build/visual/shots" "$file" \
      > "build/visual/${label}.stella.log" 2>&1 &
  local pid=$! win=''
  for k in $(seq 1 20); do
      win=$(xdotool search --onlyvisible --pid "$pid" | head -1 || true)
      if [[ -z "$win" ]]; then win=$(xdotool search --onlyvisible --name 'Stella' | head -1 || true); fi
      if [[ -n "$win" ]]; then break; fi
      if ! kill -0 "$pid" 2>/dev/null; then break; fi
      sleep 0.5
  done
  if [[ -z "$win" ]]; then
    echo "EMULATOR_WINDOW_FAIL $label"
    cat "build/visual/${label}.stella.log"
    kill "$pid" 2>/dev/null || true
    return 1
  fi
  xdotool windowfocus --sync "$win"
  # 0.2s intervals span a complete 64-frame visual gate at 60 Hz.
  for k in $(seq 1 12); do
    xdotool key --clearmodifiers F12
    sleep 0.18
  done
  if [[ "$with_select" == 1 ]]; then
    xdotool key --clearmodifiers F1 # Stella console SELECT; real UI, not simulated
    sleep 0.4
    xdotool key --clearmodifiers F12
  fi
  kill "$pid" 2>/dev/null || true
  wait "$pid" 2>/dev/null || true
  local count
  count=$(find build/visual/shots -maxdepth 1 -type f -iname "$(basename "${file%.bin}")*.png" | wc -l)
  echo "EMULATOR_CAPTURE_COUNT $label $count"
  if (( count < 3 )); then cat "build/visual/${label}.stella.log";return 1;fi
}

capture_one build/mellanrum_ntsc.bin TITLE 1
for spec in '12 0 III03_before' '12 1 III03_warning' '12 2 III03_active' '12 4 III03_after' \
            '13 0 III04_warning' '13 1 III04_active' '13 3 III04_after' \
            '14 1 III05_before' '14 2 III05_warning' '14 3 III05_active' '14 5 III05_after'; do
  read -r room tick label <<< "$spec"
  python3 scripts/make_visual_evidence_rom.py --room "$room" --beat "$tick" --output "build/visual/variants/${label}.asm"
  dasm "build/visual/variants/${label}.asm" -f3 -o"build/visual/variants/${label}.bin" -l"build/visual/variants/${label}.lst"
  test "$(wc -c < "build/visual/variants/${label}.bin")" -eq 4096
  capture_one "build/visual/variants/${label}.bin" "$label"
done
( cd build/visual && find shots variants -type f \( -name '*.png' -o -name '*.bin' \) -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS )
python3 scripts/check_visual_captures.py
