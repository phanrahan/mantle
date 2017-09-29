import operator

from magma import *
from magma.compatibility import IntegerTypes
import mantle.primitives
from .logic import DefineFoldOp, get_length


def declare_binop(name, python_op, out_type=None, signed=False):
    def simulate(self, value_store, state_store):
        in0 = BitVector(value_store.get_value(self.in0), signed=signed)
        in1 = BitVector(value_store.get_value(self.in1), signed=signed)
        out = python_op(in0, in1).as_bool_list()
        if out_type is Bit:
            assert len(out) == 1, "out_type is Bit but the operation returned a list of length {}".format(len(out))
            out = out[0]
        value_store.set_value(self.out, out)

    @cache_definition
    def Declare(N, type_):
        T = type_(N)
        return DeclareCircuit("coreir_{}{}".format(name, N),
                              'in0', In(T), 'in1', In(T),
                              'out', Out(out_type if out_type else T),
                              stateful=False,
                              simulate=simulate,
                              verilog_name="coreir_" + name,
                              coreir_name=name,
                              coreir_lib = "coreir",
                              coreir_genargs={"width": N})

    return Declare


@circuit_generator
def DefineAdd(N, cout=False, cin=False):
    has_cout = cout
    has_cin = cin
    class Add(mantle.primitives.DeclareAdd(N, cin=has_cin, cout=has_cout)):
        @classmethod
        def definition(add):
            T = Bits(N)
            coreir_io = ['in0', In(T), 'in1', In(T), 'out', Out(T)]
            coreir_genargs = {"width": N, "has_cout": has_cout, "has_cin": has_cin}
            if has_cout:
                coreir_io += ['cout', Out(Bit)]
            if has_cin:
                coreir_io += ['cin', In(Bit)]
            CoreirAdd = DeclareCircuit("coreir_" + add.name, *coreir_io,
                    coreir_name="add", coreir_lib="coreir",
                    coreir_genargs=coreir_genargs)
            coreir_add = CoreirAdd()
            wire(add.I0, coreir_add.in0)
            wire(add.I1, coreir_add.in1)
            wire(coreir_add.out, add.O)
            if has_cout:
                wire(coreir_add.cout, add.COUT)
            if has_cin:
                wire(coreir_add.cin, add.CIN)
    return Add



@circuit_generator
def DefineSub(N, cout=False, cin=False):
    has_cout = cout
    has_cin = cin
    class Sub(mantle.primitives.DeclareSub(N, cin=has_cin, cout=has_cout)):
        @classmethod
        def definition(sub):
            T = Bits(N)
            coreir_io = ['in0', In(T), 'in1', In(T), 'out', Out(T)]
            coreir_genargs = {"width": N, "has_cout": has_cout, "has_cin": has_cin}
            if has_cout:
                coreir_io += ['cout', Out(Bit)]
            if has_cin:
                coreir_io += ['cin', In(Bit)]
            CoreirSub = DeclareCircuit("coreir_" + sub.name, *coreir_io,
                    coreir_name="sub", coreir_lib="coreir",
                    coreir_genargs=coreir_genargs)
            coreir_sub = CoreirSub()
            wire(sub.I0, coreir_sub.in0)
            wire(sub.I1, coreir_sub.in1)
            wire(coreir_sub.out, sub.O)
            if has_cout:
                wire(coreir_sub.cout, sub.COUT)
            if has_cin:
                wire(coreir_sub.cin, sub.CIN)
    return Sub


@cache_definition
def DefineNegate(width):
    T = Bits(width)
    class _Negate(mantle.primitives.DeclareNegate(width)):
        @classmethod
        def definition(neg):
            CoreirNeg = DeclareCircuit("coreir_" + neg.name, "in", In(T),
                    "out", Out(T), coreir_name="neg", coreir_lib="coreir",
                    coreir_genargs={"width": width})
            coreir_neg = CoreirNeg()
            wire(neg.I, getattr(coreir_neg, "in"))
            wire(neg.O, coreir_neg.out)
    return _Negate
