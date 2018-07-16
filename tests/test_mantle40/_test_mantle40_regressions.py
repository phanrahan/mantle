from magma import *
set_mantle_target("ice40")
from mantle import*
from magma.simulator import PythonSimulator
from bit_vector import BitVector


def test_shift_sim():
    Shift = DefineLSL(8, 4)
    lsl_sim = PythonSimulator(Shift)

    I = BitVector(0x01, 8)
    O = BitVector(0x10, 8)

    lsl_sim.set_value(Shift.I, I)
    lsl_sim.evaluate()
    assert lsl_sim.get_value(Shift.O) == O
