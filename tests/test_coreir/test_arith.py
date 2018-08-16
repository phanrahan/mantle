import magma as m
from magma import *
from magma.testing import check_files_equal
from mantle.coreir.arith import DefineAdd, DefineSub, DefineNegate, DefineASR
from fault.test_vectors import generate_function_test_vectors, generate_simulator_test_vectors
from magma.simulator.coreir_simulator import CoreIRSimulator
from .util import wrap

def test_add():
    width = 4
    mask = 2**width-1
    Add = wrap(DefineAdd(width))
    assert generate_function_test_vectors(Add, lambda x, y: (x + y) & mask) == \
        generate_simulator_test_vectors(Add)

def test_add_cout_one():
    args = ['I0', In(Bits(1)), 'I1', In(Bits(1)), 'O', Out(Bits(1)), 'COUT',  Out(Bit)] + \
        ClockInterface(False, False)
    testcircuit = DefineCircuit('test_add_cout_one', *args)
    add = DefineAdd(1, cout=True)()
    wire(testcircuit.I0, add.I0)
    wire(testcircuit.I1, add.I1)
    wire(testcircuit.O, add.O)
    wire(testcircuit.COUT, add.COUT)
    EndCircuit()
    sim = CoreIRSimulator(testcircuit, testcircuit.CLK)


def test_add_cout_two():
    compile("build/test_add_cout_two", DefineAdd(4, cout=True), output="coreir")
    assert check_files_equal(__file__,
            "build/test_add_cout_two.json", "gold/test_add_cout_two.json")


def test_add_cin_two():
    compile("build/test_add_cin_two", DefineAdd(4, cin=True), output="coreir")
    assert check_files_equal(__file__,
            "build/test_add_cin_two.json", "gold/test_add_cin_two.json")


def test_sub_cout_two():
    compile("build/test_sub_cout_two", DefineSub(4, cout=True), output="coreir")
    assert check_files_equal(__file__,
            "build/test_sub_cout_two.json", "gold/test_sub_cout_two.json")


def test_sub_cin_two():
    compile("build/test_sub_cin_two", DefineSub(4, cin=True), output="coreir")
    assert check_files_equal(__file__,
            "build/test_sub_cin_two.json", "gold/test_sub_cin_two.json")


def test_negate():
    compile("build/test_negate", DefineNegate(4), output="coreir")
    assert check_files_equal(__file__,
            "build/test_negate.json", "gold/test_negate.json")


def test_asr():
    compile("build/test_asr", DefineASR(4), output="coreir")
    assert check_files_equal(__file__,
            "build/test_asr.json", "gold/test_asr.json")
