from magma import *
from .register import _RegisterName, FFs

__all__  = ['DefineRing', 'Ring']

def DefineRing(n, init=1, has_ce=False, has_reset=False):
    """
    Generate a n-bit ring counter.

    O : Out(Bits(n))
    """
    class Ring(Circuit):
        name = _RegisterName('Ring', n, init, has_ce, has_reset)
        IO = ['O', Out(Bits[ n ])] + ClockInterface(has_ce,has_reset)
        @classmethod
        def definition(ring):
            ffs = FFs(n, init=init, has_ce=has_ce, has_reset=has_reset)
            reg = scan(ffs, scanargs={"I":"O"})
            reg(reg.O[n-1])
            wire(reg.O, ring.O)
            wireclock(ring, reg)
    return Ring

def Ring(n, init=1, has_ce=False, has_reset=False, **kwargs):
    return DefineRing(n, init, has_ce, has_reset)(**kwargs)
