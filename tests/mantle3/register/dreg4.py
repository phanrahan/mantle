import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(4)
megawing.LED.on(4)

main = megawing.main()
I = main.SWITCH
O = main.LED

Register4 = DefineRegister(4)
#print(Register4, Register4.IO)

reg = Register4()

reg(I)
wire(reg.O, O)

compile(sys.argv[1], main)


