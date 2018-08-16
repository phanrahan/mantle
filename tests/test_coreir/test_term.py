from magma import compile
from magma.testing import check_files_equal
from mantle.coreir import DefineCorebitTerm
from .util import wrap

def test_bit_term():
    CorebitTerm = DefineCorebitTerm()
    assert repr(CorebitTerm) == """\
corebit_term = DeclareCircuit("corebit_term", "I", In(Bit))"""
    compile("build/test_bit_term", wrap(CorebitTerm), output="coreir")
    assert check_files_equal(__file__,
            "build/test_bit_term.json", "gold/test_bit_term.json")
