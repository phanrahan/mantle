import sys
from magma import *
from parts.xilinx.spartan6.primitives.RAM import RAM64D
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(2)

main = megawing.main()

ram = RAM64D(32*[0,1])

wire(main.SWITCH[:6], ram.A0)
wire(array(0,1,0,0,0,0), ram.A1)

wire(main.SWITCH[6], ram.I)
wire(main.SWITCH[7], ram.WE)

wire(ram.O0, main.LED[0])
wire(ram.O1, main.LED[1])

compile(sys.argv[1], main)
