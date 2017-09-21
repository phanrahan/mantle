from magma import *
from magma.testing import check_files_equal
from mantle.coreir.arith import DefineAdd, DefineSub


def test_add():
    compile("build/test_define_add", DefineAdd(4, cin=True, cout=True),
            output="coreir")
    assert check_files_equal(__file__,
            "build/test_define_add.json", "gold/test_define_add.json")


def test_sub():
    compile("build/test_define_sub", DefineSub(4, cin=True, cout=True),
            output="coreir")
    assert check_files_equal(__file__,
            "build/test_define_sub.json", "gold/test_define_sub.json")
