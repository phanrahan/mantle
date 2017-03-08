import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(1)
megawing.LED.on(1)

main = megawing.main()
I = main.SWITCH[0]
O = main.LED[0]

lut = LUT1([0,1])

lut(I)
wire(lut.O, O)

compile(sys.argv[1], main)


