### Arithmetic Operators

Mantle contains the standard arithmetic operators: 
addition,
subtraction,
multiplication,
division.

Create n-bit two-operand adders.
```
# Add :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bits(n))
add = Add(n, cin=0) 
# AddC :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bits(n)), COUT:Out(Bit)
adc = AddC(n, cin=0) 
```
The `AddC` version creates a carry out `COUT`.

Create n-bit two-operand subtractors.
```
# Sub :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bits(n))
sub = Sub(w, cin=1)
# SubC :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bits(n)), COUT:Out(Bit)
sbc = SubC(w, cin=1)
```
The `SubC` version creates a carry out `COUT`.

Create n-bit two-operand multipliers.
```
# Mul :: I0:In(Bits(n)), I1:In(Bits(m)), O:Out(Bits(n+m))
mul = Mul(n, m)
```

Create n-bit negate..
```
# Negate :: I:In(Bits(n)), O:Out(Bits(n))
neg = Negate(n)
```

Division is NYI.
