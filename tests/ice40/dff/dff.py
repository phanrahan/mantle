import sys
from magma import wire, compile
from mantle.lattice.ice40.PLB import SB_DFF
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('D').input().on()
icestick.J3[0].rename('Q').output().on()

main = icestick.main()

dff = SB_DFF()
wire(main.D, dff.D)
wire(dff.Q, main.Q)

compile(sys.argv[1], main)
