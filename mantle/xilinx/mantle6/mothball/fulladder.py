from magma import *
from ..spartan6.CLB import CARRY
from ..spartan6.LUT import LUT5x2

__all__ = ['FullAdder']

#
# return I0, ..., In, CIN -> O, COUT
#
def FullCarry(k, expr6, expr5):

    assert k <= 5

    lut = LUT5x2(expr5, expr6)

    args = []

    if k >= 1:
        args += ['input I0', lut.I0]
    else:
        wire(1, lut.I0)
    if k >= 2:
        args += ['input I1', lut.I1]
    else:
        wire(1, lut.I1)
    if k >= 3:
        args += ['input I2', lut.I2]
    else:
        wire(1, lut.I2)
    if k >= 4:
        args += ['input I3', lut.I3]
    else:
        wire(1, lut.I3)
    if k >= 5:
        args += ['input I4', lut.I4]
    else:
        wire(1, lut.I4)

    CIN = Bit()

    O, COUT = CARRY(lut.O6, lut.O5, CIN)

    args += [ "output O",    O,
              "input CIN",   CIN,
              "output COUT", COUT ]

    return AnonymousCircuit( args )

def FullAdder():
    pass

