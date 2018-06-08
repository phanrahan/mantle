from collections import Sequence
from magma import *
from ..spartan6.CLB import MUXCY, A0, A1, ZERO, ONE
from ..spartan6.LUT import LUT5x2

__all__ = ['Cascade', 'DefineCascade']

def _Name(n, k, expr1, expr2, cin):
    assert not isinstance(expr1, Sequence)
    #if isinstance(expr1, Sequence):
    #    expr1 = seq2int(expr1)
    expr1 = uint(expr1, 1<<k)
    expr2 = uint(expr2, 1<<k)
    return 'Cascade%dx%d_%X_%X_%d' % (n, k, expr1, expr2, cin)

# k is the number of input bits
# expr1 is what goes into the LUT
# expr2 is what goes into DIN
#
def FullCascade(k, expr6, expr5):

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

    mux = MUXCY()
    wire(lut.O6, mux.S)
    wire(lut.O5, mux.DI)
    wire(CIN,    mux.CI)

    args += ["output COUT", mux.O, "input CIN", CIN]
    return AnonymousCircuit( args )


def DefineCascade(n, k, expr1, expr2, cin, forkargs=[]):

    ArrayN = Array(n,Bit)
    args = []
    if k >= 1: args += ["input I0", Bit if 'I0' in forkargs else ArrayN]
    if k >= 2: args += ["input I1", Bit if 'I1' in forkargs else ArrayN]
    if k >= 3: args += ["input I2", Bit if 'I2' in forkargs else ArrayN]
    if k >= 4: args += ["input I3", Bit if 'I3' in forkargs else ArrayN]
    args += ["output O", Bit]

    class _Cascade(Circuit):
        name = _Name(n, k, expr1, expr2, cin)
        IO = args

        @classmethod
        def definition(carry):

            def f(y):
                return FullCascade(k, expr1, expr2)

            c = braid( col(f, n), foldargs={"CIN":"COUT"}, forkargs=forkargs)

            if k >= 1: wire(carry.I0, c.I0)
            if k >= 2: wire(carry.I1, c.I1)
            if k >= 3: wire(carry.I2, c.I2)
            if k >= 4: wire(carry.I3, c.I3)
            wire(c.COUT, carry.O)
            wire(cin, c.CIN)

    return _Cascade

def Cascade(n, k, expr1, expr2, cin, forkargs={}):
    return DefineCascade(n, k, expr1, expr2, cin, forkargs)()

