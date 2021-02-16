import pytest
coreir = pytest.importorskip("coreir")
from magma import *
from magma.testing import check_files_equal
from mantle.coreir.MUX import DefineMux, DefineCoreirMux, CommonlibMuxN
from magma.simulator.coreir_simulator import CoreIRSimulator
from magma.scope import Scope


def test_coreir_mux_2xNone():
    mux = DefineMux(2, None)
    print(repr(mux))
    compile("build/test_coreir_mux2xNone", mux, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_mux2xNone.json", "gold/test_coreir_mux2xNone.json")


def test_coreir_mux_2x3():
    mux = DefineMux(2, 3)
    print(repr(mux))
    compile("build/test_coreir_mux2x3", mux, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_mux2x3.json", "gold/test_coreir_mux2x3.json")


def test_coreir_mux_2xTuple():
    A = Product.from_fields("anon", dict(a=Bit, b=Bits[2]))
    B = Product.from_fields("anon", dict(a=A, b=Bits[3]))
    mux = DefineMux(2, T=B)
    print(repr(mux))
    compile("build/test_coreir_mux2xTuple", mux, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_mux2xTuple.json", "gold/test_coreir_mux2xTuple.json")


def test_coreir_mux_4xNone():
    mux = DefineMux(4, None)
    print(repr(mux))
    compile("build/test_coreir_mux4xNone", mux, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_mux4xNone.json", "gold/test_coreir_mux4xNone.json")


def test_coreir_mux_4x3():
    mux = DefineMux(4, 3)
    print(repr(mux))
    compile("build/test_coreir_mux4x3", mux, output="coreir")
    assert check_files_equal(__file__,
            "build/test_coreir_mux4x3.json", "gold/test_coreir_mux4x3.json")

def test_two_coreir_muxes():
    width = 2
    scope = Scope()
    inType = Array[ width, In(BitIn) ]
    outType = Array[ width, Out(Bit) ]
    args = ['I', inType, 'S', In(Bit), 'O', outType] + ClockInterface(False, False)

    testcircuit = DefineCircuit('test_partition', *args)
    coreir_mux = DefineCoreirMux(None)()
    coreir_mux(testcircuit.I[0], testcircuit.I[1], testcircuit.S)
    wire(coreir_mux.O, testcircuit.O[0])
    cmux = CommonlibMuxN(2, 1)
    wire(cmux.I.data[0][0], testcircuit.I[0])
    wire(cmux.I.data[1][0], testcircuit.I[1])
    wire(cmux.I.sel[0], testcircuit.S)
    wire(cmux.out[0], testcircuit.O[1])

    EndCircuit()

    sim = CoreIRSimulator(testcircuit, testcircuit.CLK,
                          namespaces=["commonlib", "mantle", "coreir", "global"])
