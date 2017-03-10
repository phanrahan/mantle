import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(6)
megawing.LED.on(4)

main = megawing.main()
I = main.SWITCH[0:4]
RESET = main.SWITCH[4]
SET = main.SWITCH[5]
O = main.LED

reg = Register(4,r=True,s=True)

O(reg(I, RESET=RESET, SET=SET))

compile(sys.argv[1], main)


