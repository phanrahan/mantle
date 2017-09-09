from magma import *
from magma.testing import check_files_equal
from mantle.coreir.arith import add, AddC


def test_add():
    T = UInt(4)
    class TestCircuit(Circuit):
        name = "test_add"
        IO = ["a", In(T), "b", In(T), "c", Out(T), "d", Out(Bit)]
        @classmethod
        def definition(circuit):
            c, carry = add(circuit.a, circuit.b)
            wire(c, circuit.c)
            wire(carry, circuit.d)

    compile("build/test_add", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_add.json", "gold/test_add.json")


def test_addc():
    T = UInt(4)
    class TestCircuit(Circuit):
        name = "test_addc"
        IO = ["a", In(T), "b", In(T), "c", In(Bit), "d", Out(T), "e", Out(Bit)]
        @classmethod
        def definition(circuit):
            addc = AddC(2, 4)
            addc(circuit.a, circuit.b)
            wire(circuit.c, addc.CIN)
            wire(addc.out, circuit.d)
            wire(addc.COUT, circuit.e)

    compile("build/test_addc", TestCircuit, output="coreir")
    assert check_files_equal(__file__,
            "build/test_addc.json", "gold/test_addc.json")


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
