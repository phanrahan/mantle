from collections.abc import Sequence
from magma import *

__all__  = ['LUT1', 'LUT2', 'LUT3', 'LUT4']
__all__ += ['LUT5', 'LUT6', 'LUT7', 'LUT8']
__all__ += ['LUT']

def LUT1(rom, **kwargs):
    lut = SB_LUT4(LUT_INIT=lutinit(rom,4),**kwargs)
    wire(0, lut.I1)
    wire(0, lut.I2)
    wire(0, lut.I3)
    return AnonymousCircuit("I0", lut.I0, 
                            "O", lut.O) 

def LUT2(rom, **kwargs):
    lut = SB_LUT4(LUT_INIT=lutinit(rom,4), **kwargs)
    wire(0, lut.I2)
    wire(0, lut.I3)
    return AnonymousCircuit("I0", lut.I0, 
                            "I1", lut.I1, 
                            "O", lut.O) 

def LUT3(rom, **kwargs):
    lut = SB_LUT4(LUT_INIT=lutinit(rom,4), **kwargs)
    wire(0, lut.I3)
    return AnonymousCircuit("I0", lut.I0, 
                            "I1", lut.I1, 
                            "I2", lut.I2, 
                            "O", lut.O) 

def LUT4(rom, **kwargs):
    return SB_LUT4(LUT_INIT=lutinit(rom,4), **kwargs)

def LUT5(rom, **kwargs):
    return None

def LUT6(rom, **kwargs):
    return None

def LUT7(rom, **kwargs):
    return None

def LUT8(rom, **kwargs):
    return None

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

