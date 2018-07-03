from magma import *

from magma.simulator import PythonSimulator
from magma.scope import Scope
from magma.bit_vector import BitVector
from magma.bitutils import int2seq, seq2int
import mantle
from mantle.common import DefineRegister

def test_shift_register():
    N = 4
    Register4 = DefineRegister(4)
    T = Bits(N)

    class ShiftRegister(Circuit):
        name = "ShiftRegister"
        IO = ["I", In(T), "O", Out(T), "CLK", In(Clock)]
        @classmethod
        def definition(io):
            regs = [Register4() for _ in range(N)]
            wireclock(io, regs)
            wire(io.I, regs[0].I)
            fold(regs, foldargs={"I":"O"})
            wire(regs[-1].O, io.O)

    simulator = PythonSimulator(ShiftRegister, clock=ShiftRegister.CLK)
    expected = [0, 0, 0] + list(range(0, 1 << N, 3))[:-3]
    actual = []
    for i in range(0, 1 << N, 3):
        simulator.set_value(ShiftRegister.I, uint(i, N))
        simulator.advance(2)
        actual.append(seq2int(simulator.get_value(ShiftRegister.O)))

    assert actual == expected
