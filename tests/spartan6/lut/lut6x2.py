import sys
from magma import *
print('magma')
from mantle.xilinx.spartan6 import LUT6x2
print('lut')
from loam.shields.megawing import MegaWing
#print(LUT4)

megawing = MegaWing()
print('megawing')
megawing.Switch.on(6)
megawing.LED.on(2)

main = megawing.main()
I = main.SWITCH
O = main.LED

lut = LUT6x2(16*[0,1],16*[1,0])

lut(I[0], I[1], I[2], I[3], I[4], I[5])
wire(lut.O5, O[0])
wire(lut.O6, O[1])

compile(sys.argv[1], main)


