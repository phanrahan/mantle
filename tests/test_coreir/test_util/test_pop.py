from hwtypes import BitVector
import magma as m
from mantle.util.compressor.pop import DefinePopCount
from magma.testing import check_files_equal
from magma.scope import Scope
from magma.simulator.coreir_simulator import CoreIRSimulator

def test_pop_count():
    PopCount8 = DefinePopCount(8)
    m.compile('build/popcount8', PopCount8, output="coreir")
    assert check_files_equal(__file__,
            "build/popcount8.json", "gold/popcount8.json")

    scope = Scope()
    sim = CoreIRSimulator(PopCount8, None)
    for I, expected_O in [(1, 1), (2, 1), (3, 2)]:
        sim.set_value(PopCount8.I, BitVector[8](I), scope)
        sim.evaluate()
        assert BitVector[8](sim.get_value(PopCount8.O, scope)).as_int() == expected_O
