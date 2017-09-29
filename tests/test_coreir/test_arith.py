from magma import *
from magma.testing import check_files_equal
from mantle.coreir.arith import DefineAdd


def test_add_cout_two():
    T = UInt(4)
    class TestCircuit(Circuit):
        name = "test_add_cout_two"
        IO = ["I0", In(T), "I1", In(T), "O", Out(T), "COUT", Out(Bit)]
        @classmethod
        def definition(circuit):
            O, COUT = DefineAdd(4, cout=True)()(circuit.I0, circuit.I1)
            wire(O, circuit.O)
            wire(COUT, circuit.COUT)
    print(repr(TestCircuit))

    compile("build/test_add_cout_two", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_add_cout_two.json", "gold/test_add_cout_two.json")


def test_add_cin_two():
    T = UInt(4)
    class TestCircuit(Circuit):
        name = "test_add_cin_two"
        IO = ["I0", In(T), "I1", In(T), "O", Out(T), "CIN", In(Bit)]
        @classmethod
        def definition(circuit):
            O = DefineAdd(4, cin=True)()(circuit.I0, circuit.I1, circuit.CIN)
            wire(O, circuit.O)
    print(repr(TestCircuit))

    compile("build/test_add_cin_two", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_add_cin_two.json", "gold/test_add_cin_two.json")


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
