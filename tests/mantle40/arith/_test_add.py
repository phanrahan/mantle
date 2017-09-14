from mantle.lattice.mantle40.fulladder import FullAdder
from mantle.lattice.mantle40.adder import DefineAdders
from magma import *

def test_full_adder():
    compile("build/test_full_adder_coreir", FullAdder, output="coreir")
    assert magma_check_files_equal(__file__, "build/test_full_adder_coreir.json",
            "gold/test_full_adder_coreir.json")

def test_adders():
    compile("build/test_add4", DefineAdders(4, False, True), output="coreir")
    assert magma_check_files_equal(__file__, "build/test_add4_coreir.json",
            "gold/test_add4_coreir.json")

if __name__ == "__main__":
    test_full_adder()
