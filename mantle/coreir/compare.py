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
    out = not_(eq(circ.I0, circ.I1))
    wire(out, circ.O)
    EndDefine()
    return circ

def NE(n, **kwargs):
    return DefineNE(n)(**kwargs)
