import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico3 import *
from loam.boards.papilio import PapilioOne

def delay(n):
    setlabel('delay')
    nop()
    movi(r8, n)
    loop = dot()
    subi(r8, 1)
    jnz(loop)
    ret()

def repeat(n, body):
    for i in range(n):
        call(body)

def baud():
    setlabel('baud')
    repeat(17,label('delay'))
    ret()

def prog():
    movi(r0, 0)
    movi(r1, 1)
    loop = dot()
    outi(r0, 0)
    call(label('baud'))
    outi(r1, 0)
    call(label('baud'))
    jmp(loop)

    delay((196-4)/2)
    baud()

mem = assemble(prog)

papilio = PapilioOne()
papilio.Clock.on()
papilio.TX.on()
#papilio.A[0].rename('TX').output().on()

main = papilio.main()

TX = FF(ce=True)
wire(TX, main.TX)

pico(mem, None, TX)

compile(sys.argv[1], main)
