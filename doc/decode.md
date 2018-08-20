### Decoders, Encoders, and Arbiters

Decode returns circuit that computes whether the n-bit input is equal to `i`.

```
op = Decode(i,n) :: I:In(Bits(n)), O:Out(Bit)
```
For example, ```Decode(3,4)``` returns 
whether the 4-bit input is is equal to 3.
It is basically an optimized version of `I == m.bits(i,n)`.

Decoder maps from single input to multiple outputs.
Decoder accepts a single n-bit input,
and returns `2^n` single bit outputs.
The ith output is 1, if the input is equal to i.
```
op = Decoder(n) :: I:In(Bits(n)),  O:Out(Bits(2^n))
```
For example, 
`Decoder(3) :: I:In(Bits(3)), O:Out(Bits(8))` sets `O[i] = (i == I)`.


An encoder is the inverse of a decoder.
An encoder accepts a single 2^n-bit input,
and outputs the n-bit binary value representing that input..
```
op = Encoder(n) :: I:In(Bits(n)). O:Out(Bits(log2(n)))
```
Since the number of output bits is less than the number of input bits,
multiple input values must map to the same output value.
This encoder is designed such that 
given an input with only a single bit set, 
the encdoer will return 
the log2(n) bit representation of the position of the set bit.
If multiple bits are set,
the log2(n) bit representations for each set bit are or'ed together.


An arbiter or priority encoder is an special encoder.
The output is set to the encoder value of the least significant set bit.
If other bits are set, the output does not change.
    ```
op = Arbiter(n) :: I:In(Bits(n)). O:Out(Bits(log(n)))
```
It is better to use an Arbiter instead of an Encoder,
since the output is more clearly defined.
