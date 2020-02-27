from magma import *
import magma as m
from hwtypes import BitVector
import hwtypes as ht
from magma.compatibility import IntegerTypes
import operator
from functools import reduce
from .util import DeclareCoreirCircuit


def get_length(value):
    if isinstance(value, m.Digital):
        return None
    elif isinstance(value, m.Array):
        return len(value)
    else:
        raise NotImplementedError("Cannot get_length of"
                " {}".format(type(value)))


def DefineFoldOp(DefineOp, name, height, width):
    if width is None:
        T = Bit
    else:
        T = Bits[width]
    IO = []
    for i in range(height):
        IO += ["I{}".format(i), In(T)]
    IO += ["O", Out(T)]
    circ = DefineCircuit("fold_{}{}{}".format(name, height, width), *IO)
    reduce_args = [getattr(circ, "I{}".format(i)) for i in range(height)]
    Op2 = DefineOp(2, width)
    wire(reduce(lambda x, y: Op2()(x, y), reduce_args), circ.O)
    EndDefine()
    return circ


def declare_bit_binop(name, python_op):
    def simulate(self, value_store, state_store):
        I0 = ht.Bit(value_store.get_value(self.I0))
        I1 = ht.Bit(value_store.get_value(self.I1))
        #O = python_op(I0, I1).as_bool_list()[0]
        O = int(python_op(I0, I1))
        value_store.set_value(self.O, O)

    return DeclareCoreirCircuit("{}".format(name),
                                'I0', In(Bit), 'I1', In(Bit), 'O', Out(Bit),
                                simulate=simulate,
                                verilog_name = "coreir_" + name,
                                firrtl_op  = name,
                                coreir_lib = "corebit")


def DefineCoreirReduce(op_name, python_op, width):
    def simulate(self, value_store, state_store):
        in_ = BitVector[width](value_store.get_value(self.I))
        O = reduce(python_op, in_)
        value_store.set_value(self.O, O)
    decl = DeclareCoreirCircuit(op_name, "I", In(Bits[width]), "O", Out(Bit),
            coreir_name = op_name,
            coreir_lib = "coreir",
            coreir_genargs = {"width": width},
            simulate = simulate)
    return decl

def DefineCoreirReduceAnd(width):
    return DefineCoreirReduce("andr", operator.and_, width)

def DefineCoreirReduceOr(width):
    return DefineCoreirReduce("orr", operator.or_, width)

def DefineCoreirReduceXOr(width):
    return DefineCoreirReduce("xorr", operator.xor, width)
    # class ReduceAnd(Circuit):
    #     name = f"reduce_and_{width}"
    #     IO = ["I", In(Bits(width)), "O", Out(Bit)]
    #     @classmethod
    #     def definition(io):
    #         circ = decl()
    #         wire(getattr(circ, "in"), io.I)
    #         wire(circ.out, io.O)
    # return ReduceAnd


def declare_bits_binop(name, python_op):

    def Declare(N):
        def simulate(self, value_store, state_store):
            I0 = BitVector[N](value_store.get_value(self.I0))
            I1 = BitVector[N](value_store.get_value(self.I1))
            O = python_op(I0, I1).as_bool_list()
            # print(f"{python_op}({I0}, {I1}), {out}")
            value_store.set_value(self.O, O)
        T = Bits[N]
        return DeclareCoreirCircuit("{}{}".format(name, N),
                                    'I0', In(T), 'I1', In(T), 'O', Out(T),
                                    simulate       = simulate,
                                    verilog_name   = "coreir_" + name,
                                    coreir_name    = name,
                                    coreir_lib     = "coreir",
                                    coreir_genargs = {"width": N})

    return Declare


@cache_definition
def DefineOp(op_name, DefineCoreirReduce, height, width):
    if width is None:
        T = Bit
    else:
        T = Bits[width]
    IO = []
    for i in range(height):
        IO += ["I{}".format(i), In(T)]
    IO += ["O", Out(T)]
    circ = DefineCircuit(f"{op_name}{height}x{width}", *IO)
    if width is None:
        reduce = DefineCoreirReduce(height)()
        for j in range(height):
            wire(reduce.I[j], getattr(circ, f"I{j}"))
        wire(reduce.O, circ.O)
    else:
        for i in range(width):
            reduce = DefineCoreirReduce(height)()
            for j in range(height):
                wire(reduce.I[j], getattr(circ, f"I{j}")[i])
            wire(reduce.O, circ.O[i])
    EndDefine()
    return circ

