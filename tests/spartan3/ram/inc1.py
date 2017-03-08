import sys
from magma import *
from parts.xilinx.spartan3.primitives.CLB import CARRY
from parts.xilinx.spartan3.primitives.RAM import RAM16
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(4)
megawing.LED.on(2)

main = megawing.main()
A = main.SWITCH

mem = 4*[1,0,0,0]

ram = RAM16(mem)
wire(A, ram.A)
wire(0, ram.I)
wire(0, ram.WE)
O0, COUT = CARRY(ram.O, ram.O, 1)

ram = RAM16(mem)
wire(A, ram.A)
wire(0, ram.I)
wire(0, ram.WE)
O1, COUT = CARRY(ram.O, ram.O, COUT)

wire(O0, main.LED[0])
wire(O1, main.LED[1])

compile(sys.argv[1], main)

