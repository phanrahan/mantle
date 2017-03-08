import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(1)
megawing.LED.on(1)

main = megawing.main()
A = main.SWITCH[0]
O = main.LED[0]

not1 = Not()

not1(A)
wire(not1.O, O)

compile(sys.argv[1], main)


