from magma import *
import types
from magma.bitutils import lutinit, int2seq
from magma.compatibility import IntegerTypes
from .CLB import _LUT6x2

__all__ = ['LUT6x2', 'LUT5x2']

# rom5 is for O5
# rom6 is for O6
def LUT6x2(rom5, rom6):
    if isinstance(rom5, types.FunctionType):
        rom5 = fun2seq(rom5, 32)
    if isinstance(rom5, IntegerTypes):
        rom5 = int2seq(rom5, 32)

    if isinstance(rom6, types.FunctionType):
        rom6 = fun2seq(rom6, 32)
    if isinstance(rom6, IntegerTypes):
        rom6 = int2seq(rom6, 32)

    lut = _LUT6x2(INIT=lutinit(rom5+rom6,1<<6))

    return AnonymousCircuit("I0", lut.I0,
                   "I1", lut.I1,
                   "I2", lut.I2,
                   "I3", lut.I3,
                   "I4", lut.I4,
                   "I5", lut.I5,
                   "O5", lut.O5,
                   "O6", lut.O6)

def LUT5x2(rom1, rom2):
    lut = LUT6x2(rom1, rom2)
    wire(1, lut.I5)
    return AnonymousCircuit("I0", lut.I0,
                   "I1", lut.I1,
                   "I2", lut.I2,
                   "I3", lut.I3,
                   "I4", lut.I4,
                   "O5", lut.O5,
                   "O6", lut.O6)

