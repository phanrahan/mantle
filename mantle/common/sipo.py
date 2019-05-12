from magma import *
from .register import _RegisterName, FFs

__all__ = ['DefineSIPO', 'SIPO']

def DefineSIPO(n, init=0, has_ce=False, has_reset=False):
    """
    Generate Serial-In, Parallel-Out shift register.

    I : In(Bits(n),  O : Bits(n)
    """

    class _SIPO(Circuit):
        name = _RegisterName('SIPO', n, init, has_ce, has_reset)
        IO = ['I', In(Bit), 'O', Out(Bits[n])] + \
                ClockInterface(has_ce,has_reset)
        @classmethod
        def definition(sipo):
            ffs = FFs(n, init=init, has_ce=has_ce, has_reset=has_reset)
            reg = scan(ffs, scanargs={"I":"O"})
            reg(sipo.I)
            wire(reg.O, sipo.O)
            wireclock(sipo, reg)
    return _SIPO

def SIPO(n, init=0, has_ce=False, has_reset=False, **kwargs):
    return DefineSIPO(n, init, has_ce, has_reset)(**kwargs)
