import pytest
import magma
from magma import compile
from magma.simulator.python_simulator import testvectors as simtest
from magma.testing.newfunction import testvectors as funtest
from magma.testing import check_files_equal
from mantle import DefineLSR, DefineLSL, DefineASR

width = 2
mask = 2**width-1
height = 2

def sim(Test, TestFun):
    tvsim = simtest(Test)
    print(tvsim)
    tvfun = funtest(Test, TestFun)
    print(tvfun)
    assert tvsim == tvfun

def com(Test, name):
    name = 'test_{}'.format(name)
    build = 'build/' + name
    gold = 'gold/' + name
    compile(build, Test)
    assert check_files_equal(__file__, build+'.v', gold+'.v')

def test_lsr():
    Test = DefineLSR(width)
    #sim( Test, lambda x, y: x >> y )
    com( Test, f'lsr{width}' )

def test_lsl():
    Test = DefineLSL(width)
    #sim( Test, lambda x, y: x << y )
    com( Test, f'lsl{width}' )

def test_asr():
    Test = DefineASR(width)
    #sim( Test, lambda x, y: x >> y )
    com( Test, f'asl{width}' )

