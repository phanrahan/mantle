### Arithmetic Operators

Mantle contains the standard arithmetic operators: 
addition,
subtraction,
multiplication,
division.

Create a half adder.
```
# HalfAdder : I:In(Bit), CIN:In(Bit), O:Out(Bit), COUT:Out(Bit)
ha = HalfAdder()
```

Create a full adder.
```
# FullAdder : I0:In(Bit), I1:In(Bit), CIN:In(Bit), O:Out(Bit), COUT:Out(Bit)
fa = FullAdder()
```

Create n-bit two-operand adders.
```
# Add :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bits(n))
add = Add(n, cin=False, cout=False) 

# AddC :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bits(n)), COUT:Out(Bit)
adc = Add(n, cout=True) 
```
Setting `cin` or `cout` to `True` causes the adder
have a `CIN` or `COUT` argument.

Create n-bit two-operand subtractors.
```
# Sub :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bits(n))
sub = Sub(w, cin=False, cout=False)
# SubC :: I0:In(Bits(n)), I1:In(Bits(n)), O:Out(Bits(n)), COUT:Out(Bit)
sbc = Sub(w, cout=True)
```
Setting `cin` or `cout` to `True` causes the subtractor
have a `CIN` or `COUT` argument.


Create n-bit negate.
```
# Negate :: I:In(Bits(n)), O:Out(Bits(n))
neg = Negate(n)
```

Create n-bit two-operand multipliers.
```
# Mul :: I0:In(Bits(n)), I1:In(Bits(m)), O:Out(Bits(n+m))
mul = Mul(n, m)
```

Division is NYI.

Create a arithmetic-shift-right barrel shifter.
The arithmetic shift unit propagates the most-significant-bit
(the sign-bit).
```
# ASR :: I:In(Bits(n)), S:In(Bits(clog(n))), O:Out(Bits(n))
asr = ASR(n)
```
