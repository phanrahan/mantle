# Mantle

### Decoders, Encoders, and Arbiters

Mantle has a decoders, encoders, and arbiters.

```
Decode
```

returns circuit that computes whether the n-bit input is equal to i.

```
op = Decode(i,n) :: I:Array(n,Bit) -> O:Bit
```
For example, ```Decode(3,4)``` returns whether the 4-bit input is
is equal to 3.

```
Decoder
``` 

maps from single input to multiple outouts.
Decoder accepts a single n-bit input,
and returns 2^n single bit outputs.
The ith output is 1, if the input is equal to i.
```
op = Decoder(n) :: I:Array(n,Bit) -> O:Array(2^n,Bit)
```
For example, 
`Decoder(3) :: I:Array(3,Bit) -> O:Array(8,Bit)` sets `O[i] = (i == I)`.


An encoder is the inverse of a decoder.
An encode accepts a single 2^n-bit input,
and outputs the n-bit binary value representing that input..
```
op = Encoder(n) :: I:Array(n,Bit) -> O:Array(log(n),Bit)
```
Since the number of output bits is less than the number of input bits,
multiple input values will map to the same output.
Normally encoders are designed such that an input
will only a single bit set, 
will yield the log(n) bit representation of the position of the bit.
If multiple bits are set,
the log(n) bit representations for each set bit are or'ed together.


An arbiter or priority encoder is an special encoder.
The output is set to the encoder value of the least significant set bit.
If other bits are set, the output does not change.
```
op = Arbiter(n) :: I:Array(n,Bit) -> O:Array(log(n),Bit)
```
