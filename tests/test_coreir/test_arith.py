from magma import *
from magma.testing import check_files_equal
from mantle.coreir.arith import add, Add


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
    assert check_files_equal(__file__,
            "build/test_add_cout_two.json", "gold/test_add_cout_two.json")


# def test_addc():
#     T = UInt(4)
#     class TestCircuit(Circuit):
#         name = "test_addc"
#         IO = ["a", In(T), "b", In(T), "c", In(Bit), "d", Out(T), "e", Out(Bit)]
#         @classmethod
#         def definition(circuit):
#             addc = AddC(2, 4)
#             addc(circuit.a, circuit.b)
#             wire(circuit.c, addc.CIN)
#             wire(addc.out, circuit.d)
#             wire(addc.COUT, circuit.e)
#
#     compile("build/test_addc", TestCircuit, output="coreir")
#     assert check_files_equal(__file__,
#             "build/test_addc.json", "gold/test_addc.json")


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
