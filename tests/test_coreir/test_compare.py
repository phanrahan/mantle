from magma import *
from magma.testing import check_files_equal
from mantle.coreir.compare import EQ, NE, ULT, ULE, UGT, UGE, SLT, SLE, SGT, \
    SGE

def check(circuit_type):
    circuit_type_name = circuit_type.__name__
    print(circuit_type_name)
    T = UInt[ 4 ]
    class TestCircuit(Circuit):
        name = "test_{}_two".format(circuit_type_name)
        IO = ["a", In(T), "b", In(T), "c", Out(Bit)]
        @classmethod
        def definition(circuit):
            print(repr(circuit))
            c = circuit_type(4)(circuit.a, circuit.b)
            wire(c, circuit.c)
    print(repr(TestCircuit))

    compile("build/test_{}_two".format(circuit_type_name), TestCircuit,
            output="coreir")
    assert check_files_equal(__file__,
            "build/test_{}_two.json".format(circuit_type_name),
            "gold/test_{}_two.json".format(circuit_type_name))

def test_eq():
    check(EQ)

def test_ne():
    check(NE)

def test_ult():
    check(ULT)

def test_ule():
    check(ULE)

def test_ugt():
    check(UGT)

def test_uge():
    check(UGE)

def test_slt():
    check(SLT)

def test_sle():
    check(SLE)

def test_sgt():
    check(SGT)

def test_sge():
    check(SGE)
