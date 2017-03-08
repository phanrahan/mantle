import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(5)
megawing.LED.on(4)

main = megawing.main()
I = main.SWITCH[0:4]
SET = main.SWITCH[4]
O = main.LED

reg = Register(4,s=True)

O(reg(I, SET=SET))

compile(sys.argv[1], main)


