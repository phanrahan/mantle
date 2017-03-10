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

def bit():
    setlabel('bit')
    outi(r1, 0)
    call(label('baud'))
    ret()

def bit0():
    setlabel('bit0')
    movi(r1, 0)
    call(label('bit'))
    ret()

def bit1():
    setlabel('bit1')
    movi(r1, 1)
    call(label('bit'))
    ret()

def putc():
    setlabel('putc')
    call(label('bit0'))
    for i in range(8):
        tsti(r0, 1<<i)
        jz(dot()+3)
        call(label('bit1'))
        jmp(dot()+2)
        call(label('bit0'))
    call(label('bit1'))
    call(label('bit1'))
    call(label('bit1'))
    call(label('bit1'))
    call(label('bit1'))
    ret()

def prog():

    loop = dot()
    for c in 'hello, world  ':
        movi(r0, ord(c))
        call(label('putc'))
    jmp(loop)

    delay((196-4)/2)
    baud()
    bit()
    bit0()
    bit1()
    putc()

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
