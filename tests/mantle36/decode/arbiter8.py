import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()

megawing.Switch.on(8)
megawing.LED.on(8)

main = megawing.main()
I = main.SWITCH
O = main.LED

arbiter = Arbiter(8)

wire( arbiter(I), O )

compile(sys.argv[1], main)
