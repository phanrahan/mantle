from hwtypes import BitVector
from .logic import (
    And      , DefineAnd   , ReduceAnd ,
    NAnd     , DefineNAnd  , ReduceNAnd,
    Or       , DefineOr    , ReduceOr  ,
    NOr      , DefineNOr   , ReduceNOr ,
    XOr      , DefineXOr   , ReduceXOr ,
    NXOr     , DefineNXOr  , ReduceNXOr,
    Invert   , DefineInvert,
    Wire   , DefineWire,
    Not      ,
    DefineStaticLeftShift  , StaticLeftShift  , static_left_shift  ,
    DefineStaticRightShift , StaticRightShift , static_right_shift ,
    DefineLSL, LSL ,
    DefineLSR, LSR,
)

#from .fulladder import FullAdder
#from .halfadder import HalfAdder
from .arith import DefineAdd, DefineSub, DefineNegate, DefineASR, ASR, \
    DefineCoreirAdd, DefineCoreirMul, DefineMul, DefineUDiv, DefineSDiv, \
    DefineUMod, DefineSMod

from .FF import FF, DFF, DefineDFF, DefineCoreirReg
from .LUT import LUT

from .MUX import Mux2, Mux4, Mux8, Mux16, DefineMux, Mux, DefineCoreirMux
from .memory import DefineRAM, DefineMemory, DefineCoreirMem
from .compare import \
    DefineEQ, DefineCoreirEq, EQ, \
    DefineNE, DefineCoreirNeq, NE, \
    DefineULT, DefineCoreirUlt, ULT, \
    DefineULE, DefineCoreirUle, ULE, \
    DefineUGT, DefineCoreirUgt, UGT, \
    DefineUGE, DefineCoreirUge, UGE, \
    DefineSLT, DefineCoreirSlt, SLT, \
    DefineSLE, DefineCoreirSle, SLE, \
    DefineSGT, DefineCoreirSgt, SGT, \
    DefineSGE, DefineCoreirSge, SGE


from magma import bits, cache_definition, Circuit, Bits, wire, Out, In, Bit
import magma as m
from .util import DeclareCoreirCircuit

def DefineCoreirConst(width, value):
    def simulate_coreir_const(self, value_store, state_store):
        value_store.set_value(self.O, value)
    return DeclareCoreirCircuit(f"coreir_const{width}{value}", "O", Out(Bits[ width ]),
            coreir_name="const", coreir_lib="coreir",
            coreir_genargs={"width": width},
            coreir_configargs={"value": BitVector[width](value)},
            simulate=simulate_coreir_const)

def DefineCorebitConst(value):
    if not isinstance(value, bool) and not (isinstance(value, int) and value in {0, 1}):
        raise ValueError("DefineCorebitConst expects a boolean value or 0 or 1")
    def simulate_corebit_const(self, value_store, state_store):
        value_store.set_value(self.O, value)
    return DeclareCoreirCircuit(f"corebit_const{value}", "O", Out(Bit),
            coreir_name="const", coreir_lib="corebit",
            default_kwargs={"value": bool(value)},
            simulate=simulate_corebit_const)


def DefineTerm(width):
    def simulate_term(self, value_store, state_store):
        pass
    return DeclareCoreirCircuit(f"term", "I", In(Bits[ width ]),
                                coreir_name="term", coreir_lib="coreir",
                                coreir_genargs={"width": width},
                                simulate=simulate_term)


def Term(width):
    return DefineTerm(width)()


def DefineCorebitTerm():
    def simulate_corebit_term(self, value_store, state_store):
        pass
    return DeclareCoreirCircuit(f"corebit_term", "I", In(Bit),
                                coreir_name="term", coreir_lib="corebit",
                                simulate=simulate_corebit_term)


def CorebitTerm():
    return DefineCorebitTerm()()

from .register import DefineRegister, Register, register
