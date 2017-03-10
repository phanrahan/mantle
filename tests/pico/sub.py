import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico3 import *
from loam.shields.megawing import MegaWing

def prog():
    ini(r0, 0)
    ini(r1, 1)
    sub(r1, r0)
    outi(r1, 0)
    jmp(0)

mem = assemble(prog)


megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(2)
megawing.LED.on(8)

main = megawing.main()

led = Register(8, ce=True)
wire( led, main.LED )

pico(mem, [main.SWITCH[0], main.SWITCH[1]], led)


compile(sys.argv[1], main)
