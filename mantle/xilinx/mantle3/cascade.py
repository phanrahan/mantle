from collections import Sequence
from magma import *
from ..spartan3.CLB import MUXCY, ANDCY, A0, A1, ZERO, ONE
from .LUT import LUTN

__all__ = ['DefineCascade', 'Cascade']

def _Name(n, k, expr1, expr2, cin):
    assert not isinstance(expr1, Sequence)
    #if isinstance(expr1, Sequence):
    #    expr1 = seq2int(expr1)

    expr1 = uint(expr1, 1<<k)
    expr2 = uint(expr2, 1<<k)
    return 'Cascade%dx%d_%X_%X_%d' % (n, k, expr1, expr2, cin)

#
# create an And/NAnd gate from MUXCY
#
#  cout = MUXCY( expr2, cin, LUTN(expr1, k) )
#
# k is the number of input bits
# expr1 is what goes into the LUT
# expr2 is what goes into DIN
#   A0
#   A1
#   A0&A1
#   ZERO
#   ONE
#
# I0 : Bit, ..., Ik : Bit, CIN : Bit -> COUT : BIT
#
def FullCascade(k, expr1, expr2):

    assert k <= 4

    lut = LUTN(expr1, k)

    args = []
    if k >= 1:
         I0 = Bit()
         wire(I0, lut.I0)
         args += ['input I0', I0]
    if k >= 2:
         I1 = Bit()
         wire(I1, lut.I1)
         args += ['input I1', I1]
    if k >= 3: args += ['input I2', lut.I2]
    if k >= 4: args += ['input I3', lut.I3]


    if expr2 == A0&A1:
       and1 = ANDCY()
       wire(I0, and1.I0)
       wire(I1, and1.I1)
       DI = and1.LO
    elif expr2 == A0:
       DI = I0
    elif expr2 == A1:
       DI = I1
    elif expr2 == ZERO:
       DI = 0
    elif expr2 == ONE:
       DI = 1

    CIN = Bit()

    mux = MUXCY()
    wire(lut.O, mux.S)
    wire(DI,    mux.DI)
    wire(CIN,   mux.CI)

    args += ["output COUT", mux.O, "input CIN", CIN]
    return AnonymousCircuit( args )


#
# k is the number of input bits per unit
# n is the number of units 
# expr1 goes into LUT
# expr2 goes into DIN

# cin is a constant carry in: 0 or 1
#
# the inputs are either forked or joined, depending on forkargs
#  I0 : Bit/Array(n,Bit), ..., Ik : Bit/Array(n,Bit) -> O : Bit
#
def DefineCascade(n, k, expr1, expr2, cin, forkargs={}):

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

            c = braid( col(f, n), foldargs={"CIN":"COUT"}, forkargs=forkargs )

            if k >= 1: wire(carry.I0, c.I0)
            if k >= 2: wire(carry.I1, c.I1)
            if k >= 3: wire(carry.I2, c.I2)
            if k >= 4: wire(carry.I3, c.I3)
            wire(c.COUT, carry.O)
            wire(cin, c.CIN)

    return _Cascade

def Cascade(n, k, expr1, expr2, cin, forkargs={}):
    return DefineCascade(n, k, expr1, expr2, cin, forkargs)()


