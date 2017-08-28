### Counters

Create an n-bit up counter, 
with optional `CE` (clock enable), `RESET`, and `SET`.
`CLK` is always included.

```
# UpCounter :: O:Out(Bits(n), COUT:Out(Bit)
UpCounter(n, cin=False, cout=True, incr=1, next=False, 
    has_ce=False, has_r=False, has_s=False)
```

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
# DownCounter :: O:Out(Bits(n), COUT:Out(Bit)
DownCounter(n, cin=False, cout=True, incr=1, next=False, 
    has_ce=False, has_r=False, has_s=False)
```

```
# UpDownCounter :: Up:In(Bit), Down:In(Bit), O:Out(Bits(n)), COUT:Out(Bit)
UpDownCounter(n, cout=True, next=False, ce=False, r=False, s=False)
```
Generate an up-down counter.
The counter is incremented by (Up-Down).

```
# CounterModM :: O:Out(Bits(n), COUT:Out(Bit)
counter = CounterModN(m, n, cin=False, cout=True, incr=1, next=False, has_ce=False)
```
Counter wraps around to 0 when count equals m-1.


```
# CounterLoad :: DATA:In(Bits(n), LOAD:In(Bit), O:Out(Bits(n), COUT:Out(Bit)
counter = CounterLoad(n, cin=False, cout=True, incr=1,
            has_ce=False, has_reset=False, has_set=False)
