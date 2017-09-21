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
        return DeclareCircuit("coreir_{}{}".format(name, N),
                              'in0', In(T), 'in1', In(T),
                              'out', Out(out_type if out_type else T),
                              stateful=False,
                              simulate=simulate,
                              verilog_name="coreir_" + name,
                              coreir_name=name,
                              coreir_lib = "coreir",
                              coreir_genargs={"width": N})

    return Declare


def coreir_add_sub_factory(op):
    class DefineCoreirOp(CircuitGenerator):
        base_name = "coreir_{}".format(op)
        def generate(self, N, has_cout=False, has_cin=False):
            T = Bits(N)
            IO = ['in0', In(T), 'in1', In(T), 'out', Out(T)]
            gen_args = {"width": N}
            if has_cout:
                IO += ['cout', Out(Bit)]
                gen_args['has_cout'] = True
            if has_cin:
                IO += ['cin', In(Bit)]
                gen_args['has_cin'] = True
            return DeclareCircuit(self.cached_name, *IO,
                              stateful=False,
                              verilog_name="coreir_{}".format(op),
                              coreir_name=op,
                              coreir_lib = "coreir",
                              coreir_genargs=gen_args)

    return DefineCoreirOp


DefineCoreirAdd = coreir_add_sub_factory("add")


class DefineAdd(CircuitGenerator):
    base_name = "Add"
    def generate(self, n, cin=False, cout=False):
        width = n
        T = Bits(width)
        IO = ["I0", In(T), "I1", In(T)]
        if cin:
            IO += ["CIN", In(Bit)]
        IO += ["O", Out(T)]
        if cout:
            IO += ["COUT", Out(Bit)]

        circ = DefineCircuit(self.cached_name, *IO)

        add = DefineCoreirAdd(width, has_cout=cout, has_cin=cin)()
        wire(circ.I0, add.in0)
        wire(circ.I1, add.in1)
        wire(circ.O, add.out)
        if cout:
            wire(circ.COUT, add.cout)
        if cin:
            wire(circ.CIN, add.cin)
        EndDefine()
        return circ


def Add(n, cin=False, cout=False, **kwargs):
    return DefineAdd(n, cin, cout)(**kwargs)


def AddC(n, **kwargs):
    return Add(n, cin=True, cout=True, **kwargs)


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

