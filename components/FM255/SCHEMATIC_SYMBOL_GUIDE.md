# FM255 schematic symbol construction guide

## Symbol layout
Use one rectangular module body labelled FM255, with two connector groups:
- J1 / UART on the left, pins 1–4.
- J2 / USB on the right, pins 1–5.

The SVG is a visual layout reference only, not a native Proteus .LIB file.

## J1 — UART (1.25 mm pitch)
| Pin | Name | Direction at module |
|---:|---|---|
| 1 | GND | Power return |
| 2 | UART_RX | Input |
| 3 | UART_TX | Output |
| 4 | VCC | Power input |

## J2 — USB (1.25 mm pitch)
| Pin | Name | Direction at module |
|---:|---|---|
| 1 | VCC | Power input |
| 2 | NC | Not connected |
| 3 | DM | USB D− |
| 4 | DP | USB D+ |
| 5 | GND | Power return |

## Suggested Proteus settings
- Device name: FM255
- Reference prefix: U
- Category: Modules
- Keep J1 and J2 as separate connector groups with independent numbering.
- J1 pin 2: INPUT; J1 pin 3: OUTPUT.
- J2 pins 3 and 4: bidirectional data pins, if supported by the installed Proteus pin editor.
- J2 pin 2 must remain NC.
- Do not assign a PCB package yet.

## Native-library status
Proteus device libraries (.LIB and .IDX) are generated/managed by Proteus Library Manager. This repository does not yet contain a native FM255 device library. Recreate the symbol in ISIS using Library > Make Device, save it to a writable user library, then reopen it and verify all nine pin numbers and names.

## Electrical safety
The supplied photos and pinout do not confirm the allowed VCC range or UART logic voltage. Confirm these values with the manufacturer before powering the module or connecting it directly to an MCU.
