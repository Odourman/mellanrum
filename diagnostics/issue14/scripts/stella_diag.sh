#!/usr/bin/env bash
# Actual stock Stella 6.7+ GUI emulator; genuine uninstrumented diagnostic ROM
set -euo pipefail
mkdir -p build/stella
export SDL_AUDIODRIVER=dummy
stella -rominfo build/diag.bin > build/stella/rominfo.txt 2>&1 || true
stella -video software -fullscreen 0 -tia.zoom 3 -sssingle 0 -ss1x 1 -snapsavedir "${PWD}/build/stella" build/diag.bin > build/stella/stella.log 2>&1 &
PID=$!
trap 'kill "$PID" 2>/dev/null || true' EXIT
WIN=""
for attempt in $(seq 1 30);do
 WIN=$(xdotool search --onlyvisible --pid "$PID" | head -1 || true)
 if [[ -z "$WIN" ]];then WIN=$(xdotool search --onlyvisible --class '[Ss]tella' | head -1 || true);fi
 if [[ -n "$WIN" ]];then break;fi
 sleep 1
done
if [[ -z "$WIN" ]];then echo STELLA_WINDOW_NOT_FOUND;cat build/stella/stella.log;exit 1;fi
xdotool windowfocus --sync "$WIN"
# LEFT Difficulty A to enter campaign, not FRI SKOG where exit glyph is deliberately hidden.
xdotool key --clearmodifiers F5
sleep 0.4
xdotool key --clearmodifiers F12
sleep 1
# Hold FIRE for multiple 60Hz frames; there is no memory injection in Stella screenshots.
xdotool keydown --clearmodifiers space
sleep 0.40
xdotool keyup --clearmodifiers space
sleep 2
xdotool key --clearmodifiers F12
sleep 1
xdotool key --clearmodifiers F12
sleep 1
N=$(find build/stella -type f -iname '*.png'|wc -l)
echo "STELLA_REAL_SCREENSHOTS=$N"
if (( N<2 ));then cat build/stella/stella.log;exit 1;fi
