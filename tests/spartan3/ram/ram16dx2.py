import sys
from magma import *
from mantle.xilinx.spartan3.RAM import RAM16DxN
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(7)
megawing.LED.on(4)

main = megawing.main()
A0 = array(main.SWITCH[0], main.SWITCH[1], 0, 0)
A1 = array(main.SWITCH[2], main.SWITCH[3], 0, 0)
I  = array(main.SWITCH[4], main.SWITCH[5])
WE = main.SWITCH[6]
O0 = main.LED[0:2]
O1 = main.LED[2:4]

ram = RAM16DxN(2)
wire(A0, ram.A0)
wire(A1, ram.A1)
wire(I, ram.I)
wire(WE, ram.WE)
wire(main.CLK, ram.CLK)

wire(ram.O0, O0)
wire(ram.O1, O1)

compile(sys.argv[1], main)


