import sys
from magma import *
from mantle.xilinx.spartan6.RAM import RAM32x2
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(2)

main = megawing.main()

ram = RAM32x2(16*[0,1], 16*[1,0])

wire(main.SWITCH[:5], ram.A)
wire(main.SWITCH[5], ram.I0)
wire(main.SWITCH[6], ram.I1)
wire(main.SWITCH[7], ram.WE)

wire(ram.O0, main.LED[0])
wire(ram.O1, main.LED[1])

compile(sys.argv[1], main)
