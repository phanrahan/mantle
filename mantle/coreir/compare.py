from magma import *
from .arith import declare_binop, get_length
from .logic import not_, XOr
import operator


DefineCoreirEQ = declare_binop("eq", operator.eq, out_type=Bit)


@cache_definition
def DefineEQ(n):
    T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("EQ{}".format(n), *IO)
    coreir_eq = DefineCoreirEQ(n, Bits)()
    wire(circ.I0, coreir_eq.in0)
    wire(circ.I1, coreir_eq.in1)
    wire(coreir_eq.out, circ.O)
    EndDefine()
    return circ

def EQ(n, **kwargs):
    return DefineEQ(n)(**kwargs)


@cache_definition
def DefineNE(n):
    T = Bits(n)
    circ = DefineCircuit("NE{}".format(n),
        "I0", In(T), "I1", In(T), "O", Out(Bit))
    eq = EQ(n)
    out = not_(eq(circ.I0, circ.I1))
    wire(out, circ.O)
    EndDefine()
    return circ

def NE(n, **kwargs):
    return DefineNE(n)(**kwargs)


DefineCoreirULT = declare_binop("ult", operator.lt, out_type=Bit)


@cache_definition
def DefineULT(n):
    T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("ULT{}".format(n), *IO)
    coreir_ult = DefineCoreirULT(n, Bits)()
    wire(circ.I0, coreir_ult.in0)
    wire(circ.I1, coreir_ult.in1)
    wire(coreir_ult.out, circ.O)
    EndDefine()
    return circ

def ULT(n, **kwargs):
    return DefineULT(n)(**kwargs)


DefineCoreirULE = declare_binop("ule", operator.le, out_type=Bit)


@cache_definition
def DefineULE(n):
    T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("ULE{}".format(n), *IO)
    coreir_ule = DefineCoreirULE(n, Bits)()
    wire(circ.I0, coreir_ule.in0)
    wire(circ.I1, coreir_ule.in1)
    wire(coreir_ule.out, circ.O)
    EndDefine()
    return circ

def ULE(n, **kwargs):
    return DefineULE(n)(**kwargs)


DefineCoreirUGT = declare_binop("ugt", operator.lt, out_type=Bit)


@cache_definition
def DefineUGT(n):
    T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("UGT{}".format(n), *IO)
    coreir_ugt = DefineCoreirUGT(n, Bits)()
    wire(circ.I0, coreir_ugt.in0)
    wire(circ.I1, coreir_ugt.in1)
    wire(coreir_ugt.out, circ.O)
    EndDefine()
    return circ

def UGT(n, **kwargs):
    return DefineUGT(n)(**kwargs)


DefineCoreirUGE = declare_binop("uge", operator.le, out_type=Bit)


@cache_definition
def DefineUGE(n):
    T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("UGE{}".format(n), *IO)
    coreir_uge = DefineCoreirUGE(n, Bits)()
    wire(circ.I0, coreir_uge.in0)
    wire(circ.I1, coreir_uge.in1)
    wire(coreir_uge.out, circ.O)
    EndDefine()
    return circ

def UGE(n, **kwargs):
    return DefineUGE(n)(**kwargs)


DefineCoreirSLT = declare_binop("slt", operator.lt, out_type=Bit)


@cache_definition
def DefineSLT(n):
    T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("SLT{}".format(n), *IO)
    coreir_slt = DefineCoreirSLT(n, Bits)()
    wire(circ.I0, coreir_slt.in0)
    wire(circ.I1, coreir_slt.in1)
    wire(coreir_slt.out, circ.O)
    EndDefine()
    return circ

def SLT(n, **kwargs):
    return DefineSLT(n)(**kwargs)


DefineCoreirSLE = declare_binop("sle", operator.le, out_type=Bit)


@cache_definition
def DefineSLE(n):
    T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("SLE{}".format(n), *IO)
    coreir_sle = DefineCoreirSLE(n, Bits)()
    wire(circ.I0, coreir_sle.in0)
    wire(circ.I1, coreir_sle.in1)
    wire(coreir_sle.out, circ.O)
    EndDefine()
    return circ

def SLE(n, **kwargs):
    return DefineSLE(n)(**kwargs)


DefineCoreirSGT = declare_binop("sgt", operator.lt, out_type=Bit)


@cache_definition
def DefineSGT(n):
    T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("SGT{}".format(n), *IO)
    coreir_sgt = DefineCoreirSGT(n, Bits)()
    wire(circ.I0, coreir_sgt.in0)
    wire(circ.I1, coreir_sgt.in1)
    wire(coreir_sgt.out, circ.O)
    EndDefine()
    return circ

def SGT(n, **kwargs):
    return DefineSGT(n)(**kwargs)


DefineCoreirSGE = declare_binop("sge", operator.le, out_type=Bit)


@cache_definition
def DefineSGE(n):
    T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCircuit("SGE{}".format(n), *IO)
    coreir_sge = DefineCoreirSGE(n, Bits)()
    wire(circ.I0, coreir_sge.in0)
    wire(circ.I1, coreir_sge.in1)
    wire(coreir_sge.out, circ.O)
    EndDefine()
    return circ

def SGE(n, **kwargs):
    return DefineSGE(n)(**kwargs)
