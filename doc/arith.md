### Arithmetic Operators

```
# Add :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bits(n))
add = Add(n, cin=0) 
# AddC :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bits(n)), COUT:Out(Bit)
adc = AddC(n, cin=0) 
```

```
# Sub :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bits(n))
sub = Sub(w, cin=1)
# SubC :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bits(n)), COUT:Out(Bit)
sbc = SubC(w, cin=1)
```

```
# Negate :: I:In(Bits(n)), OOut(Bits(n))
neg = Negate(n)
```

Multiplication and Division are not yet implemented.
