import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(8)
megawing.LED.on(1)

main = megawing.main()
I = main.SWITCH
O = main.LED[0]

lut = LUT8(128*[0,1])

lut(I[0], I[1], I[2], I[3], I[4], I[5], I[6], I[7])
wire(lut.O, O)

compile(sys.argv[1], main)


