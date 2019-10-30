from magma import *
from hwtypes import BitVector
from .arith import declare_binop, get_length
from .logic import not_, XOr
import operator
from .util import DefineCoreirCircuit, DeclareCoreirCircuit


def DefineEQ(width):
    def simulate(self, value_store, state_store):
        I0 = BitVector[width](value_store.get_value(self.I0))
        I1 = BitVector[width](value_store.get_value(self.I1))
        #O = operator.eq(I0, I1).as_bool_list()[0]
        O = int(operator.eq(I0, I1))
        value_store.set_value(self.O, O)
    if width is None:
        circ = DefineCircuit('corebit_eq', 'I0', In(Bit), 'I1', In(Bit), 'O', Out(Bit))
        wire(circ.O, not_(XOr(2, None)(circ.I0, circ.I1)))
        EndDefine()
        return circ
    else:
        T = Bits[width]
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

def DefineNE(n):
    if n is None:
        T = Bit
    else:
        T = Bits[n]
    circ = DefineCircuit("NE{}".format(n),
        "I0", In(T), "I1", In(T), "O", Out(Bit))
    eq = EQ(n)
    O = not_(eq(circ.I0, circ.I1))
    wire(O, circ.O)
    EndDefine()
    return circ

def NE(n, **kwargs):
    return DefineNE(n)(**kwargs)


DefineCoreirUlt = declare_binop("ult", operator.lt, out_type=Bit)


def DefineULT(n):
    return DefineCoreirUlt(n)

def ULT(n, **kwargs):
    return DefineULT(n)(**kwargs)


DefineCoreirUle = declare_binop("ule", operator.le, out_type=Bit)


def DefineULE(n):
    return DefineCoreirUle(n)

def ULE(n, **kwargs):
    return DefineULE(n)(**kwargs)


DefineCoreirUgt = declare_binop("ugt", operator.gt, out_type=Bit)


def DefineUGT(n):
    return DefineCoreirUgt(n)

def UGT(n, **kwargs):
    return DefineUGT(n)(**kwargs)


DefineCoreirUge = declare_binop("uge", operator.ge, out_type=Bit)


def DefineUGE(n):
    return DefineCoreirUge(n)

def UGE(n, **kwargs):
    return DefineUGE(n)(**kwargs)


DefineCoreirSlt = declare_binop("slt", operator.lt, out_type=Bit)


def DefineSLT(n):
    return DefineCoreirSlt(n)

def SLT(n, **kwargs):
    return DefineSLT(n)(**kwargs)


DefineCoreirSle = declare_binop("sle", operator.le, out_type=Bit)


def DefineSLE(n):
    return DefineCoreirSle(n)

def SLE(n, **kwargs):
    return DefineSLE(n)(**kwargs)


DefineCoreirSgt = declare_binop("sgt", operator.gt, out_type=Bit)


def DefineSGT(n):
    return DefineCoreirSgt(n)

def SGT(n, **kwargs):
    return DefineSGT(n)(**kwargs)


DefineCoreirSge = declare_binop("sge", operator.ge, out_type=Bit)


def DefineSGE(n):
    return DefineCoreirSge(n)

def SGE(n, **kwargs):
    return DefineSGE(n)(**kwargs)
