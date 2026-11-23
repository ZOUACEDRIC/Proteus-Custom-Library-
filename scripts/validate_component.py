# OFP:C38A5F20D1E7496B82C4A03F5E9167D2
#!/usr/bin/env python3
"""Consistency checker for custom Proteus component folders.

Every component folder under ``components/`` must carry the same set of
sources and they must agree with each other. This script fails loudly
instead of letting a pin table drift away from the CSV that Proteus
builders actually copy from.

Usage:
    python scripts/validate_component.py            # check every component
    python scripts/validate_component.py FM255      # check one component
    python scripts/validate_component.py --strict   # warnings become errors

Exit code 0 = all checks passed, 1 = at least one error.
"""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
COMPONENTS_DIR = REPO_ROOT / "components"

# Files every component folder is expected to provide.
REQUIRED_FILES = (
    "pinout.csv",
    "PROTEUS8_PIN_MAP.csv",
    "COMPONENT_SPEC.md",
)

# Electrical type spellings that are the same thing under different names.
TYPE_ALIASES = {
    "PASSIVE": "PS",
    "PS": "PS",
    "INPUT": "IP",
    "IP": "IP",
    "OUTPUT": "OP",
    "OP": "OP",
    "BIDIRECTIONAL": "IO",
    "IO": "IO",
    "BIDI": "IO",
    "TRISTATE": "TS",
    "TS": "TS",
    "PULLUP": "PU",
    "PU": "PU",
    "PULLDOWN": "PD",
    "PD": "PD",
    "POWER": "PP",
    "POWERPIN": "PP",
    "PP": "PP",
    "NC": "NC",
    "NOTCONNECTED": "NC",
    "NCNOTCONNECTED": "NC",
}


def normalise_type(value: str) -> str:
    """Map any accepted spelling of a pin type onto one canonical code."""
    key = re.sub(r"[^A-Z]", "", value.upper())
    return TYPE_ALIASES.get(key, value.strip().upper())


def normalise_connector(value: str) -> str:
    """Reduce a connector label to a comparable key.

    ``pinout.csv`` names the connectors ``UART`` and ``USB`` while the
    Proteus map names them ``J1_UART`` and ``J2_USB``; both must collapse
    onto the same key.
    """
    key = re.sub(r"^J\s*\d+\s*_?", "", value.upper().strip())
    return re.sub(r"[^A-Z]", "", key)


@dataclass
class Pin:
    connector: str
    connector_pin: str
    signal: str
    ptype: str
    device_pin: str = ""


@dataclass
class Report:
    component: str
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return [
            {k.strip(): (v or "").strip() for k, v in row.items() if k}
            for row in csv.DictReader(handle)
            if any((v or "").strip() for v in row.values())
        ]


def load_pinout(path: Path, report: Report) -> list[Pin]:
    rows = read_csv(path)
    pins: list[Pin] = []
    for row in rows:
        signal = row.get("signal", "")
        if not signal:
            report.error(f"pinout.csv: row without a signal: {row}")
            continue
        pins.append(
            Pin(
                connector=row.get("connector", ""),
                connector_pin=row.get("pin", ""),
                signal=signal,
                ptype=row.get("proteus_electrical_type", ""),
            )
        )
    return pins


def load_device_map(path: Path, report: Report) -> list[Pin]:
    rows = read_csv(path)
    pins: list[Pin] = []
    for row in rows:
        device_pin = row.get("DevicePin", "")
        if not device_pin:
            report.error(f"PROTEUS8_PIN_MAP.csv: row without DevicePin: {row}")
            continue
        pins.append(
            Pin(
                connector=row.get("Connector", ""),
                connector_pin=row.get("ConnectorPin", ""),
                signal=row.get("Signal", ""),
                ptype=row.get("ProteusElectricalType", ""),
                device_pin=device_pin,
            )
        )
    return pins


def load_markdown_pin_tables(folder: Path) -> dict[str, list[dict[str, str]]]:
    """Collect every 'pin number | pin name | electrical type' table in *.md.

    Markdown tables are recognised loosely: a header row mentioning a pin
    number and a type, then rows starting with a number. This keeps the
    checker usable for the free-form docs already in the repo.
    """
    tables: dict[str, list[dict[str, str]]] = {}
    for md in sorted(folder.glob("*.md")):
        lines = md.read_text(encoding="utf-8").splitlines()
        index = 0
        while index < len(lines):
            header = lines[index]
            if header.lstrip().startswith("|") and "type" in header.lower():
                cols = [c.strip().lower() for c in header.strip().strip("|").split("|")]
                if not any("pin" in c for c in cols):
                    index += 1
                    continue
                rows: list[dict[str, str]] = []
                probe = index + 1
                while probe < len(lines) and lines[probe].lstrip().startswith("|"):
                    cells = [c.strip() for c in lines[probe].strip().strip("|").split("|")]
                    if set("".join(cells)) <= set("-: "):
                        probe += 1
                        continue
                    if len(cells) == len(cols):
                        rows.append(dict(zip(cols, cells)))
                    probe += 1
                if rows:
                    tables[f"{md.name}:{index + 1}"] = rows
                    index = probe
                    continue
            index += 1
    return tables


