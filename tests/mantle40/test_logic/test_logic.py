import pytest
from magma import compile
from magma.testing import check_files_equal
from mantle.lattice.mantle40.arith import DefineAnd, DefineOr
from mantle.lattice.mantle40 import DefineLSR, DefineLSL, DefineASR

def test_lsr():
    width = 4
    shift = 2
    TestCircuit = DefineLSR(width, shift)
    compile("build/test_lsr", TestCircuit)
    assert check_files_equal(__file__, "build/test_lsr.v", "gold/test_lsr.v")

def test_lsl():
    width = 4
    shift = 2
    TestCircuit = DefineLSL(width, shift)
    compile("build/test_lsl", TestCircuit)
    assert check_files_equal(__file__, "build/test_lsl.v", "gold/test_lsl.v")

def test_asr():
    width = 4
    shift = 2
    TestCircuit = DefineASR(width, shift)
    compile("build/test_asr", TestCircuit)
    assert check_files_equal(__file__, "build/test_asr.v", "gold/test_asr.v")

def test_and():
    width = 4
    And4 = DefineAnd(width)
    compile("build/test_and4", And4)
    assert check_files_equal(__file__, "build/test_and4.v", "gold/test_and4.v")

def test_or():
    width = 4
    Or4 = DefineOr(width)
    compile("build/test_or4", Or4)
    assert check_files_equal(__file__, "build/test_or4.v", "gold/test_or4.v")