def DefineAnd(height=2, width=None):
    if height is 2:
        if width is None:
            return declare_bit_binop("and", operator.and_)
        else:
            return declare_bits_binop("and", operator.and_)(width)
    return DefineOp("And", DefineCoreirReduceAnd, height, width)


def And(height, width=None, **kwargs):
    return DefineAnd(height, width)(**kwargs)

def ReduceAnd(height=2, **kwargs):
    return uncurry(And(height, **kwargs))


def DefineNAnd(height=2, width=None):
    if width is None:
        T = Bit
    else:
        T = Bits[width]
    IO = []
    for i in range(height):
        IO += ["I{}".format(i), In(T)]
    IO += ["O", Out(T)]
    circ = DefineCircuit("NAnd{}{}".format(height, width),
        *IO)
    inputs = [getattr(circ, 'I{}'.format(i)) for i in range(height)]
    if width is None:
        inv = Not()
    else:
        inv = Invert(width)
    O = inv(And(height, width)(*inputs))
    wire(O, circ.O)
    EndDefine()
    return circ


def NAnd(height, width=None, **kwargs):
    return DefineNAnd(height, width)(**kwargs)

def ReduceNAnd(height=2, **kwargs):
    return uncurry(NAnd(height, **kwargs))


def simulate_bit_not(self, value_store, state_store):
    _in = ht.Bit(value_store.get_value(self.I))
    #O = (~_in).as_bool_list()[0]
    O = ~_in
    value_store.set_value(self.O, bool(O))


Not = DeclareCoreirCircuit("not", 'I', In(Bit), 'O', Out(Bit),
    simulate=simulate_bit_not, verilog_name="coreir_bitnot", coreir_lib="corebit")


def not_(arg, **kwargs):
    return Not(get_length(arg), **kwargs)(arg)


def DefineOr(height=2, width=None):
    if height is 2:
        if width is None:
            return declare_bit_binop("or", operator.or_)
        else:
            return declare_bits_binop("or", operator.or_)(width)
    return DefineOp("Or", DefineCoreirReduceOr, height, width)


def Or(height, width=None, **kwargs):
    return DefineOr(height, width)(**kwargs)

def ReduceOr(height=2, **kwargs):
    return uncurry(Or(height, **kwargs))


def DefineNOr(height=2, width=None):
    if width is None:
        T = Bit
    else:
        T = Bits[width]
    IO = []
    for i in range(height):
        IO += ["I{}".format(i), In(T)]
    IO += ["O", Out(T)]
    circ = DefineCircuit("NOr{}{}".format(height, width),
        *IO)
    inputs = [getattr(circ, 'I{}'.format(i)) for i in range(height)]
    if width is None:
        inv = Not()
    else:
        inv = Invert(width)
    O = inv(Or(height, width)(*inputs))
    wire(O, circ.O)
    EndDefine()
    return circ


def NOr(height, width=None, **kwargs):
    return DefineNOr(height, width)(**kwargs)

def ReduceNOr(height=2, **kwargs):
    return uncurry(NOr(height, **kwargs))


def DefineXOr(height=2, width=None):
    if height is 2:
        if width is None:
            return declare_bit_binop("xor", operator.xor)
        else:
            return declare_bits_binop("xor", operator.xor)(width)
    else:
        return DefineFoldOp(DefineXOr, "xor", height, width)


def XOr(height, width=None, **kwargs):
    return DefineXOr(height, width)(**kwargs)

def ReduceXOr(height=2, **kwargs):
    return uncurry(XOr(height, **kwargs))


def DefineNXOr(height=2, width=None):
    if width is None:
        T = Bit
    else:
        T = Bits[width]
    IO = []
    for i in range(height):
        IO += ["I{}".format(i), In(T)]
    IO += ["O", Out(T)]
    circ = DefineCircuit("NXOr{}{}".format(height, width),
        *IO)
    inputs = [getattr(circ, 'I{}'.format(i)) for i in range(height)]
    if width is None:
        inv = Not()
    else:
        inv = Invert(width)
    O = inv(XOr(height, width)(*inputs))
    wire(O, circ.O)
    EndDefine()
    return circ


def NXOr(height, width=None, **kwargs):
    return DefineNXOr(height, width)(**kwargs)

