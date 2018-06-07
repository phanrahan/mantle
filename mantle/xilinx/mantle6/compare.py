from magma import *
from .LUT import LUT2, LUT3, LUT4, A0, A1, A2, A3, ZERO
from .arith import DefineSub
from .logic import Not
from .cascade import HalfCascade

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

class EQ1(Circuit):
    IO = ["I0", In(Bit), "I1", In(Bit), "O", Out(Bit)]
    @classmethod
    def definition(io):
        wire( LUT2(EQ1LUT)(io.I0, io.I1), io.O )

class EQ2(Circuit):
    T = Bits(2)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    @classmethod
    def definition(io):
        wire( LUT4(EQ2LUT)(io.I0[0], io.I1[0], io.I0[1], io.I1[1]), io.O )

@cache_definition
def DefineEQ(n):
    assert n % 2 == 0
    T = Bits(n)
    class _EQ(Circuit):
        name = "EQ{}".format(n)
        IO = ['I0', In(T), 'I1', In(T), "O", Out(Bit)]
        @classmethod
        def definition(io):
             eq = HalfCascade(n//2, 4, EQ2LUT, ZERO, 1)
             for i in range(n//2):
                 wire(io.I0[2*i], eq.I0[i])
                 wire(io.I1[2*i], eq.I1[i])
                 wire(io.I0[2*i+1], eq.I2[i])
                 wire(io.I1[2*i+1], eq.I3[i])
             wire(eq.O, io.O)
    return _EQ

def EQ(n, **kwargs):
    if   n == 1:
        return EQ1(**kwargs)
    elif n == 2:
        return EQ2(**kwargs)
    return DefineEQ(n)(**kwargs)

NE1LUT = (A0^A1)
NE2LUT = (A0^A1)|(A2^A3)

class NE1(Circuit):
    IO = ["I0", In(Bit), "I1", In(Bit), "O", Out(Bit)]
    @classmethod
    def definition(io):
        wire( LUT2(NE1LUT)(io.I0, io.I1), io.O )

class NE2(Circuit):
    T = Bits(2)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    @classmethod
    def definition(io):
        wire( LUT4(NE2LUT)(io.I0[0], io.I1[0], io.I0[1], io.I1[1]), io.O )

@cache_definition
def DefineNE(n):
    assert n % 2 == 0
    T = Bits(n)
    class _NE(Circuit):
        name = "NE{}".format(n)
        IO = ['I0', In(T), 'I1', In(T), "O", Out(Bit)]
        @classmethod
        def definition(io):
             ne =  HalfCascade(n//2, 4, NE2LUT, ZERO, 1)
             for i in range(n//2):
                 wire(io.I0[2*i], ne.I0[i])
                 wire(io.I1[2*i], ne.I1[i])
                 wire(io.I0[2*i+1], ne.I2[i])
                 wire(io.I1[2*i+1], ne.I3[i])
             wire(ne.O, io.O)
    return _NE

def NE(n, **kwargs):
    if   n == 1:
        return NE1(**kwargs)
    elif n == 2:
        return NE2(**kwargs)
    return DefineNE(n)(**kwargs)


# unsigned comparisons

def DefineUCMP(opname, reverse, negate, n):
    T = UInt(n)
    class _UCMP(Circuit):
        name = "{}{}".format(opname, n)
        IO = ['I0', In(T), 'I1', In(T), "O", Out(Bit)]
        @classmethod
        def definition(io):
            sub = DefineSub(n,1,True)()
            if not reverse:
                sub(io.I0, io.I1)
            else:
                sub(io.I1, io.I0)
            if not negate:
                wire(sub.COUT, io.O)
            else:
                wire(Not()(sub.COUT), io.O)
    return _UCMP

@cache_definition
def DefineUGE(n):
    return DefineUCMP('UGE', False, False, n)

def UGE(n, **kwargs):
    return DefineUGE(n)(**kwargs)

@cache_definition
def DefineULE(n):
    return DefineUCMP('ULE', True, False, n)

def ULE(n, **kwargs):
    return DefineULE(n)(**kwargs)

@cache_definition
def DefineULT(n):
    return DefineUCMP('ULT', False, True, n)

def ULT(n, **kwargs):
    return DefineULT(n)(**kwargs)

@cache_definition
def DefineUGT(n):
    return DefineUCMP('UGT', True, True, n)

def UGT(n, **kwargs):
    return DefineUGT(n)(**kwargs)


# signed comparison

def _sge(c_msb, a_msb, b_msb):
    return int((~(a_msb ^ b_msb) & ~c_msb) | (~a_msb & b_msb)) & 1

def _slt(c_msb, a_msb, b_msb):
    return int((~(a_msb ^ b_msb) & c_msb) | (a_msb & ~b_msb)) & 1

def DefineSCMP(opname, op, reverse, n):
    T = SInt(n)
    class _SCMP(Circuit):
        name = "{}{}".format(opname,n)
        IO = ['I0', In(T), 'I1', In(T), "O", Out(Bit)]
        @classmethod
        def definition(io):
            sub = DefineSub(n)()
            cmp = LUT3(op)
            if not reverse:
                wire(cmp( sub(io.I0, io.I1)[-1], io.I0[-1], io.I1[-1] ), io.O)
            else:
                wire(cmp( sub(io.I1, io.I0)[-1], io.I1[-1], io.I0[-1] ), io.O)
    return _SCMP

@cache_definition
def DefineSGE(n):
    return DefineSCMP('SGE', _sge, False, n)

def SGE(n, **kwargs):
    return DefineSGE(n)(**kwargs)

@cache_definition
def DefineSLE(n):
    return DefineSCMP('SLE', _sge, True, n)

def SLE(n, **kwargs):
    return DefineSLE(n)(**kwargs)

@cache_definition
def DefineSLT(n):
    return DefineSCMP('SLT', _slt, False, n)

def SLT(n, **kwargs):
    return DefineSLT(n)(**kwargs)

@cache_definition
def DefineSGT(n):
    return DefineSCMP('SGT', _slt, True, n)

def SGT(n, **kwargs):
    return DefineSGT(n)(**kwargs)

