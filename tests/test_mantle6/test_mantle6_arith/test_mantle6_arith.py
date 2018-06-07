import pytest
from magma import compile
from magma.testing import check_files_equal
from mantle.xilinx.mantle6.arith import \
    DefineAdd, DefineSub, \
    DefineNegate, \
    DefineASR

widths = [2, 4]

def com(Test, name):
    name = 'test_{}'.format(name)
    build = 'build/' + name
    gold = 'gold/' + name
    compile(build, Test)
    assert check_files_equal(__file__, build+'.v', gold+'.v')


def test_add():
    for width in widths:
        Test = DefineAdd(width)
        com( Test, 'add{}'.format(width) )
    for width in widths:
        Test = DefineAdd(width, cin=True, cout=True)
        com( Test, 'adc{}'.format(width) )

def test_sub():
    for width in widths:
        Test = DefineSub(width)
        com( Test, 'sub{}'.format(width) )
    for width in widths:
        Test = DefineSub(width, cin=True, cout=True)
        com( Test, 'sbc{}'.format(width) )

def test_negate():
    for width in widths:
        Test = DefineNegate(width)
        com( Test, 'negate{}'.format(width) )

def test_asr():
    for width in widths:
        shift = width // 2
        Test = DefineASR(width, shift)
        com( Test, 'asr{}x{}'.format(width, shift) )
