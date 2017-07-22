import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('I0').input().on()
icestick.J1[1].rename('I1').input().on()
icestick.D5.on()

main = icestick.main()

srff = SRFF()

srff(main.I0, main.I1)

wire(srff, main.D5)

compile(sys.argv[1], main)
