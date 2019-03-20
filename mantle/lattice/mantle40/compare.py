from magma import *
from .LUT import *
from .arith import DefineSub
from .logic import Not

__all__  = ['DefineEQ', 'EQ']
__all__ += ['DefineNE', 'NE']
__all__ += ['DefineUGE']
__all__ += ['DefineULE']
__all__ += ['DefineUGT']
__all__ += ['DefineULT']
__all__ += ['DefineSGE']
__all__ += ['DefineSLE']
__all__ += ['DefineSGT']
__all__ += ['DefineSLT']

#
# n is the number of luts
# k is the number of bits per lut
# expr goes into each LUT
# fold the luts by wiring O to I0
# extra args can be forked or joined
#
def _Cascade(n, k, expr, cin, forkargs={}):

    assert k <= 3

    def f(y):
        return LUT(expr, k+1)

    cascade = braid( col(f, n), foldargs={"I0":"O"}, forkargs=forkargs )

    wire( cin, cascade.I0 )

    args = []
    if k > 0: args += ["I0", cascade.I1]
    if k > 1: args += ["I1", cascade.I2]
    if k > 2: args += ["I2", cascade.I3]
    args += ["O", cascade.O]

    return AnonymousCircuit(*args)

class EQNone(Circuit):
    IO = ["I0", In(Bit), "I1", In(Bit), "O", Out(Bit)]
    @classmethod
    def definition(io):
        EQ1LUT = ((A0&A1)|(~A0&~A1))
        wire( LUT2(EQ1LUT)(io.I0, io.I1), io.O )

class EQ1(Circuit):
    IO = ["I0", In(Bits[ 1 ]), "I1", In(Bits[ 1 ]), "O", Out(Bit)]
    @classmethod
    def definition(io):
        wire(EQNone()(io.I0[0], io.I1[0]), io.O)

class EQ2(Circuit):
    T = Bits[ 2 ]
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    @classmethod
    def definition(io):
        EQ2LUT = ((A0&A1)|(~A0&~A1)) & ((A2&A3)|(~A2&~A3))
        wire( LUT4(EQ2LUT)(io.I0[0], io.I1[0], io.I0[1], io.I1[1]), io.O )

def DefineEQ(n):
    T = Bits[ n ]
    class _EQ(Circuit):
        name = "EQ{}".format(n)
        IO = ['I0', In(T), 'I1', In(T), "O", Out(Bit)]
        @classmethod
        def definition(io):
             eq = _Cascade(n, 2, A0&((A1&A2)|(~A1&~A2)), 1)
             wire(eq(io.I0, io.I1), io.O)
    return _EQ

def EQ(n, **kwargs):
    if   n == None:
        return EQNone(**kwargs)
    elif n == 1:
        return EQ1(**kwargs)
    elif n == 2:
        return EQ2(**kwargs)
    return DefineEQ(n)(**kwargs)


class NE1(Circuit):
    IO = ["I0", In(Bit), "I1", In(Bit), "O", Out(Bit)]
    @classmethod
    def definition(io):
        NE1LUT = (A0^A1)
        wire( LUT2(NE1LUT)(io.I0, io.I1), io.O )

class NE2(Circuit):
    T = Bits[ 2 ]
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    @classmethod
    def definition(io):
        NE2LUT = (A0^A1)|(A2^A3)
        wire( LUT4(NE2LUT)(io.I0[0], io.I1[0], io.I0[1], io.I1[1]), io.O )

def DefineNE(n):
    T = Bits[ n ]
    class _NE(Circuit):
        name = "NE{}".format(n)
        IO = ['I0', In(T), 'I1', In(T), "O", Out(Bit)]
        @classmethod
        def definition(io):
             ne =  _Cascade(n, 2, A0|(A1^A2), 0)
             wire(ne(io.I0, io.I1), io.O)
    return _NE

def NE(n, **kwargs):
    if   n == 1:
        return NE1(**kwargs)
    elif n == 2:
        return NE2(**kwargs)
    return DefineNE(n)(**kwargs)


# unsigned comparisons

def DefineUCMP(opname, reverse, negate, n):
    T = UInt[n]
    class _UCMP(Circuit):
        name = "{}{}".format(opname, n)
        IO = ['I0', In(T), 'I1', In(T), "O", Out(Bit)]
        @classmethod
        def definition(io):
            sub = DefineSub(n, False, True)()
            if not reverse:
                sub(io.I0, io.I1)
            else:
                sub(io.I1, io.I0)
            if not negate:
                wire(sub.COUT, io.O)
            else:
                wire(Not()(sub.COUT), io.O)
    return _UCMP

def DefineUGE(n):
    return DefineUCMP('UGE', False, False, n)

def DefineULE(n):
    return DefineUCMP('ULE', True, False, n)

def DefineULT(n):
    return DefineUCMP('ULT', False, True, n)

def DefineUGT(n):
    return DefineUCMP('UGT', True, True, n)


# signed comparison

def _sge(c_msb, a_msb, b_msb):
    return int((~(a_msb ^ b_msb) & ~c_msb) | (~a_msb & b_msb)) & 1

def _slt(c_msb, a_msb, b_msb):
    return int((~(a_msb ^ b_msb) & c_msb) | (a_msb & ~b_msb)) & 1

def DefineSCMP(opname, op, reverse, n):
    T = SInt[n]
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

def DefineSGE(n):
    return DefineSCMP('SGE', _sge, False, n)

def DefineSLE(n):
    return DefineSCMP('SLE', _sge, True, n)

def DefineSLT(n):
    return DefineSCMP('SLT', _slt, False, n)

def DefineSGT(n):
    return DefineSCMP('SGT', _slt, True, n)

