from collections import Sequence
from magma import *
from .LUT import LUTN, LOG_BITS_PER_LUT, A0, A1, A2, A3, ZERO, ONE
from .carry import HalfCarry

__all__  = ['DefineFlatHalfCascade', 'FlatCascade']
#__all__ += ['AndCascade', 'NAndCascade', 'OrCascade', 'NOrCascade']

__all__ += ['DefineHalfCascade', 'HalfCascade']

def InputArgs(n, k, forkargs):
    T = Bits(n)
    I = []
    for i in range(k):
       name = "I{}".format(i)
       I.append(name)
       I.append(In(Bit) if name in forkargs else In(T))
    return I

def _CascadeName(name, n, lutexpr, andexpr, cin):
    if isinstance(lutexpr, Sequence):
        lutexpr = "_".join(["%04X" % (e & 0xffff) for e in lutexpr])
    else:
        lutexpr = "%04X" % (lutexpr & 0xffff)
    andexpr = "%04X" % (andexpr & 0xffff)
    return '%s%d_%s_%s_%d' % (name ,n, lutexpr, andexpr, cin)

#
# Build a column of LUTs feeding into MUXCY. In the Half version
# the XORCY is not used.
#
#  IO = ["I", In(Bits(n)), "O", Out(Bit)]
#
#  n is the total number of inputs desired.
#  k is the number of inputs per LUT (normally 4)
#
#  lutexpr is the expression that goes into each LUT
#
# The output of MUXCY is selected by the output of the LUT
#   cin is the value going into the first MUXCY in the column   
#
def DefineFlatHalfCascade(n, k, lutexpr, andexpr, cin, name=None):
    if name is None:
        nm = _CascadeName('FlatHalfCascade', n, lutexpr, andexpr, cin)
    else:
        nm = name + str(n)
    class _FlatHalfCascade(Circuit):
        name = nm
        IO = ["I", In(Bits(n)), "O", Out(Bit)]
        @classmethod
        def definition(io):
            def f(y):
                e = lutexpr[y] if isinstance(lutexpr, Sequence) else lutexpr
                return HalfCarry(k, e, andexpr, use_rom=True)

            # calculate number of LUTs
            nluts = (n+LOG_BITS_PER_LUT-1)//LOG_BITS_PER_LUT

            c = braid( col(f, nluts), foldargs={"CIN":"COUT"})
            c = flat(c)
            #print(repr(c))
            for i in range(LOG_BITS_PER_LUT*nluts):
                wire(io.I[i], c.I[i])

            wire(c.COUT, io.O)
            wire(cin, c.CIN)

    return _FlatHalfCascade

def FlatHalfCascade(n, k, lutexpr, andexpr, cin, name=None):
    return DefineFlatHalfCascade(n, k, lutexpr, andexpr, cin, name=name)()

#def AndCascade( n ):
#    return FlatHalfCascade(n, 4,   A0&A1&A2&A3,  ZERO, 1, 'AndCascade')
#
#def NAndCascade( n ):
#    return FlatHalfCascade(n, 4,   A0&A1&A2&A3,   ONE, 0)
#
#def OrCascade( n ):
#    return FlatHalfCascade(n, 4, ~(A0|A1|A2|A3),  ONE, 0)
#
#def NOrCascade( n ):
#    return FlatHalfCascade(n, 4, ~(A0|A1|A2|A3), ZERO, 1)


def DefineHalfCascade(n, k, lutexpr, andexpr, cin, forkargs={}, name=None):
    if name is None:
        nm = _CascadeName('HalfCascade', n, lutexpr, andexpr, cin)
    else:
        nm = '{}_{}'.format(name, n)
    class _HalfCascade(Circuit):
        name = nm
        IO = InputArgs(n, k, forkargs) + ["O", Out(Bit)]
        @classmethod
        def definition(io):
            def f(y):
                e = lutexpr[y] if isinstance(lutexpr, Sequence) else lutexpr
                return HalfCarry(k, e, andexpr)

            c = braid( col(f, n), foldargs={"CIN":"COUT"}, forkargs=forkargs)
            #print(repr(c))
            if k >= 1: wire(io.I0, c.I0)
            if k >= 2: wire(io.I1, c.I1)
            if k >= 3: wire(io.I2, c.I2)
            if k >= 4: wire(io.I3, c.I3)

            wire(c.COUT, io.O)
            wire(cin, c.CIN)

    return _HalfCascade

