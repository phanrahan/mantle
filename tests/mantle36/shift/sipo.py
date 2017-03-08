import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.LED.on(4)

main = megawing.main()
O = main.LED

clock = Counter(24)
ring = SIPO(4, init=1, ce=True)

O( ring(ring.O[3], CE=clock.COUT) )

compile(sys.argv[1], main)


