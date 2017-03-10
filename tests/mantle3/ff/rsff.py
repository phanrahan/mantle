import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(2)
megawing.LED.on(1)

main = megawing.main()
S = main.SWITCH[0]
R = main.SWITCH[1]
O = main.LED[0]

ff = RSFF()

O( ff(R, S) )

compile(sys.argv[1], main)


