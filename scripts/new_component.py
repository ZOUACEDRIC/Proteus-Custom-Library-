#!/usr/bin/env python3
"""Create a new component folder from templates/component.

Usage:
    python scripts/new_component.py ESP32C3 "ESP32-C3 module, 22 pins"

The new folder is created under components/<NAME>/ with the template files
copied in and __NAME__ replaced. Nothing is overwritten: an existing folder
stops the script.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = REPO_ROOT / "templates" / "component"
COMPONENTS_DIR = REPO_ROOT / "components"


def main(argv: list[str]) -> int:
    if not argv:
        print('usage: python scripts/new_component.py NAME "short description"')
        return 2

    name = argv[0].strip()
    description = argv[1].strip() if len(argv) > 1 else ""

    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", name):
        print(f"invalid component name {name!r}: use letters, digits, - and _")
        return 2

    target = COMPONENTS_DIR / name.upper()
    if target.exists():
        print(f"{target.relative_to(REPO_ROOT)} already exists - nothing changed")
        return 1

    if not TEMPLATE_DIR.is_dir():
        print(f"template folder missing: {TEMPLATE_DIR}")
        return 1

    target.mkdir(parents=True)
    for source in sorted(TEMPLATE_DIR.iterdir()):
        if not source.is_file():
            continue
        text = source.read_text(encoding="utf-8")
        text = text.replace("__NAME__", name.upper())
        if description:
            text = text.replace("__FILL_IN__", description, 1)
        (target / source.name).write_text(text, encoding="utf-8")
        print(f"created {target.joinpath(source.name).relative_to(REPO_ROOT)}")

    print()
    print("next steps:")
    print(f"  1. replace the sample rows in {target.name}/pinout.csv")
    print(f"  2. keep {target.name}/PROTEUS8_PIN_MAP.csv in sync with it")
    print(f"  3. python scripts/validate_component.py {target.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
