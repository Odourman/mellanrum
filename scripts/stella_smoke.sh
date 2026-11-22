#!/usr/bin/env bash
# Actual Stella 6.7+ emulator smoke with virtual X display. NOT full 15-room verification.
set -euo pipefail
mkdir -p build/stella
export SDL_AUDIODRIVER=dummy
export DISPLAY="${DISPLAY:-:99}"
# Save precise emulator/ROM metadata first.
stella -rominfo build/mellanrum_ntsc.bin > build/stella/rominfo.txt 2>&1 || true
stella -video software -fullscreen 0 -tia.zoom 3 -sssingle 0 -ss1x 1 -snapsavedir "${PWD}/build/stella" build/mellanrum_ntsc.bin > build/stella/stella.log 2>&1 &
PID=$!
trap 'kill "$PID" 2>/dev/null || true' EXIT
sleep 4
WIN=$(xdotool search --onlyvisible --name 'Stella' | head -1 || true)
if [[ -z "$WIN" ]]; then
  echo 'STELLA_SMOKE_FAIL: no visible emulator window'; cat build/stella/stella.log; exit 1
fi
xdotool windowfocus --sync "$WIN"
xdotool key --clearmodifiers F12
sleep 1
xdotool key --clearmodifiers space
sleep 4
xdotool key --clearmodifiers F12
sleep 1
ls -lh build/stella
PNGS=$(find build/stella -type f -name '*.png' | wc -l)
if (( PNGS < 1 )); then
  echo 'STELLA_SMOKE_FAIL: no real Stella screenshot captured'
  cat build/stella/stella.log
  exit 1
fi
echo "STELLA_BOOT_SNAPSHOT_CAPTURED: $PNGS original emulator captures. Human/manual visual and gameplay review still required."
