# Proteus Custom Library

Reusable Proteus component definitions and documentation.

## Components

| Component | Type | Device pins | Schematic symbol | Native `.LIB` |
|---|---|---|---|---|
| [FM255](components/FM255/) | UART + USB module | 9 | documented, build guide ready | not built yet |

"Native `.LIB`" means a device compiled by Proteus itself with **Library → Make Device**.
Until that file exists, a component is documentation and drawing, not a device you can
pick from the Proteus library selector.

## Repository layout

```
components/<NAME>/     one folder per part: pinout.csv, PROTEUS8_PIN_MAP.csv, spec, guides
templates/component/   skeleton copied by scripts/new_component.py
scripts/               validator and scaffolding tools
```

## Adding or changing a component

```bash
# new part from the template
python scripts/new_component.py ESP32C3 "ESP32-C3 module, 22 pins"

# check every component folder
python scripts/validate_component.py

# check one
python scripts/validate_component.py FM255
```

The validator is the source of truth for consistency: it rejects duplicate or gapped
device pin numbers, pinout rows that do not match the Proteus map, electrical types that
disagree between the CSV files and the Markdown tables, and documents that reference
files which do not exist. CI runs it on every push.

## First component: FM255 module

This first contribution records the FM255 connector pinout supplied by the project owner and defines the requirements for its reusable Proteus symbol.

### Confirmed connector pinout

**UART connector — 1.25 mm pitch, 4 pins**

| Pin | Signal | Direction at FM255 | Suggested Proteus type |
|---:|---|---|---|
| 1 | GND | Power return | POWER |
| 2 | UART_RX | Input to module | INPUT |
| 3 | UART_TX | Output from module | OUTPUT |
| 4 | VCC | Power input | POWER |

**USB connector — 1.25 mm pitch, 5 pins**

| Pin | Signal | Notes |
|---:|---|---|
| 1 | VCC | USB power |
| 2 | NC | Leave unconnected |
| 3 | DM | USB D− |
| 4 | DP | USB D+ |
| 5 | GND | Ground |

### Files

Authoritative data first — when two files disagree, the CSVs win and the other file is a bug.

- `components/FM255/pinout.csv` — physical pinout (connector, pin, signal, type).
- `components/FM255/PROTEUS8_PIN_MAP.csv` — connector pin → unique Proteus device pin.
- `components/FM255/COMPONENT_SPEC.md` — symbol, connector and footprint requirements.
- `components/FM255/PROTEUS8_BUILD_GUIDE.md` — step-by-step Make Device walkthrough.
- `components/FM255/PROTEUS8_QUICK_START.md` — condensed build specification.
- `components/FM255/PROTEUS8_IMPLEMENTATION_STATUS.md` — what is prepared and what is not.
- `components/FM255/FM255_SCHEMATIC_REFERENCE.svg` — drawing to copy into ISIS.
- `components/FM255/SCHEMATIC_SYMBOL_GUIDE.md`, `MECHANICAL_REFERENCE.md` — symbol and mechanical notes.
- `components/FM255/SIMULATION.md` — simulation scope and limitations.

### Current status

The pin assignments are transcribed from the information supplied by the project owner. The module outline, connector orientation, pin-1 markings, mounting holes and pad geometry still need a clear photograph or mechanical drawing.

**Important:** A schematic symbol is not a functional device simulation. No manufacturer simulation model or UART protocol specification has been supplied. This initial contribution is a documented pinout/specification, not a verified native Proteus library release.

Proteus device pin numbers must be unique across the complete device. For the schematic device, use UART pins 1–4 and USB pins 5–9; retain the USB connector's physical pin labels 1–5 in adjacent text/documentation. See PROTEUS8_BUILD_GUIDE.md. The native Proteus symbol and verified PCB footprint must be generated and checked against the installed Proteus version and physical module before being labelled release-ready.
