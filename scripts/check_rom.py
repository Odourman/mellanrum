#!/usr/bin/env python3
"""Basic ROM artifact sanity, not emulator or gameplay verification."""
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("usage: python3 scripts/check_rom.py build/mellanrum_ntsc.bin")
rom = Path(sys.argv[1])
data = rom.read_bytes()
valid_sizes = {2048, 4096, 8192, 16384, 32768}
if len(data) not in valid_sizes:
    raise SystemExit(f"BUILD_FAIL: Unexpected ROM size {len(data)} bytes. Update policy for the approved mapper.")
if not any(data):
    raise SystemExit("BUILD_FAIL: ROM is all zero bytes.")
print(f"BUILD_ARTIFACT_CHECK_PASS: {rom} = {len(data)} bytes")
print("EMULATOR_NOT_RUN: image timing, audio, gameplay and cartridge mapper still unverified.")
