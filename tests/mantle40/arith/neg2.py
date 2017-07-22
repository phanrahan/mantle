import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.J1[0].rename('I0').input().on()
icestick.J1[1].rename('I1').input().on()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()
I = array(main.I0, main.I1)
O = array(main.D1, main.D2)

neg = Negate(2)

wire( neg(I), O )

compile(sys.argv[1], main)
