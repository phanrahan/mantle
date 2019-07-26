from collections.abc import Sequence
from magma import *
from ..spartan3.CLB import ANDCY, XORCY, MUXCY
from .LUT import LUT, LOG_BITS_PER_LUT, A0, A1, A2, A3, ZERO, ONE
from .ROM import ROMN

__all__  = ['HalfCarry', 'FullCarry']
__all__ += ['FullCascade']
__all__ += ['HalfCascade', 'FlatFalfCascade']

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
        lut = LUT(lutexpr, k)
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

    return CIN, mux.O, lut.O, args 

def fullcarry(k, lutexpr, andexpr, use_rom):

    CIN, COUT, O, args = halfcarry(k, lutexpr, andexpr, use_rom)

    xor = XORCY()
    wire(O,   xor.LI)
    wire(CIN, xor.CI)

    return CIN, COUT, xor.O, args


def HalfCarry(k, lutexpr, andexpr, use_rom=False):

    CIN, COUT, O, args = halfcarry(k, lutexpr, andexpr, use_rom)

    args += ['CIN', CIN, 'O', O, 'COUT', COUT]

    return AnonymousCircuit(args)


def FullCarry(k, lutexpr, andexpr, use_rom=False):

    CIN, COUT, O, args = fullcarry(k, lutexpr, andexpr, use_rom)

    args += ['CIN', CIN, 'O', O, 'COUT', COUT]

    return AnonymousCircuit(args)


#def _CascadeName(name, n, lutexpr, andexpr, cin):
#    if isinstance(lutexpr, Sequence):
#        lutexpr = "_".join(["%04X" % (e & 0xffff) for e in lutexpr])
#    else:
#        lutexpr = "%04X" % (lutexpr & 0xffff)
#    andexpr = "%04X" % (andexpr & 0xffff)
#    return '%s%d_%s_%s_%d' % (name ,n, lutexpr, andexpr, cin)

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
def FlatHalfCascade(n, k, lutexpr, andexpr, cin):
    # calculate number of LUTs
    nluts = (n+LOG_BITS_PER_LUT-1)//LOG_BITS_PER_LUT

    def f(y):
        e = lutexpr[y] if isinstance(lutexpr, Sequence) else lutexpr
        return HalfCarry(k, e, andexpr, use_rom=True)

    c = braid( col(f, nluts), foldargs={"CIN":"COUT"})
    c = flat(c)

    wire(cin, c.CIN)

    return AnonymousCircuit("I", c.I, "O", c.COUT)

def HalfCascade(n, k, lutexpr, andexpr, cin, forkargs={}):
    def f(y):
        e = lutexpr[y] if isinstance(lutexpr, Sequence) else lutexpr
        return HalfCarry(k, e, andexpr)

    c = braid( col(f, n), foldargs={"CIN":"COUT"}, forkargs=forkargs)
    #print(repr(c))

    args = []
    if k >= 1: args += ['I0', c.I0]
    if k >= 2: args += ['I1', c.I1]
    if k >= 3: args += ['I2', c.I2]
    if k >= 4: args += ['I3', c.I3]

    args += ['O', c.COUT]

    if cin is 0 or cin is 1:
        wire(cin, c.CIN)
    elif cin:
        args += ['CIN', c.CIN]
    else:
        wire(0, c.CIN)

    return AnonymousCircuit(args)

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
#
# create an n-bit Adder from n FullAdders
#
#   I0rn], ..., Ik[n], <CIN> -> O[n], <COUT>
#
# if cin is None, CIN is added to the circuit 
# if cin==0 or cin==1, cin is wired to CIN
#
# if cout: COUT is added to the circuit
#
def FullCascade(n, k, lutexpr, andexpr, cin, cout, forkargs=[]):

    def f(x):
        e = lutexpr[y] if isinstance(lutexpr, Sequence) else lutexpr
        return FullCarry(k, e, andexpr)

    c = braid( col(f, n), foldargs={"CIN":"COUT"}, forkargs=forkargs)

    args = []
    if k >= 1: args += ['I0', c.I0]
    if k >= 2: args += ['I1', c.I1]
    if k >= 3: args += ['I2', c.I2]
    if k >= 4: args += ['I3', c.I3]

    if cin is 0 or cin is 1:
        wire(cin, c.CIN)
    elif cin:
        args += ['CIN', c.CIN]
    else:
        wire(0, c.CIN)

    args += ['O', c.O]

    if cout:
        args += ['COUT', c.COUT]

    return AnonymousCircuit(args)
