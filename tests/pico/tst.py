import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico3 import *
from loam.shields.megawing import MegaWing

def prog():
    ini(r0, 0)
    movi(r1, 0)

    for i in range(8): 
        tsti(r0, 1<<i)
        jz(dot()+2)
        ori(r1, 1<<i)

    outi(r1, 0)

    jmp(0)

mem = assemble(prog)
#print([hex(mem[i]) for i in range(64)])

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(8)

main = megawing.main()

leds = Register(8, ce=True)
wire(leds, main.LED)

pico(mem, main.SWITCH, leds)

compile(sys.argv[1], main)
