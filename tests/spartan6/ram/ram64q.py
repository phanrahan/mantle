import sys
from magma import *
from mantle.xilinx.spartan6.RAM import RAM64Q
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(8)

main = megawing.main()

ram = RAM64Q([32 * [0,1], 32 * [1,1], 32 * [1,0], 32 * [0,0]])

wire(main.CLK, ram.CLK)
wire(0, ram.WE)

wire(main.SWITCH[:6], ram.AA)
wire(main.SWITCH[:6], ram.AB)
wire(main.SWITCH[:6], ram.AC)
wire(main.SWITCH[:6], ram.AD)

wire(ram.OA, main.LED[0])
wire(ram.OA, main.LED[1])

wire(ram.OB, main.LED[2])
wire(ram.OB, main.LED[3])

wire(ram.OC, main.LED[4])
wire(ram.OC, main.LED[5])

wire(ram.OD, main.LED[6])
wire(ram.OD, main.LED[7])

wire(0, ram.IA)
wire(0, ram.IB)
wire(0, ram.IC)
wire(0, ram.ID)

compile(sys.argv[1], main)
