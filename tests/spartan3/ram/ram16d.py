import sys
from magma import *
from parts.xilinx.spartan3.primitives.RAM import RAM16D
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(6)
megawing.LED.on(2)

main = megawing.main()
A0 = array(main.SWITCH[0], main.SWITCH[1], 0, 0)
A1 = array(main.SWITCH[2], main.SWITCH[3], 0, 0)
O0 = main.LED[0]
O1 = main.LED[1]

mem = 4 * [1, 0, 0, 0]
ram = RAM16D(mem)
wire(A0, ram.A0)
wire(A1, ram.A1)
wire(main.SWITCH[4], ram.I)
wire(main.SWITCH[5], ram.WE)
wire(main.CLK, ram.CLK)

wire(ram.O0, O0)
wire(ram.O1, O1)

compile(sys.argv[1], main)


