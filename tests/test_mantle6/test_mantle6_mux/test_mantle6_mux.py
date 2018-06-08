import pytest
from magma import compile, set_mantle_target
from magma.simulator.python_simulator import testvectors as simtest
from magma.testing.newfunction import testvectors as funtest
from magma.testing import check_files_equal

from mantle.xilinx.mantle6 import Mux2, Mux4, Mux8, Mux16, DefineMux

def sim(Test, TestFun):
    pass
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

#def test_mux2():
#    Test = Mux2
#    com( Test, 'mux2' )

#def test_mux4():
#    Test = Mux4
#    #sim( Test, lambda i, s: (i>>s)&1 )
#    com( Test, 'mux4' )

def test_mux8():
    Test = Mux8
    com( Test, 'mux8' )

def test_mux16():
    Test = Mux16
    com( Test, 'mux16' )

def test_mux():
    Test = DefineMux(2,2)
    com( Test, 'mux2x2' )

