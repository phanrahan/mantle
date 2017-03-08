import sys
from magma import *
from parts.xilinx.spartan6.primitives import LUT5x2
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(6)
megawing.LED.on(2)

main = megawing.main()
I = main.SWITCH
O = main.LED

lut = LUT5x2(16*[0,1],16*[1,0])

lut(I[0], I[1], I[2], I[3], I[4])
wire(lut.O5, O[0])
wire(lut.O6, O[1])

compile(sys.argv[1], main)


