from magma import *
from magma.testing import check_files_equal
from mantle.coreir.arith import DefineAdd, DefineSub, DefineNegate, DefineASR


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


def test_negate():
    compile("build/test_define_negate", DefineNegate(4),
            output="coreir")
    assert check_files_equal(__file__,
            "build/test_define_negate.json", "gold/test_define_negate.json")


def test_asr():
    compile("build/test_define_asr", DefineASR(4),
            output="coreir")
    assert check_files_equal(__file__,
            "build/test_define_asr.json", "gold/test_define_asr.json")
