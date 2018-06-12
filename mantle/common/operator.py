from functools import wraps

from magma import *
from magma.bitutils import clog2, seq2int
from mantle import And, NAnd, Or, NOr, XOr, NXOr, LSL, LSR, Not, Invert, EQ, ULT, ULE, UGT, UGE, SLT, SLE, SGT, SGE, Mux
from mantle.common.arith import ASR, Add, Sub, Negate

def get_length(value):
    if isinstance(value, (BitType, ClockType, EnableType, ResetType)):
        return None
    elif isinstance(value, ArrayType):
        return len(value)
    else:
        raise NotImplementedError("Cannot get_length of"
                " {}".format(type(value)))

def check_operator_args(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if len(args) < 2:
            raise RuntimeError("{} requires at least 2 arguments".format(fn.__name__))
        width = get_length(args[0])
        if not all(get_length(x) == width for x in args):
            raise ValueError(f"All arguments should have the same length: {args}")
        return fn(*args, **kwargs)
    return wrapped


@check_operator_args
def and_(*args, **kwargs):
    width = get_length(args[0])
    return And(len(args), width, **kwargs)(*args)


@check_operator_args
def nand(*args, **kwargs):
    width = get_length(args[0])
    return NAnd(len(args), width, **kwargs)(*args)


@check_operator_args
def or_(*args, **kwargs):
    width = get_length(args[0])
    return Or(len(args), width, **kwargs)(*args)


@check_operator_args
def nor(*args, **kwargs):
    width = get_length(args[0])
    return NOr(len(args), width, **kwargs)(*args)


@check_operator_args
def xor(*args, **kwargs):
    width = get_length(args[0])
    return XOr(len(args), width, **kwargs)(*args)


@check_operator_args
def nxor(*args, **kwargs):
    width = get_length(args[0])
    return NXOr(len(args), width, **kwargs)(*args)


def lsl(I0, I1, **kwargs):
    width = get_length(I0)
    shift = get_length(I1)
    if shift != clog2(width):
        raise ValueError("LSL shift should be equal to the clog2 of width")
    return LSL(width, **kwargs)(I0, I1)

def lsr(I0, I1, **kwargs):
    width = get_length(I0)
    shift = get_length(I1)
    if shift != clog2(width):
        raise ValueError("LSR shift should be equal to the clog2 of width")
    return LSR(width, **kwargs)(I0, I1)

def asr(I0, I1, **kwargs):
    width = get_length(I0)
    shift = get_length(I1)
    if shift != clog2(width):
        raise ValueError("ASR shift should be equal to the clog2 of width")
    return ASR(width, **kwargs)(I0, I1)

def not_(arg, **kwargs):
    return Not(**kwargs)(arg)

def invert(arg, **kwargs):
    width = get_length(arg)
    if width is None:
        return Not(**kwargs)(arg)
    else:
        return Invert(width, **kwargs)(arg)

def neg(arg, **kwargs):
    if isinstance(arg, int):
        return -arg
    return Negate(get_length(arg), **kwargs)(arg)

@check_operator_args
def eq(I0, I1, **kwargs):
    width = get_length(I0)
    return EQ(width, **kwargs)(I0, I1)

@check_operator_args
def add(I0, I1, **kwargs):
    width = get_length(I0)
    return Add(width, **kwargs)(I0, I1)

@check_operator_args
def sub(I0, I1, **kwargs):
    width = get_length(I0)
    return Sub(width)(I0, I1)

@check_operator_args
def mul(I0, I1, **kwargs):
    raise NotImplementedError("Coreir does not have Mul")
    width = get_length(I0)
    return Mul(width)(I0, I1)

@check_operator_args
def div(I0, I1, **kwargs):
    raise NotImplementedError("Coreir does not have Div")
    width = get_length(I0)
    return Div(width)(I0, I1)

bitwise_ops = [
    ("__and__", and_),
    ("__or__", or_),
    ("__xor__", xor),
    ("__invert__", invert),
    ("__lshift__", lsl),
    ("__rshift__", lsr),
    # ("__eq__", eq)
]

for method, op in bitwise_ops:
    setattr(BitType, method, op)
    setattr(BitsType, method, op)

arithmetic_ops = [
    ("__neg__", neg),
    ("__add__", add),
    ("__sub__", sub),
    ("__mul__", mul),
    ("__div__", div)
]

@check_operator_args
def lt(I0, I1, **kwargs):
    width = get_length(I0)
    if isinstance(I0, SIntType):
        return SLT(width)(I0, I1)
    else:
        return ULT(width)(I0, I1)

@check_operator_args
def le(I0, I1, **kwargs):
    width = get_length(I0)
    if isinstance(I0, SIntType):
        return SLE(width)(I0, I1)
    else:
        return ULE(width)(I0, I1)

@check_operator_args
def gt(I0, I1, **kwargs):
    width = get_length(I0)
    if isinstance(I0, SIntType):
        return SGT(width)(I0, I1)
    else:
        return UGT(width)(I0, I1)

@check_operator_args
def ge(I0, I1, **kwargs):
    width = get_length(I0)
    if isinstance(I0, SIntType):
        return SGE(width)(I0, I1)
    else:
        return UGE(width)(I0, I1)


relational_ops = [
    ("__lt__", lt),
    ("__le__", le),
    ("__gt__", gt),
    ("__ge__", ge)
]

for method, op in arithmetic_ops + relational_ops:
    setattr(SIntType, method, op)
    setattr(UIntType, method, op)

def mux(I, S):
    if isinstance(S, int):
        return I[S]
    elif S.const():
        return I[seq2int(S.bits())]
    return Mux(len(I), get_length(I[0]))(*I, S)
