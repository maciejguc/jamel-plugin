"""Regenerate the golden .xlsx fixtures from the golden inputs.

Run after intended render changes, review the output manually (against
offers/estimates/sprint-est.xlsx and ina-management-est.xlsx), then commit.

    ../.venv/bin/python regenerate_golden.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import json

from generate_wycena_xlsx import generate_from_payload

GOLDEN_DIR = Path(__file__).resolve().parent / "golden"

for name in ("range", "fixed"):
    payload = json.loads((GOLDEN_DIR / f"{name}-input.json").read_text(encoding="utf-8"))
    out = GOLDEN_DIR / f"{name}-golden.xlsx"
    out.write_bytes(generate_from_payload(payload))
    print(f"Wrote {out}")
