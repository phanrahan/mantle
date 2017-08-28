# Mantle
[![Build Status](https://travis-ci.com/phanrahan/mantle.svg?token=BftLM4kSr1QfgPspi6aF&branch=master)](https://travis-ci.com/phanrahan/mantle)


Mantle is part of the Magma ecosystem.

Magma is a programming model for building hardware.
The key abstractions in Magma is a Circuit.
Circuits are created and then wired together.

Mantle is a library of useful circuits.
Examples of mantle circuits are logic operators,
arithmetic operators,
comparison operators,
multiplexers,
decoders and encoders,
registers,
counters,
shift regiseters
and memory.

## Documentation

[Logical Operators](doc/logic.md)

[Arithmetic Operators](doc/arith.md)

[Comparison Operators](doc/compare.md)

[Multiplexers](doc/mux.md)

[Decoders and Encoders](doc/decode.md)

[Register](doc/register.md)

[Counters](doc/counter.md)

[Shift Registers](doc/shift.md)

[Memory](doc/memory.md)

[ICE40 Primitives](doc/ice40.md)

## Configuring Mantle

Mantle can be configured to synthesize low-level primitives
for a particular FPGA.
For example, to use mantle with the Lattice ice40,
set the `MANTLE_TARGET`  environment variable.
```bash
export MANTLE_TARGET=ice40
```

