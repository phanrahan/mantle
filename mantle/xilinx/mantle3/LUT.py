from collections.abc import Sequence
from magma import *
from magma.bitutils import lutinit, int2seq
from magma.compatibility import IntegerTypes
from ..spartan3.CLB import *

__all__  = ['LUT1', 'LUT2', 'LUT3', 'LUT4']
__all__ += ['LUT5', 'LUT6', 'LUT7', 'LUT8']
__all__ += ['LUT']
__all__ += ['A0', 'A1', 'A2', 'A3', 'ZERO', 'ONE']

def LUT1(rom, **kwargs):
    return _LUT1(INIT=lutinit(rom,1<<1), **kwargs)

def LUT2(rom, **kwargs):
    return _LUT2(INIT=lutinit(rom,1<<2), **kwargs)

def LUT3(rom, **kwargs):
    return _LUT3(INIT=lutinit(rom,1<<3), **kwargs)

def LUT4(rom, **kwargs):
    return _LUT4(INIT=lutinit(rom,1<<4), **kwargs)

def LUT5(rom, **kwargs):
    if isinstance(rom, IntegerTypes):
        rom = int2seq(rom, 32)
    I0, I1, I2, I3, I4 = Bit(), Bit(), Bit(), Bit(), Bit()
    lut = fork( LUT4(rom[ 0:16]), LUT4(rom[16:32]) )
    lut(I0, I1, I2, I3)
    mux = MUXF5()
    mux(lut.O[0], lut.O[1], I4)
    return AnonymousCircuit("I0", I0, 
                            "I1", I1,
                            "I2", I2,
                            "I3", I3,
                            "I4", I4,
                            "O", mux.O)

def LUT6(rom, **kwargs):
    if isinstance(rom, IntegerTypes):
        rom = int2seq(rom, 64)
    I0, I1, I2, I3, I4, I5 = Bit(), Bit(), Bit(), Bit(), Bit(), Bit()
    lut = fork( LUT5(rom[ 0:32]), LUT5(rom[32:64]))
    mux = MUXF6()
    lut(I0, I1, I2, I3, I4)
    mux(lut.O[0], lut.O[1], I5)
    return AnonymousCircuit("I0", I0, 
                            "I1", I1,
                            "I2", I2,
                            "I3", I3,
                            "I4", I4,
                            "I5", I5,
                            "O", mux.O)

def LUT7(rom, **kwargs):
    if isinstance(rom, IntegerTypes):
        rom = int2seq(rom, 128)
    I0, I1, I2, I3, I4, I5, I6 = Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit()
    lut = fork( LUT6(rom[ 0:64]), LUT6(rom[64:128]))
    mux = MUXF7()
    lut(I0, I1, I2, I3, I4, I5)
    mux(lut.O[0], lut.O[1], I6)
    return AnonymousCircuit("I0", I0, 
                            "I1", I1,
                            "I2", I2,
                            "I3", I3,
                            "I4", I4,
                            "I5", I5,
                            "I6", I6,
                            "O", mux.O)

def LUT8(rom, **kwargs):
    if isinstance(rom, IntegerTypes):
        rom = int2seq(rom, 256)
    I0, I1, I2, I3, I4, I5, I6, I7 = Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit(), Bit()
    lut = fork( LUT7(rom[ 0:128]), LUT7(rom[128:256]))
    mux = MUXF8()
    lut(I0, I1, I2, I3, I4, I5, I6)
    mux(lut.O[0], lut.O[1], I7)
    return AnonymousCircuit("I0", I0, 
                            "I1", I1,
                            "I2", I2,
                            "I3", I3,
                            "I4", I4,
                            "I5", I5,
                            "I6", I6,
                            "I7", I7,
                            "O", mux.O)


def LUT(rom, n=None, **kwargs):
    """
    n-bit LUT

    I[n] -> n
    """

    if n is not None:
        n = 1 << n

    if isinstance(rom, Sequence):
        if n is None:
            n = len(rom)
        else:
            assert n == len(rom)

    assert n is not None

    if n == 2:
        return LUT1(rom, **kwargs)
    if n == 4:
        return LUT2(rom, **kwargs)
    if n == 8:
        return LUT3(rom, **kwargs)
    if n == 16:
        return LUT4(rom, **kwargs)
    if n == 32:
        return LUT5(rom, **kwargs)
    if n == 64:
        return LUT6(rom, **kwargs)
    if n == 128:
        return LUT7(rom, **kwargs)
    if n == 256:
        return LUT8(rom, **kwargs)

    return None

