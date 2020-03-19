import operator
from hwtypes import BitVector
import magma as m
from .arith import declare_binop, get_length
from .logic import not_, XOr
from .util import DeclareCoreirCircuit


def DefineEQ(width):

    def _simulate(self, value_store, state_store):
        I0 = BitVector[width](value_store.get_value(self.I0))
        I1 = BitVector[width](value_store.get_value(self.I1))
        O = int(operator.eq(I0, I1))
        value_store.set_value(self.O, O)

    if width is None:

        class corebit_eq(m.Circuit):
            name = "corebit_eq"
            io = m.IO(I0=m.In(m.Bit), I1=m.In(m.Bit), O=m.Out(m.Bit))
            m.wire(io.O, not_(XOr(2, None)(io.I0, io.I1)))

        return _corebit_eq

    T = m.Bits[width]
    return DeclareCoreirCircuit("coreir_eq_{}".format(width),
                                'I0', m.In(T), 'I1', m.In(T),
                                'O', m.Out(m.Bit),
                                stateful=False,
                                simulate=_simulate,
                                verilog_name="coreir_eq",
                                coreir_name="eq",
                                coreir_lib="coreir",
                                coreir_genargs={"width": width})


DefineCoreirEq = DefineEQ


def EQ(n, **kwargs):
    return DefineEQ(n)(**kwargs)


DefineCoreirNeq = declare_binop("neq", operator.ne, out_type=m.Bit)


def DefineNE(n):
    T = m.Bit if n is None else m.Bits[n]

    class _NE(m.Circuit):
        name = f"NE{n}"
        io = m.IO(I0=m.In(T), I1=m.In(T), O=m.Out(m.Bit))
        eq = EQ(n)
        O = not_(eq(io.I0, io.I1))
        m.wire(O, io.O)

    return _NE


def NE(n, **kwargs):
    return DefineNE(n)(**kwargs)


DefineCoreirUlt = declare_binop("ult", operator.lt, out_type=m.Bit)


def DefineULT(n):
    return DefineCoreirUlt(n)


def ULT(n, **kwargs):
    return DefineULT(n)(**kwargs)


DefineCoreirUle = declare_binop("ule", operator.le, out_type=m.Bit)


def DefineULE(n):
    return DefineCoreirUle(n)


def ULE(n, **kwargs):
    return DefineULE(n)(**kwargs)


DefineCoreirUgt = declare_binop("ugt", operator.gt, out_type=m.Bit)


def DefineUGT(n):
    return DefineCoreirUgt(n)


def UGT(n, **kwargs):
    return DefineUGT(n)(**kwargs)


DefineCoreirUge = declare_binop("uge", operator.ge, out_type=m.Bit)


def DefineUGE(n):
    return DefineCoreirUge(n)


def UGE(n, **kwargs):
    return DefineUGE(n)(**kwargs)


DefineCoreirSlt = declare_binop("slt", operator.lt, out_type=m.Bit)


def DefineSLT(n):
    return DefineCoreirSlt(n)


def SLT(n, **kwargs):
    return DefineSLT(n)(**kwargs)


DefineCoreirSle = declare_binop("sle", operator.le, out_type=m.Bit)


def DefineSLE(n):
    return DefineCoreirSle(n)


def SLE(n, **kwargs):
    return DefineSLE(n)(**kwargs)


DefineCoreirSgt = declare_binop("sgt", operator.gt, out_type=m.Bit)


def DefineSGT(n):
    return DefineCoreirSgt(n)


def SGT(n, **kwargs):
    return DefineSGT(n)(**kwargs)


DefineCoreirSge = declare_binop("sge", operator.ge, out_type=m.Bit)


def DefineSGE(n):
    return DefineCoreirSge(n)


def SGE(n, **kwargs):
    return DefineSGE(n)(**kwargs)
