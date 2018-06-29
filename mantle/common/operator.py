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
        T = type(args[0])
        if not all(type(x) == T for x in args):
            raise TypeError("Currently Arguments to operators must be of the same type")
        return fn(width, *args, **kwargs)
    return wrapped

operators = {}

def _pass_closure_vars_as_args(*closure_args):
    def _wrapped(fn):
        @wraps(fn)
        def _wrapped_inner(*args, **kwargs):
            return fn(*closure_args, *args, **kwargs)
        return _wrapped_inner
    return _wrapped

def preserve_type(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        retval = fn(*args, **kwargs)
        T = type(args[0])
        if isinstance(T, UIntKind):
            return uint(retval)
        elif isinstance(T, SIntKind):
            return sint(retval)
        return retval
    return wrapper

for _operator_name, _Circuit in (
    ("and_", And),
    ("nand", NAnd),
    ("or_", Or),
    ("nor", NOr),
    ("xor", XOr),
    ("nxor", NXOr),
    ("add", Add),
    ("sub", Sub),
    # TODO: These lack implementations
    # ("mul", Mul),
    # ("div", Div)
):
    # Because Python uses dynamic scoping, the closures will use the
    # last value of _Circuit rather than capturing the lexical value.
    # Hacky workaround is to pass _Circuit as an argument to a
    # decorator so the "lexical" value is captured.
    @preserve_type
    @check_operator_args
    @_pass_closure_vars_as_args(_Circuit, _operator_name)
    def operator(circuit, name, width, *args, **kwargs):
        if name in ["add", "sub"]:
            # These don't have a height
            if len(args) > 2:
                raise Exception(f"{name} operator expects 2 arguments")
            return circuit(width, **kwargs)(*args)
        else:
            return circuit(len(args), width, **kwargs)(*args)
    operator.__name__ = _operator_name
    operator.__qualname__ = _operator_name
    operators[_operator_name] = operator
    exec(f"{_operator_name} = operator")

@preserve_type
def lsl(I0, I1, **kwargs):
    width = get_length(I0)
    shift = get_length(I1)
    T = type(I0)
    return LSL(width, **kwargs)(I0, I1)

@preserve_type
def lsr(I0, I1, **kwargs):
    width = get_length(I0)
    shift = get_length(I1)
    return LSR(width, **kwargs)(I0, I1)

@preserve_type
def asr(I0, I1, **kwargs):
    width = get_length(I0)
    shift = get_length(I1)
    return ASR(width, **kwargs)(I0, I1)

@preserve_type
def not_(arg, **kwargs):
    return Not(**kwargs)(arg)

@preserve_type
def invert(arg, **kwargs):
    width = get_length(arg)
    if width is None:
        return Not(**kwargs)(arg)
    else:
        return Invert(width, **kwargs)(arg)

@preserve_type
def neg(arg, **kwargs):
    if isinstance(arg, int):
        return -arg
    return Negate(get_length(arg), **kwargs)(arg)

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
    # ("__mul__", mul),
    # ("__div__", div)
]

@check_operator_args
def lt(width, I0, I1, **kwargs):
    if isinstance(I0, SIntType):
        return SLT(width, **kwargs)(I0, I1)
    else:
        return ULT(width, **kwargs)(I0, I1)

@check_operator_args
def le(width, I0, I1, **kwargs):
    if isinstance(I0, SIntType):
        return SLE(width, **kwargs)(I0, I1)
    else:
        return ULE(width, **kwargs)(I0, I1)

@check_operator_args
def gt(width, I0, I1, **kwargs):
    if isinstance(I0, SIntType):
        return SGT(width, **kwargs)(I0, I1)
    else:
        return UGT(width, **kwargs)(I0, I1)

@check_operator_args
def ge(width, I0, I1, **kwargs):
    if isinstance(I0, SIntType):
        return SGE(width, **kwargs)(I0, I1)
    else:
        return UGE(width, **kwargs)(I0, I1)

@check_operator_args
def eq(width, I0, I1, **kwargs):
    return EQ(width, **kwargs)(I0, I1)


relational_ops = [
    ("__lt__", lt),
    ("__le__", le),
    ("__gt__", gt),
    ("__ge__", ge)
]

for method, op in arithmetic_ops + relational_ops:
    setattr(SIntType, method, op)
    setattr(UIntType, method, op)

@preserve_type
def mux(I, S):
    if isinstance(S, int):
        return I[S]
    elif S.const():
        return I[seq2int(S.bits())]
    return Mux(len(I), get_length(I[0]))(*I, S)
