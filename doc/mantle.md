# Mantle

Mantle is a library of parameterized hardware primitives.

## Combinational Logic

### Logic

The number of inputs is equal to the height ```n```.
```n``` must be greater than or equal to 2;
the default value for ```n``` is 2. 
```
op = And(n)  :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = NAnd(n) :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = Or(n)   :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = NOr(n)  :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = Xor(n)  :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = NXor(n) :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
```

These functions can also be called with an extra width ```w``` aargument.
In this case, the arguments to the circuit arrays of width ```w``` bits.
```
op = And(h, w)  :: I0:In(Bits(w)), ..., Ih:In(Bits(w)), O:Out(Bits(w))
op = NAnd(h, w) :: I0:In(Bits(w)), ..., Ih:In(Bits(w)), O:Out(Bits(w))
op = Or(h, w)   :: I0:In(Bits(w)), ..., Ih:In(Bits(w)), O:Out(Bits(w))
op = NOr(h, w)  :: I0:In(Bits(w)), ..., Ih:In(Bits(w)), O:Out(Bits(w))
op = Xor(h, w)  :: I0:In(Bits(w)), ..., Ih:In(Bits(w)), O:Out(Bits(w))
op = NXor(h, w) :: I0:In(Bits(w)), ..., Ih:In(Bits(w)), O:Out(Bits(w))
```

These are also versions of the above functions
that produce a single bit from an array of bits.
```
op = ReduceAnd(w)  :: I:In(Bits(w), O:Out(Bit)
op = ReduceNAnd(w) :: I:In(Bits(w), O:Out(Bit)
op = ReduceOr(w)   :: I:In(Bits(w), O:Out(Bit)
op = ReduceNOr(w)  :: I:In(Bits(w), O:Out(Bit)
op = ReduceXor(w)  :: I:In(Bits(w), O:Out(Bit)
op = ReduceNXor(w}) :: I:In(Bits(w), O:Out(Bit)
```

There are also two unary operators.
Logical negation
```
op = Not() :: I:In(Bit), O:Out(Bit)
```
and bitwise inversion
```
op = Invert(w) :: I:In(Bits(w)), O:Out(Bits(w))
```

### Arithmetic

```
add = Add(w, cin=0)
adc = AddC(w, cin=0)

sub = Sub(w, cin=1)
sbc = SubC(w, cin=1)
```

```
neg = Negate(w)
```

```
# NYI
mul = Mul(wn, wm)
```

Barrel shifter.


### Comparison

These functions implement comparison tests between two n-bit inputs.

Equality and inequality testing.

```
op = EQ(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = NE(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
```

Signed comparisons.
```
op = LT(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = LE(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = GT(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = GE(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
```

Unsigned comparisons.
```
op = ULT(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = ULE(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = UGT(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = UGE(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
```

### MUXs

The second fundamental combinational primitive 
in an FPGA is a multiplexer, or a MUX.

The simplest MUXes select amongts a small number of inputs.
```I``` is an array of n 1-bit values, or ```Bits(n)```
```S``` is the selector; it has ```log(n)``` bits.

```
mux = Mux2()  :: I:In(Bits(2)), S:In(Bit), O:Out(Bit)
mux = Mux4()  :: I:In(Bits(4)), S:In(Bits(2)), O:Out(Bit)
mux = Mux8()  :: I:In(Bits(8)), S:In(Bits(3)), O:Out(Bit)
mux = Mux16() :: I:In(Bits(16)), S:In(Bits(4)), O:Out(Bit)
```

A more general MUX selects amongst ```height``` inputs
each with a given ```width```.

```
mux = Mux(height, width) :: 
    I:Array(height, Bits(width)),
    S:Array(log(height), Bits(width)),
    O:Out(Bits(width))
```

## Sequential Logic

### Flip-Flops
```
# DFF :: I:In(Bit), O:Out(Bit)
DFF(init=0, has_ce=False, has_reset=False, has_set=False)
```

```
# SRFF :: S:In(Bit), R:In(Bit), O:Out(Bit)
SRFF(init=0, has_ce=False)
```

```
# RSFF :: R:In(Bit), S:In(Bit), O:Out(Bit)
RSFF(init=0, has_ce=False)
```

```
# JKFF :: J:In(Bit), K:In(Bit), O:Out(Bit)
JKFF(init=0, has_ce=False, has_reset=False, has_set=False)
```

```
# TFF :: I:In(Bit), O:Out(Bit)
TFF(init=0, has_ce=False, has_reset=False, has_set=False)
```
If I is true, toggle the flip-flop.

There is also a utility function to create a list of n ```DFF```s

```
FFs(n, init=0, has_ce=False, has_reset=False, has_set=False)
```


### Registers
```
# Register :: I:In(T(n)), O:Out(T(n))
Register(n, init=0, has_ce=False, has_reset=False, has_set=False, T=Bits)
```
```

