import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(5)
megawing.LED.on(4)

main = megawing.main()
RESET = main.SWITCH[4]
I = main.SWITCH[0:4]
O = main.LED

reg = Register(4,r=True)

O( reg(I, RESET=RESET) )


compile(sys.argv[1], main)


