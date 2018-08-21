### Shift Registers

Serial-In Serial-Out (SISO) shift register.
```
# SISO :: I:In(Bit), O:Out(Bit)
SISO(n, init=1, has_ce=False, has_reset=False)
```

Serial-In Parallel-Out (SIPO) shift register.
```
# SIPO :: I:In(Bit), O:Out(Bits(n)) 
SIPO(n, init=1, has_ce=False, has_reset=False)
```

Parallel-In Serial-Out (PISO) shift register.
```
# PISO :: SI:In(Bit), PI:In(Bits(n)), LOAD:In(Bit), O:Out(Bits(n))
PISO(n, init=1, has_ce=False, has_reset=False, has_set=False)
```

Parallel-In Parallel-Out (PIPO) shift register.
```
# PIPO :: SI:In(Bit, PI:In(Bits(n)), LOAD:In(Bit), O:Out(Bit)
PIPO(n, init=1, has_ce=False, has_reset=False)
```

### Ring Counter

```
# Ring :: O:Out(Bits(n))
Ring(n, init=1, has_ce=False, has_reset=False)
```

### Johnson Counter

```
# Johnson :: O:Out(Bits(n))
Johnson(n, init=1, has_ce=False, has_reset=False)
```

