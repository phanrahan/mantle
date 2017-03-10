import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico3 import *
from loam.shields.megawing import MegaWing

def prog():
    ini(r0, 0)
    outi(r0, 0)

    jmp(0)

mem = assemble(prog)

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(8)

main = megawing.main()

leds = Register(8, ce=True)
wire(leds, main.LED)

pico(mem, main.SWITCH, leds)

compile(sys.argv[1], main)
