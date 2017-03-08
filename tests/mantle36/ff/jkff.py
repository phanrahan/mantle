import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(2)
megawing.LED.on(1)

main = megawing.main()
J = main.SWITCH[0]
K = main.SWITCH[1]
O = main.LED[0]

ff = JKFF()

O( ff(J, K) )

compile(sys.argv[1], main)


