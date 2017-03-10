import sys
from magma import *
from mantle import Counter
from mantle.util.lhca import LHCA
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.LED.on(8)

main = megawing.main()

clock = Counter(24)

lhca = LHCA( 8, ce=True )
lhca(CE=clock.COUT) 

wire(lhca, main.LED)

compile(sys.argv[1], main)

