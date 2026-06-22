#!/usr/bin/env python3
"""Validiert ein einfaches JSON-Intake fuer Geburtshoroskop-Deutungen.

Dieses Skript berechnet kein Horoskop. Es prueft nur, ob die fuer eine Deutung
wichtigen Eingaben plausibel vorhanden sind.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TIME_RE = re.compile(r"^\d{2}:\d{2}$")
REQUIRED = ["birth_date", "birth_time", "birth_place"]


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SystemExit(f"fehler: JSON konnte nicht gelesen werden: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit("fehler: Intake muss ein JSON-Objekt sein")
    return data


def validate(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in REQUIRED:
        if not str(data.get(key, "")).strip():
            errors.append(f"fehlendes Feld: {key}")

    birth_date = str(data.get("birth_date", ""))
    birth_time = str(data.get("birth_time", ""))
    if birth_date and not DATE_RE.match(birth_date):
        errors.append("birth_date muss YYYY-MM-DD verwenden")
    if birth_time and not TIME_RE.match(birth_time):
        errors.append("birth_time muss HH:MM verwenden")

    if "focus" in data and not isinstance(data["focus"], (str, list)):
        errors.append("focus muss String oder Liste sein")
    if "chart_positions_provided" in data and not isinstance(data["chart_positions_provided"], bool):
        errors.append("chart_positions_provided muss boolesch sein")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Geburtshoroskop-Intake JSON validieren")
    parser.add_argument("json_path", type=Path)
    args = parser.parse_args()
    data = load_json(args.json_path)
    errors = validate(data)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("Intake gueltig. Hinweis: Dieses Skript berechnet kein Horoskop.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
