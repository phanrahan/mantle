import sys
from magma import *
from mantle import *
from mantle.util.lfsr import LFSR
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.LED.on(8)

main = megawing.main()

clock = Counter(24)

lfsr = LFSR( 8, ce=True )
lfsr(CE=clock.COUT) 

wire(lfsr, main.LED)

compile(sys.argv[1], main)

