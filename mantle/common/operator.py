from functools import wraps

import magma as m
from magma.bitutils import seq2int
from mantle import And, NAnd, Or, NOr, XOr, NXOr, LSL, LSR, Not, Invert, UDiv, SDiv, UMod, SMod, Mul
from mantle import ASR
from mantle import EQ, NE, ULT, ULE, UGT, UGE, SLT, SLE, SGT, SGE
from mantle import Mux
from .arith import Add, Sub, Negate

__all__ = []


def get_length(value):
    if isinstance(value, m.Digital):
        return None
    elif isinstance(value, m.Array):
        return len(value)
    elif isinstance(value, int):
        return value.bit_length()
    else:
        raise NotImplementedError(f"Cannot get_length of {type(value)}")

def check_widths(width, args):
    for arg in args:
        arg_len = get_length(arg)
        # Allow integers with widths less than the width (they will be
        # promoted)
        if arg_len != width \
                and not ((isinstance(arg, int) and arg_len is 1 and width is None) or \
                         (isinstance(arg, int) and arg_len < width)):
            raise ValueError(
                f"All arguments should have the same length: {args}")


def check_operator_args(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if len(args) < 2:
            raise RuntimeError(
                f"{fn.__name__} requires at least 2 arguments")
        width = get_length(args[0])
        check_widths(width, args)
        T = type(args[0])
        if not (all(issubclass(type(x).__class__, T.__class__) for x in args) or (
                all(issubclass(T.__class__, type(x).__class__) for x in args))):
            raise TypeError(
                "Currently Arguments to operators must be of the same type")
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


def export(fn):
    global __all__
    __all__ += [fn.__name__]
    return fn


def preserve_type(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        retval = fn(*args, **kwargs)
        T = type(args[0])
        if issubclass(T, m.UInt):
            return m.uint(retval)
        elif issubclass(T, m.SInt):
            return m.sint(retval)
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
    ("mul", Mul),
    ("udiv", UDiv),
    ("sdiv", SDiv),
    ("umod", UMod),
    ("smod", SMod)
):
    __all__ += [_operator_name]

    # Because Python uses dynamic scoping, the closures will use the
    # last value of _Circuit rather than capturing the lexical value.
    # Hacky workaround is to pass _Circuit as an argument to a
    # decorator so the "lexical" value is captured.
    @preserve_type
    @check_operator_args
    @_pass_closure_vars_as_args(_Circuit, _operator_name)
    def operator(circuit, name, width, *args, **kwargs):
        for arg in args:
            if not isinstance(arg, (m.Type, int)):
                raise TypeError("Operators only defined on magma types and Python ints")
        if name == "le" and args[0].isinput :
            assert len(args) == 2, "Expected two arguments for assignment (<=)"
            if not isinstance(args[1], int) and not args[1].isoutput():
                raise TypeError("Can only assign an output to an input")
        else:
            for arg in args:
                if not isinstance(arg, int) and arg.isinput():
                    raise TypeError("Non-assigment operators are only defined on non input types")

        if name == "le" and args[0].isinput():
            # We could just call wire here, but we dispatch to the default
            # magma implementation so we only have to maintain the logic in one
            # place
            m.Type.__le__(args[0], args[1])
        else:
            if name in ["add", "sub", "mul", "udiv", "sdiv", 'umod', 'smod']:
                # These don't have a height
                if len(args) > 2:
                    raise Exception(f"{name} operator expects 2 arguments")
                return circuit(width, T=type(args[0]), **kwargs)(*args)
            else:
                return circuit(len(args), width, **kwargs)(*args)
    operator.__name__ = _operator_name
    operator.__qualname__ = _operator_name
    operators[_operator_name] = operator
    exec(f"{_operator_name} = operator")


@export
@preserve_type
def lsl(I0, I1, **kwargs):
    width = get_length(I0)
    return LSL(width, **kwargs)(I0, I1)


@export
@preserve_type
def lsr(I0, I1, **kwargs):
    width = get_length(I0)
    return LSR(width, **kwargs)(I0, I1)


@export
@preserve_type
def asr(I0, I1, **kwargs):
    width = get_length(I0)
    return ASR(width, **kwargs)(I0, I1)


@export
@preserve_type
def not_(arg, **kwargs):
    return Not(**kwargs)(arg)


@export
@preserve_type
def invert(arg, **kwargs):
    width = get_length(arg)
    if width is None:
        return Not(**kwargs)(arg)
    else:
        return Invert(width, **kwargs)(arg)


@export
@preserve_type
def neg(arg, **kwargs):
    if isinstance(arg, int):
        return -arg
    return Negate(get_length(arg), **kwargs)(arg)


def ite(self, a, b):
    assert type(a) == type(b)
    T = type(a)

    @m.circuit.combinational
    def ite(s: m.Bit, a: T, b: T) -> T:
        if s:
            return a
        else:
            return b
    return ite(self, a, b)


def adc(self, other, carry):
    assert type(self) == type(other)
    T = type(self)

    @m.circuit.combinational
    def adc(a: T, b: T, c: m.Bit) -> (T, m.Bit):
        a = m.uint(m.zext(a, 1))
        b = m.uint(m.zext(b, 1))
        c = m.uint(m.zext(m.bits(c, 1), len(T)))
        res = a + b + c
        return res[0:-1], res[-1]
    return adc(self, other, carry)


def overflow(self, other, result):
    assert type(self) == type(other)
    T = type(self)
    @m.circuit.combinational
    def overflow(a: T, b: T, res: T) -> m.Bit:
        msb_a = a[-1]
        msb_b = b[-1]
        N = res[-1]
        return (msb_a & msb_b & ~N) | (~msb_a & ~msb_b & N)
    return overflow(self, other, result)


arithmetic_ops = [
    ("__neg__", neg),
    ("__add__", add),
    ("__sub__", sub),
    ("__mul__", mul),
    ("adc", adc),
    ("overflow", overflow),
]


@export
@check_operator_args
def lt(width, I0, I1, **kwargs):
    if isinstance(I0, m.SIntType):
        return SLT(width, **kwargs)(I0, I1)
    else:
        return ULT(width, **kwargs)(I0, I1)


@export
@check_operator_args
def le(width, I0, I1, **kwargs):
    if I0.isinput():
        return m.Type.__le__(I0, I1)
    if isinstance(I0, m.SIntType):
        return SLE(width, **kwargs)(I0, I1)
    else:
        return ULE(width, **kwargs)(I0, I1)


@export
@check_operator_args
def gt(width, I0, I1, **kwargs):
    if isinstance(I0, m.SIntType):
        return SGT(width, **kwargs)(I0, I1)
    else:
        return UGT(width, **kwargs)(I0, I1)


@export
@check_operator_args
def ge(width, I0, I1, **kwargs):
    if isinstance(I0, m.SIntType):
        return SGE(width, **kwargs)(I0, I1)
    else:
        return UGE(width, **kwargs)(I0, I1)


@export
@check_operator_args
def eq(width, I0, I1, **kwargs):
    return EQ(width, **kwargs)(I0, I1)


@export
@check_operator_args
def ne(width, I0, I1, **kwargs):
    return NE(width, **kwargs)(I0, I1)


@export
@preserve_type
def mux(I, S, **kwargs):
    if isinstance(S, int):
        return I[S]
    elif S.const():
        return I[seq2int(S.bits())]
    T = type(I[0])
    # Support using Bits(1) for select on 2 elements
    if len(I) == 2 and isinstance(S, m.Array) and \
            issubclass(S.T, m.Digital) and len(S) == 1:
        S = S[0]
    return Mux(len(I), T=T, **kwargs)(*I, S)


orig_get_item = m.Array.__getitem__


def dynamic_mux_select(self, S):
    if isinstance(S, m.Type):
        if issubclass(self.T, m.Digital):
            length = None
        else:
            length = len(self.T)
        height = len(self)
        inputs = self.ts[:]
        if m.mantle_target == "ice40" and height not in [2, 4, 8, 16]:
            if height > 16:
                raise NotImplementedError()
            orig_height = height
            height = 2 ** m.bitutils.clog2(height)
            if not isinstance(inputs[0], m.Digital):
                raise NotImplementedError(type(inputs[0]))
            inputs.extend([m.bit(0) for _ in range(height - orig_height)])

        return Mux(height, length)(*inputs, S)
    return orig_get_item(self, S)


setattr(m.Array, "__getitem__", dynamic_mux_select)
