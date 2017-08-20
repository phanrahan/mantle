# Mantle

### Shift Registers
```
# SISO :: I:In(Bit), O:Out(Bit)
SISO(n, init=1, has_ce=False, has_reset=False, has_set=False)
```

```
# SIPO :: I:In(Bit), O:Out(Bits(n)) 
SIPO(n, init=1, has_ce=False, has_reset=False, has_set=False)
```

```
# PISO :: SI:In(Bit), PI:In(Bits(n)), LOAD:In(Bit), O:Out(Bits(n))
PISO(n, init=1, has_ce=False, has_reset=False, has_set=False)
```

```
# PIPO :: SI:In(Bit, PI:In(Bits(n)), LOAD:In(Bit), O:Out(Bit)
PIPO(n, init=1, has_ce=False, has_reset=False, has_set=False)
```

## Ring

```
# Ring :: O:Out(Bits(n))
Ring(n, init=1, has_ce=False, has_reset=False, has_set=False)
```

# Johnson Counter

```
# Johnson :: O:Out(Bits(n))
Johnson(n, init=1, has_ce=False, has_reset=False, has_set=False)
```

