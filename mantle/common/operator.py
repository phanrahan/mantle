from functools import wraps

from magma import *
from magma.bitutils import clog2
from mantle import And, NAnd, Or, NOr, XOr, NXOr, LSL, LSR, ASR, Not, Invert

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
            raise ValueError("All arguments should have the same length")
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
    width = get_length(arg)
    if width is None:
        return Not(**kwargs)(arg)
    else:
        return Invert(width, **kwargs)(arg)
