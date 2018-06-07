import pytest
from magma import compile
from magma.testing import check_files_equal
from mantle.xilinx.mantle6.compare import \
    DefineEQ, DefineNE, \
    DefineUGE, DefineULE, DefineUGT, DefineULT, \
    DefineSGE, DefineSLE, DefineSGT, DefineSLT \

widths = [2, 4, 8]

def com(Test, name):
    name = 'test_{}'.format(name)
    build = 'build/' + name
    gold = 'gold/' + name
    compile(build, Test)
    assert check_files_equal(__file__, build+'.v', gold+'.v')


def test_eq():
    for width in widths:
        Test = DefineEQ(width)
        com( Test, 'eq{}'.format(width) )

def test_ne():
    for width in widths:
        Test = DefineNE(width)
        com( Test, 'ne{}'.format(width) )


def test_uge():
    for width in widths:
        Test = DefineUGE(width)
        com( Test, 'uge{}'.format(width) )

def test_ule():
    for width in widths:
        Test = DefineULE(width)
        com( Test, 'ule{}'.format(width) )

def test_ugt():
    for width in widths:
        Test = DefineUGT(width)
        com( Test, 'ugt{}'.format(width) )

def test_ult():
    for width in widths:
        Test = DefineULT(width)
        com( Test, 'ult{}'.format(width) )


def test_sge():
    for width in widths:
        Test = DefineSGE(width)
        com( Test, 'sge{}'.format(width) )

def test_sle():
    for width in widths:
        Test = DefineSLE(width)
        com( Test, 'sle{}'.format(width) )

def test_sgt():
    for width in widths:
        Test = DefineSGT(width)
        com( Test, 'sgt{}'.format(width) )

def test_slt():
    for width in widths:
        Test = DefineSLT(width)
        com( Test, 'slt{}'.format(width) )