def HalfCascade(n, k, lutexpr, andexpr, cin, forkargs={}, name=None):
    return DefineHalfCascade(n, k, lutexpr, andexpr, cin, forkargs, name)()

#
#def _Name(n, k, expr1, expr2, cin):
#    assert not isinstance(expr1, Sequence)
#    #if isinstance(expr1, Sequence):
#    #    expr1 = seq2int(expr1)
#
#    expr1 = "%0X" % (expr1 & 0xffff) # uint(expr1, 1<<k)
#    expr2 = "%0X" % (expr1 & 0xffff) # uint(expr2, 1<<k)
#    return 'Cascade%dx%d_%X_%X_%d' % (n, k, expr1, expr2, cin)
#
##
## Create circuit consisting of an LUT feeding into MUXCY.
##
##
##  LUT
##   k is the number of input bits
##   expr1 is what goes into the LUT
##
##  MUXCY
##   the output of the LUT selects the output 
##   expr2 selects what goes into the 0 slot 
##    A0
##    A1
##    A0&A1
##    ZERO
##    ONE
##   CIN goes into the 1 slot 
##
## The resulting circuit has the following interface
##
##  ['I0', rom.I0, ..., 'Ik", rom.Ik, "COUT", mux.COUT, "CIN", CIN]
##
##def FullCascade(k, expr1, expr2):
##
##    assert k <= 4
##
##    lut = LUTN(expr1, k)
##
##    args = []
##    if k >= 1:
##         I0 = Bit()
##         wire(I0, lut.I0)
##         args += ['I0', I0]
##    if k >= 2:
##         I1 = Bit()
##         wire(I1, lut.I1)
##         args += ['I1', I1]
##    if k >= 3: args += ['I2', lut.I2]
##    if k >= 4: args += ['I3', lut.I3]
##
##
##    if expr2 == A0&A1:
##       and1 = ANDCY()
##       wire(I0, and1.I0)
##       wire(I1, and1.I1)
##       DI = and1.LO
##    elif expr2 == A0:
##       DI = I0
##    elif expr2 == A1:
##       DI = I1
##    elif expr2 == ZERO:
##       DI = 0
##    elif expr2 == ONE:
##       DI = 1
##
##    CIN = Bit()
##
##    mux = MUXCY()
##    wire(lut.O, mux.S)
##    wire(DI,    mux.DI)
##    wire(CIN,   mux.CI)
##
##    args += ["COUT", mux.O, "CIN", CIN]
##    return AnonymousCircuit( args )
#
#
##
## k is the number of bits per input
## n is the number of inputs 
## expr1 goes into LUT
## expr2 goes into DIN
#
## cin is a constant carry in: 0 or 1
##
## the inputs are either forked or joined, depending on forkargs
##  I0 : Bit/Array(n,Bit), ..., Ik : Bit/Array(n,Bit) -> O : Bit
##
##def DefineHalfCascade(n, k, expr1, expr2, cin, forkargs={}):
##
##    T = In(Bits(n))
##    args = []
##    if k >= 1: args += ["I0", In(Bit) if 'I0' in forkargs else T]
##    if k >= 2: args += ["I1", In(Bit) if 'I1' in forkargs else T]
##    if k >= 3: args += ["I2", In(Bit) if 'I2' in forkargs else T]
##    if k >= 4: args += ["I3", In(Bit) if 'I3' in forkargs else T]
##    args += ["O", Out(Bit)]
##
##    class _HalfCascade(Circuit):
##        name = _CascadeName('HalfCascade', n, k, expr1, expr2, cin, 0)
##        IO = args
##
##        @classmethod
##        def definition(io):
##
##            def f(y):
##                return HalfCarry(k, expr1, expr2)
##
##            c = braid( col(f, n), foldargs={"CIN":"COUT"}, forkargs=forkargs )
##
##            if k >= 1: wire(io.I0, c.I0)
##            if k >= 2: wire(io.I1, c.I1)
##            if k >= 3: wire(io.I2, c.I2)
##            if k >= 4: wire(io.I3, c.I3)
##            wire(c.COUT, io.O)
##            wire(cin, c.CIN)
##
##    return _HalfCascade
##
#
#
