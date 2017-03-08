from magma import *
from magma.compatibility import IntegerTypes
from mantle.xilinx.port import FFs

__all__ = ['Register', 'DefineRegister']

## Register module name
def _RegisterName(name, n, init, ce, r, s):
    name += str(n)
    if ce: name += 'CE'
    if r:  name += 'R'
    if s:  name += 'S'

    # fix me
    assert isinstance(init, IntegerTypes)
    if init is not 0: name += "_%s" % init

    return name


def DefineRegister(n, init=0, ce=False, r=False, s=False):
    """
    Generate an n-bit register

    I : Array(n, Bit) -> O : Array(n, Bit)
    """

    T = Array(n, Bit)
    class _Register(Circuit):
        name = _RegisterName('Register', n, init, ce, r, s)
        IO  = ['input I', T, 'output O', T] + ClockInterface(ce,r,s)
        @classmethod
        def definition(reg):
            ffs = join(FFs(n, init, ce, r, s))
            wire(reg.I, ffs.I)
            wire(ffs.O, reg.O)
            wireclock(reg, ffs)
    return _Register

def Register(n, init=0, ce=False, r=False, s=False):
    return DefineRegister(n, init, ce, r, s)()

