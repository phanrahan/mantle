from magma import *
from magma.simulator_interactive_frontend import simulate
from mantle.lattice.ice40.PLB import SB_LUT4
from loam.boards.icestick import IceStick

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

simulate(main)
