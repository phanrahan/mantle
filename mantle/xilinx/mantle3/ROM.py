from collections.abc import Sequence
from magma import *
from magma.bitutils import int2seq
from magma.compatibility import IntegerTypes
from ..spartan3.CLB import MUXF5, MUXF6, MUXF7, MUXF8
from .LUT import *

__all__  = ['ROM1', 'ROM2', 'ROM3', 'ROM4']
__all__ += ['ROM5', 'ROM6', 'ROM7', 'ROM8']
__all__ += ['ROMN']
#__all__ += ['ROM16xN']

# Move the lutinit function to Circuit init
def ROM1(rom, **kwargs):
    return uncurry(LUT1(rom, **kwargs))

def ROM2(rom, **kwargs):
    return uncurry(LUT2(rom, **kwargs))

def ROM3(rom, **kwargs):
    return uncurry(LUT3(rom, **kwargs))

def ROM4(rom, **kwargs):
    return uncurry(LUT4(rom, **kwargs))

def ROM5(rom, **kwargs):
    return uncurry(LUT5(rom, **kwargs))

def ROM6(rom, **kwargs):
    return uncurry(LUT6(rom, **kwargs))

def ROM7(rom, **kwargs):
    return uncurry(LUT7(rom, **kwargs))

def ROM8(rom, **kwargs):
    return uncurry(LUT8(rom, **kwargs))

def ROMN(rom, n=None, **kwargs):
    """
    n-bit LUT

    I[n] -> n
    """

    # rom must be a sequence
    if isinstance(rom, Sequence):
        assert n == len(rom) 
    else:
        assert n is not None
        n = 1 << n

    if n == 2:
        return ROM1(rom, **kwargs)
    if n == 4:
        return ROM2(rom, **kwargs)
    if n == 8:
        return ROM3(rom, **kwargs)
    if n == 16:
        return ROM4(rom, **kwargs)
    if n == 32:
        return ROM5(rom, **kwargs)
    if n == 64:
        return ROM6(rom, **kwargs)
    if n == 128:
        return ROM7(rom, **kwargs)
    if n == 256:
        return ROM8(rom, **kwargs)

    return None

#def ROM(rom, **kwargs):
#    """
#    n-bit ROM
#
#    I[n] -> n
#    """
#    return ROMN(rom, **kwargs)
#
#
#def _ROMName(name, n):
#    return name + '%d' % n
#
#ROMCache = {}
#
#def DefineROM16xN(rom):
#    """
#    Construct a 16 entry ROM of arbitrary width.
#
#    rom[16][w]
#    """
#    assert(len(rom) == 16)
#    # transpose - rom must be a sequence of sequences
#    rom = list(zip(*rom))
#    n = len(rom)
#
#    # could be different memory contents ...
#    name = _ROMName('ROM16x', n)
#    if name in ROMCache:
#        return ROMCache[name]
#
#    args = ['I', In(Array4), 'O', Out(Array(n, Bit))]
#
#    define = DefineCircuit(name, *args)
#
#    def ROM(y):
#        return ROM4(rom[y])
#
#    rom = fork(col(ROM, n))
#
#    rom(define.I)
#    wire(rom.O, define.O)
#
#    EndCircuit()
#
#    ROMCache[name] = define
#    return define
#
#def ROM16xN(rom, **kwargs):
#    return DefineROM16xN(rom)(**kwargs)
