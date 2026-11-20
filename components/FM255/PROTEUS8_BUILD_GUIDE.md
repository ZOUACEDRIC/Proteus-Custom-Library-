# Building the FM255 device in Proteus 8 (ISIS)

This guide targets Proteus 8. It uses Proteus's own **Make Device** workflow so the saved part is a genuine Proteus device in a writable user library.

## 1. Create the symbol drawing

1. Open Proteus 8 and start a schematic in ISIS.
2. Choose 2D Graphics mode and draw a rectangular module body.
3. Label the body `FM255`.
4. Choose Component Pin mode.
5. Place four pins on the left side and five pins on the right side. Keep pin ends facing outward so wires connect at the outer ends.
6. Edit each pin and set its name, default pin number and electrical type using the table below.

## 2. Pin table — enter exactly

### Left group: UART connector J1
| Pin number | Pin name | Electrical type |
|---:|---|---|
| 1 | GND | POWER |
| 2 | UART_RX | INPUT |
| 3 | UART_TX | OUTPUT |
| 4 | VCC | POWER |

### Right group: USB connector J2
| Pin number | Pin name | Electrical type |
|---:|---|---|
| 1 | VCC | POWER |
| 2 | NC | NC (Not Connected) |
| 3 | DM | BIDIRECTIONAL |
| 4 | DP | BIDIRECTIONAL |
| 5 | GND | POWER |

**Important numbering note:** Proteus device pin numbers must be unique within one device. The seller's drawing numbers the two physical connectors independently, so the combined schematic device must use unique Proteus pin numbers. To preserve the physical connector labels without duplicate device pin numbers, use:
- UART pins: 1, 2, 3, 4
- USB pins: 5, 6, 7, 8, 9

Add visible text labels beside the USB group reading `J2: physical pins 1–5` and use the mapping:
- Proteus pin 5 = USB physical pin 1 (VCC)
- Proteus pin 6 = USB physical pin 2 (NC)
- Proteus pin 7 = USB physical pin 3 (DM)
- Proteus pin 8 = USB physical pin 4 (DP)
- Proteus pin 9 = USB physical pin 5 (GND)

This avoids duplicate Proteus pin numbers while documenting the physical connector numbering.

## 3. Make the device

1. Exit pin placement.
2. Drag a selection box around the entire body, all nine pins and all labels.
3. Choose **Library > Make Device** (or right-click the selected drawing and choose Make Device).
4. Set Device Name to `FM255`.
5. Set Reference Prefix to `U`.
6. Choose a suitable category such as Connectors or Miscellaneous, depending on the categories available in your Proteus 8 installation.
7. Do not assign a PCB package yet.
8. On the final page, save to a writable user library such as `USERDVC` or a new personal library. Do not try to save into a read-only Labcenter library.
9. Finish and open Pick Devices; search for `FM255` and place it on a fresh schematic to test the saved device.

## 4. What is not ready for PCB

No PCB package is assigned. The supplied drawing does not provide enough verified information for a fabrication-ready package. Do not fabricate a board using a guessed footprint.

## 5. Electrical and simulation cautions

- Confirm module VCC range and UART logic voltage with the manufacturer before powering it.
- Host TX connects to FM255 UART_RX; host RX connects to FM255 UART_TX.
- USB pin 2 is NC.
- This symbol is a schematic representation only. It does not simulate the module firmware, USB behavior or UART protocol.

## References

- Labcenter, Proteus Design Tutorials: https://www.labcenter.com/downloads/Tutorials.pdf
- Labcenter, Library Facilities: https://labcenter.s3.amazonaws.com/downloads/proteusLibraryFacilities.pdf
