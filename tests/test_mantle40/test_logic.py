import pytest
import magma
from magma import compile
from magma.simulator.python_simulator import testvectors as simtest
from magma.testing.newfunction import testvectors as funtest
from magma.testing import check_files_equal
from mantle.lattice.mantle40.logic import \
    DefineReduceAnd, DefineReduceNAnd, \
    DefineReduceOr,  DefineReduceNOr, \
    DefineReduceXOr, DefineReduceNXOr, \
    DefineAnd, DefineNAnd, \
    DefineOr,  DefineNOr, \
    DefineXOr, DefineNXOr, \
    DefineInvert
from mantle.lattice.mantle40 import DefineLSR, DefineLSL, DefineASR

width = 2
mask = 2**width-1
height = 2
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


def test_lsr():
    Test = DefineLSR(width, shift)
    #sim( Test, lambda x, y: x >> y )
    com( Test, 'lsr{}x{}'.format(width,shift) )

def test_lsl():
    Test = DefineLSL(width, shift)
    #sim( Test, lambda x, y: x << y )
    com( Test, 'lsl{}x{}'.format(width,shift) )

def test_asr():
    Test = DefineASR(width, shift)
    #sim( Test, lambda x, y: x >> y )
    com( Test, 'asl{}x{}'.format(width,shift) )

