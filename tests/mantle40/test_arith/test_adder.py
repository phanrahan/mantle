import pytest
from magma import compile
from magma.testing import check_files_equal
from mantle.lattice.mantle40.halfadder import HalfAdder
from mantle.lattice.mantle40.fulladder import FullAdder
from mantle.lattice.mantle40.arith import DefineAdd, DefineSub
from mantle.lattice.mantle40.arith import DefineASR

def test_asr():
    width = 4
    shift = 2
    TestCircuit = DefineASR(width, shift)
    compile("build/test_asr", TestCircuit)
    assert check_files_equal(__file__, "build/test_asr.v", "gold/test_asr.v")

def test_fa():
    compile("build/test_fa", FullAdder)
    assert check_files_equal(__file__, "build/test_fa.v", "gold/test_fa.v")

def test_ha():
    compile("build/test_ha", HalfAdder)
    assert check_files_equal(__file__, "build/test_ha.v", "gold/test_ha.v")

def test_add():
    width = 4
    Add4 = DefineAdd(width)
    compile("build/test_add4", Add4)
    assert check_files_equal(__file__, "build/test_add4.v", "gold/test_add4.v")

def test_sub():
    width = 4
    Sub4 = DefineSub(width)
    compile("build/test_sub4", Sub4)
    assert check_files_equal(__file__, "build/test_sub4.v", "gold/test_sub4.v")

