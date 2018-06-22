import pytest
from magma import compile
from magma.testing import check_files_equal
from mantle.xilinx.mantle3.logic import \
    DefineReduceAnd, DefineReduceNAnd, \
    DefineReduceOr,  DefineReduceNOr, \
    DefineReduceXOr, DefineReduceNXOr, \
    DefineAnd, DefineNAnd, \
    DefineOr,  DefineNOr, \
    DefineXOr, DefineNXOr, \
    DefineInvert, \
    DefineLSR, DefineLSL

from mantle.xilinx.mantle3 import DefineLSR, DefineLSL, DefineASR

width = 2
mask = 2**width-1
heights = [4, 8]
shift = 4

def com(Test, name):
    name = 'test_{}'.format(name)
    build = 'build/' + name
    gold = 'gold/' + name
    compile(build, Test)
    assert check_files_equal(__file__, build+'.v', gold+'.v')

def test_reduceand():
    for height in heights:
        Test = DefineReduceAnd(height)
        com( Test, 'reduceand{}'.format(height) )

def test_reducenand():
    for height in heights:
        Test = DefineReduceNAnd(height)
        com( Test, 'reducenand{}'.format(height) )

def test_reduceor():
    for height in heights:
        Test = DefineReduceOr(height)
        com( Test, 'reduceor{}'.format(height) )

def test_reducenor():
    for height in heights:
        Test = DefineReduceNOr(height)
        com( Test, 'reducenor{}'.format(height) )

def test_reducexor():
    for height in heights:
        Test = DefineReduceXOr(height)
        com( Test, 'reducexor{}'.format(height) )

def test_reducenxor():
    for height in heights:
        Test = DefineReduceNXOr(height)
        com( Test, 'reducenxor{}'.format(height) )


def test_and():
    for height in heights:
        Test = DefineAnd(height, width)
        com( Test, 'and{}x{}'.format(height,width) )

def test_nand():
    for height in heights:
        Test = DefineNAnd(height, width)
        com( Test, 'nand{}x{}'.format(height,width) )

def test_or():
    for height in heights:
        Test = DefineOr(height, width)
        com( Test, 'or{}x{}'.format(height,width) )

def test_nor():
    for height in heights:
        Test = DefineNOr(height, width)
        com( Test, 'nor{}x{}'.format(height,width) )

def test_xor():
    for height in heights:
        Test = DefineXOr(height, width)
        com( Test, 'xor{}x{}'.format(height,width) )

def test_nxor():
    for height in heights:
        Test = DefineNXOr(height, width)
        com( Test, 'nxor{}x{}'.format(height,width) )


def test_invert():
    Test = DefineInvert(width)
    com( Test, 'invert{}'.format(width) )


def test_lsr():
    for height in heights:
        shift = height // 2
        Test = DefineLSR(height, shift)
        com( Test, 'lsr{}x{}'.format(height,shift) )

def test_lsl():
    for height in heights:
        shift = height // 2
        Test = DefineLSL(height, shift)
        com( Test, 'lsl{}x{}'.format(height,shift) )

