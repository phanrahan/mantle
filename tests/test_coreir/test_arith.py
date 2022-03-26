import magma as m
from magma import *
from magma.testing import check_files_equal
from mantle.coreir.arith import DefineAdd, DefineSub, DefineNegate, DefineASR, \
    DefineUDiv, DefineSDiv, DefineUMod, DefineSMod, DefineMul
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
    args = ['I0', In(Bits[ 1 ]), 'I1', In(Bits[ 1 ]), 'O', Out(Bits[ 1 ]), 'COUT',  Out(Bit)] + \
        ClockInterface(False, False)
    testcircuit = DefineCircuit('test_add_cout_one', *args)
    add = DefineAdd(1, cout=True)()
    wire(testcircuit.I0, add.I0)
    wire(testcircuit.I1, add.I1)
    wire(testcircuit.O, add.O)
    wire(testcircuit.COUT, add.COUT)
    EndCircuit()


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


def test_mul():
    compile("build/test_mul", wrap(DefineMul(4)), output="coreir")
    assert check_files_equal(__file__,
            "build/test_mul.json", "gold/test_mul.json")


def test_udiv():
    compile("build/test_udiv", wrap(DefineUDiv(4)), output="coreir")
    assert check_files_equal(__file__,
            "build/test_udiv.json", "gold/test_udiv.json")


def test_sdiv():
    compile("build/test_sdiv", wrap(DefineSDiv(4)), output="coreir")
    assert check_files_equal(__file__,
            "build/test_sdiv.json", "gold/test_sdiv.json")


def test_umod():
    compile("build/test_umod", wrap(DefineUMod(4)), output="coreir")
    assert check_files_equal(__file__,
            "build/test_umod.json", "gold/test_umod.json")


def test_smod():
    compile("build/test_smod", wrap(DefineSMod(4)), output="coreir")
    assert check_files_equal(__file__,
            "build/test_smod.json", "gold/test_smod.json")
