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


Register4 = DefineRegister(4,ce=True)
#print(Register4, Register4.IO)

reg = Register4()

O(reg(I, CE=CE))


compile(sys.argv[1], main)


