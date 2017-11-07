import os
os.environ["MANTLE"] = "coreir"
from magma import compile
from magma.testing import check_files_equal
from mantle.coreir import CoreBitTerm

def test_bit_term():
    assert repr(CoreBitTerm) == """\
corebit_term = DefineCircuit("corebit_term", "in", In(Bit))
EndCircuit()"""
    compile("build/test_bit_term", CoreBitTerm, output="coreir")
    assert check_files_equal(__file__,
            "build/test_bit_term.json", "gold/test_bit_term.json")
