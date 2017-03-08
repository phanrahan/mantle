import sys
from magma import *
from parts.xilinx.spartan6.primitives.RAM import RAM128D
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(2)

main = megawing.main()

ram = RAM128D(32 * [1,1,0,0])

wire(0, ram.WE)

wire(main.SWITCH[:7], ram.A0)
wire(main.SWITCH[7],  ram.I)

wire(array(1,0,0,1,0,0,0), ram.A1)

wire(ram.O0, main.LED[0])
wire(ram.O1, main.LED[1])

compile(sys.argv[1], main)
