import operator

import magma as m
from magma import *
from magma.compatibility import IntegerTypes
from hwtypes import BitVector
import mantle.primitives
from .logic import DefineFoldOp, get_length, Invert, Not
from .util import DeclareCoreirCircuit, get_int_vector_type
from magma.logging import root_logger


LOGGER = root_logger()


def declare_binop(name, python_op, out_type=None, signed=False):
    def simulate(self, value_store, state_store):
        I0 = get_int_vector_type(signed)(value_store.get_value(self.I0))
        I1 = get_int_vector_type(signed)(value_store.get_value(self.I1))
        O = python_op(I0, I1).as_bool_list()
        if out_type is Bit:
            assert len(O) == 1, "out_type is Bit but the operation returned a list of length {}".format(len(O))
            O = O[0]
        value_store.set_value(self.O, O)

    def Declare(width, T=Bits):
        if width is None:
            T = Bit
            return DeclareCoreirCircuit("coreir_bit_{}{}".format(name, width),
                                  'I0', In(T), 'I1', In(T),
                                  'O', Out(out_type if out_type else T),
                                  stateful=False,
                                  simulate=simulate,
                                  verilog_name="coreir_" + name,
                                  coreir_name=name,
                                  coreir_lib = "corebit")
        else:
            if issubclass(T, m.BFloat):
                coreir_lib = "float"
                if T.N != 16:
                    raise NotImplementedError("Only BFloat16 supported")
                coreir_genargs = {"exp_bits": 8, "frac_bits": 7}
            else:
                coreir_lib = "coreir"
                coreir_genargs = {"width": width}
            T = T[width]
            return DeclareCoreirCircuit("coreir_{}{}".format(name, width),
                                  'I0', In(T), 'I1', In(T),
                                  'O', Out(out_type if out_type else T),
                                  stateful=False,
                                  simulate=simulate,
                                  verilog_name="coreir_" + name,
                                  coreir_name=name,
                                  coreir_lib = coreir_lib,
                                  coreir_genargs=coreir_genargs)

    return Declare

DefineCoreirMul = declare_binop("mul", operator.mul)

def DefineCoreirAdd(width, T=m.Bits):
    def simulate_coreir_add(self, value_store, state_store):
        I0 = BitVector[width](value_store.get_value(self.I0))
        I1 = BitVector[width](value_store.get_value(self.I1))
        value_store.set_value(self.O, I0 + I1)
    if issubclass(T, m.BFloat):
        coreir_lib = "float"
        if T.N != 16:
            raise NotImplementedError("Only BFloat16 supported")
        coreir_genargs = {"exp_bits": 8, "frac_bits": 7} # , "has_cout": has_cout, "has_cin": has_cin}
    else:
        coreir_lib = "coreir"
        coreir_genargs = {"width": width} # , "has_cout": has_cout, "has_cin": has_cin}
    T = T[width]
    coreir_io = ['I0', In(T),
                 'I1', In(T),
                 'O', Out(T)]
    return DeclareCoreirCircuit(f"coreir_add{width}", *coreir_io,
            coreir_name="add", coreir_lib=coreir_lib,
            coreir_genargs=coreir_genargs,
            simulate=simulate_coreir_add)

@circuit_generator
def DefineAdd(N=None, cout=False, cin=False, width=None, T=m.Bits):
    if N is None:
        if width is None:
            raise ValueError("Either N or width must be not None")
        N = width
    elif width is not None:
        LOGGER.warning("Both N and width are not None, using N")
    has_cout = cout
    has_cin = cin
    if not has_cout and not has_cin:
        return DefineCoreirAdd(N, T)
    class Add(mantle.primitives.DeclareAdd(N, cin=has_cin, cout=has_cout)):
        @classmethod
        def definition(add):
            width = N
            if has_cout:
                width += 1
            CoreirAdd = DefineCoreirAdd(width, T)
            coreir_add = CoreirAdd()
            I0 = add.I0
            I1 = add.I1
            if has_cout:
                I0 = concat(add.I0, bits(0, n=1))
                I1 = concat(add.I1, bits(0, n=1))
            if has_cin:
                coreir_add_cin = CoreirAdd()
                wire(coreir_add_cin.I0, concat(bits(add.CIN), bits(0,
                    n=width-1)))
                wire(coreir_add_cin.I1, I0)
                I0 = coreir_add_cin.O
            wire(I0, coreir_add.I0)
            wire(I1, coreir_add.I1)
            O = coreir_add.O
            if has_cout:
                COUT = O[-1]
                O = O[:-1]
            wire(O, add.O)
            if has_cout:
                wire(COUT, add.COUT)
    return Add


@circuit_generator
def DefineSub(N, cout=False, cin=False, T=m.Bits):
    has_cout = cout
    has_cin = cin
    class Sub(mantle.primitives.DeclareSub(N, cin=has_cin, cout=has_cout, T=T)):
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


def DefineNegate(width):
    T = Bits[width]
    class _Negate(mantle.primitives.DeclareNegate(width)):
        @classmethod
        def definition(neg):
            CoreirNeg = DeclareCircuit("coreir_neg", "in", In(T),
                    "out", Out(T), coreir_name="neg", coreir_lib="coreir",
                    coreir_genargs={"width": width})
            coreir_neg = CoreirNeg()
            wire(neg.I, getattr(coreir_neg, "in"))
            wire(neg.O, coreir_neg.out)
    return _Negate


def DefineASR(width):
    T = Bits[width]
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

def ASR(width, **kwargs):
    return DefineASR(width)(**kwargs)


DefineCoreirMul = declare_binop("mul", operator.mul)

DefineMul = DefineCoreirMul


DefineCoreirUDiv = declare_binop("udiv", operator.truediv)

DefineUDiv = DefineCoreirUDiv


DefineCoreirSDiv = declare_binop("sdiv", operator.truediv)

DefineSDiv = DefineCoreirSDiv


DefineCoreirUMod = declare_binop("urem", operator.mod)

DefineUMod = DefineCoreirUMod


DefineCoreirSMod = declare_binop("srem", operator.mod)

DefineSMod = DefineCoreirSMod
