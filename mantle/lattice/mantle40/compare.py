from magma import *
from ..ice40.PLB import A0, A1, A2, A3
from .cascade import Cascade
from .LUT import *
from .arith import Sub
from .logic import Not

__all__  = ['EQ', 'NE']
__all__ += ['ULT', 'ULE', 'UGT', 'UGE']
#__all__ += ['LT',  'LE',  'GT',  'GE']

EQ1LUT = ((A0&A1)|(~A0&~A1))
EQ2LUT = ((A0&A1)|(~A0&~A1)) & ((A2&A3)|(~A2&~A3))

def EQ1(**kwargs):
    """Test equality of 2 1-bit inputs."""
    return LUT2(EQ1LUT, **kwargs)

def EQ2(**kwargs):
    """Test equality of 2 2-bit inputs."""
    lut = LUT4(EQ2LUT, **kwargs)
    return AnonymousCircuit('I0', array(lut.I0, lut.I2),
                            'I1', array(lut.I1, lut.I3),
                            'O', lut.O)

def EQ(n, **kwargs):
    if n == 1:
        return EQ1(**kwargs)
    if n == 2:
        return EQ2(**kwargs)
    return Cascade(n, 2, A0&((A1&A2)|(~A1&~A2)), 1, **kwargs)


NE1LUT = (A0^A1)
NE2LUT = (A0^A1)|(A2^A3)

def NE1(**kwargs):
    """Test non-equality of 2 1-bit inputs."""
    return LUT2(NE1LUT, **kwargs)

def NE2(**kwargs):
    """Test non-equality of 2 2-bit inputs."""
    lut = LUT4(NE2LUT, **kwargs)
    return AnonymousCircuit('I0', array(lut.I0, lut.I2),
                            'I1', array(lut.I1, lut.I3),
                            'O', lut.O)

def NE(n, **kwargs):
    if n == 1:
        return NE1(**kwargs)
    if n == 2:
        return NE2(**kwargs)
    return Cascade(n, 2, A0|(A1^A2), 0, **kwargs)


def ULT(n, **kwargs):
    not_ = Not()
    uge = UGE(n, **kwargs)
    return compose(not_, uge)

def ULE(n, **kwargs):
    sub = Sub(n, **kwargs)
    return AnonymousCircuit("I0", sub.I1, "I1", sub.I0, "O", sub.COUT)

def UGT(n, **kwargs):
    not_ = Not()
    ule = ULE(n, **kwargs)
    return compose(not_, ule)

def UGE(n, **kwargs):
    sub = Sub(n, **kwargs)
    return AnonymousCircuit("I0", sub.I0, "I1", sub.I1, "O", sub.COUT)


def LT(n, **kwargs):
    return None

def LE(n, **kwargs):
    return None

def GT(n, **kwargs):
    return None

def GE(n, **kwargs):
    return None

