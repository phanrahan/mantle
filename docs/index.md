## Mantle

Mantle can be configured to synthesize low-level primitives
for a particular FPGA.
For example, to use mantle with the Lattice ice40,
set the `Mantle` target
```python
import magma
magma.set_mantle_target('ice40')
```
The default target is to generate `coreir`.


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


### Mantle Operators and Overloading
Mantle provides a set of common operators similar to Python's built-in
`operator` library. Mantle uses these to overload the operators of various
magma types.  The implementation lives in `mantle/common/operator.py`. Similar
to Python's built-in `operator` library, users can import
`mantle.common.operator` to access functions like `add`.  These are defined
generically over the Mantle primitives, so they can be used with any backend.

#### Logical Operators
These operators are defined on the magma types: `Bit` and `Bits`. In this list
we provide the function name, followed by the overloaded operator (`None` if an
overloaded operator does not exist).
* `and_`, `&`
* `nand`, `None`
* `or`, `^`
* `nor`, `None`
* `xor`, `^`
* `nxor`, `None`
* `lsl`, `<<`
* `lsr`, `>>`
* `asr`, `None`
* `not`, `None`
* `invert`, `~`
* `eq`

#### Arithmetic Operators
* `negate`, `-`
* `add`, `+`
* `sub`, `-`
* `mul` (NYI)
* `div` (NYI)

#### Comparison Operators
* `lt`, `<`
* `le`, `<=`
* `gt`, `>`
* `ge`, `>=`

#### Other
* `mux`, `None`
