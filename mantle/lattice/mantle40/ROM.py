from collections import Sequence
from magma import *
from .LUT import LUT1, LUT2, LUT3, LUT4, LUT5, LUT6, LUT7, LUT8

__all__  = ['ROM1', 'ROM2', 'ROM3', 'ROM4']
__all__ += ['ROM5', 'ROM6', 'ROM7', 'ROM8']
__all__ += ['ROMN', 'ROM']

__all__ += ['ROM16xN']

# Move the lutinit function to Circuit init
def ROM1(rom, **kwargs):
    I = In(Array1)()
    lut = LUT1(rom, **kwargs)
    lut(I[0])
    return AnonymousCircuit("I", I, "O", lut.O)

def ROM2(rom, **kwargs):
    I = In(Array2)()
    lut = LUT2(rom, **kwargs)
    lut(I[0], I[1])
    return AnonymousCircuit("I", I, "O", lut.O)

def ROM3(rom, **kwargs):
    I = In(Array3)()
    lut = LUT3(rom, **kwargs)
    lut(I[0], I[1], I[2])
    return AnonymousCircuit("I", I, "O", lut.O)

def ROM4(rom, **kwargs):
    I = In(Array4)()
    lut = LUT4(rom, **kwargs)
    lut(I[0], I[1], I[2], I[3])
    return AnonymousCircuit("I", I, "O", lut.O)

def ROM5(rom, **kwargs):
    I = In(Array5)()
    lut = LUT5(rom, **kwargs)
    lut(I[0], I[1], I[2], I[3], I[4])
    return AnonymousCircuit("I", I, "O", lut.O)

def ROM6(rom, **kwargs):
    I = In(Array6)()
    lut = LUT6(rom, **kwargs)
    lut(I[0], I[1], I[2], I[3], I[4], I[5])
    return AnonymousCircuit("I", I, "O", lut.O)

def ROM7(rom, **kwargs):
    I = In(Array7)()
    lut = LUT7(rom, **kwargs)
    lut(I[0], I[1], I[2], I[3], I[4], I[5], I[6])
    return AnonymousCircuit("I", I, "O", lut.O)

def ROM8(rom, **kwargs):
    I = In(Array8)()
    lut = LUT8(rom, **kwargs)
    lut(I[0], I[1], I[2], I[3], I[4], I[5], I[6], I[7])
    return AnonymousCircuit("I", I, "O", lut.O)


#
# create a ROM with n entries and initialize if to the comtents of rom
#
# if n is None: n = lem(rom)
#
def ROMN(rom, n=None, **kwargs):
    """
    n-bit LUT

    I[n] -> n
    """

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

def ROM(rom, **kwargs):
    return ROMN(rom, **kwargs)

ROMCache = {}

def DefineROM16xN(rom):
    """
    Construct a 16 entry ROM of arbitrary width.

    rom[16][w]
    """
    assert(len(rom) == 16)
    # transpose - rom must be a sequence of sequences
    rom = zip(*rom)
    n = len(rom)

    # could be different memory contents ...
    name = _ROMName('ROM16x', n)
    if name in ROMCache:
        return ROMCache[name]

    args = ['I', In(Array4), 'O', Out(Array(n, Bit))]

    define = DefineCircuit(name, *args)

    def ROM(y):
        return ROM4(rom[y])

    rom = fork(col(ROM, n))

    rom(define.I)
    wire(rom.O, define.O)

    EndCircuit()

    ROMCache[name] = define
    return define

#
# Create a 16xN ROM
#
def ROM16xN(rom):
    return DefineROM16xN(rom)(**kwargs)
