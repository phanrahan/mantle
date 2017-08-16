from mantle.lattice.mantle40.fulladder import FullAdder
from magma import *

def test_full_adder():
    compile("build/test_full_adder_coreir", FullAdder, output="coreir")
    magma_check_files_equal(__file__, "build/test_full_adder_coreir.json",
            "gold/test_full_adder_coreir.json")

if __name__ == "__main__":
    test_full_adder()
