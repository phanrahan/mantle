## Logic operators

The following functions generate gates with a given number of inputs.
The number of inputs is equal to `n`.
`n` must be greater than or equal to 1;
the default value for `n` is 2. 
The inputs and outputs to the circuits will have type `Bit`.
```
op = And(n)  :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = NAnd(n) :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = Or(n)   :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = NOr(n)  :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = XOr(n)  :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
op = NXOr(n) :: I0:In(Bit), ..., In:In(Bit), O:Out(Bit)
```

These functions can also be called with an optional width `w`.
In this case, the arguments to the circuits 
will be `Bits` of width ```w```.
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
that produce a single `Bit` from array of `Bits`.
```
op = ReduceAnd(n)  :: I:In(Bits(n), O:Out(Bit)
op = ReduceNAnd(n) :: I:In(Bits(n), O:Out(Bit)
op = ReduceOr(n)   :: I:In(Bits(n), O:Out(Bit)
op = ReduceNOr(n)  :: I:In(Bits(n), O:Out(Bit)
op = ReduceXOr(n)  :: I:In(Bits(n), O:Out(Bit)
op = ReduceNXOr(n) :: I:In(Bits(n), O:Out(Bit)
```

There are also two unary operators,
logical negation
```
op = Not() :: I:In(Bit), O:Out(Bit)
```
and bitwise invert
```
op = Invert(n) :: I:In(Bits(n)), O:Out(Bits(n))
```

Create a logical-shift-right barrel shifter.
The logical shift unit shifts 0s into the most-significant bits.
```
# LSR :: I:In(Bits(n)), S:In(Bits(clog(n))), O:Out(Bits(n))
lsr = LSR(n)
```

Create a logical-shift-left barrel shifter.
The logical shift unit shifts 0s into the least-significant bits.
```
# LSL :: I:In(Bits(n)), S:In(Bits(clog(n))), O:Out(Bits(n))
lsl = LSL(n)
```

Create a rotate-right unit.
The rotate right unit rotates the bits rightwards;
the bits exiting on the right enter on the left.
```
# ROR :: I:In(Bits(n)), S:In(Bits(clog(n))), O:Out(Bits(n))
ror = ROR(n)
```

Create a rotate-left unit.
The rotate left unit rotates the bits leftwards;
the bits exiting on the left enter on the right.
```
# ROL :: I:In(Bits(n)), S:In(Bits(clog(n))), O:Out(Bits(n))
rol = ROL(n)
```
