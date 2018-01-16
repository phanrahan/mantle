### Counters

Counter consists of an adder connected to a register.
The adder is combinational and is computing the next value
by incrementing the current value.
Normally the output of the counter is the register,
but by setting `next=True`, the output is the adder.

The counters have flags to control whether the
adder has carry in or carry out.
The `COUT` will be true if the current value is generating a carry.
For example, an 8-bit counter will generate a COUT 
when the count equals 255.

Since counters contain state,
they have optional `CE` (clock enable), `RESET`, and `SET` inputs.
`CLK` is always included.


Create an n-bit up counter, 
```
# UpCounter :: O:Out(Bits(n), COUT:Out(Bit)
UpCounter(n, cin=False, cout=True, incr=1, next=False, 
    has_ce=False, has_r=False, has_s=False)
```

```
# DownCounter :: O:Out(Bits(n), COUT:Out(Bit)
DownCounter(n, cin=False, cout=True, incr=1, next=False, 
    has_ce=False, has_r=False, has_s=False)
```

```
# UpDownCounter :: U:In(Bit), D:In(Bit), O:Out(Bits(n)), COUT:Out(Bit)
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
