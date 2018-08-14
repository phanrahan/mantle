from magma import *
from magma.bit_vector import BitVector
from .arith import declare_binop, get_length
from .logic import not_, XOr
import operator
from .util import DefineCoreirCircuit, DeclareCoreirCircuit


def DefineEQ(width):
    def simulate(self, value_store, state_store):
        I0 = BitVector(value_store.get_value(self.I0))
        I1 = BitVector(value_store.get_value(self.I1))
        O = operator.eq(I0, I1).as_bool_list()[0]
        value_store.set_value(self.O, O)
    if width is None:
        circ = DefineCoreirCircuit('corebit_eq', 'I0', In(Bit), 'I1', In(Bit), 'O', Out(Bit))
        wire(circ.O, not_(XOr(2, None)(circ.I0, circ.I1)))
        EndDefine()
        return circ
    else:
        T = Bits(width)
        return DeclareCoreirCircuit("coreir_eq_{}".format(width),
                              'I0', In(T), 'I1', In(T),
                              'O', Out(Bit),
                              stateful=False,
                              simulate=simulate,
                              verilog_name="coreir_eq",
                              coreir_name="eq",
                              coreir_lib = "coreir",
                              coreir_genargs={"width": width})

DefineCoreirEq = DefineEQ

def EQ(n, **kwargs):
    return DefineEQ(n)(**kwargs)


DefineCoreirNeq = declare_binop("neq", operator.ne, out_type=Bit)

@cache_definition
def DefineNE(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    circ = DefineCoreirCircuit("NE{}".format(n),
        "I0", In(T), "I1", In(T), "O", Out(Bit))
    eq = EQ(n)
    O = not_(eq(circ.I0, circ.I1))
    wire(O, circ.O)
    EndDefine()
    return circ

def NE(n, **kwargs):
    return DefineNE(n)(**kwargs)


DefineCoreirUlt = declare_binop("ult", operator.lt, out_type=Bit)


@cache_definition
def DefineULT(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCoreirCircuit("ULT{}".format(n), *IO)
    coreir_ult = DefineCoreirUlt(n, Bits)()
    wire(circ.I0, coreir_ult.I0)
    wire(circ.I1, coreir_ult.I1)
    wire(coreir_ult.O, circ.O)
    EndDefine()
    return circ

def ULT(n, **kwargs):
    return DefineULT(n)(**kwargs)


DefineCoreirUle = declare_binop("ule", operator.le, out_type=Bit)


@cache_definition
def DefineULE(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCoreirCircuit("ULE{}".format(n), *IO)
    coreir_ule = DefineCoreirUle(n, Bits)()
    wire(circ.I0, coreir_ule.I0)
    wire(circ.I1, coreir_ule.I1)
    wire(coreir_ule.O, circ.O)
    EndDefine()
    return circ

def ULE(n, **kwargs):
    return DefineULE(n)(**kwargs)


DefineCoreirUgt = declare_binop("ugt", operator.lt, out_type=Bit)


@cache_definition
def DefineUGT(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCoreirCircuit("UGT{}".format(n), *IO)
    coreir_ugt = DefineCoreirUgt(n, Bits)()
    wire(circ.I0, coreir_ugt.I0)
    wire(circ.I1, coreir_ugt.I1)
    wire(coreir_ugt.O, circ.O)
    EndDefine()
    return circ

def UGT(n, **kwargs):
    return DefineUGT(n)(**kwargs)


DefineCoreirUge = declare_binop("uge", operator.le, out_type=Bit)


@cache_definition
def DefineUGE(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCoreirCircuit("UGE{}".format(n), *IO)
    coreir_uge = DefineCoreirUge(n, Bits)()
    wire(circ.I0, coreir_uge.I0)
    wire(circ.I1, coreir_uge.I1)
    wire(coreir_uge.O, circ.O)
    EndDefine()
    return circ

def UGE(n, **kwargs):
    return DefineUGE(n)(**kwargs)


DefineCoreirSlt = declare_binop("slt", operator.lt, out_type=Bit)


@cache_definition
def DefineSLT(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCoreirCircuit("SLT{}".format(n), *IO)
    coreir_slt = DefineCoreirSlt(n, Bits)()
    wire(circ.I0, coreir_slt.I0)
    wire(circ.I1, coreir_slt.I1)
    wire(coreir_slt.O, circ.O)
    EndDefine()
    return circ

def SLT(n, **kwargs):
    return DefineSLT(n)(**kwargs)


DefineCoreirSle = declare_binop("sle", operator.le, out_type=Bit)


@cache_definition
def DefineSLE(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCoreirCircuit("SLE{}".format(n), *IO)
    coreir_sle = DefineCoreirSle(n, Bits)()
    wire(circ.I0, coreir_sle.I0)
    wire(circ.I1, coreir_sle.I1)
    wire(coreir_sle.O, circ.O)
    EndDefine()
    return circ

def SLE(n, **kwargs):
    return DefineSLE(n)(**kwargs)


DefineCoreirSgt = declare_binop("sgt", operator.lt, out_type=Bit)


@cache_definition
def DefineSGT(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCoreirCircuit("SGT{}".format(n), *IO)
    coreir_sgt = DefineCoreirSgt(n, Bits)()
    wire(circ.I0, coreir_sgt.I0)
    wire(circ.I1, coreir_sgt.I1)
    wire(coreir_sgt.O, circ.O)
    EndDefine()
    return circ

def SGT(n, **kwargs):
    return DefineSGT(n)(**kwargs)


DefineCoreirSge = declare_binop("sge", operator.le, out_type=Bit)


@cache_definition
def DefineSGE(n):
    if n is None:
        T = Bit
    else:
        T = Bits(n)
    IO = ["I0", In(T), "I1", In(T), "O", Out(Bit)]
    circ = DefineCoreirCircuit("SGE{}".format(n), *IO)
    coreir_sge = DefineCoreirSge(n, Bits)()
    wire(circ.I0, coreir_sge.I0)
    wire(circ.I1, coreir_sge.I1)
    wire(coreir_sge.O, circ.O)
    EndDefine()
    return circ

def SGE(n, **kwargs):
    return DefineSGE(n)(**kwargs)
