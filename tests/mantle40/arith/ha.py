import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('A').input().on()
icestick.J1[1].rename('B').input().on()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()
A = main.A
B = main.B

ha = HalfAdder()

ha(A, B)

wire(ha.O, main.D1)
wire(ha.COUT, main.D2)

compile(sys.argv[1], main)
