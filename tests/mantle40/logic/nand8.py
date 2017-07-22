import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
for i in range(8):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

nand8 = NAndN(8)
nand8(main.J1)
wire(nand8.O, main.D5)

compile(sys.argv[1], main)
