import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(4)
megawing.LED.on(1)

main = megawing.main()

and2 = And4()

and2(main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3])
wire(and2, main.LED[0])

compile(sys.argv[1], main)


