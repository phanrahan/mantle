from magma import *
from mantle import Not
from .register import _RegisterName, FFs

__all__ = ['DefineJohnson', 'Johnson']

def DefineJohnson(n, has_ce=False, has_reset=False):
    """
    Generate a n-bit johnson counter.

    Walking ring counter / Moebios counter

    O : Out(Bits(n))
    """
    class Johnson(Circuit):
        name = _RegisterName('Johnson', n, 0, has_ce, has_reset)
        IO = ['O', Out(Bits[ n ])] + ClockInterface(has_ce,has_reset)
        @classmethod
        def definition(johnson):
            ffs = FFs(n, has_ce=has_ce, has_reset=has_reset)
            reg = scan(ffs, scanargs={"I":"O"})
            johnson.O(reg(Not()(reg.O[n-1])))
            wireclock(johnson, reg)
    return Johnson

def Johnson(n, has_ce=False, has_reset=False, **kwargs):
    return DefineJohnson(n, has_ce, has_reset)(**kwargs)
