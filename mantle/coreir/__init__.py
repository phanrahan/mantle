from .logic import (
    And      , DefineAnd   , ReduceAnd ,
    NAnd     , DefineNAnd  , ReduceNAnd,
    Or       , DefineOr    , ReduceOr  ,
    NOr      , DefineNOr   , ReduceNOr ,
    XOr      , DefineXOr   , ReduceXOr ,
    NXOr     , DefineNXOr  , ReduceNXOr,
    Invert   , DefineInvert,
    Not      , DefineNot   ,
    DefineStaticLeftShift  , StaticLeftShift  , static_left_shift  ,
    DefineStaticRightShift , StaticRightShift , static_right_shift ,
    DefineLSL , LSL , lsl ,
    DefineLSR, LSR, lsr,
)

from .arith import DefineAdd, DefineSub, DefineNegate, DefineASR, DefineCoreirAdd

from .FF import FF, DFF, DefineDFF, DefineCoreirReg
from .LUT import LUT

from .MUX import DefineMux, Mux, DefineCoreirMux
from .memory import DefineRAM, DefineMemory
from .compare import DefineEQ, EQ, \
                     DefineNE, NE, \
                     DefineULT, ULT, \
                     DefineULE, ULE, \
                     DefineUGT, UGT, \
                     DefineUGE, UGE, \
                     DefineSLT, SLT, \
                     DefineSLE, SLE, \
                     DefineSGT, SGT, \
                     DefineSGE, SGE

from magma import bits, cache_definition, Circuit, Bits, wire, Out

@cache_definition
def DefineCoreirConst(width, value):
    class CoreirConst(Circuit):
        name = f"coreir_const{width}{value}"
        IO = ["out", Out(Bits(width))]
        @classmethod
        def definition(io):
            wire(io.out, bits(value, width))
    return CoreirConst
