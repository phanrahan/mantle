import pytest
coreir = pytest.importorskip("coreir")
from magma import *
from magma.testing import check_files_equal
from mantle.coreir import And, Or, XOr, Not, Invert, ReduceAnd, ReduceOr, ReduceXOr
from mantle.coreir import NAnd, NOr, NXOr, ReduceNAnd, ReduceNOr, ReduceNXOr
from mantle.coreir import static_left_shift, static_right_shift, Wire
from mantle import lsl, lsr
import fault


def test_coreir_bit():
    class TestCircuit(Circuit):
        name = "test_coreir_bit"
        IO = ["a", In(Bit), "b", In(Bit), "c", In(Bit), "d", Out(Bit)]
        @classmethod
        def definition(circuit):
            d = Or(2)(Not()(And(2)(circuit.a, circuit.b)),
                      XOr(2)(circuit.b, circuit.c))
            wire(d, circuit.d)
    compile("build/test_coreir_bit", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_bit.json", "gold/test_coreir_bit.json")


def test_coreir_bit_2():
    class TestCircuit(Circuit):
        name = "test_coreir_bit_2"
        IO = ["a", In(Bit), "b", In(Bit), "c", In(Bit), "d", Out(Bit)]
        @classmethod
        def definition(circuit):
            d = NOr(2)((NAnd(2)(circuit.a, circuit.b)),
                        NXOr(2)(circuit.b, circuit.c))
            wire(d, circuit.d)
    compile("build/test_coreir_bit_2", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_bit_2.json", "gold/test_coreir_bit_2.json")


def test_coreir_bits():
    width = 4
    class TestCircuit(Circuit):
        name = "test_coreir_bits"
        IO = ["a", In(Bits[ width ]), "b", In(Bits[ width ]), "c", In(Bits[ width ]), "d", Out(Bits[ width ])]
        @classmethod
        def definition(circuit):
            d = Or(2, width)(Invert(width)(And(2, width)(circuit.a, circuit.b)),
                      XOr(2, width)(circuit.b, circuit.c))
            wire(d, circuit.d)
    compile("build/test_coreir_bits", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_bits.json", "gold/test_coreir_bits.json")


def test_coreir_bits_2():
    width = 4
    class TestCircuit(Circuit):
        name = "test_coreir_bits_2"
        IO = ["a", In(Bits[ width ]), "b", In(Bits[ width ]), "c", In(Bits[ width ]), "d", Out(Bits[ width ])]
        @classmethod
        def definition(circuit):
            d = NOr(2, width)(NAnd(2, width)(circuit.a, circuit.b),
                      NXOr(2, width)(circuit.b, circuit.c))
            wire(d, circuit.d)
    compile("build/test_coreir_bits_2", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_bits_2.json", "gold/test_coreir_bits_2.json")


def test_three_args():
    width = 4
    class TestCircuit(Circuit):
        name = "test_coreir_three_args"
        IO = ["a", In(Bits[ width ]), "b", In(Bits[ width ]), "c", In(Bits[ width ]), "d", Out(Bits[ width ])]
        @classmethod
        def definition(circuit):
            d = Or(3, width)(circuit.a,
                             Invert(width)(And(3, width)(circuit.a, circuit.b, circuit.c)),
                             XOr(3, width)(circuit.b, circuit.c, circuit.a))
            wire(d, circuit.d)
    compile("build/test_coreir_three_args", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_three_args.json", "gold/test_coreir_three_args.json")


def test_reduce():
    width = 4
    class TestCircuit(Circuit):
        name = "test_coreir_reduce"
        IO = ["a", In(Bits[ width ]), "b", In(Bits[ width ]), "c", In(Bits[ width ]), "d", Out(Bit)]
        @classmethod
        def definition(circuit):
            d = Or(3, None)(ReduceAnd(width)(circuit.a),
                            ReduceOr(width)(circuit.b),
                            ReduceXOr(width)(circuit.b))
            wire(d, circuit.d)
    compile("build/test_coreir_reduce", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_reduce.json", "gold/test_coreir_reduce.json")


def test_reduce_2():
    width = 4
    class TestCircuit(Circuit):
        name = "test_coreir_reduce_2"
        IO = ["a", In(Bits[ width ]), "b", In(Bits[ width ]), "c", In(Bits[ width ]), "d", Out(Bit)]
        @classmethod
        def definition(circuit):
            d = Or(3, None)(ReduceNAnd(width)(circuit.a),
                            ReduceNOr(width)(circuit.b),
                            ReduceNXOr(width)(circuit.b))
            wire(d, circuit.d)
    compile("build/test_coreir_reduce_2", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_reduce_2.json", "gold/test_coreir_reduce_2.json")


def test_static_shift():
    width = 4
    class TestCircuit(Circuit):
        name = "test_coreir_static_shift"
        IO = ["a", In(Bits[ width ]), "b", In(Bits[ width ]), "c", Out(Bits[ width ])]
        @classmethod
        def definition(circuit):
            c = Or(2, width)(static_left_shift(circuit.a, 2),
                             static_right_shift(circuit.b, 3))
            wire(c, circuit.c)
    compile("build/test_coreir_static_shift", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_static_shift.json", "gold/test_coreir_static_shift.json")


def test_ls():
    width = 4
    class TestCircuit(Circuit):
        name = "test_coreir_ls"
        IO = ["a", In(Bits[ width ]), "b", In(UInt[ width ]), "c", Out(Bits[ width ])]
        @classmethod
        def definition(circuit):
            c = Or(2, width)(lsl(circuit.a, circuit.b),
                             lsr(circuit.a, circuit.b))
            wire(c, circuit.c)
    compile("build/test_coreir_ls", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_ls.json", "gold/test_coreir_ls.json")


def test_wire():
    width = 4
    class TestCircuit(Circuit):
        name = "test_coreir_wire"
        IO = ["a", In(Bits[ width ]), "b", Out(Bits[ width ]), "e", Out(Bit)]
        @classmethod
        def definition(circuit):
            c = Wire(width, name="c")
            wire(c(circuit.a), circuit.b)
            d = Wire(None, name="d")
            wire(d(circuit.a[0]), circuit.e)
    compile("build/test_coreir_wire", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_wire.json", "gold/test_coreir_wire.json")
    tester = fault.Tester(TestCircuit)
    for i in range(0, 1 << 4):
        tester.poke(TestCircuit.a, i)
        tester.eval()
        tester.expect(TestCircuit.b, i)
    tester.compile_and_run(target="python")

# def test_coreir_uint():
#     class TestCircuit(Circuit):
#         name = "test_coreir_uint"
#         IO = ["a", In(UInt(4)), "b", In(UInt(4)), "c", Out(UInt(4))]
#         @classmethod
#         def definition(circuit):
#             tmp1 = circuit.a + circuit.b
#             tmp2 = circuit.a - circuit.b
#             tmp3 = tmp1 * tmp2
#             tmp4 = tmp3 / circuit.a
#             wire(tmp4, circuit.c)
#     compile("build/test_coreir_uint", TestCircuit, output="coreir")
#     assert check_files_equal(__file__,
#             "build/test_coreir_uint.json", "gold/test_coreir_uint.json")

# def test_coreir_shift_register():
#     N = 4
#     Register4 = DefineRegister(4)
#     T = Bits(N)
#
#     class ShiftRegister(Circuit):
#         name = "ShiftRegister"
#         IO = ["I", In(T), "O", Out(T), "CLK", In(Clock)]
#         @classmethod
#         def definition(io):
#             regs = [Register4() for _ in range(N)]
#             wireclock(io, regs)
#             wire(io.I, getattr(regs[0], "in"))
#             fold(regs, foldargs={"in":"out"})
#             wire(regs[-1].out, io.O)
#
#     compile("build/test_shift_register_coreir", ShiftRegister, 'coreir')
#     assert check_files_equal(__file__,
#             "build/test_coreir_shift_register.json",
#             "gold/test_coreir_shift_register.json")
