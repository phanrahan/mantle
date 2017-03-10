import sys
from magma import *
from mantle.xilinx.spartan6.RAM import RAM256
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(1)

main = megawing.main()

ram = RAM256(32 * [0,1] + 32 * [1,1] + 32 * [1,0] + 32 * [1,1])

wire(main.CLK, ram.CLK)
wire(0, ram.WE)

wire(main.SWITCH, ram.A)

wire(0, ram.I)

wire(ram.O, main.LED[0])

compile(sys.argv[1], main)
