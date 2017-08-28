## Logic operators

The following functions generate gates with a given number of inputs.
The number of inputs is equal to ```n```.
```n``` must be greater than or equal to 1;
the default value for ```n``` is 2. 
```
op = And(n)  :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = NAnd(n) :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = Or(n)   :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = NOr(n)  :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = XOr(n)  :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = NXOr(n) :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
```

These functions can also be called with an optional width ```w``` aargument.
In this case, the arguments to the circuit arrays of width ```w``` bits.
The width must be greater than or equal to 1.
```
op = And(h, w)  :: I0:In(Bits(w)), ..., Ih:In(Bits(w)), O:Out(Bits(w))
op = NAnd(h, w) :: I0:In(Bits(w)), ..., Ih:In(Bits(w)), O:Out(Bits(w))
op = Or(h, w)   :: I0:In(Bits(w)), ..., Ih:In(Bits(w)), O:Out(Bits(w))
op = NOr(h, w)  :: I0:In(Bits(w)), ..., Ih:In(Bits(w)), O:Out(Bits(w))
op = XOr(h, w)  :: I0:In(Bits(w)), ..., Ih:In(Bits(w)), O:Out(Bits(w))
op = NXOr(h, w) :: I0:In(Bits(w)), ..., Ih:In(Bits(w)), O:Out(Bits(w))
```

These are also versions of the above functions
that produce a single bit from an array of bits.
```
op = ReduceAnd(w)  :: I:In(Bits(w), O:Out(Bit)
op = ReduceNAnd(w) :: I:In(Bits(w), O:Out(Bit)
op = ReduceOr(w)   :: I:In(Bits(w), O:Out(Bit)
op = ReduceNOr(w)  :: I:In(Bits(w), O:Out(Bit)
op = ReduceXOr(w)  :: I:In(Bits(w), O:Out(Bit)
op = ReduceNXOr(w}) :: I:In(Bits(w), O:Out(Bit)
```

There are also two unary operators,
logical negation
```
op = Not() :: I:In(Bit), O:Out(Bit)
```
and bitwise invert
```
op = Invert(w) :: I:In(Bits(w)), O:Out(Bits(w))
```