def ReduceNXOr(height=2, **kwargs):
    return uncurry(NXOr(height, **kwargs))

def DefineInvert(width):
    T = Bits[width]


    def simulate_bits_invert(self, value_store, state_store):
        _in = BitVector[width](value_store.get_value(self.I))
        O = (~_in).as_bool_list()
        value_store.set_value(self.O, O)
    return DeclareCoreirCircuit("Invert{}".format(width),
            'I', In(T), 'O', Out(T),
            simulate       = simulate_bits_invert,
            verilog_name   = "coreir_not",
            coreir_name    = "not",
            coreir_lib     = "coreir",
            coreir_genargs = {"width": width})

def Invert(width=None, **kwargs):
    return DefineInvert(width)(**kwargs)


def simulate_wire(self, value_store, state_store):
    value_store.set_value(self.O, value_store.get_value(self.I))


def DefineWire(width):
    if width is None:
        T = Bit
        coreir_lib = "corebit"
        genargs = None
    else:
        T = Bits[width]
        coreir_lib = "coreir"
        genargs = {"width": width}
    return DeclareCoreirCircuit("Wire{}".format(width),
            'I', In(T), 'O', Out(T),
            simulate       = simulate_wire,
            coreir_name    = "wire",
            coreir_lib     = coreir_lib,
            coreir_genargs = genargs)

def Wire(width=None, **kwargs):
    return DefineWire(width)(**kwargs)


def invert(arg, **kwargs):
    return Invert(get_length(arg), **kwargs)(arg)


def DefineLSL(width):
    T = Bits[width]
    def simulate(self, value_store, state_store):
        I0 = BitVector[width](value_store.get_value(self.I0))
        I1 = BitVector[width](value_store.get_value(self.I1))
        O = (I0 << I1).as_bool_list()
        value_store.set_value(self.O, O)

    return DeclareCoreirCircuit("shl{}".format(width), 'I0', In(T), 'I1',
            In(UInt[width]), 'O', Out(T), verilog_name="coreir_shl",
            coreir_name="shl", coreir_lib="coreir", simulate=simulate,
            coreir_genargs={"width": width})


def LSL(width, **kwargs):
    return DefineLSL(width)(**kwargs)


def DefineLSR(width):
    T = Bits[width]
    def simulate(self, value_store, state_store):
        I0 = BitVector[width](value_store.get_value(self.I0))
        I1 = BitVector[width](value_store.get_value(self.I1))
        O = (I0 << I1).as_bool_list()
        value_store.set_value(self.O, O)

    return DeclareCoreirCircuit("lshr{}".format(width), 'I0', In(T), 'I1',
            In(UInt[width]), 'O', Out(T), verilog_name="coreir_lshr",
            coreir_name="lshr", coreir_lib="coreir", simulate=simulate,
            coreir_genargs={"width": width})


def LSR(width, **kwargs):
    return DefineLSR(width)(**kwargs)


def DefineStaticLeftShift(width, shift_amount):
    T = Bits[width]
    class _StaticLeftShift(Circuit):
        name = 'StaticLeftShift_{}{}'.format(width, shift_amount)

        IO = ["I", In(T), "O", Out(T)]

        @classmethod
        def definition(io):
            output = concat(io.I[shift_amount:width], bits(0, shift_amount))
            wire(output, io.O)
    return _StaticLeftShift

def StaticLeftShift(width, shift_amount, **kwargs):
    return DefineStaticLeftShift(width, shift_amount)(**kwargs)

def static_left_shift(arg, shift_amount, **kwargs):
    width = get_length(arg)
    return StaticLeftShift(width, shift_amount, **kwargs)(arg)

def DefineStaticRightShift(width, shift_amount):
    T = Bits[width]
    class _StaticRightShift(Circuit):
        name = 'StaticRightShift_{}{}'.format(width, shift_amount)

        IO = ["I", In(T), "O", Out(T)]

        @classmethod
        def definition(io):
            output = concat(bits(0, shift_amount), io.I[:width-shift_amount])
            wire(output, io.O)
    return _StaticRightShift

def StaticRightShift(width, shift_amount, **kwargs):
    return DefineStaticRightShift(width, shift_amount)(**kwargs)

def static_right_shift(arg, shift_amount, **kwargs):
    width = get_length(arg)
    return StaticRightShift(width, shift_amount, **kwargs)(arg)
