### Comparison Operators

These functions implement comparison tests between two n-bit inputs.

Equality and inequality testing.

```
op = EQ(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = NE(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
```

Signed comparisons.
```
op = SLT(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = SLE(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = SGT(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = SGE(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
```

Unsigned comparisons.
```
op = ULT(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = ULE(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = UGT(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
op = UGE(n) :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bit)
```
