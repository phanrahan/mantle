import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico3 import *
from loam.boards.papilio import PapilioOne
from .lib.spi import transfer

_CS = 0
_MOSI = 1
_SCLK = 2

def prog():

    movi(r0, 0)
    movi(r1, 1)

    outi(r0, _SCLK)
    outi(r0, _MOSI)

    outi(r1, _CS)
    outi(r0, _CS)
    outi(r1, _CS)

    loop = dot()
    outi(r0, _CS)
    movi(r2, 0)
    call(label('transfer'))
    ini(r2, 0)
    call(label('transfer'))
    outi(r1, _CS)
    jmp(loop)

    transfer()

mem = assemble(prog)

papilio = PapilioOne()
papilio.Clock.on()
for i in range(8):
    papilio.C[i].rename('SWITCH%d' % i).input().on()
papilio.A[0].rename('CS').output().on()
papilio.A[1].rename('MOSI').output().on()
#papilio.A[2].rename('MISO').input().on()
papilio.A[3].rename('SCLK').output().on()

main = papilio.main()

SWITCH = array(main.SWITCH0, main.SWITCH1, main.SWITCH2, main.SWITCH3,
               main.SWITCH4, main.SWITCH5, main.SWITCH6, main.SWITCH7)

CS = FF(ce=True)
wire(CS, main.CS)
MOSI = FF(ce=True)
wire(MOSI, main.MOSI)
SCLK = FF(ce=True)
wire(SCLK, main.SCLK)

pico(mem, SWITCH, [CS, MOSI, SCLK])

compile(sys.argv[1], main)
