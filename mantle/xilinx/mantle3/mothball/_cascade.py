from collections import Sequence
from magma import *
from ..spartan3.CLB import MUXCY, ANDCY, A0, A1, ZERO, ONE
from .LUT import LUTN

__all__ = ['DefineCascade', 'Cascade']

def _Name(n, k, expr1, expr2, cin):
    assert not isinstance(expr1, Sequence)
    #if isinstance(expr1, Sequence):
    #    expr1 = seq2int(expr1)

    expr1 = "%0X" % (expr1 & 0xffff) # uint(expr1, 1<<k)
    expr2 = "%0X" % (expr1 & 0xffff) # uint(expr2, 1<<k)
    return 'Cascade%dx%d_%X_%X_%d' % (n, k, expr1, expr2, cin)

#
# Create circuit consisting of an LUT feeding into MUXCY.
#
#
#  LUT
#   k is the number of input bits
#   expr1 is what goes into the LUT
#
#  MUXCY
#   the output of the LUT selects the output 
#   expr2 selects what goes into the 0 slot 
#    A0
#    A1
#    A0&A1
#    ZERO
#    ONE
#   CIN goes into the 1 slot 
#
# The resulting circuit has the following interface
#
#  ['I0', rom.I0, ..., 'Ik", rom.Ik, "COUT", mux.COUT, "CIN", CIN]
#
def FullCascade(k, expr1, expr2):

    assert k <= 4

    lut = LUTN(expr1, k)

    args = []
    if k >= 1:
         I0 = Bit()
         wire(I0, lut.I0)
         args += ['I0', I0]
    if k >= 2:
         I1 = Bit()
         wire(I1, lut.I1)
         args += ['I1', I1]
    if k >= 3: args += ['I2', lut.I2]
    if k >= 4: args += ['I3', lut.I3]


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

    args += ["COUT", mux.O, "CIN", CIN]
    return AnonymousCircuit( args )


#
# k is the number of bits per input
# n is the number of inputs 
# expr1 goes into LUT
# expr2 goes into DIN

# cin is a constant carry in: 0 or 1
#
# the inputs are either forked or joined, depending on forkargs
#  I0 : Bit/Array(n,Bit), ..., Ik : Bit/Array(n,Bit) -> O : Bit
#
def DefineCascade(n, k, expr1, expr2, cin, forkargs={}):

    T = In(Bits(n))
    args = []
    if k >= 1: args += ["I0", In(Bit) if 'I0' in forkargs else T]
    if k >= 2: args += ["I1", In(Bit) if 'I1' in forkargs else T]
    if k >= 3: args += ["I2", In(Bit) if 'I2' in forkargs else T]
    if k >= 4: args += ["I3", In(Bit) if 'I3' in forkargs else T]
    args += ["O", Out(Bit)]

    class _Cascade(Circuit):
        name = _Name(n, k, expr1, expr2, cin)
        IO = args

        @classmethod
        def definition(io):

            def f(y):
                return FullCascade(k, expr1, expr2)

            c = braid( col(f, n), foldargs={"CIN":"COUT"}, forkargs=forkargs )

            if k >= 1: wire(io.I0, c.I0)
            if k >= 2: wire(io.I1, c.I1)
            if k >= 3: wire(io.I2, c.I2)
            if k >= 4: wire(io.I3, c.I3)
            wire(c.COUT, io.O)
            wire(cin, c.CIN)

    return _Cascade

def Cascade(n, k, expr1, expr2, cin, forkargs={}):
    return DefineCascade(n, k, expr1, expr2, cin, forkargs)()


