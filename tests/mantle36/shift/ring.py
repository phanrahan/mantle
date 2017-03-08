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
ring = Ring(4, init=1, ce=True)
print(ring.interface)

O( ring( CE=clock.COUT ) )

compile(sys.argv[1], main)


