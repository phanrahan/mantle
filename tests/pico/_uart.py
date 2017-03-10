import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico import *
from loam.shields.megawing import MegaWing

def putc():
    setlabel('putc')
    loop = dot()
    ini(r1, 0) # loop until FIFO is not full 
    jnz(loop)
    outi(r0, 0)
    ret()

def prog():
    s = 'hello, world\r\n'
    loop = dot()
    for c in s:
        movi(r0, ord(c))
        call(label('putc'))
    jmp(loop)

    putc()

mem = assemble(prog)

megawing = MegaWing()
megawing.Clock.on()
megawing.USART.on()

main = megawing.main()

uart = AnonymousCircuit("input I", main.TXD, "input CE", main.TXWRITE)

pico(mem, main.TXSTATUS, uart)

compile(sys.argv[1], main)
