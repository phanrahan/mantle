import pytest
coreir = pytest.importorskip("coreir")
from magma import *
from magma.bitutils import seq2int
from mantle.coreir.MUX import DefineMux, DefineCoreirMux, CommonlibMuxN
from magma.simulator.coreir_simulator import CoreIRSimulator
from mantle.common.counter import DefineUpDownCounter, DefineCeilFloorUpDownCounter
from magma.scope import Scope

def test_updown_counter():
    width = 2
    scope = Scope()
    counter = DefineUpDownCounter(width, False)

    sim = CoreIRSimulator(counter, counter.CLK,
                          namespaces=["commonlib", "mantle", "coreir", "global"])

    # This pattern tests corner cases.
    # Pattern: set D on first clock to underflow to 3, then hold by setting U and D for a clock,
    # finally, counter from 3 to 1 and back to 3
    u_pattern = [False, True, False, False, True, True]
    d_pattern = [True, True, True, True, False, False]
    out_pattern = [0, 3, 3, 2, 1, 2, 3]
    for i in range(len(u_pattern)):
        sim.set_value(counter.U, u_pattern[i], scope)
        sim.set_value(counter.D, d_pattern[i], scope)
        sim.evaluate()

        assert seq2int(sim.get_value(counter.O, scope)) == out_pattern[i]
        sim.advance_cycle()
        assert seq2int(sim.get_value(counter.O, scope)) == out_pattern[i+1]

def test_ceil_floor_updown_counter():
    scope = Scope()
    counter = DefineCeilFloorUpDownCounter(5, False)

    sim = CoreIRSimulator(counter, counter.CLK,
                          namespaces=["commonlib", "mantle", "coreir", "global"])

    # This pattern tests corner cases.
    # Pattern: set D on first clock to do nothing, then hold by setting U and D for a clock,
    # then count up to 4, then do nothing by trying to overflow, and finally hold by setting U and D for a clock
    u_pattern = [False, True, True, True, True, True, True, True]
    d_pattern = [True, True, False, False, False, False, False, True]
    out_pattern = [0, 0, 0, 1, 2, 3, 4, 4, 4]
    for i in range(len(u_pattern)):
        sim.set_value(counter.U, u_pattern[i], scope)
        sim.set_value(counter.D, d_pattern[i], scope)
        sim.evaluate()

        assert seq2int(sim.get_value(counter.O, scope)) == out_pattern[i]
        sim.advance_cycle()
        assert seq2int(sim.get_value(counter.O, scope)) == out_pattern[i+1]

