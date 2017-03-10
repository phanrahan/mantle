import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(1)
megawing.LED.on(1)

main = megawing.main()
I = main.SWITCH[0]
O = main.LED[0]

ff = FF()

O(ff(I))

compile(sys.argv[1], main)


