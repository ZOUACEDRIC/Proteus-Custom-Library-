# FM255 — component specification

## Identity

- Component name: FM255
- Category: external module with UART and USB interfaces
- Intended use: reusable schematic representation in Proteus
- Connector pitch: 1.25 mm for both connectors, as supplied by the project owner

## Schematic symbol requirements

Represent the module as one rectangular device with two separately named connectors:

1. UART, 4 pins: GND, UART_RX, UART_TX, VCC.
2. USB, 5 pins: VCC, NC, DM, DP, GND.

Use the pin numbers exactly as shown in `pinout.csv`. The seller's connector numbering is independent (UART 1–4, USB 1–5). Proteus device pin numbers, however, must be unique across the complete device. Use Proteus pins 1–4 for UART and 5–9 for USB, with visible labels/documentation mapping USB Proteus pins 5–9 to physical connector pins 1–5.

Suggested designators:
- Module: U?
- UART connector: J_UART
- USB connector: J_USB

Show USB pin 2 as NC. Do not assign it to another signal.

## PCB footprint requirements

The supplied 1.25 mm pitch establishes adjacent pin spacing only. It does not define the complete connector or module footprint. Before making a fabrication footprint, confirm:

- connector mating-face orientation and pin-1 location;
- surface-mount or through-hole contacts;
- pad dimensions and exact row geometry;
- connector body dimensions and board-edge clearance;
- module PCB outline and mounting-hole positions, if any.

Do not use an unverified generic footprint for fabrication.

## Electrical notes

- Confirm the module supply-voltage range from manufacturer documentation before connecting VCC.
- UART_RX is an input to the FM255; UART_TX is an output from the FM255.
- For a host UART: host TX → FM255 UART_RX; host RX ← FM255 UART_TX.
- Confirm UART logic-voltage compatibility before direct MCU connection.
- USB DM and DP are differential data signals.
- USB pin 2 is NC according to the supplied pinout.

## Validation checklist

- [ ] Verify pin-1 orientation from a clear module photograph or datasheet.
- [ ] Confirm supply voltage and UART logic levels.
- [ ] Confirm connector mechanical dimensions.
- [ ] Create native Proteus schematic library symbol.
- [ ] Create and verify PCB footprint against the physical module.
- [ ] Open the library in the target Proteus version and check every pin number.
- [ ] Test a host-to-module UART wiring example.
