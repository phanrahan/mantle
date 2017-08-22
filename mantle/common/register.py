from magma import *
from magma.compatibility import IntegerTypes
from magma.bitutils import int2seq
from mantle import FF
from collections import Sequence

__all__  = ['FFs']

__all__ += ['Register', 'DefineRegister']
__all__ += ['_RegisterName']

#
# Create a column of n FFs initialized to init
#
# Each FF may have a ce, r, and s signal.
#
def FFs(n, init=0, has_ce=False, has_reset=False, has_set=False):
    if isinstance(init, IntegerTypes):
        init = int2seq(init, n)

    def f(y):
        return FF(init[y], has_ce=has_ce, has_reset=has_reset, has_set=has_set)

    return col(f, n)

## Register module name
def _RegisterName(name, n, init, ce, r, s):
    name += str(n)
    if ce: name += 'CE'
    if r:  name += 'R'
    if s:  name += 'S'

    if isinstance(init, Sequence):
         init = seq2int(init)
    if init is not 0: name += "_%04X" % init

    return name


def DefineRegister(n, init=0, has_ce=False, has_reset=False, has_set=False, _type=Bits):
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
    T = _type(n)
    class _Register(Circuit):
        name = _RegisterName('Register', n, init, has_ce, has_reset, has_set)
        IO  = ['I', In(T), 'O', Out(T)] + ClockInterface(has_ce,has_reset,has_set)
        @classmethod
        def definition(reg):
            ffs = join(FFs(n, init, has_ce, has_reset, has_set))
            wire(reg.I, ffs.I)
            wire(ffs.O, reg.O)
            wireclock(reg, ffs)
    return _Register

def Register(n, init=0, has_ce=False, has_reset=False, has_set=False, **kwargs):
    return DefineRegister(n, init, has_ce, has_reset, has_set)(**kwargs)

