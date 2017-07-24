import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
for i in range(8):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

xor8 = ReduceXOr(8)
xor8(main.J1)
wire(xor8.O, main.D5)

compile(sys.argv[1], main)
