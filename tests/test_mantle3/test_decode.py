import pytest
from magma import compile
from magma.testing import check_files_equal
from mantle.xilinx.mantle3.decode import DefineDecode

heights = [8, 16]
i = 4

def com(Test, name):
    name = 'test_{}'.format(name)
    build = 'build/' + name
    gold = 'gold/' + name
    compile(build, Test)
    assert check_files_equal(__file__, build+'.v', gold+'.v')

def test_decode():
    for height in heights:
        Test = DefineDecode(i, height)
        com( Test, 'decode{}'.format(height) )

