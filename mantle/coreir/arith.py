import operator

from magma import *
from magma.compatibility import IntegerTypes
from magma.bit_vector import BitVector
import mantle.primitives
from .logic import DefineFoldOp, get_length, Invert, Not


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
        if N is None:
            T = Bit
        else:
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

    def simulate_coreir_add(self, value_store, state_store):
        width = N
        if has_cout:
            width = N + 1
        in0 = BitVector(value_store.get_value(self.in0), width)
        in1 = BitVector(value_store.get_value(self.in1), width)
        value_store.set_value(self.out, in0 + in1)
    class Add(mantle.primitives.DeclareAdd(N, cin=has_cin, cout=has_cout)):
        @classmethod
        def definition(add):
            coreir_genargs = {"width": N} # , "has_cout": has_cout, "has_cin": has_cin}
            if has_cout:
                coreir_genargs["width"] += 1
            T = Bits(coreir_genargs["width"])
            coreir_io = ['in0', In(T), 'in1', In(T), 'out', Out(T)]
            CoreirAdd = DeclareCircuit("coreir_" + add.name, *coreir_io,
                    coreir_name="add", coreir_lib="coreir",
                    coreir_genargs=coreir_genargs,
                    simulate=simulate_coreir_add)
            coreir_add = CoreirAdd()
            I0 = add.I0
            I1 = add.I1
            if has_cout:
                I0 = concat(add.I0, bits(0, n=1))
                I1 = concat(add.I1, bits(0, n=1))
            if has_cin:
                coreir_add_cin = CoreirAdd()
                wire(coreir_add_cin.in0, concat(bits(add.CIN), bits(0,
                    n=coreir_genargs["width"]-1)))
                wire(coreir_add_cin.in1, I0)
                I0 = coreir_add_cin.out
            wire(I0, coreir_add.in0)
            wire(I1, coreir_add.in1)
            O = coreir_add.out
            if has_cout:
                COUT = O[-1]
                O = O[:-1]
            wire(O, add.O)
            if has_cout:
                wire(COUT, add.COUT)
    return Add


@circuit_generator
def DefineSub(N, cout=False, cin=False):
    has_cout = cout
    has_cin = cin
    class Sub(mantle.primitives.DeclareSub(N, cin=has_cin, cout=has_cout)):
        @classmethod
        def definition(io):
            invert = Invert(N)
            add = DefineAdd(N, cin=True, cout=cout)()
            wire(io.I0, add.I0)
            wire(io.I1, invert.I)
            wire(invert.O, add.I1)
            wire(add.O, io.O)
            if cin:
                wire( Not()(io.CIN), add.CIN )
            else:
                wire( 1, add.CIN )
            if cout:
                wire(add.COUT, io.COUT)
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


@cache_definition
def DefineASR(width):
    T = Bits(width)
    class _ASR(mantle.primitives.DeclareASR(width)):
        @classmethod
        def definition(asr):
            CoreirASR = DeclareCircuit("coreir_" + asr.name, "in0", In(T),
                    "in1", In(T), "out", Out(T), coreir_name="ashr",
                    coreir_lib="coreir", coreir_genargs={"width": width})
            coreir_asr = CoreirASR()
            wire(asr.I0, coreir_asr.in0)
            wire(asr.I1, coreir_asr.in1)
            wire(asr.O, coreir_asr.out)
    return _ASR
