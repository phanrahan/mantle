### Counters

Counter consists of an adder connected to a register.
The adder is combinational and is computing the next value
by incrementing the current value.

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
UpCounter(n, cin=False, cout=True, incr=1, 
    has_ce=False, has_reset=False)
```

```
# DownCounter :: O:Out(Bits(n), COUT:Out(Bit)
DownCounter(n, cin=False, cout=True, decr=1, 
    has_ce=False, has_reset=False)
```

```
# UpDownCounter :: U:In(Bit), D:In(Bit), O:Out(Bits(n)), COUT:Out(Bit)
UpDownCounter(n, cout=True, has_ce=False, has_reset=False)
```
Generate an up-down counter.
The counter is incremented by (Up-Down).

```
# CounterModM :: O:Out(Bits(n), COUT:Out(Bit)
counter = CounterModN(m, n, cin=False, cout=True, has_ce=False, has_reset=False)
```
Counter wraps around to 0 when count equals m-1.


```
# CounterLoad :: DATA:In(Bits(n), LOAD:In(Bit), O:Out(Bits(n), COUT:Out(Bit)
counter = CounterLoad(n, cin=False, cout=True, incr=1,
            has_ce=False, has_reset=False)
```
