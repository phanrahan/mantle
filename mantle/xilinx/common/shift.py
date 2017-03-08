from magma import *
from mantle.xilinx.port import FFs, Not, And2, Mux2
from mantle.xilinx.common.register import _RegisterName, Register

__all__  = ['DefineSIPO', 'SIPO']
__all__ += ['DefineSISO', 'SISO']
__all__ += ['DefinePIPO', 'PIPO']
__all__ += ['DefinePISO', 'PISO']

def DefineSIPO(n, init=0, ce=False, r=False, s=False):
    """
    Generate Serial-In, Parallel-Out shift register.

    I : Bit -> O : Array(n, Bit)
    """

    class _SIPO(Circuit):
        name = _RegisterName('SIPO',n, init, ce, r, s)
        IO = ['I', In(Bit), 'O', Out(Array(n,Bit))] + ClockInterface(ce,r,s)
        @classmethod
        def definition(sipo):
            ffs = FFs(n, init=init, ce=ce, r=r, s=s)
            reg = braid(ffs, scanargs={"I":"O"})
            reg(sipo.I)
            wire(reg.O, sipo.O)
            wireclock(sipo, reg)
    return _SIPO

def SIPO(n, init=0, ce=False, r=False, s=False):
    return DefineSIPO(n, init, ce, r, s)()


def DefineSISO(n, init=0, ce=False, r=False, s=False):
    """
    Generate Serial-In, Serial-Out shift register.

    I : Bit -> O : Bit
    """

    class _SISO(Circuit):
        name = _RegisterName('SISO',n, init, ce, r, s)
        IO = ['I', In(Bit), 'O', Out(Bit)] + ClockInterface(ce,r,s)
        @classmethod
        def definition(siso):
            ffs = FFs(n, init=init, ce=ce, r=r, s=s)
            reg = braid(ffs, foldargs={"I":"O"})
            reg(siso.I)
            wire(reg.O, siso.O)
            wireclock(siso, reg)
    return _SISO

def SISO(n, init=0, ce=False, r=False, s=False):
    return DefineSISO(n, init=init, ce=ce, r=r, s=s)()


def DefinePIPO(n, init=0, ce=False, r=False, s=False):
    """
    Generate Parallel-In, Parallel-Out shift register.

    SI : Bit, PI : Array(n, Bit), LOAD : Bit -> O : Array(n, Bit)
    """

    T = Array(n, Bit)
    class _PIPO(Circuit):
        name = _RegisterName('PIPO', n, init, ce, r, s)
        IO = ['SI', In(Bit), 'PI', In(T), 'LOAD', In(Bit),
              'O', Out(T)] + ClockInterface(ce,r,s)
        @classmethod
        def definition(pipo):
            def mux2(y):
                return curry(Mux2(), prefix='I')

            mux = braid(col(mux2, n), forkargs=['S'])
            reg = Register(n, init=init, ce=ce, r=r, s=s)

            si = concat(array(pipo.SI),reg.O[0:n-1])
            mux(si, pipo.PI, pipo.LOAD)
            reg(mux)
            wire(reg.O, pipo.O)
            wireclock(pipo, reg)

    return _PIPO

def PIPO(n, init=0, ce=False, r=False, s=False):
    return DefinePIPO(n, init, ce, r, s)()
    

def DefinePISO(n, init=0, ce=False, r=False, s=False ):
    """
    Generate Parallel-In, Serial-Out shift register.

    SI : Bit, PI : Array(n, Bit), LOAD : Bit -> O : Bit
    """

    T = Array(n, Bit)
    class _PISO(Circuit):
        name = _RegisterName('PISO', n, init, ce, r, s)
        IO = ['SI', In(Bit), 'PI', In(T), 'LOAD', In(Bit),
              'O', Out(Bit)] + ClockInterface(ce,r,s)
        @classmethod
        def definition(piso):
            def mux2(y):
                return curry(Mux2(), prefix='I')

            mux = braid(col(mux2, n), forkargs=['S'])
            reg = Register(n, init=init, ce=ce, r=r, s=s)

            si = concat(array(piso.SI),reg.O[0:n-1])
            mux(si, piso.PI, piso.LOAD)
            reg(mux)
            wire(reg.O[n-1], piso.O)
            wireclock(piso, reg)

    return _PISO

def PISO(n, init=0, ce=False, r=False, s=False):
    return DefinePISO(n, init, ce, r, s)()
    
