import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('SWITCH').input().on()
icestick.D1.on()

main = icestick.main()

ff = FF(1)
ff(main.SWITCH)
wire(ff, main.D1)

compile(sys.argv[1], main)
