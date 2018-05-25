from magma import *
from ..spartan6.CLB import *
from .LUT import *
from .cascade import Cascade

__all__  = ['EQ', 'NE']
__all__ += [ 'LT',  'LE',  'GT',  'GE']
__all__ += ['ULT', 'ULE', 'UGT', 'UGE']

EQ1LUT = ((A0&A1)|(~A0&~A1))
EQ2LUT = ((A0&A1)|(~A0&~A1)) & ((A2&A3)|(~A2&~A3))
EQ3LUT = ((A0&A1)|(~A0&~A1)) & ((A2&A3)|(~A2&~A3)) & ((A4&A5)|(~A4&~A5))

def EQ1():
    """Test equality of 2 1-bit inputs."""
    return LUT2(EQ1LUT)

def EQ2():
    """Test equality of 2 2-bit inputs."""
    lut = LUT4(EQ2LUT)
    return AnonymousCircuit('I0', array(lut.I0, lut.I2),
                            'I1', array(lut.I1, lut.I3),
                            'O', lut.O)

def EQ3():
    """Test equality of 3 2-bit inputs."""
    lut = LUT6(EQ3LUT)
    return AnonymousCircuit('I0', array(lut.I0, lut.I2, lut.I4),
                            'I1', array(lut.I1, lut.I3, lut.I5),
                            'O', lut.O)

def EQ(n):
    if n == 1:
        return EQ1()
    if n == 2:
        return EQ2()
    if n == 3:
        return EQ3()
    return Cascade(n, 2, EQ1LUT, ZERO, 1)


NE1LUT = (A0^A1)
NE2LUT = (A0^A1)|(A2^A3)
NE3LUT = (A0^A1)|(A2^A3)|(A4^A5)

def NE1():
    """Test non-equality of 2 1-bit inputs."""
    return LUT2(NE1LUT)

def NE2():
    """Test non-equality of 2 2-bit inputs."""
    lut = LUT4(NE2LUT)
    return AnonymousCircuit('I0', array(lut.I0, lut.I2),
                            'I1', array(lut.I1, lut.I3),
                            'O', lut.O)

def NE3():
    """Test non-equality of 3 2-bit inputs."""
    lut = LUT6(NE3LUT)
    return AnonymousCircuit('I0', array(lut.I0, lut.I2, lut.I4),
                            'I1', array(lut.I1, lut.I3, lut.I5),
                            'O', lut.O)

def NE(n):
    if n == 1:
        return NE1()
    if n == 2:
        return NE2()
    if n == 3:
        return NE3()
    return Cascade(n, 2, EQ1LUT, ONE, 0)


def ULT(n):
    return Cascade(n, 2, EQ1LUT, I1, 0)

def ULE(n):
    return Cascade(n, 2, EQ1LUT, I1, 1)

def UGT(n):
    return Cascade(n, 2, EQ1LUT, I0, 0)

def UGE(n):
    return Cascade(n, 2, EQ1LUT, I0, 1)

LT = ULT
LE = ULE
GT = UGT
GE = UGE

