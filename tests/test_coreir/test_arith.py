from magma import *
from magma.testing import check_files_equal
from mantle.coreir.arith import add


def test_add():
    T = UInt(4)
    class TestCircuit(Circuit):
        name = "test_add"
        IO = ["a", In(T), "b", In(T), "c", Out(T)]
        @classmethod
        def definition(circuit):
            c = add(circuit.a, circuit.b)
            wire(c, circuit.c)

    compile("build/test_add", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_add.json", "gold/test_add.json")


def test_sub():
    T = SInt(4)
    class TestCircuit(Circuit):
        name = "test_sub"
        IO = ["a", In(T), "b", In(T), "c", Out(T)]
        @classmethod
        def definition(circuit):
            c = sub(circuit.a, circuit.b)
            wire(c, circuit.c)

    compile("build/test_sub", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_sub.json", "gold/test_sub.json")
