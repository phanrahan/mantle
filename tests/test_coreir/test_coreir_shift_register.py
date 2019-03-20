import magma as m
from magma.simulator import PythonSimulator
from mantle import DefineRegister


def test_shift_register():
    N = 4
    Register4 = DefineRegister(4)
    T = m.Bits[ N ]

    class ShiftRegister(m.Circuit):
        name = "ShiftRegister"
        IO = ["I", m.In(T), "O", m.Out(T), "CLK", m.In(m.Clock)]
        @classmethod
        def definition(io):
            regs = [Register4() for _ in range(N)]
            m.wire(io.I, regs[0].I)
            m.fold(regs, foldargs={"I": "O"})
            m.wire(regs[-1].O, io.O)

    simulator = PythonSimulator(ShiftRegister, clock=ShiftRegister.CLK)
    expected = [0, 0, 0] + list(range(0, 1 << N, 3))[:-3]
    actual = []
    for i in range(0, 1 << N, 3):
        simulator.set_value(ShiftRegister.I, i)
        simulator.advance(2)
        actual.append(simulator.get_value(ShiftRegister.O))

    assert actual == expected

    m.compile("build/ShiftRegister", ShiftRegister, output="coreir")
    assert m.testing.check_files_equal(__file__, "build/ShiftRegister.json",
                                       "gold/ShiftRegister.json")
