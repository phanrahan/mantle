from magma import compile
from magma.testing import check_files_equal
from mantle.coreir import DefineCoreirConst, DefineCorebitConst
from .util import wrap


def test_const():
    Const8 = DefineCoreirConst(width=4, value=8)
    assert repr(Const8) == """\
coreir_const48 = DeclareCircuit("coreir_const48", "O", Out(Bits[4]))"""
    compile("build/test_const", wrap(Const8), output="coreir")
    assert check_files_equal(__file__,
            "build/test_const.json", "gold/test_const.json")


def test_bit_const():
    BitConst = DefineCorebitConst(value=1)
    assert repr(BitConst) == """\
corebit_const1 = DeclareCircuit("corebit_const1", "O", Out(Bit))"""
    compile("build/test_bit_const", wrap(BitConst), output="coreir")
    assert check_files_equal(__file__,
            "build/test_bit_const.json", "gold/test_bit_const.json")
