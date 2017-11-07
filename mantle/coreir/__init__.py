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
def DefineCoreBitConst(value):
    if not isinstance(value, bool) and not (isinstance(value, int) and value in {0, 1}):
        raise ValueError("DefineCoreBitConst expects a boolean value or 0 or 1")
    class CoreBitConst(Circuit):
        name = f"corebit_const{value}"
        IO = ["out", Out(Bit)]
        @classmethod
        def definition(io):
            wire(io.out, value)
    return CoreBitConst

@cache_definition
def DefineCoreBitTerm():
    class CoreBitTerm(Circuit):
        name = f"corebit_term"
        IO = ["in", In(Bit)]
        @classmethod
        def definition(io):
            pass
    return CoreBitTerm

CoreBitTerm = DefineCoreBitTerm()
