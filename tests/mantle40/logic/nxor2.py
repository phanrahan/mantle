import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
for i in range(2):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

nxor2 = NXOr(2)
nxor2(main.J1[0], main.J1[1])
wire(nxor2.O, main.D5)

compile(sys.argv[1], main)
