from magma import *
from magma.compatibility import IntegerTypes
from magma.bitutils import int2seq, seq2int
from mantle import FF
from collections.abc import Sequence

__all__  = ['FFs']

__all__ += ['Register', 'DefineRegister', 'register']

__all__ += ['_RegisterName']

#
# Create a column of n FFs initialized to init
#
# Each FF may have a ce, r, and s signal.
#
def FFs(n, init=0, has_ce=False, has_reset=False, has_async_reset=False):
    if isinstance(init, IntegerTypes):
        init = int2seq(init, n)

    def f(y):
        if mantle_target == "coreir":
            return FF(init[y], has_ce=has_ce, has_reset=has_reset, has_async_reset=has_async_reset)
        else:
            if has_async_reset:
                raise NotImplementedError()
            return FF(init[y], has_ce=has_ce, has_reset=has_reset)

    return col(f, n)

## Register module name
def _RegisterName(name, n, init, ce, r):
    name += str(n)
    if ce: name += 'CE'
    if r:  name += 'R'

    if isinstance(init, Sequence):
         init = seq2int(init)
    if init is not 0: name += "_%04X" % init

    return name


def DefineRegister(n, init=0, has_ce=False, has_reset=False, has_async_reset=False, _type=Bits):
    """
    Generate an n-bit register

    Params
    ------
        `_type` - Bits, UInt, or SInt

    Interface
    ---------
        I : In(_type(n)), O : Out(_type(n))
    """
    if _type not in {Bits, UInt, SInt}:
        raise ValueError("Argument _type must be Bits, UInt, or SInt")
    T = _type[n]
    class _Register(Circuit):
        name = _RegisterName('Register', n, init, has_ce, has_reset)
        IO  = ['I', In(T), 'O', Out(T)] + ClockInterface(has_ce=has_ce,has_reset=has_reset,has_async_reset=has_async_reset)
        @classmethod
        def definition(reg):
            ffs = join(FFs(n, init, has_ce, has_reset, has_async_reset))
            wire(reg.I, ffs.I)
            wire(ffs.O, reg.O)
            wireclock(reg, ffs)
            wiredefaultclock(reg, ffs)
    return _Register

def Register(n, init=0, has_ce=False, has_reset=False, has_async_reset=False, _type=Bits, **kwargs):
    return DefineRegister(n, init, has_ce, has_reset, has_async_reset, _type)(**kwargs)

def register(I, ce=None, reset=None, async_reset=None, **kwargs):
    has_ce = ce is not None
    has_reset = reset is not None
    has_async_reset = async_reset is not None
    reg = Register(len(I),
                   has_ce=has_ce,
                   has_reset=has_reset,
                   has_async_reset=has_async_reset,
                   **kwargs)
    reg(I)
    if has_ce:
        wire(ce, reg.CE)
    if has_reset:
        wire(reset, reg.RESET)
    if has_async_reset:
        wire(reset, reg.ASYNCRESET)

