import operator

from magma import *
from magma.compatibility import IntegerTypes
from .logic import DefineFoldOp, get_length


def declare_binop(name, python_op, out_type=None, signed=False):
    def simulate(self, value_store, state_store):
        in0 = BitVector(value_store.get_value(self.in0), signed=signed)
        in1 = BitVector(value_store.get_value(self.in1), signed=signed)
        out = python_op(in0, in1).as_bool_list()
        if out_type is Bit:
            assert len(out) == 1, "out_type is Bit but the operation returned a list of length {}".format(len(out))
            out = out[0]
        value_store.set_value(self.out, out)

    @cache_definition
    def Declare(N, type_):
        T = type_(N)
        return DeclareCircuit("{}{}".format(name, N),
                              'in0', In(T), 'in1', In(T),
                              'out', Out(out_type if out_type else T),
                              stateful=False,
                              simulate=simulate,
                              verilog_name="coreir_" + name,
                              coreir_name=name,
                              coreir_lib = "coreir",
                              default_kwargs={"width": N})

    return Declare


DefineCoreirAdd = declare_binop("add", operator.add)


@cache_definition
def DefineAdd(n, cin=False, cout=False):
    width = n
    T = Bits(width)
    IO = ["I0", In(T), "I1", In(T)]
    if cin:
        IO += ["CIN", In(Bit)]
    IO += ["O", Out(T)]
    if cout:
        IO += ["COUT", Out(Bit)]

    circ = DefineCircuit("Add{}{}".format(width, T.__name__),
        *IO)

    if cout:
        width += 1

    add = DefineCoreirAdd(width, Bits)()
    for a, b in [(circ.I0, add.in0), (circ.I1, add.in1)]:
        if cout:
            a = concat(bits(0, n=1), a)
        wire(a, b)
    out = add.out
    if cin:
        add_cin = DefineCoreirAdd(width, Bits)()
        wire(concat(bits(0, n=width-1), bits(circ.CIN, n=1)), add_cin.in0)
        wire(out, add_cin.in1)
        out = add_cin.out
    if cout:
        wire(out[0], circ.COUT)
        out = out[1:]
    wire(out, circ.O)
    EndDefine()
    return circ

# def Add(height=2, width=1, T=UInt, **kwargs):
#     return DefineAdd(height, width, T)(**kwargs)
def Add(n, cin=False, cout=False, **kwargs):
    return DefineAdd(n, cin, cout)(**kwargs)


def add(*args, **kwargs):
    width = get_length(args[0])
    if not all(get_length(arg) == width for arg in args):
        # TODO: Something more specific than a ValueError?
        raise ValueError("Arguments to add should all be the same width")
    if not all(isinstance(arg, BitsType) for arg in args):
        # TODO: Something more specific than a ValueError?
        raise ValueError("Arguments to add should be all Bits"
                " {}".format([(arg, type(arg)) for arg in args]))
    adders = [Add(width, **kwargs) for _ in range(len(args) - 1)]
    curr = adders[0]
    wire(args[0], curr.I0)
    wire(args[1], curr.I1)
    if len(args) > 2:
        next_ = adders[1]
        for i in range(1, len(adders)):
            next_ = adders[i]
            wire(curr.O, next_.I0)
            wire(args[i + 1], next_.I1)
            curr = next_
    return curr.O


# def Sub(height=2, width=1, **kwargs):
#     return DefineSub(height, width)(**kwargs)
#
# def sub(*args, **kwargs):
#     width = get_length(args[0])
#     if not all(get_length(arg) == width for arg in args):
#         # TODO: Something more specific than a ValueError?
#         raise ValueError("Arguments to sub should all be the same width")
#     if not (all(isinstance(arg, SIntType) for arg in args)):
#         # TODO: Something more specific than a ValueError?
#         raise ValueError("Arguments to sub should be all SInts, not"
#                 " {}".format([(arg, type(arg)) for arg in args]))
#     type_ = type(args[0])
#     return Sub(len(args), width, **kwargs)(*args)

