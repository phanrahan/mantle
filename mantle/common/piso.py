from magma import *
from mantle import Mux
from .register import _RegisterName, Register, FFs

__all__ = ['DefinePISO', 'PISO']

def DefinePISO(n, init=0, has_ce=False, has_reset=False):
    """
    Generate Parallel-In, Serial-Out shift register.

    SI : In(Bit), PI : Out(Bits(n)), LOAD : In(Bit), O : Out(Bit)
    """

    T = Bits[ n ]
    class _PISO(Circuit):
        name = _RegisterName('PISO', n, init, has_ce, has_reset)
        IO = ['SI', In(Bit), 'PI', In(T), 'LOAD', In(Bit),
              'O', Out(Bit)] + ClockInterface(has_ce,has_reset)
        @classmethod
        def definition(piso):
            def mux2(y):
                return curry(Mux(2), prefix='I')

            mux = braid(col(mux2, n), forkargs=['S'])
            reg = Register(n, init, has_ce=has_ce, has_reset=has_reset)

            #si = array(*[piso.SI] + [reg.O[i] for i in range(n-1)])
            si = concat(array(piso.SI),reg.O[0:n-1])
            mux(si, piso.PI, piso.LOAD)
            reg(mux)
            wire(reg.O[n-1], piso.O)
            wireclock(piso, reg)

    return _PISO

def PISO(n, init=0, has_ce=False, has_reset=False, **kwargs):
    return DefinePISO(n, init, has_ce, has_reset)(**kwargs)

