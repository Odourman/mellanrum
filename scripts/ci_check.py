#!/usr/bin/env python3
"""Mellanrum: bootstrap static project checks. NO Atari emulator testing."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "README.md",
    "AGENTS.md",
    "docs/CURRENT_PROJECT_STATE.md",
    "docs/DECISIONS.md",
    "docs/DESIGN_INTAKE.md",
    "docs/SOURCE_REGISTRY.md",
    "docs/WORKFLOW.md",
    "docs/WORK_ORDER_TEMPLATE.md",
    "docs/VERIFICATION_TEMPLATE.md",
    "rom/README.md",
    ".github/workflows/ci.yml",
)
errors = []
for filename in FILES:
    target = ROOT / filename
    if not target.is_file() or target.stat().st_size == 0:
        errors.append(f"Missing or empty: {filename}")
for filename, must_contain in {
    "README.md": ["Mellanrum", "Verification"],
    "AGENTS.md": ["MAIN", "VERIFICATION", "Källhierarki"],
    "docs/CURRENT_PROJECT_STATE.md": ["NOT_RUN", "G0"],
    "docs/DECISIONS.md": ["MEL-001", "MEL-005"],
    "docs/SOURCE_REGISTRY.md": ["M-REF-001", "M-REF-002"],
}.items():
    p = ROOT / filename
    if p.is_file():
        content = p.read_text(encoding="utf-8")
        for item in must_contain:
            if item not in content:
                errors.append(f"{filename} lacks required marker {item!r}")

if errors:
    for err in errors:
        print("ERROR:", err, file=sys.stderr)
    raise SystemExit(1)
print("CI_STATIC_PASS: project files and handoff markers present.")
print("EMULATOR_NOT_RUN: no Stella/Gopher execution in this check.")