# DefineSSub = declare_binop("sub", SInt, SIntType, "__sub__", operator.sub)
# DefineSMul = declare_binop("mul", SInt, SIntType, "__mul__", operator.mul)
# DefineSDiv = declare_binop("sdiv", SInt, SIntType, "__div__", operator.truediv)
# declare_binop("sdiv", SInt, SIntType, "__truediv__", operator.truediv)
#
# # In mantle, LT = SLT
# DefineSLT = declare_binop("slt",  SInt, SIntType, "__lt__", operator.lt, out_type=Bit)
# DefineSLE = declare_binop("sle", SInt, SIntType, "__le__", operator.le, out_type=Bit)
# DefineSGT = declare_binop("sgt",  SInt, SIntType, "__gt__", operator.gt, out_type=Bit)
# DefineSGE = declare_binop("sge", SInt, SIntType, "__ge__", operator.ge, out_type=Bit)
#
#
# def simulate_neg(self, value_store, state_store):
#     _in = BitVector(value_store.get_value(getattr(self, "in")), signed=True)
#     out = (-_in).as_bool_list()
#     value_store.set_value(self.out, out)
#
#
# def DeclareNegate(N):
#     return DeclareCircuit("neg{}".format(N), 'in', In(SInt(N)), 'out',
#             Out(SInt(N)), simulate=simulate_neg, verilog_name="coreir_not",
#             coreir_name="not", coreir_lib="coreir", default_kwargs={"width": N})
#
#
# def __neg__(self):
#     return DeclareNegate(self.N)()(self)
#
# SIntType.__neg__ = __neg__
#
#
# DefineUAdd = declare_binop("add", UInt, UIntType, "__add__", operator.add)
# DefineUSub = declare_binop("sub", UInt, UIntType, "__sub__", operator.sub)
# DefineUMul = declare_binop("mul", UInt, UIntType, "__mul__", operator.mul)
# DefineUDiv = declare_binop("udiv", UInt, UIntType, "__div__", operator.truediv)
# declare_binop("udiv", UInt, UIntType, "__truediv__", operator.truediv)
#
# DefineULT = declare_binop("ult",  UInt, UIntType, "__lt__", operator.lt, out_type=Bit)
# DefineULE = declare_binop("ule", UInt, UIntType, "__le__", operator.le, out_type=Bit)
# DefineUGT = declare_binop("ugt",  UInt, UIntType, "__gt__", operator.gt, out_type=Bit)
# DefineUGE = declare_binop("uge", UInt, UIntType, "__ge__", operator.ge, out_type=Bit)
#
#
# def arithmetic_shift_right(self, other):
#     N = self.N
#     T = SInt(N)
#     if isinstance(other, IntegerTypes):
#         if other < 0:
#             raise ValueError("Second argument to arithmetic_shift_right must be "
#                     "positive, not {}".format(other))
#
#         def simulate_arithmetic_shift_right(self, value_store, state_store):
#             _in = BitVector(value_store.get_value(getattr(self, "in")), signed=True)
#             out = _in.arithmetic_shift_right(other)
#             value_store.set_value(self.out, out.as_bool_list())
#         circ =  DeclareCircuit("ashr{}".format(N), 'in', In(UInt(N)),
#                 'out', Out(T), verilog_name="coreir_ashr",
#                 coreir_name="ashr",
#                 coreir_lib = "coreir",
#                 simulate=simulate_arithmetic_shift_right)
#         return circ(width=self.N, SHIFTBITS=other)(self)
#     elif isinstance(other, Type):
#         if not isinstance(other, UIntType):
#             raise TypeError("Second argument to arithmetic_shift_right must be "
#                     "a UInt, not {}".format(type(other)))
#
#         def simulate(self, value_store, state_store):
#             in0 = BitVector(value_store.get_value(self.in0), signed=True)
#             in1 = BitVector(value_store.get_value(self.in1))
#             out = in0.arithmetic_shift_right(in1).as_bool_list()
#             value_store.set_value(self.out, out)
#
#         circ = DeclareCircuit("dashr{}".format(N), 'in0', In(T), 'in1',
#                 In(UInt(N)), 'out', Out(T), verilog_name="coreir_dashr",
#                 coreir_name="dashr", coreir_lib="coreir", simulate=simulate)
#         return circ(width=self.N)(self, other)
#     else:
#         raise TypeError(">> not implemented for argument 2 of type {}".format(
#             type(other)))
#
#
# SIntType.arithmetic_shift_right = arithmetic_shift_right
