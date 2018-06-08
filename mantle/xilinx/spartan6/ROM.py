from magma import *
from .LUT import LUT5x2, LUT6x2

__all__ = ['ROM6x2', 'ROM5x2']

def ROM5x2(rom5, rom6):
    I = In(Bits(5))()
    lut = LUT5X2(rom5, rom6)
    lut(I[0], I[1], I[2], I[3], I[4])
    return AnonymousCircuit("I", I, "O5", lut.O5, "O6", lut.O6)

def ROM6x2(rom5, rom6):
    I = In(Bits(6))()
    lut = LUT6X2(rom5, rom6)
    lut(I[0], I[1], I[2], I[3], I[4], I[5])
    return AnonymousCircuit("I", I, "O5", lut.O5, "O6", lut.O6)

