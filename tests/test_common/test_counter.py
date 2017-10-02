from magma import *
from magma.simulator import PythonSimulator
from magma.bit_vector import BitVector
import os
os.environ["MANTLE"] = "lattice"
from mantle.common import DefineCounter, DefineDownCounter, DefineUpDownCounter
import types


def coroutine(func):
    class Coroutine:
        """
        Makes the initial call to __next__ upon construction to immediately
        start the routine.

        Overrides __getattr__ to support inspection of the local variables
        """
        def __init__(self, *args, **kwargs):
            self.definition = func
            self.reset(*args, **kwargs)

        def reset(self, *args, **kwargs):
            self.co = types.coroutine(self.definition)(*args, **kwargs)
            next(self.co)

        def __getattr__(self, key):
            return self.co.gi_frame.f_locals[key]

        def send(self, *args, **kwargs):
            return self.co.send(*args, **kwargs)

        def __next__(self):
            return next(self.co)
    return Coroutine


def check(circuit, sim, number_of_cycles):
    simulator = PythonSimulator(circuit, clock=circuit.CLK)
    for cycle in range(number_of_cycles):
        for i in range(2):
            simulator.step()
            simulator.evaluate()
        # Coroutine has an implicit __next__ call on construction so it already
        # is init it's initial state
        assert sim.O == BitVector(simulator.get_value(circuit.O)).as_int()
        print(sim.O)
        next(sim)


@coroutine
def counter4_sim():
    while True:
        for i in range(0, 1<<4):
            O = i
            yield O


def test_counter():
    Counter4 = DefineCounter(4)

    check(Counter4, counter4_sim(), 1<<4 * 2)

@coroutine
def down_counter4_sim():
    # Counter starts at 0, then counts down
    while True:
        O = 0
        yield O
        for i in range((1<<4) - 1, 0, -1):
            O = i
            print(O)
            yield O


def test_downcounter():
    DownCounter4 = DefineDownCounter(4)

    check(DownCounter4, down_counter4_sim(), 1<<4 * 2)
