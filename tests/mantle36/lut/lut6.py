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

lut = LUT6(32*[0,1])

lut(I[0], I[1], I[2], I[3], I[4], I[5])
wire(lut.O, O)

compile(sys.argv[1], main)


