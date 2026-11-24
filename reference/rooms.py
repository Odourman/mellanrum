"""Issue #21: 15 explicitly authored, unique and source-model-tested rooms.
This file loads the committed room ledger, not the 5 repeated historical layouts.
Reference model does not prove joystick travel, TIA timing or real emulator completion.
"""
import json
from pathlib import Path
from engine import Room

DOCUMENT = json.loads((Path(__file__).parent / "rooms.json").read_text())
assert len(DOCUMENT) == 15
ROOMS = []
for data in DOCUMENT:
    room = Room(
        data["id"], data["act"], data["title"],
        tuple(data["half_rows"]), tuple(data["owl_start"]),
        tuple(data["stone"]), tuple(data["exit"]),
        data["stone_initial"], data["note"], data["note"],
        data.get("exit_gate",0), data.get("exit_extra",0),
    )
    room.validate()
    ROOMS.append(room)
assert len(set(tuple(r.half) for r in ROOMS)) == 15
