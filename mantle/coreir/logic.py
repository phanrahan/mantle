from magma import *
import operator
from functools import reduce


# # logical shifts
# __all__ += ['LeftShift', 'RightShift']


@cache_definition
def DefineFoldOp(DefineOp, name, height, width):
    if width is None:
        T = Bit
    else:
        T = Bits(width)
    IO = []
    for i in range(height):
        IO += ["in{}".format(i), In(T)]
    IO += ["out", Out(T)]
    circ = DefineCircuit("fold_{}{}{}".format(name, height, width), *IO)
    reduce_args = [getattr(circ, "in{}".format(i)) for i in range(height)]
    Op2 = DefineOp(2, width)
    wire(reduce(lambda x, y: Op2()(x, y), reduce_args), circ.out)
    EndDefine()
    return circ


def declare_bit_binop(name, python_op):
    def simulate(self, value_store, state_store):
        in0 = BitVector(value_store.get_value(self.in0))
        in1 = BitVector(value_store.get_value(self.in1))
        out = python_op(in0, in1).as_bool_list()[0]
        value_store.set_value(self.out, out)

    return DeclareCircuit("{}".format(name),
                          'in0', In(Bit), 'in1', In(Bit), 'out', Out(Bit),
                          simulate=simulate,
                          verilog_name = "coreir_" + name,
                          coreir_lib = "coreir")


BitAnd = declare_bit_binop("bitand", operator.and_)
BitOr  = declare_bit_binop("bitor", operator.or_)
BitXOr = declare_bit_binop("bitxor", operator.xor)


def declare_bits_binop(name, python_op):
    def simulate(self, value_store, state_store):
        in0 = BitVector(value_store.get_value(self.in0))
        in1 = BitVector(value_store.get_value(self.in1))
        out = python_op(in0, in1).as_bool_list()
        value_store.set_value(self.out, out)

    @cache_definition
    def Declare(N):
        T = Bits(N)
        return DeclareCircuit("{}{}".format(name, N),
                              'in0', In(T), 'in1', In(T), 'out', Out(T),
                              simulate       = simulate,
                              verilog_name   = "coreir_" + name,
                              coreir_name    = name,
                              coreir_lib     = "coreir",
                              default_kwargs = {"width": N})

    return Declare

DefineCoreirAnd = declare_bits_binop("and", operator.and_)

@cache_definition
def DefineAnd(height=2, width=None):
    if height is 2:
        if width is None:
            return BitAnd
        else:
            return DefineCoreirAnd(width)
    else:
        return DefineFoldOp(DefineAnd, "and", height, width)


def And(height, width=None, **kwargs):
    return DefineAnd(height, width)(**kwargs)

def ReduceAnd(height=2, **kwargs):
    return uncurry(And(height, **kwargs), prefix="in")


def and_(*args, **kwargs):
    width = get_length(args[0])
    if not all(get_length(x) == width for x in args):
        raise ValueError("All arguments should have the same length")
    return And(len(args), width, **kwargs)(*args)


@cache_definition
def DefineNAnd(height=2, width=None):
    if width is None:
        T = Bit
    else:
        T = Bits(width)
    IO = []
    for i in range(height):
        IO += ["in{}".format(i), In(T)]
    IO += ["out", Out(T)]
    circ = DefineCircuit("NAnd{}{}".format(height, width),
        *IO)
    inputs = [getattr(circ, 'in{}'.format(i)) for i in range(height)]
    if width is None:
        inv = Not()
    else:
        inv = Invert(width)
    out = inv(And(height, width)(*inputs))
    wire(out, circ.out)
    EndDefine()
    return circ


def NAnd(height, width=None, **kwargs):
    return DefineNAnd(height, width)(**kwargs)

def ReduceNAnd(height=2, **kwargs):
    return uncurry(NAnd(height, **kwargs), prefix="in")


def nand(*args, **kwargs):
    width = get_length(args[0])
    if not all(get_length(x) == width for x in args):
        raise ValueError("All arguments should have the same length")
    return NAnd(len(args), width, **kwargs)(*args)


def simulate_bit_not(self, value_store, state_store):
    _in = BitVector(value_store.get_value(getattr(self, "in")))
    out = (~_in).as_bool_list()[0]
    value_store.set_value(self.out, out)


DefineCoreirNot = DeclareCircuit("bitnot", 'in', In(Bit), 'out', Out(Bit),
    simulate=simulate_bit_not, verilog_name="coreir_bitnot", coreir_lib="coreir")

