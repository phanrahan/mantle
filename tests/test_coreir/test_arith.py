from magma import *
from magma.testing import check_files_equal
from mantle.coreir.arith import add, Add, AddC

import os

CHECK_OUTPUT = os.environ.get("MANTLE_CHECK_COREIR_OUTPUT", False)


def test_add_two():
    T = UInt(4)
    class TestCircuit(Circuit):
        name = "test_add_two"
        IO = ["a", In(T), "b", In(T), "c", Out(T)]
        @classmethod
        def definition(circuit):
            c = add(circuit.a, circuit.b)
            wire(c, circuit.c)
    print(repr(TestCircuit))

    compile("build/test_add_two", TestCircuit, output="coreir")
    if CHECK_OUTPUT:
        assert check_files_equal(__file__,
                "build/test_add_two.json", "gold/test_add_two.json")


def test_add_three():
    T = UInt(4)
    class TestCircuit(Circuit):
        name = "test_add_three"
        IO = ["a", In(T), "b", In(T), "c", In(T), "d", Out(T)]
        @classmethod
        def definition(circuit):
            d = add(circuit.a, circuit.b, circuit.c)
            wire(d, circuit.d)
    print(repr(TestCircuit))

    compile("build/test_add_three", TestCircuit, output="coreir")
    if CHECK_OUTPUT:
        assert check_files_equal(__file__,
                "build/test_add_three.json", "gold/test_add_three.json")


def test_add_cout_two():
    T = UInt(4)
    class TestCircuit(Circuit):
        name = "test_add_cout_two"
        IO = ["I0", In(T), "I1", In(T), "O", Out(T), "COUT", Out(Bit)]
        @classmethod
        def definition(circuit):
            O, COUT = Add(4, cout=True)(circuit.I0, circuit.I1)
            wire(O, circuit.O)
            wire(COUT, circuit.COUT)
    print(repr(TestCircuit))

    compile("build/test_add_cout_two", TestCircuit, output="coreir")
    if CHECK_OUTPUT:
        assert check_files_equal(__file__,
                "build/test_add_cout_two.json", "gold/test_add_cout_two.json")


def test_add_cin_two():
    T = UInt(4)
    class TestCircuit(Circuit):
        name = "test_add_cin_two"
        IO = ["I0", In(T), "I1", In(T), "O", Out(T), "CIN", In(Bit)]
        @classmethod
        def definition(circuit):
            O = Add(4, cin=True)(circuit.I0, circuit.I1, circuit.CIN)
            wire(O, circuit.O)
    print(repr(TestCircuit))

    compile("build/test_add_cin_two", TestCircuit, output="coreir")
    if CHECK_OUTPUT:
        assert check_files_equal(__file__,
                "build/test_add_cin_two.json", "gold/test_add_cin_two.json")


def test_addc_two():
    T = UInt(4)
    class TestCircuit(Circuit):
        name = "test_addc_two"
        IO = ["I0", In(T), "I1", In(T), "O", Out(T), "CIN", In(Bit), "COUT", Out(Bit)]
        @classmethod
        def definition(circuit):
            O, COUT = AddC(4)(circuit.I0, circuit.I1, circuit.CIN)
            wire(O, circuit.O)
            wire(COUT, circuit.COUT)
    print(repr(TestCircuit))

    compile("build/test_addc_two", TestCircuit, output="coreir")
    if CHECK_OUTPUT:
        assert check_files_equal(__file__,
                "build/test_addc_two.json", "gold/test_addc_two.json")


# def test_sub():
#     T = SInt(4)
#     class TestCircuit(Circuit):
#         name = "test_sub"
#         IO = ["a", In(T), "b", In(T), "c", Out(T)]
#         @classmethod
#         def definition(circuit):
#             c = sub(circuit.a, circuit.b)
#             wire(c, circuit.c)
#
#     compile("build/test_sub", TestCircuit, output="coreir")
#     assert check_files_equal(__file__,
#             "build/test_sub.json", "gold/test_sub.json")
