### Registers and Flip-Flops

### Flip-Flops
```
# DFF :: I:In(Bit), O:Out(Bit)
DFF(init=0, has_ce=False, has_reset=False, has_set=False)
```

```
# SRFF :: S:In(Bit), R:In(Bit), O:Out(Bit)
SRFF(init=0, has_ce=False)
```

```
# RSFF :: R:In(Bit), S:In(Bit), O:Out(Bit)
RSFF(init=0, has_ce=False)
```

```
# JKFF :: J:In(Bit), K:In(Bit), O:Out(Bit)
JKFF(init=0, has_ce=False, has_reset=False, has_set=False)
```

```
# TFF :: I:In(Bit), O:Out(Bit)
TFF(init=0, has_ce=False, has_reset=False, has_set=False)
```
If I is true, toggle the flip-flop.

There is also a utility function to create a list of n ```DFF```s

```
FFs(n, init=0, has_ce=False, has_reset=False, has_set=False)
```


### Registers
```
# Register :: I:In(T(n)), O:Out(T(n))
Register(n, init=0, has_ce=False, has_reset=False, has_set=False, T=Bits)
```

