# Mantle

### Counters

Counters have a ```COUT```.
```
# Counter :: O:Out(Bits(n), COUT:Out(Bit)
Counter(n, next=False, has_ce=False, has_r=False, has_s=False)
```
Create an n-bit counter, with optional `CE` (clock enable), `RESET`, and `SET`.

The counter consists of an adder connected to a register.
The adder is combinational and is computing the next value
of the counter by incrementing the current value.
Normally the output of the counter is the register,
but by setting `next=True`, the output is the adder.

The adder also generates a carry, `COUT`.
`COUT` will be true if the current value is generating a carry.
For example, an 8-bit counter will generate a COUT 
when the count equals 255.

```
# UpDownCounter :: Up:Bit, Down  Bit -> O:Array[n, Bit], COUT:Bit
UpDownCounter(n, next=False, ce=False, r=False, s=False)
```
Generate an up-down counter.
The counter is incremented by (Up-Down).

```
counter = CounterModN(m, n)
```
Counter clears when count equals m-1.

```
counter = CounterIncr(n)
```
