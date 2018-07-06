from .logic import (
    And      , DefineAnd   , ReduceAnd ,
    NAnd     , DefineNAnd  , ReduceNAnd,
    Or       , DefineOr    , ReduceOr  ,
    NOr      , DefineNOr   , ReduceNOr ,
    XOr      , DefineXOr   , ReduceXOr ,
    NXOr     , DefineNXOr  , ReduceNXOr,
    Invert   , DefineInvert,
    Not      ,
    DefineStaticLeftShift  , StaticLeftShift  , static_left_shift  ,
    DefineStaticRightShift , StaticRightShift , static_right_shift ,
    DefineLSL , LSL , lsl ,
    DefineLSR, LSR, lsr,
)

from .decode import decode, Decode, DefineDecode

from .arith import DefineAdd, DefineSub, DefineNegate, DefineASR, DefineCoreirAdd, DefineCoreirMul

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

@cache_definition
def DefineCoreirConst(width, value):
    class CoreirConst(Circuit):
        name = f"coreir_const{width}{value}"
        IO = ["out", Out(Bits(width))]
        @classmethod
        def definition(io):
            wire(io.out, bits(value, width))
    return CoreirConst

@cache_definition
def DefineCorebitConst(value):
    if not isinstance(value, bool) and not (isinstance(value, int) and value in {0, 1}):
        raise ValueError("DefineCorebitConst expects a boolean value or 0 or 1")
    class CorebitConst(Circuit):
        name = f"corebit_const{value}"
        IO = ["out", Out(Bit)]
        @classmethod
        def definition(io):
            wire(io.out, value)
    return CorebitConst

@cache_definition
def DefineCorebitTerm():
    class CorebitTerm(Circuit):
        name = f"corebit_term"
        IO = ["in", In(Bit)]
        @classmethod
        def definition(io):
            pass
    return CorebitTerm

CorebitTerm = DefineCorebitTerm()