@cache_definition
def DefineNot(width=None):
    if width != None:
        raise ValueError("Not is only defined as a 1-bit operation, width must"
                " be None")
    return DefineCoreirNot

def Not(width=None):
    return DefineNot(width)()



DefineCoreirOr  = declare_bits_binop("or", operator.or_)


@cache_definition
def DefineOr(height=2, width=None):
    if height is 2:
        if width is None:
            return BitOr
        else:
            return DefineCoreirOr(width)
    else:
        return DefineFoldOp(DefineOr, "or", height, width)


def Or(height, width=None, **kwargs):
    return DefineOr(height, width)(**kwargs)

def ReduceOr(height=2, **kwargs):
    return uncurry(Or(height, **kwargs), prefix="in")


def or_(*args, **kwargs):
    width = get_length(args[0])
    if not all(get_length(x) == width for x in args):
        raise ValueError("All arguments should have the same length")
    return Or(len(args), width, **kwargs)(*args)


@cache_definition
def DefineNOr(height=2, width=None):
    if width is None:
        T = Bit
    else:
        T = Bits(width)
    IO = []
    for i in range(height):
        IO += ["in{}".format(i), In(T)]
    IO += ["out", Out(T)]
    circ = DefineCircuit("NOr{}{}".format(height, width),
        *IO)
    inputs = [getattr(circ, 'in{}'.format(i)) for i in range(height)]
    if width is None:
        inv = Not()
    else:
        inv = Invert(width)
    out = inv(Or(height, width)(*inputs))
    wire(out, circ.out)
    EndDefine()
    return circ


def NOr(height, width=None, **kwargs):
    return DefineNOr(height, width)(**kwargs)

def ReduceNOr(height=2, **kwargs):
    return uncurry(NOr(height, **kwargs), prefix="in")


def nor(*args, **kwargs):
    width = get_length(args[0])
    if not all(get_length(x) == width for x in args):
        raise ValueError("All arguments should have the same length")
    return NOr(len(args), width, **kwargs)(*args)


DefineCoreirXOr = declare_bits_binop("xor", operator.xor)


@cache_definition
def DefineXOr(height=2, width=None):
    if height is 2:
        if width is None:
            return BitXOr
        else:
            return DefineCoreirXOr(width)
    else:
        return DefineFoldOp(DefineXOr, "xor", height, width)


def XOr(height, width=None, **kwargs):
    return DefineXOr(height, width)(**kwargs)


def xor(*args, **kwargs):
    width = get_length(args[0])
    if not all(get_length(x) == width for x in args):
        raise ValueError("All arguments should have the same length")
    return XOr(len(args), width, **kwargs)(*args)

def ReduceXOr(height=2, **kwargs):
    return uncurry(XOr(height, **kwargs), prefix="in")


@cache_definition
def DefineNXOr(height=2, width=None):
    if width is None:
        T = Bit
    else:
        T = Bits(width)
    IO = []
    for i in range(height):
        IO += ["in{}".format(i), In(T)]
    IO += ["out", Out(T)]
    circ = DefineCircuit("NXOr{}{}".format(height, width),
        *IO)
    inputs = [getattr(circ, 'in{}'.format(i)) for i in range(height)]
    if width is None:
        inv = Not()
    else:
        inv = Invert(width)
    out = inv(XOr(height, width)(*inputs))
    wire(out, circ.out)
    EndDefine()
    return circ


def NXOr(height, width=None, **kwargs):
    return DefineXOr(height, width)(**kwargs)


def nxor(*args, **kwargs):
    width = get_length(args[0])
    if not all(get_length(x) == width for x in args):
        raise ValueError("All arguments should have the same length")
    return NXOr(len(args), width, **kwargs)(*args)

def ReduceNXOr(height=2, **kwargs):
    return uncurry(NXOr(height, **kwargs), prefix="in")


def simulate_bits_invert(self, value_store, state_store):
    _in = BitVector(value_store.get_value(getattr(self, "in")))
    out = (~_in).as_bool_list()
    value_store.set_value(self.out, out)

@cache_definition
def DefineInvert(width):
    T = Bits(width)
    return DeclareCircuit("Invert{}".format(width),
            'in', In(T), 'out', Out(T),
            simulate       = simulate_bits_invert,
            verilog_name   = "coreir_not",
            coreir_name    = "not",
            coreir_lib     = "coreir",
            default_kwargs = {"width": width})

def Invert(width=None, **kwargs):
    return DefineInvert(width)(**kwargs)


def invert(arg, **kwargs):
    return Invert(get_length(arg), **kwargs)(arg)
