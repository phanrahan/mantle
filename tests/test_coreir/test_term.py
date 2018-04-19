import os
os.environ["MANTLE"] = "coreir"
from magma import compile
from magma.testing import check_files_equal
from mantle.coreir import DefineCorebitTerm

def test_bit_term():
    CorebitTerm = DefineCorebitTerm()
    assert repr(CorebitTerm) == """\
corebit_term = DefineCircuit("corebit_term", "in", In(Bit))
EndCircuit()"""
    compile("build/test_bit_term", CorebitTerm, output="coreir")
    assert check_files_equal(__file__,
            "build/test_bit_term.json", "gold/test_bit_term.json")
