# FM255 simulation notes

## What the schematic representation can do

The FM255 can be represented as an external module with its supplied UART and USB connector pinouts. This supports wiring diagrams and system-level circuit design.

## What is not yet simulated

A connector symbol does not reproduce the module's internal firmware, recognition behavior, USB enumeration, or UART command responses.

A functional simulation requires at least one of:

- an official Proteus/VSM model from the manufacturer;
- a documented UART protocol and a custom behavioral model;
- a testable firmware/command specification sufficient to reproduce the required responses.

Until such a model exists, treat the FM255 as an external, non-simulated device in Proteus. A successful schematic compile is not proof that the physical module works.