def check_component(folder: Path) -> Report:
    report = Report(component=folder.name)

    missing = [name for name in REQUIRED_FILES if not (folder / name).is_file()]
    for name in missing:
        report.error(f"missing required file: {name}")
    if missing:
        return report

    pinout = load_pinout(folder / "pinout.csv", report)
    device_map = load_device_map(folder / "PROTEUS8_PIN_MAP.csv", report)
    if report.errors:
        return report

    # --- device pin numbers -------------------------------------------------
    numbers: list[str] = [p.device_pin for p in device_map]
    if len(set(numbers)) != len(numbers):
        duplicates = {n for n in numbers if numbers.count(n) > 1}
        report.error(f"duplicate device pin numbers: {sorted(duplicates)}")

    try:
        numeric = sorted(int(n) for n in numbers)
    except ValueError as exc:
        report.error(f"device pin numbers must be integers: {exc}")
        numeric = []
    if numeric and numeric != list(range(1, len(numeric) + 1)):
        report.error(
            "device pin numbers must run 1..N without gaps "
            f"(found {numeric[0]}..{numeric[-1]} for {len(numeric)} pins)"
        )

    # --- connector pins -----------------------------------------------------
    connector_keys = [(p.connector, p.connector_pin) for p in device_map]
    if len(set(connector_keys)) != len(connector_keys):
        report.error("PROTEUS8_PIN_MAP.csv repeats a connector pin")

    # --- the two CSV files must describe the same part ----------------------
    if len(pinout) != len(device_map):
        report.error(
            f"pinout.csv lists {len(pinout)} pins but "
            f"PROTEUS8_PIN_MAP.csv lists {len(device_map)}"
        )

    pinout_index = {
        (normalise_connector(p.connector), p.connector_pin): p for p in pinout
    }
    for pin in device_map:
        key = (normalise_connector(pin.connector), pin.connector_pin)
        reference = pinout_index.get(key)
        if reference is None:
            report.error(
                f"{pin.connector} pin {pin.connector_pin} is in the device map "
                "but has no matching row in pinout.csv"
            )
            continue
        if reference.signal != pin.signal:
            report.error(
                f"{pin.connector} pin {pin.connector_pin}: signal {reference.signal!r} "
                f"in pinout.csv vs {pin.signal!r} in the device map"
            )
        if normalise_type(reference.ptype) != normalise_type(pin.ptype):
            report.error(
                f"{pin.connector} pin {pin.connector_pin} ({pin.signal}): electrical "
                f"type differs ({reference.ptype} vs {pin.ptype})"
            )

    # --- markdown tables must not contradict the CSV -----------------------
    types_by_name: dict[str, set[str]] = {}
    for pin in device_map:
        types_by_name.setdefault(pin.signal.upper(), set()).add(normalise_type(pin.ptype))
    for where, rows in load_markdown_pin_tables(folder).items():
        for row in rows:
            name = (row.get("pin name") or row.get("name") or "").strip().upper()
            declared = normalise_type(
                row.get("electrical type") or row.get("proteus type") or ""
            )
            if not name or not declared or name not in types_by_name:
                continue
            if declared not in types_by_name[name]:
                expected = "/".join(sorted(types_by_name[name]))
                report.error(
                    f"{where}: {name} is listed as {declared} but the CSV says {expected}"
                )

    # --- documents may only reference files that exist ---------------------
    for md in sorted(folder.glob("*.md")):
        for token in re.findall(r"`([A-Za-z0-9_.-]+\.(?:csv|md|svg|lib|LIB|idx|IDX|hex|HEX))`", md.read_text(encoding="utf-8")):
            if not (folder / token).is_file() and not (REPO_ROOT / token).is_file():
                report.error(f"{md.name}: references missing file {token}")

    # --- release hygiene ----------------------------------------------------
    lib_files = [p for p in folder.glob("*.LIB")] + [p for p in folder.glob("*.LIB".lower())]
    if not lib_files:
        report.warn(
            "no compiled Proteus library (*.LIB) in this folder - the device still "
            "has to be built with ISIS Make Device before it counts as release-ready"
        )

    return report


def iter_components(selection: Iterable[str]) -> list[Path]:
    if not COMPONENTS_DIR.is_dir():
        return []
    folders = sorted(p for p in COMPONENTS_DIR.iterdir() if p.is_dir())
    wanted = [s.lower() for s in selection]
    if wanted:
        folders = [p for p in folders if p.name.lower() in wanted]
    return folders


def main(argv: list[str]) -> int:
    strict = "--strict" in argv
    selection = [a for a in argv if not a.startswith("-")]

    folders = iter_components(selection)
    if not folders:
        print("no component folders found under components/")
        return 1

    failures = 0
    for folder in folders:
        report = check_component(folder)
        status = "FAIL" if report.errors or (strict and report.warnings) else "PASS"
        failures += 1 if status == "FAIL" else 0
        print(f"[{status}] {folder.name}")
        for message in report.errors:
            print(f"   error: {message}")
        for message in report.warnings:
            print(f"   warn:  {message}")

    print()
    print(f"{len(folders) - failures}/{len(folders)} component folder(s) valid")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
