import pytest
from magma import compile
from magma.testing import check_files_equal
from magma.testing.newfunction import testvectors as funtest
#from magma.simulator.python_simulator import testvectors as simtest
from mantle.xilinx.mantle3.halfadder import HalfAdder
from mantle.xilinx.mantle3.fulladder import FullAdder
from mantle.xilinx.mantle3.arith import \
    DefineAdd, DefineSub, \
    DefineNegate, \
    DefineASR

width = 2
mask = 2**width-1
shift = 2

def sim(Test, TestFun):
    pass
    #tvsim = simtest(Test)
    #print(tvsim)
    #tvfun = funtest(Test, TestFun)
    #print(tvfun)
    #assert tvsim == tvfun

def com(Test, name):
    name = 'test_{}'.format(name)
    build = 'build/' + name
    gold = 'gold/' + name
    compile(build, Test)
    assert check_files_equal(__file__, build+'.v', gold+'.v')


def test_ha():
    Test = HalfAdder
    com( Test, 'ha' )

def test_fa():
    Test = FullAdder
    com( Test, 'fa' )

def test_add():
    Test = DefineAdd(width)
    #sim( Test, lambda x, y: (x + y) & mask )
    com( Test, 'add{}'.format(width) )

def test_sub():
    Test = DefineSub(width)
    #sim( Test, lambda x, y: (x - y) & mask )
    com( Test, 'sub{}'.format(width) )

def test_negate():
    Test = DefineNegate(width)
    com( Test, 'negate{}'.format(width) )

def test_asr():
    Test = DefineASR(width, shift)
    com( Test, 'asr{}x{}'.format(width, shift) )
