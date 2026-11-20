# FM255 Mechanical Reference (Photo-Based)

## What the supplied seller drawing confirms

- Board outline is shown with rounded corners; the corner callout is R1.00.
- The drawing labels the board height as 15.00 mm.
- Two mounting holes are called out as 2 × Ø3.20 mm.
- The connector edge is shown with two female sockets:
  - UART: 1.25 mm pitch, 4 pins, on the left in the seller's bottom-view drawing.
  - USB: 1.25 mm pitch, 5 pins, on the right in the seller's bottom-view drawing.
- In the seller's connector view, pin numbering runs left to right for both connectors.

## Connector pinout

| Connector | Pin | Signal |
|---|---:|---|
| UART | 1 | GND |
| UART | 2 | UART_RX |
| UART | 3 | UART_TX |
| UART | 4 | VCC |
| USB | 1 | VCC |
| USB | 2 | NC |
| USB | 3 | DM |
| USB | 4 | DP |
| USB | 5 | GND |

## Do not fabricate from this reference alone

The supplied photo does not clearly provide the complete board length, exact hole-center coordinates, connector body dimensions, pad geometry, or an unambiguous scale/orientation for every feature. The Ø6.00 callout visible in the drawing is not sufficient by itself to define a connector footprint.

Therefore:
- Do not treat this document as a verified PCB footprint.
- Do not infer the missing board length or hole coordinates.
- Confirm the drawing against a dimensioned manufacturer CAD file or direct measurements before fabrication.
- Confirm module supply-voltage range and UART logic levels from the manufacturer before wiring.

## Proteus status

This is a photo-based mechanical reference for the schematic/library project. It does not constitute a native Proteus simulation model or a verified PCB package.
