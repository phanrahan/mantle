import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico3 import *
from loam.shields.megawing import MegaWing

DELAY = -1 # 255 falls outside the range of signed

def delay():
    setlabel('delay')

    movi(r1, DELAY)
    loop1 = dot()
    movi(r2, DELAY)
    loop2 = dot()
    movi(r3, DELAY)
    loop3 = dot()
    subi(r3, 1)
    jnz(loop3)
    subi(r2, 1)
    jnz(loop2)
    subi(r1, 1)
    jnz(loop1)
    ret()

def prog():

    movi(r0, 0)

    loop = dot()

    call(label('delay'))

    xori(r0, 1)
    outi(r0, 0)

    mov( r1, r0)
    xori(r1, 1)
    outi(r1, 1)

    jmp(loop)

    delay()


mem = assemble(prog)

#print([hex(mem[i]) for i in range(32)])


megawing = MegaWing()
megawing.Clock.on()
megawing.LED.on(2)

main = megawing.main()

led0 = FF(ce=True)
led1 = FF(ce=True)
wire(led0, main.LED[0])
wire(led1, main.LED[1])

pico(mem, None, [led0, led1])

compile(sys.argv[1], main)
