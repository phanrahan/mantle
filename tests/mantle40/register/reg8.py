import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

N = 8

icestick = IceStick()
icestick.Clock.on()
for i in range(N):
    icestick.J1[i].input().on()
    icestick.J3[i].output().on()

main = icestick.main()

reg = Register(N)
wire( reg(main.J1), main.J3 )

compile(sys.argv[1], main)
