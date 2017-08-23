import os
os.environ['MANTLE'] = 'lattice'
from magma import wire
from magma.simulator_interactive_frontend import simulate
from magma.python_simulator import PythonSimulator
from magma.scope import Scope
from loam.boards.icestick import IceStick
from mantle.lattice.ice40.PLB import SB_LUT4

def test_lut4():
    icestick = IceStick()
    icestick.Clock.on()
    icestick.J1[0].rename('I0').input().on()
    icestick.J1[1].rename('I1').input().on()
    icestick.J1[2].rename('I2').input().on()
    icestick.J1[3].rename('I3').input().on()
    icestick.J3[0].rename('D0').output().on()

    main = icestick.main()

    lut = SB_LUT4(LUT_INIT="16'h8000")
    wire(main.I0, lut.I0)
    wire(main.I1, lut.I1)
    wire(main.I2, lut.I2)
    wire(main.I3, lut.I3)
    wire(lut.O, main.D0)

    simulator = PythonSimulator(main)
    scope = Scope()
    simulator.set_value(main.I0, scope, False)
    simulator.set_value(main.I1, scope, False)
    simulator.set_value(main.I2, scope, False)
    simulator.set_value(main.I3, scope, False)
    for j in range(2):
        simulator.step()
        simulator.evaluate()
    assert simulator.get_value(main.D0, scope) == False
    simulator.set_value(main.I0, scope, True)
    simulator.set_value(main.I1, scope, True)
    simulator.set_value(main.I2, scope, True)
    simulator.set_value(main.I3, scope, True)
    for j in range(2):
        simulator.step()
        simulator.evaluate()
    assert simulator.get_value(main.D0, scope) == True
