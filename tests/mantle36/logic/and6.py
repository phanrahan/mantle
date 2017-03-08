import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(6)
megawing.LED.on(1)

main = megawing.main()
I = main.SWITCH
O = main.LED[0]

a = AndN(6)

a(I)
wire(a.O, O)

compile(sys.argv[1], main)


