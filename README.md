# Proteus Custom Library

Reusable Proteus component definitions and documentation.

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

- `components/FM255/pinout.csv` — machine-readable pin table.
- `components/FM255/COMPONENT_SPEC.md` — symbol, connector and footprint requirements.
- `components/FM255/SIMULATION.md` — simulation scope and limitations.

### Current status

The pin assignments are transcribed from the information supplied by the project owner. The module outline, connector orientation, pin-1 markings, mounting holes and pad geometry still need a clear photograph or mechanical drawing.

**Important:** A schematic symbol is not a functional device simulation. No manufacturer simulation model or UART protocol specification has been supplied. This initial contribution is a documented pinout/specification, not a verified native Proteus library release.

Proteus device pin numbers must be unique across the complete device. For the schematic device, use UART pins 1–4 and USB pins 5–9; retain the USB connector's physical pin labels 1–5 in adjacent text/documentation. See PROTEUS8_BUILD_GUIDE.md. The native Proteus symbol and verified PCB footprint must be generated and checked against the installed Proteus version and physical module before being labelled release-ready.
