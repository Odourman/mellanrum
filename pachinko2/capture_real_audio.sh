#!/usr/bin/env bash
# Gopher2600 -wav is native TIA audio output. GUl-only refresh-rate safety
# guard is applied at Gopher build step for headless Xvfb; emulator core untouched.
set -Eeuo pipefail
ROOT="$(pwd)"
ROM="$ROOT/rom/bin/mellanrum_ntsc.bin"
EXE="$ROOT/build/pachinko/audio_build/gopher2600_wav_gui"
OUT="$ROOT/build/pachinko/real-audio"
mkdir -p "$OUT"
cd "$OUT"
export SDL_AUDIODRIVER=dummy
export LIBGL_ALWAYS_SOFTWARE=1
export SDL_VIDEODRIVER=x11
for MODE in CAMPAIGN FREE; do
  mkdir -p "$MODE"
  cd "$MODE"
  "$EXE" PLAY -wav "$ROM" > player.log 2>&1 &
  PID=$!
  sleep 3
  WIN=""
  for i in {1..12}; do
    WIN=$(xdotool search --onlyvisible --name '[Gg]opher2600' | head -1 || true)
    [[ -n "$WIN" ]] && break
    if ! kill -0 "$PID" 2>/dev/null; then break; fi
    sleep 1
  done
  if [[ -z "$WIN" ]]; then
    echo "AUDIO_OBSERVE_BLOCKED: no SDL window, $MODE" | tee -a player.log
    kill "$PID" 2>/dev/null || true
    wait "$PID" || true
    cd ..
    continue
  fi
  xdotool windowactivate --sync "$WIN" || true
  if [[ "$MODE" == "CAMPAIGN" ]]; then
    # physical left A in Gopher front-panel mapping via debugger not GUI.
    # default A under Gopher preferences; audit via logs if present.
    xdotool keydown --clearmodifiers space
    sleep 0.4
    xdotool keyup --clearmodifiers space
    sleep 14
  else
    # LEFT B on Gopher GUI might not be reliably mapped in remote Xvfb.
    # do not assume this output is FRI unless gameplay state is proven.
    xdotool keydown --clearmodifiers space
    sleep 0.4
    xdotool keyup --clearmodifiers space
    sleep 9
  fi
  kill -INT "$PID" 2>/dev/null || true
  sleep 2
  if kill -0 "$PID" 2>/dev/null; then kill -TERM "$PID" || true; fi
  wait "$PID" || true
  echo "AUD_FILES_MODE=$MODE"
  find . -maxdepth 1 -name '*.wav' -ls || true
  cd ..
done
