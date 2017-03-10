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


def prog():
    loop = dot()
    movi(r0,0)
    outi(r0,0)
    repeat(17,label("delay")) 
    movi(r0,1)
    outi(r0,0)
    repeat(17,label("delay")) 
    jmp(loop)

    delay((196-4)/2)

mem = assemble(prog)

papilio = PapilioOne()
papilio.Clock.on()
papilio.TX.on()
#papilio.A[0].Out('TX')

main = papilio.main()

TX = FF(ce=True)
wire(TX, main.TX)

pico(mem, None, TX)

compile(sys.argv[1], main)
