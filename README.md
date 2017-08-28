# Mantle
[![Build Status](https://travis-ci.com/phanrahan/mantle.svg?token=BftLM4kSr1QfgPspi6aF&branch=master)](https://travis-ci.com/phanrahan/mantle)

Mantle is part of the Magma ecosystem
of python programming tools for FPGAs.

[Magma](https://github.com/phanrahan/magma)
is a programming model for building hardware.
The main abstraction in Magma is a Circuit.
Circuits are created and then wired together.
Magma circuits can be saved as structual verilog files.

[Mantle](https://github.com/phanrahan/mantle)
is a library of useful circuits.
Examples of mantle circuits are logic operators,
arithmetic operators,
comparison operators,
multiplexers,
decoders and encoders,
registers,
counters,
shift regiseters
and memory.

[Loam](https://github.com/phanrahan/loam)
is used to model FPGAs, peripherals, parts (ICs) and boards.
Loam makes it easy to build applications
on a variety of different FPGA demonstration boards.

Currently, Mantle supports generic verilog
and the Lattice ice40
(and its open source [icestorm](http://www.clifford.at/icestorm/) toolchain).
A Xilinx (spartan3, spartan6, zynq) backends will be released soon.
An Alterna backend is in the works.

## Documentation

- Combinational logic
  - [Logical Operators](doc/logic.md)
  - [Arithmetic Operators](doc/arith.md)
  - [Comparison Operators](doc/compare.md)
  - [Multiplexers](doc/mux.md)
  - [Decoders, Encoders, and Arbiters](doc/decode.md)
- Sequential logic
  - [Flip-flops and Register](doc/register.md)
  - [Counters](doc/counter.md)
  - [Shift Registers](doc/shift.md)
- [Memory](doc/memory.md)

There also exist libraries for low-level FPGA-specific primitives.

- [ICE40 Primitives](doc/ice40.md)

## Configuring Mantle

Mantle can be configured to synthesize low-level primitives
for a particular FPGA.

For example, to use mantle with the Lattice ice40,
set the `MANTLE_TARGET`  environment variable.
```bash
export MANTLE_TARGET=ice40
```

