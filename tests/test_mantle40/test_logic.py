import pytest
import magma
from magma import compile
from magma.testing import check_files_equal
from mantle.lattice.mantle40.logic import \
    DefineReduceAnd, DefineReduceNAnd, \
    DefineReduceOr,  DefineReduceNOr, \
    DefineReduceXOr, DefineReduceNXOr, \
    DefineAnd, DefineNAnd, \
    DefineOr,  DefineNOr, \
    DefineXOr, DefineNXOr, \
    DefineInvert
from fault.test_vectors import generate_function_test_vectors, \
    generate_simulator_test_vectors

width = 2
mask = 2**width-1
height = 2

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

def test_reduceand():
    Test = DefineReduceAnd(height)
    def f(x):
        res = 1
        for i in range(height):
            res &= (x >> i) & 1
        return res
    sim( Test, f )
    com( Test, 'reduceand{}'.format(height) )

def test_reducenand():
    def f(x):
        res = 1
        for i in range(height):
            res &= (x >> i) & 1
        return ~res & 1
    Test = DefineReduceNAnd(height)
    sim( Test, f )
    com( Test, 'reducenand{}'.format(height) )

def test_reduceor():
    Test = DefineReduceOr(height)
    def f(x):
        res = 0
        for i in range(height):
            res |= (x >> i) & 1
        return res
    sim( Test, f )
    com( Test, 'reduceor{}'.format(height) )

def test_reducenor():
    def f(x):
        res = 0
        for i in range(height):
            res |= (x >> i) & 1
        return ~res & 1
    Test = DefineReduceNOr(height)
    sim( Test, f )
    com( Test, 'reducenor{}'.format(height) )

def test_reducexor():
    Test = DefineReduceXOr(height)
    def f(x):
        res = 0
        for i in range(height):
            res ^= (x >> i) & 1
        return res
    sim( Test, f )
    com( Test, 'reducexor{}'.format(height) )

def test_reducenxor():
    def f(x):
        res = 0
        for i in range(height):
            res ^= (x >> i) & 1
        return ~res & 1
    Test = DefineReduceNXOr(height)
    sim( Test, f )
    com( Test, 'reducenxor{}'.format(height) )


def test_and():
    Test = DefineAnd(height, width)
    sim( Test, lambda x, y: x & y )
    com( Test, 'and{}x{}'.format(height,width) )

def test_nand():
    Test = DefineNAnd(height, width)
    sim( Test, lambda x, y: ~(x & y) & mask )
    com( Test, 'nand{}x{}'.format(height,width) )

def test_or():
    Test = DefineOr(height, width)
    sim( Test, lambda x, y: x | y )
    com( Test, 'or{}x{}'.format(height,width) )

def test_nor():
    Test = DefineNOr(height, width)
    sim( Test, lambda x, y: ~(x | y) & mask )
    com( Test, 'nor{}x{}'.format(height,width) )

def test_xor():
    Test = DefineXOr(height, width)
    sim( Test, lambda x, y: x ^ y )
    com( Test, 'xor{}x{}'.format(height,width) )

def test_nxor():
    Test = DefineNXOr(height, width)
    sim( Test, lambda x, y: ~(x ^ y) & mask )
    com( Test, 'nxor{}x{}'.format(height,width) )


def test_invert():
    Test = DefineInvert(width)
    sim( Test, lambda x: ~x & mask )
    com( Test, 'invert{}'.format(width) )


