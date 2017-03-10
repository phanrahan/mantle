import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico import *
from loam.shields.megawing import MegaWing

def prog():
    loop = dot()
    movi(r0, 0x34)
    outi(r0, 0)
    movi(r0, 0x12)
    outi(r0, 1)
    jmp(loop)

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
