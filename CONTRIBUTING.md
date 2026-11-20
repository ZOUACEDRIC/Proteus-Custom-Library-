# Contributing

This repository holds part definitions for Proteus, so accuracy matters more than volume.
A wrong pin number silently breaks a design weeks later.

## Ground rules

1. **The CSVs are the source of truth.** `pinout.csv` describes the physical part;
   `PROTEUS8_PIN_MAP.csv` describes the Proteus device. Prose, SVG and guides must match them.
2. **Never invent electrical detail.** If the supply range, logic level or connector series
   is unknown, write "not verified" instead of a plausible number.
3. **Device pin numbers are unique per device.** When a part has several connectors that each
   number from 1, keep the physical labels in documentation and assign distinct Proteus numbers
   (FM255: UART 1–4, USB 5–9).
4. **No footprint without a verified mechanical drawing.** A guessed pad layout produces
   unbuildable boards.

## Adding a component

```bash
python scripts/new_component.py <NAME> "<one line description>"
```

Then fill in `pinout.csv`, mirror it in `PROTEUS8_PIN_MAP.csv`, and rewrite `COMPONENT_SPEC.md`.
Keep the folder flat — no sub-folders per revision.

## Before you commit

```bash
python scripts/validate_component.py
```

CI runs the same command. A red check means the tables disagree with each other.

## Reporting that a device is release-ready

Only after all of these:

- [ ] `python scripts/validate_component.py` passes with no errors.
- [ ] The device was created in Proteus with Library → Make Device into a writable library.
- [ ] Proteus was restarted and the part appears in Pick Devices.
- [ ] The part was placed on a fresh schematic and every pin number and name inspected.
- [ ] `USERDVC.LIB` / `.IDX` (or the equivalent exported library pair) is committed.

Record the Proteus version used, because library files are version specific.
