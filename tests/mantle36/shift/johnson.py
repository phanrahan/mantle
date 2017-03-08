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

johnson = Johnson(4, ce=True)

O( johnson(CE=clock.COUT) )

compile(sys.argv[1], main)


