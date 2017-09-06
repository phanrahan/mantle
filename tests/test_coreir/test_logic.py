import os
import pytest
coreir = pytest.importorskip("coreir")
from magma import *
from magma.testing import check_files_equal
from mantle.coreir import And, Or, XOr, Not, Invert, ReduceAnd, ReduceOr, ReduceXOr


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


def test_coreir_bits():
    width = 4
    class TestCircuit(Circuit):
        name = "test_coreir_bits"
        IO = ["a", In(Bits(width)), "b", In(Bits(width)), "c", In(Bits(width)), "d", Out(Bits(width))]
        @classmethod
        def definition(circuit):
            d = Or(2, width)(Invert(width)(And(2, width)(circuit.a, circuit.b)), 
                      XOr(2, width)(circuit.b, circuit.c))
            wire(d, circuit.d)
    compile("build/test_coreir_bits", TestCircuit, output="coreir")
    assert check_files_equal(__file__, 
            "build/test_coreir_bits.json", "gold/test_coreir_bits.json")


def test_three_args():
    width = 4
    class TestCircuit(Circuit):
        name = "test_coreir_bits"
        IO = ["a", In(Bits(width)), "b", In(Bits(width)), "c", In(Bits(width)), "d", Out(Bits(width))]
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
        name = "test_coreir_bits"
        IO = ["a", In(Bits(width)), "b", In(Bits(width)), "c", In(Bits(width)), "d", Out(Bit)]
        @classmethod
        def definition(circuit):
            d = Or(3, None)(ReduceAnd(width)(circuit.a),
                            ReduceOr(width)(circuit.b),
                            ReduceXOr(width)(circuit.b))
            wire(d, circuit.d)
    compile("build/test_coreir_reduce", TestCircuit, output="coreir")
    assert check_files_equal(__file__, 
            "build/test_coreir_reduce.json", "gold/test_coreir_reduce.json")

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
