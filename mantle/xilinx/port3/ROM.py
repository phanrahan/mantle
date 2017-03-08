from collections import Sequence
from magma import *
from magma.compatibility import IntegerTypes
from parts.xilinx.spartan3.primitives.CLB import MUXF5, MUXF6, MUXF7, MUXF8
from mantle.xilinx.port3.LUT import *

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
    if isinstance(rom, IntegerTypes):
        rom = int2seq(rom, 32)
    I = In(Array5)()
    lut = fork( ROM4(rom[ 0:16]), ROM4(rom[16:32]) )
    lut(I[0:4])
    mux = MUXF5()
    mux(lut.O[0], lut.O[1], I[4])
    return AnonymousCircuit("I", I, "O", mux.O)

def ROM6(rom, **kwargs):
    if isinstance(rom, IntegerTypes):
        rom = int2seq(rom, 64)
    I = In(Array6)()
    lut = fork( ROM5(rom[ 0:32]), ROM5(rom[32:64]))
    mux = MUXF6()
    lut(I[0:5])
    mux(lut.O[0], lut.O[1], I[5])
    return AnonymousCircuit("I", I, "O", mux.O)

def ROM7(rom, **kwargs):
    if isinstance(rom, IntegerTypes):
        rom = int2seq(rom, 128)
    I = In(Array7)()
    lut = fork( ROM6(rom[ 0:64]), ROM6(rom[64:128]))
    mux = MUXF7()
    lut(I[0:6])
    mux(lut.O[0], lut.O[1], I[6])
    return AnonymousCircuit("I", I, "O", mux.O)

def ROM8(rom, **kwargs):
    if isinstance(rom, IntegerTypes):
        rom = int2seq(rom, 256)
    I = In(Array8)()
    lut = fork( ROM7(rom[ 0:128]), ROM7(rom[128:256]))
    mux = MUXF8()
    lut(I[0:7])
    mux(lut.O[0], lut.O[1], I[7])
    return AnonymousCircuit("I", I, "O", mux.O)

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
    """
    n-bit ROM

    I[n] -> n
    """
    return ROMN(rom, **kwargs)


def _ROMName(name, n):
    return name + '%d' % n

ROMCache = {}

def DefineROM16xN(rom):
    """
    Construct a 16 entry ROM of arbitrary width.

    rom[16][w]
    """
    assert(len(rom) == 16)
    # transpose - rom must be a sequence of sequences
    rom = list(zip(*rom))
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

def ROM16xN(rom, **kwargs):
    return DefineROM16xN(rom)(**kwargs)
