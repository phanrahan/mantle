import pytest
import magma
from magma import compile
from magma.testing import check_files_equal
from mantle.lattice.mantle40.compare import \
    DefineEQ, DefineNE, \
    DefineUGE, DefineULE, DefineUGT, DefineULT, \
    DefineSGE, DefineSLE, DefineSGT, DefineSLT \
from fault.test_vectors import generate_function_test_vectors, \
    generate_simulator_test_vectors

width = 2
mask = 2**width-1

def sim(Test, TestFun):
    tvsim = generate_simulator_test_vectors(Test)
    tvfun = generate_function_test_vectors(Test, TestFun)
    assert tvsim == tvfun

def com(Test, name):
    name = 'test_{}'.format(name)
    build = 'build/' + name
    gold = 'gold/' + name
    compile(build, Test)
    assert check_files_equal(__file__, build+'.v', gold+'.v')


def test_eq():
    Test = DefineEQ(width)
    sim( Test, lambda x, y: int(x == y) )
    com( Test, 'eq{}'.format(width) )

def test_ne():
    Test = DefineNE(width)
    sim( Test, lambda x, y: int(x != y) )
    com( Test, 'ne{}'.format(width) )


def test_uge():
    Test = DefineUGE(width)
    sim( Test, lambda x, y: int(x >= y) )
    com( Test, 'uge{}'.format(width) )

def test_ule():
    Test = DefineULE(width)
    sim( Test, lambda x, y: int(x <= y) )
    com( Test, 'ule{}'.format(width) )

def test_ugt():
    Test = DefineUGT(width)
    sim( Test, lambda x, y: int(x > y) )
    com( Test, 'ugt{}'.format(width) )

def test_ult():
    Test = DefineULT(width)
    sim( Test, lambda x, y: int(x < y) )
    com( Test, 'ult{}'.format(width) )


def test_sge():
    Test = DefineSGE(width)
    print(Test.interface)
    sim( Test, lambda x, y: int(x >= y) )
    com( Test, 'sge{}'.format(width) )

def test_sle():
    Test = DefineSLE(width)
    sim( Test, lambda x, y: int(x <= y) )
    com( Test, 'sle{}'.format(width) )

def test_sgt():
    Test = DefineSGT(width)
    sim( Test, lambda x, y: int(x > y) )
    com( Test, 'sgt{}'.format(width) )

def test_slt():
    Test = DefineSLT(width)
    sim( Test, lambda x, y: int(x < y) )
    com( Test, 'slt{}'.format(width) )

