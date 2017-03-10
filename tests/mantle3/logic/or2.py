import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(2)
megawing.LED.on(1)

main = megawing.main()
A = main.SWITCH[0]
B = main.SWITCH[1]
O = main.LED[0]

or2 = Or2()

or2(A, B)
wire(or2.O, O)

compile(sys.argv[1], main)


