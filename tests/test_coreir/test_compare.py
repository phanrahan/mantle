from magma import *
from magma.testing import check_files_equal
from mantle.coreir.compare import EQ, NE


def test_eq_two():
    T = UInt(4)
    class TestCircuit(Circuit):
        name = "test_eq_two"
        IO = ["a", In(T), "b", In(T), "c", Out(Bit)]
        @classmethod
        def definition(circuit):
            c = EQ(4)(circuit.a, circuit.b)
            wire(c, circuit.c)
    print(repr(TestCircuit))

    compile("build/test_eq_two", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_eq_two.json", "gold/test_eq_two.json")


def test_ne_two():
    T = UInt(4)
    class TestCircuit(Circuit):
        name = "test_ne_two"
        IO = ["a", In(T), "b", In(T), "c", Out(Bit)]
        @classmethod
        def definition(circuit):
            c = NE(4)(circuit.a, circuit.b)
            wire(c, circuit.c)
    print(repr(TestCircuit))

    compile("build/test_ne_two", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_ne_two.json", "gold/test_ne_two.json")
