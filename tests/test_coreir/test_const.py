import os
os.environ["MANTLE"] = "coreir"
from magma import compile
from magma.testing import check_files_equal
from mantle.coreir import DefineCoreirConst


def test_const():
    Const8 = DefineCoreirConst(width=4, value=8)
    assert repr(Const8) == """\
coreir_const48 = DefineCircuit("coreir_const48", "out", Out(Bits(4)))
wire(0, coreir_const48.out[0])
wire(0, coreir_const48.out[1])
wire(0, coreir_const48.out[2])
wire(1, coreir_const48.out[3])
EndCircuit()"""
    compile("build/test_const", Const8, output="coreir")
    assert check_files_equal(__file__,
            "build/test_const.json", "gold/test_const.json")
