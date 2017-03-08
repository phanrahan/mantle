import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(3)
megawing.LED.on(1)

main = megawing.main()
I = main.SWITCH
O = main.LED[0]

lut = LUT3(4*[0,1])

lut(I[0], I[1], I[2])
wire(lut.O, O)

compile(sys.argv[1], main)


