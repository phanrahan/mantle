import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, DFF

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('I').input().on()
icestick.J1[1].rename('CE').input().on()
icestick.D5.on()

main = icestick.main()

dff = DFF(ce=True)
dff(main.I, CE=main.CE)
wire(dff, main.D5)

compile(sys.argv[1], main)
