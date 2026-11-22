#!/usr/bin/env bash
# Best-effort genuine Stella built-in debugger RAM/RIOT observation, not a custom CPU model.
set -euo pipefail
export SDL_AUDIODRIVER=dummy SDL_VIDEODRIVER=x11
mkdir -p build/ab/debugger
for spec in 'A B' 'B A'; do
  read -r left right <<< "$spec"
  name="LEFT_${left}_RIGHT_${right}"
  dir="${PWD}/build/ab/debugger/${name}"
  mkdir -p "$dir/home/.config/stella"
  cp build/mellanrum_ntsc.bin "$dir/${name}.bin"
  cat > "$dir/${name}.script" <<EOF
print *SWCHB
print *\$B8
frame 5
print *SWCHB
print *\$B8
joy0Fire 1
frame 5
print *SWCHB
print *\$B8
saveSes
EOF
  (
    cd "$dir"
    HOME="$dir/home" stella -debug -dbg.res 1250x800 -holdjoy0 F -video software -fullscreen 0 -ld "$left" -rd "$right" "$dir/${name}.bin" > "$dir/${name}.debug.log" 2>&1 &
    PID=$!
    sleep 16
    kill "$PID" 2>/dev/null || true
    wait "$PID" 2>/dev/null || true
  )
  find "$dir" -type f -printf '%p (%s)\n' > "$dir/files.txt"
  echo "STELLA_DEBUGGER_PROBE $name files=$(wc -l < "$dir/files.txt")"
done
find build/ab/debugger -type f \( -name '*.txt' -o -name '*.log' \) | sort
