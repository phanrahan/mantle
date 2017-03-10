import sys
from magma import *
from mantle.xilinx.spartan3.CLB import CARRY
from mantle.xilinx.spartan3.RAM import RAM16x2
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(4)
megawing.LED.on(2)

main = megawing.main()
A = main.SWITCH

mem = 4*[1,0,0,0]
ram = RAM16x2(mem, mem)
wire(A, ram.A)
wire(0, ram.I0)
wire(0, ram.I1)
wire(0, ram.WE)

O0, COUT = CARRY(ram.O0, ram.O0, 1)
O1, COUT = CARRY(ram.O1, ram.O1, COUT)

wire(O0, main.LED[0])
wire(O1, main.LED[1])

compile(sys.argv[1], main)


