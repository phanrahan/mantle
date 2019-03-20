from magma import *
from mantle import Mux
from .register import _RegisterName, Register

__all__ = ['DefinePIPO', 'PIPO']

def DefinePIPO(n, init=0, has_ce=False, has_reset=False):
    """
    Generate Parallel-In, Parallel-Out shift register.

    SI : In(Bit), PI : In(Bits(n)), LOAD : Bit, O : Out(Bits(n))
    """

    T = Bits[ n ]
    class _PIPO(Circuit):
        name = _RegisterName('PIPO', n, init, has_ce, has_reset)
        IO = ['SI', In(Bit), 'PI', In(T), 'LOAD', In(Bit),
              'O', Out(T)] + ClockInterface(has_ce,has_reset)
        @classmethod
        def definition(pipo):
            def mux2(y):
                return curry(Mux(2), prefix='I')

            mux = braid(col(mux2, n), forkargs=['S'])
            reg = Register(n, init=init, has_ce=has_ce, has_reset=has_reset)

            #si = array([pipo.SI] + [reg.O[i] for i in range(n-1)])
            si = concat(array(pipo.SI),reg.O[0:n-1])
            mux(si, pipo.PI, pipo.LOAD)
            reg(mux)
            wire(reg.O, pipo.O)
            wireclock(pipo, reg)

    return _PIPO

def PIPO(n, init=0, has_ce=False, has_reset=False, **kwargs):
    return DefinePIPO(n, init, has_ce, has_reset)(**kwargs)

