import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(5)
megawing.LED.on(4)

main = megawing.main()
CE = main.SWITCH[4]
I = main.SWITCH[0:4]
O = main.LED

reg = Register(4,ce=True)

reg(I, CE=CE)
wire(reg.O, O)


compile(sys.argv[1], main)


