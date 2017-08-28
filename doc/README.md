## Mantle

Mantle can be configured to synthesize low-level primitives
for a particular FPGA.

For example, to use mantle with the Lattice ice40,
set the `MANTLE_TARGET`  environment variable.
```bash
export MANTLE_TARGET=ice40
```

The default configuration is to generate generic verilog.


### Combinational Logic

- [Logical Operators](logic.md)

- [Arithmetic Operators](arith.md)

- [Comparison Operators](compare.md)

- [Multiplexers](mux.md)

- [Decoders, Encoders, and Arbiters](decode.md)


### Sequential Logic

- [Register and Flip-FLops](register.md)

- [Counters](counter.md)

- [Shift Registers](shift.md)


### Memory

- [LUTs, ROMs, RAMs, and Memory](memory.md)


### Primitives

- [ICE40 Primitives](ice40.md)

