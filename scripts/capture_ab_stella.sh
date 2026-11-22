#!/usr/bin/env bash
# Native Atari 2600 Stella 6.7+ with real SWCHB controls. Screenshots are original emulator PNGs.
# This is coarse-time live-control observation, NOT cycle-exact emulator RAM tracing.
set -euo pipefail
export SDL_AUDIODRIVER=dummy SDL_VIDEODRIVER=x11
mkdir -p build/ab/record build/ab/snapshots
: > build/ab/input_events.tsv
echo -e 'case\tevent\tkeys\tseconds_after_start' >> build/ab/input_events.tsv
run_case() {
  local id="$1" left="$2" right="$3" alt
  [[ "$left" == A ]] && alt=B || alt=A
  local shotdir="${PWD}/build/ab/snapshots/$id";mkdir -p "$shotdir"
  local start=$(date +%s)
  stella -video software -fullscreen 0 -tia.zoom 3 -sssingle 0 -ss1x 1 \
    -ld "$left" -rd "$right" -snapsavedir "$shotdir" \
    "${PWD}/build/mellanrum_ntsc.bin" > "build/ab/${id}.stella.log" 2>&1 &
  local pid=$! win=''
  for j in $(seq 1 30); do
    win=$(xdotool search --onlyvisible --pid "$pid" | head -1 || true)
    [[ -n "$win" ]] || win=$(xdotool search --onlyvisible --name '[Ss]tella' | head -1 || true)
    if [[ -n "$win" ]]; then break;fi
    kill -0 "$pid" 2>/dev/null || break
    sleep 0.5
  done
  if [[ -z "$win" ]]; then cat "build/ab/${id}.stella.log";echo "STELLA_START_FAIL $id";kill "$pid" 2>/dev/null || true;return 1;fi
  xdotool windowfocus --sync "$win"
  event() { local tag="$1";shift;xdotool key --clearmodifiers "$@";echo -e "$id\t$tag\t$*\t$(( $(date +%s)-start ))" >> build/ab/input_events.tsv;sleep .25; }
  capture() {
    local tag="$1" f
    event "SNAP:$tag" F12
    f=$(find "$shotdir" -type f -name '*.png' -printf '%T@ %p\n' | sort -nr | head -1 | cut -d' ' -f2-)
    if [[ -z "$f" ]];then echo "NO_CAPTURE $id $tag";return 1;fi
    cp "$f" "build/ab/record/${id}_${tag}.png"
  }
  # F5/F6 and F7/F8 are the actual Stella console difficulty hotkeys.
  if [[ "$left" == A ]]; then event "LEFT_A" F5;else event "LEFT_B" F6;fi
  if [[ "$right" == A ]]; then event "RIGHT_A" F7;else event "RIGHT_B" F8;fi
  sleep 1;capture title
  event SELECT_TITLE F1
  event TITLE_UP Up;event TITLE_DOWN Down;event TITLE_LEFT Left;event TITLE_RIGHT Right
  capture title_after_select_joystick
  event FIRE_DOWN_NOT_SELECT space
  sleep 2;capture running_initial
  if [[ "$alt" == A ]]; then event LEFT_CHANGED_MIDGAME F5;else event LEFT_CHANGED_MIDGAME F6;fi
  if [[ "$right" == A ]]; then event RIGHT_CHANGED_MIDGAME F8;else event RIGHT_CHANGED_MIDGAME F7;fi
  capture running_after_difficulty_change
  event RESET F2
  sleep 0.8;capture title_after_reset
  event FIRE_AFTER_RESET space
  sleep 2;capture running_after_reset
  kill "$pid" 2>/dev/null || true
  wait "$pid" 2>/dev/null || true
  echo "STELLA_AB_CASE_PASS $id LEFT=$left RIGHT=$right"
}
run_case LEFT_A A A
run_case LEFT_B B B
( cd build/ab && sha256sum record/*.png > SHA256SUMS )
python3 scripts/check_ab_stella.py
