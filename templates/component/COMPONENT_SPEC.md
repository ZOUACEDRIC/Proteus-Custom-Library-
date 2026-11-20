# __NAME__ — component specification

## Identity

- Component name: __NAME__
- Category: __FILL_IN__ (e.g. sensor module, connector, power device)
- Intended use: reusable schematic representation in Proteus
- Source of the pinout: __FILL_IN__ (datasheet, seller drawing, measured module)

## Schematic symbol requirements

Describe the body shape, pin grouping and any text that must appear on the
symbol. State the reference prefix (U, J, R, ...) and whether a PCB package is
assigned.

Use device pin numbers that are unique across the whole device. If the physical
part uses several connectors that each number their pins from 1, keep the
physical labels in the documentation and give each pin a distinct Proteus
number here and in `PROTEUS8_PIN_MAP.csv`.

## PCB footprint requirements

List what still has to be verified before a footprint may be drawn: pad
geometry, pin-1 marking, connector orientation, board outline, mounting holes.

Do not assign a package that has not been checked against the physical part.

## Electrical notes

Record supply voltage, logic levels and any pin that must stay unconnected.

## Validation checklist

- [ ] Pinout confirmed against a datasheet or measurement.
- [ ] `PROTEUS8_PIN_MAP.csv` filled in with unique device pin numbers.
- [ ] `python scripts/validate_component.py __NAME__` passes.
- [ ] Native Proteus device built with Library > Make Device.
- [ ] Device placed on a test schematic and all pins checked.
