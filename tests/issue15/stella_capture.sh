#!/usr/bin/env bash
# Real stock Stella screenshots of NORMAL unmodified candidate ROM, not instrumented cartridge.
set -euo pipefail
mkdir -p build/issue15_stella
export SDL_AUDIODRIVER=dummy
stella -rominfo build/candidate.bin > build/issue15_stella/rominfo.txt 2>&1 || true
stella -video software -fullscreen 0 -tia.zoom 3 -sssingle 0 -ss1x 1 -snapsavedir "${PWD}/build/issue15_stella" build/candidate.bin > build/issue15_stella/stella.log 2>&1 &
PID=$!
trap 'kill "$PID" 2>/dev/null || true' EXIT
WIN=""
for attempt in $(seq 1 35);do
  WIN=$(xdotool search --onlyvisible --pid "$PID" | head -1 || true)
  if [[ -z "$WIN" ]];then WIN=$(xdotool search --onlyvisible --class '[Ss]tella' | head -1 || true);fi
  if [[ -n "$WIN" ]];then break;fi
  sleep 1
done
if [[ -z "$WIN" ]];then echo 'STELLA_WINDOW_NOT_FOUND';cat build/issue15_stella/stella.log;exit 1;fi
xdotool windowfocus --sync "$WIN"
xdotool key --clearmodifiers F5
sleep 0.4
xdotool key --clearmodifiers F12
sleep 1
xdotool keydown --clearmodifiers space
sleep 0.40
xdotool keyup --clearmodifiers space
sleep 2
xdotool key --clearmodifiers F12
sleep 0.8
xdotool key --clearmodifiers F12
sleep 0.8
N=$(find build/issue15_stella -iname '*.png' -type f | wc -l)
echo "STELLA_ISSUE15_GENUINE_SCREENSHOTS=$N"
if (( N < 2 ));then exit 1;fi
