import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('A0').input().on()
icestick.J1[1].rename('B0').input().on()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()
A = array(main.A0)
B = array(main.B0)
O = array(main.D1)

add = Add(1)
add(A, B)
wire(add.O[0], main.D1)
wire(add.COUT, main.D2)

compile(sys.argv[1], main)
