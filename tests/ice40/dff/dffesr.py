import sys
from magma import wire, compile
from mantle.lattice.ice40.PLB import SB_DFFESR
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('I0').input().on()
icestick.J1[1].rename('CE').input().on()
icestick.J1[2].rename('RESET').input().on()
icestick.J3[0].rename('D0').output().on()

main = icestick.main()

dff = SB_DFFESR()
wire(main.I0, dff.D)
wire(main.CE, dff.E)
wire(main.RESET, dff.R)
wire(dff.Q, main.D0)

compile(sys.argv[1], main)
