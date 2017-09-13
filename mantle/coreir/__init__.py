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
    DefineDynamicLeftShift , DynamicLeftShift , dynamic_left_shift ,
    DefineDynamicRightShift, DynamicRightShift, dynamic_right_shift,
)

from .arith import (
    DefineAdd, Add, add,
    # DefineSub, Sub, sub,
)

from .mux import DefineMux, Mux
