# FM255 — Proteus 8 quick-start

This is the build specification for the schematic-only FM255 device.

## Device identity
- Device name: `FM255`
- Reference prefix: `U`
- Default value: `FM255`
- Symbol body: rectangular module block
- Packaging: none assigned (no verified PCB footprint)

## Pins
Use `PROTEUS8_PIN_MAP.csv` as the authoritative mapping. Place UART pins on the left and USB pins on the right. Keep the two connector headings visible on the symbol.

## Recommended pin types
- GND/VCC: Power
- UART_RX: Input
- UART_TX: Output
- DM/DP: Bidirectional
- NC: NC / not connected

If the Proteus 8 pin-type menu does not offer the exact label above, choose the closest supported electrical type and keep the signal name and pin number unchanged.

## Build route
ISIS creates devices directly on a schematic: draw the symbol, place and annotate pins, select the complete symbol, then use **Library → Make Device**. Save it into a writable custom library (not a read-only Labcenter library). Do not assign a package yet.

This quick-start intentionally does not prescribe physical pad sizes or connector footprints because the connector series and complete mechanical dimensions have not been confirmed.
