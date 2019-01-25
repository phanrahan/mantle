from magma import *
from .register import _RegisterName, FFs

__all__ = ['DefineSISO', 'SISO']

def DefineSISO(n, init=0, has_ce=False, has_reset=False):
    """
    Generate Serial-In, Serial-Out shift register.

    I : In(Bit), O : Out(Bit)
    """

    class _SISO(Circuit):
        name = _RegisterName('SISO', n, init, has_ce, has_reset)
        IO = ['I', In(Bit), 'O', Out(Bit)] + \
               ClockInterface(has_ce,has_reset)
        @classmethod
        def definition(siso):
            ffs = FFs(n, init=init, has_ce=has_ce, has_reset=has_reset)
            reg = braid(ffs, foldargs={"I":"O"})
            reg(siso.I)
            wire(reg.O, siso.O)
            wireclock(siso, reg)
            wiredefaultclock(siso, reg)
    return _SISO

def SISO(n, init=0, has_ce=False, has_reset=False, **kwargs):
    return DefineSISO(n, has_ce=has_ce, has_reset=has_reset)(**kwargs)
