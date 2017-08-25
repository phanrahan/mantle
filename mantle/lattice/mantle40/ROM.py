from collections import Sequence
from magma import *
from magma.bitutils import lutinit
from .LUT import LUT1, LUT2, LUT3, LUT4, LUT5, LUT6, LUT7, LUT8, A0, A1, A2, A3
from .MUX import Mux2

__all__  = ['ROM1', 'ROM2', 'ROM3', 'ROM4']
__all__ += ['ROM5', 'ROM6', 'ROM7', 'ROM8']
__all__ += ['ROMN']
__all__ += ['DefineROM', 'ROM']

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


#
# create a ROM with n entries and initialize if to the comtents of rom
#
# if n is None: n = lem(rom)
#
def ROMN(rom, height=None, width=None, **kwargs):
    """
    n-bit LUT

    I : In(Bits(n)), O : Bit
    """
    n = height

    # rom must be a sequence
    if isinstance(rom, Sequence):
        assert n is None
        n = len(rom)
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

ROMCache = {}

# Rom Module name
def _ROMName(name, height, width, data):
    return '%s%dx%d_%d' % (name, height, width, abs(hash(__builtin__.tuple(data))))

def DefineROM(rom, height=None, width=8):
    """
    Construct a 16 entry ROM of arbitrary width.

    rom[height][width]
    """
    assert(len(rom) == 16)
    if height is None:
        height = len(rom)
    # transpose - rom must be a sequence of sequences
    rom = zip(*rom)

    # could be different memory contents ...
    name = _ROMName('ROM', width, rom)
    if name in ROMCache:
        return ROMCache[name]

    args = ['I', In(Bits(4)), 'O', Out(Bits(width))]

    define = DefineCircuit(name, *args)

    def ROM(y):
        return ROM4(rom[y])

    rom = fork(col(ROM, width))

    rom(define.I)
    wire(rom.O, define.O)

    EndCircuit()

    ROMCache[name] = define
    return define

#
# Create a 16xN ROM
#
def ROM(rom, height=None, width=8, **kwargs):
    if width is None:
        return ROMN(rom, height=height, **kwargs)
    return DefineROM(rom, height=height, width=width)(**kwargs)
