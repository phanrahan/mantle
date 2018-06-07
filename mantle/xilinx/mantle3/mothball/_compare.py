from magma import *
from ..spartan3.CLB import *
from .cascade import Cascade
from .LUT import *

__all__  = ['DefineEQ', 'EQ']
__all__ += ['DefineNE', 'NE']
__all__ += ['DefineUGE', 'UGE']
__all__ += ['DefineULE', 'ULE']
__all__ += ['DefineUGT', 'UGT']
__all__ += ['DefineULT', 'ULT']
__all__ += ['DefineSGE', 'SGE']
__all__ += ['DefineSLE', 'SLE']
__all__ += ['DefineSGT', 'SGT']
__all__ += ['DefineSLT', 'SLT']

EQ1LUT = ((A0&A1)|(~A0&~A1))
EQ2LUT = ((A0&A1)|(~A0&~A1)) & ((A2&A3)|(~A2&~A3))

def EQ1():
    """Test equality of 2 1-bit inputs."""
    return LUT2(EQ1LUT)

def EQ2():
    """Test equality of 2 2-bit inputs."""
    lut = LUT4(EQ2LUT)
    return AnonymousCircuit('I0', bits([lut.I0, lut.I2]),
                            'I1', bits([lut.I1, lut.I3]),
                            'O', lut.O)

def EQ(n):
    if n == 1:
        return EQ1()
    if n == 2:
        return EQ2()
    return Cascade(n, 2, EQ1LUT, ZERO, 1)


NE1LUT = (A0^A1)
NE2LUT = (A0^A1)|(A2^A3)

def NE1():
    """Test non-equality of 2 1-bit inputs."""
    return LUT2(NE1LUT)

def NE2():
    """Test non-equality of 2 2-bit inputs."""
    lut = LUT4(NE2LUT)
    return AnonymousCircuit('I0', bits([lut.I0, lut.I2]),
                            'I1', bits([lut.I1, lut.I3]),
                            'O', lut.O)

def NE(n):
    if n == 1:
        return NE1()
    if n == 2:
        return NE2()
    return Cascade(n, 2, EQ1LUT, ONE, 0)


def ULT(n):
    return Cascade(n, 2, EQ1LUT, I1, 0)

def ULE(n):
    return Cascade(n, 2, EQ1LUT, I1, 1)

def UGT(n):
    return Cascade(n, 2, EQ1LUT, I0, 0)

def UGE(n):
    return Cascade(n, 2, EQ1LUT, I0, 1)


def SLT(n):
    pass

def SLE(n):
    pass

def SGT(n):
    pass

def SGE(n):
    pass

