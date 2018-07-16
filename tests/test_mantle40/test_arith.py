import pytest
from magma import compile
from magma.testing import check_files_equal
from magma.testing.newfunction import testvectors as funtest
from magma.simulator.python_simulator import testvectors as simtest
from mantle.lattice.mantle40.halfadder import HalfAdder
import mantle
from mantle.lattice.mantle40.arith import \
    DefineAdd, DefineSub, DefineNegate

width = 2
mask = 2**width-1
shift = 2

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


def test_ha():
    Test = HalfAdder
    com( Test, 'ha' )

def test_fa():
    Test = mantle.FullAdder
    assert mantle.FullAdder is mantle.lattice.mantle40.FullAdder
    # This is actually true since FullAdder is cached based on the name, so the
    # redefinition doesn't cause a problem here
    # assert mantle.FullAdder is not mantle.common.arith.FullAdder
    com( Test, 'fa' )

def test_add():
    Test = DefineAdd(width)
    sim( Test, lambda x, y: (x + y) & mask )
    com( Test, 'add{}'.format(width) )

def test_sub():
    Test = DefineSub(width)
    sim( Test, lambda x, y: (x - y) & mask )
    com( Test, 'sub{}'.format(width) )

def test_negate():
    Test = DefineNegate(width)
    sim( Test, lambda x: -x & mask )
    com( Test, 'negate{}'.format(width) )

