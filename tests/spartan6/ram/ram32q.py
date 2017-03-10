import sys
from magma import *
from mantle.xilinx.spartan6.RAM import RAM32Q
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(8)

main = megawing.main()

ram = RAM32Q([16 * [1,0],
              16 * [1,1],
              16 * [0,1],
              16 * [0,0]])

wire(main.CLK, ram.CLK)
wire(0, ram.WE)

wire(main.SWITCH[:5], ram.AA)
wire(main.SWITCH[:5], ram.AB)
wire(main.SWITCH[:5], ram.AC)
wire(main.SWITCH[:5], ram.AD)

wire(ram.OA, main.LED[0:2])
wire(ram.OB, main.LED[2:4])
wire(ram.OC, main.LED[4:6])
wire(ram.OD, main.LED[6:8])

wire(array(0,0), ram.IA)
wire(array(0,0), ram.IB)
wire(array(0,0), ram.IC)
wire(array(0,0), ram.ID)

compile(sys.argv[1], main)
