import pytest
import magma
from magma import compile
from fault.test_vectors import generate_function_test_vectors, generate_simulator_test_vectors
from magma.testing import check_files_equal
from mantle import DefineLSR, DefineLSL, DefineASR

width = 2
mask = 2**width-1
height = 2

def sim(Test, TestFun):
    return
    tvsim = generate_simulator_test_vectors(Test)
    tvfun = generate_function_test_vectors(Test, TestFun)
    assert tvsim == tvfun

def com(Test, name):
    name = '{}'.format(name)
    build = 'build/' + name
    gold = 'gold/' + name
    compile(build, Test)
    assert check_files_equal(__file__, build+'.v', gold+'.v')

def test_lsr():
    Test = DefineLSR(width)
    sim( Test, lambda x, y: x >> y )
    com( Test, f'lsr{width}' )

def test_lsl():
    Test = DefineLSL(width)
    sim( Test, lambda x, y: x << y )
    com( Test, f'lsl{width}' )

def test_asr():
    Test = DefineASR(width)
    sim( Test, lambda x, y: x >> y )
    com( Test, f'asr{width}' )

