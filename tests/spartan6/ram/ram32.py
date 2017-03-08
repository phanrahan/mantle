import sys
from magma import *
from parts.xilinx.spartan6.primitives.RAM import RAM32
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(1)

main = megawing.main()

ram = RAM32(16*[0,1])

wire(main.SWITCH[:5], ram.A)
wire(main.SWITCH[6], ram.I)
wire(main.SWITCH[7], ram.WE)

wire(ram.O, main.LED[0])

compile(sys.argv[1], main)
