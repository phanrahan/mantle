import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()

megawing.Switch.on(4)
megawing.LED.on(3)

main = megawing.main()
A = main.SWITCH[0:2]
B = main.SWITCH[2:4]
O = main.LED[0:2]

subc2 = SubC(2)

subc2(A,B)
wire( subc2.O, O )
wire(subc2.COUT, main.LED[2])

compile(sys.argv[1], main)


