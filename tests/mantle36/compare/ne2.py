import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()

megawing.Switch.on(4)
megawing.LED.on(1)

main = megawing.main()
A = main.SWITCH[0:2]
B = main.SWITCH[2:4]
O = main.LED[0]

ne2 = NE(2)

O(ne2(A, B))

compile(sys.argv[1], main)


