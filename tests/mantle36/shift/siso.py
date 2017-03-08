import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.LED.on(1)

main = megawing.main()
O = main.LED[0]

clock = Counter(24)
ring = SISO(4, init=1, ce=True)

O( ring(ring.O, CE=clock.COUT) )

compile(sys.argv[1], main)


