import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
for i in range(2):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

xor2 = XOr(2)
xor2(main.J1[0], main.J1[1])
wire(xor2.O, main.D5)

compile(sys.argv[1], main)
