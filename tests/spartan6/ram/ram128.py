import sys
from magma import *
from parts.xilinx.spartan6.primitives.RAM import RAM128
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(7)
megawing.LED.on(1)

main = megawing.main()

ram = RAM128(64*[0,1])

ADDR = main.SWITCH[0:7]

wire(ram(ADDR, 0, 0), main.LED[0])

compile(sys.argv[1], main)
