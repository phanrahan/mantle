# Mantle Primitives
The mantle primitives define a set of generator interfaces that each mantle
target must implement.  They are designed to be equivalent to the coreir
primitives.

## Arithmetic (arith)

Issues:
* Parameter names are not consistent (e.g. `n` vs `width`)
* `cin, cout` parameters

Generators:
* `Add(n, cin, cout)` - **TODO: Different than coreir.add, which doesn't have cin or cout**
* `Sub(n, cin, cout)` - **TODO: Same issue as add**
* `Negate(width)`
* `ASR(width)` - **TODO: Missing in mantle**
* `Mul(width)` - **TODO: Missing in mantle**
* `UDiv(width)` - **TODO: Missing in mantle**
* `SDiv(width)` - **TODO: Missing in mantle**
* `UMod(width)` - **TODO: Missing in mantle**
* `SMod(width)` - **TODO: Missing in mantle**

## Logic

Issues:
* mantle uses a `height` parameter whereas coreir generators are binary
* `mantle40` uses `n` for `DefineReduce{Op}` parameter but `height` for
  `Reduce{Op}`

Generators:
* `And(height, width)`
* `ReduceAnd(height, width)`
* `NAnd(height, width)`
* `ReduceNAnd(height)`
* `Not` - 1-bit invert
* `Or(height, width)`
* `ReduceOr(height)`
* `NOr(height, width)`
* `ReduceNOr(height)`
* `XOr(height, width)`
* `ReduceXOr(height)`
* `NXOr(height, width)`
* `ReduceNXOr(height)`
* `Invert(width)` - **TODO: mantle40 uses `n` parameter for `Invert`**
* `LSL(width, shift_amount)`
* `LSR(width, shift_amount)`
* `StaticLeftShift(width)` - **TODO: Should these primitives? Issue is that if we instantiate an LSL, we don't know if the shift input is constant or dynamic. We could have a pass that inspects all LSL/LSR instances and changes those with static shift amounts to only use wiring. Then we could just have LSL and LSR**
* `StaticRightShift(width)`

## Compare

Issues:
* Define+Instance variants of comparisons (e.g. `ULT(n)`) missing from
  `mantle40`, they only have `Define{op}` variants

Generators:
* `EQ(n)`
* `NE(n)`
* `ULT(n)`
* `ULE(n)`
* `UGT(n)`
* `UGE(n)`
* `SLT(n)`
* `SLE(n)`
* `SGT(n)`
* `SGE(n)`

## Mux

Issues:

Generators:
* `Mux(height, width)` - **TODO: mantle40 limited to heights `[2, 4, 8, 16]`**

## Flip Flops (FF)

Issues:
* mantle has many more parameters not available in coreir, we could move to
  having a basic FF primitive, then have these higher level features built on
  top of them

Generators:
* `DFF(init, has_ce, has_reset, edge, sync)`
* `SRFF(init, has_ce, has_reset, edge, sync)` - **TODO: Missing from mantle.coreir**
* `RSFF(init, has_ce, has_reset, edge, sync)` - **TODO: Missing from mantle.coreir**
* `JKFF(init, has_ce, has_reset, edge, sync)` - **TODO: Missing from mantle.coreir**
* `TFF(init, has_ce, has_reset, edge, sync)` - **TODO: Missing from mantle.coreir**

## LUT
Issues:
* mantle.coreir uses `init` parameter instead of `rom` (used by mantle40) and `N`
  instead of `n`

Generators:
* `LUT(rom, n)` - `rom` is the initialization value, `n` is the number of bits
  (optional, can be inferred from `rom`)

## Memory

Issues:
* mantle.coreir has custom RAM implementation, should it just use the common.RAM?

Generators:
* `Memory(height, width, rom, readonly)` - **TODO: mantle.coreir does not have rom parameter and does not support ROMs. I think this is an old artifact of coreir lacking support for ROMs, which it should now support. also missing define+instance variant**
