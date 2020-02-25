from collections.abc import Sequence
from magma import *
from magma.bitutils import lutinit, int2seq
from magma.compatibility import IntegerTypes
from ..spartan6.CLB import *


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
    return _LUT5(INIT=lutinit(rom,1<<5), **kwargs)

def LUT6(rom, **kwargs):
    return _LUT6(INIT=lutinit(rom,1<<6), **kwargs)

def LUT7(rom, **kwargs):
    if isinstance(rom, IntegerTypes):
        rom = int2seq(rom, 128)
    I = Bits[ 7 ]()
    # need to convert rom to a sequence
    lut0 = LUT6(rom[ 0: 64])
    lut1 = LUT6(rom[64:128])
    lut = fork(lut0, lut1)
    lut(I[0], I[1], I[2], I[3], I[4], I[5])
    mux = MUXF7()
    mux(lut.O[0], lut.O[1], I[6])
    return AnonymousCircuit("I0", I[0], 
                   "I1", I[1], 
                   "I2", I[2], 
                   "I3", I[3], 
                   "I4", I[4], 
                   "I5", I[5], 
                   "I6", I[6], 
                   "O", mux.O)

def LUT8(rom, **kwargs):
    if isinstance(rom, IntegerTypes):
        rom = int2seq(rom, 256)
    I = Bits[ 8 ]()
    # need to convert rom to a sequence
    lut0 = LUT7(rom[  0:128])
    lut1 = LUT7(rom[128:256])
    lut = fork(lut0, lut1)
    lut(I[0], I[1], I[2], I[3], I[4], I[5], I[6])
    mux = MUXF8()
    mux(lut.O[0], lut.O[1], I[7])
    return AnonymousCircuit("I0", I[0], 
                   "I1", I[1], 
                   "I2", I[2], 
                   "I3", I[3], 
                   "I4", I[4], 
                   "I5", I[5], 
                   "I6", I[6], 
                   "I7", I[7], 
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
