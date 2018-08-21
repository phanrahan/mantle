### Multiplexers

The basic multiplixers select an array bits.
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
mux = Mux(height=2, width=None) :: 
    I0:In(Bits(width)),
    I1:In(Bits(width)),
    ...
    In:In(Bits(width)), # n=log2(height)
    S:Bits(log2(height)),
    O:Out(Bits(width))
```
For height=1, `S` has type `Bit`.
