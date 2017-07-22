import os
os.environ["MANTLE"] = "lattice"

from magma import *
from magma.simulator_interactive_frontend import simulate
from mantle import *
from loam.boards.icestick import IceStick
from magma.python_simulator import PythonSimulator
from magma.scope import Scope

def bit_list_to_int(_list):
    return int("".join(str(int(i)) for i in _list[::-1]), 2)

def test_counter():
    icestick = IceStick()
    icestick.Clock.on()
    icestick.D1.on()
    icestick.D2.on()
    icestick.D3.on()
    main = icestick.main()
    count = Counter(2)
    wire(count.O[0], main.D1)
    wire(count.O[1], main.D2)
    wire(count.COUT, main.D3)

    simulator = PythonSimulator(main)
    scope = Scope()
    for i in range(2):
        for i in range(4):
            for j in range(2):
                simulator.step()
                simulator.evaluate()
            assert bit_list_to_int(simulator.get_value(count.O, scope)) == i
        assert int(simulator.get_value(main.D3, scope)) == 1


