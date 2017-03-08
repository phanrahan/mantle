import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(2)
megawing.LED.on(4)

main = megawing.main()
O = main.LED
U = main.SWITCH[0]
D = main.SWITCH[1]

clock = Counter(24)
counter = UpDownCounter(4, ce=True)

O( counter(U, D, CE=clock.COUT) )

compile(sys.argv[1], main)


