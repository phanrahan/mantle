import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico3 import *
from loam.parts.generic.display import Display
from loam.shields.megawing import MegaWing

DELAY = -1

def delay():
    setlabel('delay')
    loop1 = dot()
    movi(r1, -1)
    loop2 = dot()
    movi(r2, -1)
    loop3 = dot()
    subi(r2, 1)
    jnz(loop3)
    subi(r1, 1)
    jnz(loop2)
    subi(r0, 1)
    jnz(loop1)
    ret()

def display():
    setlabel('display')
    outi(r8, 0)
    outi(r9, 1)
    ret()

def prog():
    movi(r8,0)
    movi(r9,0)
    loop = dot()
    call(label('display'))
    movi(r0, 4)
    call(label('delay'))
    addi(r8,1)
    adci(r9,0)
    jmp(loop)

    display()

    delay()

mem = assemble(prog)

megawing = MegaWing()
megawing.Clock.on()
megawing.Display.on()

main = megawing.main()

# Display digits from left to right
digit0 = Register(8, ce=True)
digit1 = Register(8, ce=True)
digits = array( digit1.O[4:8], digit1.O[0:4], 
                digit0.O[4:8], digit0.O[0:4] )
wire(digits, main.DIGITS)

# digit0 is the lsb on the right of the display
# digit1 is the msb on the left of the display
pico(mem, None, [digit0, digit1] )

compile(sys.argv[1], main)
