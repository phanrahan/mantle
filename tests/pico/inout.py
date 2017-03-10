import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico3 import *
from loam.shields.megawing import MegaWing

def prog():
    for i in range(8):
        ini(r0, i)
        mov(r1, r0)
        outi(r1, i)
    jmp(0)

mem = assemble(prog)
#print([hex(mem[i]) for i in range(16)])


megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(8)

main = megawing.main()

ins = [main.SWITCH[i] for i in range(8)]
outs = []
for i in range(8):
    ff = FF(ce=True)
    wire(ff, main.LED[i])
    outs.append(ff)

pico(mem, ins, outs)

compile(sys.argv[1], main)
