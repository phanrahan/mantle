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
counter = Counter(4, ce=True)

O( counter(CE=clock.COUT) )

compile(sys.argv[1], main)


