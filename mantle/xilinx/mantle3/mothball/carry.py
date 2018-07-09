from magma import *
from ..spartan3.CLB import ANDCY, XORCY, MUXCY
from .LUT import LUTN, A0, A1, ZERO, ONE
from .ROM import ROMN

__all__ = ['HalfCarry', 'FullCarry']

#
# return I0, ..., In, CIN -> O, COUT
#
def halfcarry(k, lutexpr, andexpr, use_rom):

    assert k <= 4
    args = []

    if use_rom:
        lut = ROMN(lutexpr,k)
        args += ['I', lut.I]
        if k >= 1:
            I0 = Bit()
            wire(I0, lut.I[0])
        if k >= 2:
            I1 = Bit()
            wire(I1, lut.I[1])
    else:
        lut = LUTN(lutexpr, k)
        if k >= 1:
            I0 = Bit()
            wire(I0, lut.I0)
            args += ['I0', I0]
        if k >= 2:
            I1 = Bit()
            wire(I1, lut.I1)
            args += ['I1', I1]
        if k >= 3:
            args += ['I2', lut.I2]
        if k >= 4:
            args += ['I3', lut.I3]

    if andexpr == A0 & A1:
        assert k >= 2
        and1 = ANDCY()
        wire(I0, and1.I0)
        wire(I1, and1.I1)
        DI = and1.LO
    elif andexpr == A0:
        assert k >= 1
        DI = I0
    elif andexpr == A1:
        assert k >= 2
        DI = I1
    elif andexpr == ZERO:
        DI = 0
    elif andexpr == ONE:
        DI = 1

    CIN = Bit()

    mux = MUXCY()
    wire(lut.O, mux.S)
    wire(DI,    mux.DI)
    wire(CIN,   mux.CI)

    COUT = mux.O
    O = lut.O

    args += ["CIN", CIN, "O", O, "COUT", COUT]

    return CIN, COUT, O, args 

def fullcarry(k, lutexpr, andexpr, use_rom):

    CIN, COUT, O, args = halfcarry(k, lutexpr, andexpr, use_rom)

    xor = XORCY()
    wire(O,   xor.LI)
    wire(CIN, xor.CI)

    O = xor.O

    return CIN, COUT, O, args


def HalfCarry(k, lutexpr, andexpr, use_rom=False):

    CIN, COUT, O, args = halfcarry(k, lutexpr, andexpr, use_rom)

    return AnonymousCircuit(args)


def FullCarry(k, lutexpr, andexpr, use_rom=False):

    CIN, COUT, O, args = fullcarry(k, lutexpr, andexpr, use_rom)

    return AnonymousCircuit(args)
