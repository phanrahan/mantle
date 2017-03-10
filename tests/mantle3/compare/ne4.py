import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()

megawing.Switch.on(8)
megawing.LED.on(1)

main = megawing.main()
A = main.SWITCH[0:4]
B = main.SWITCH[4:8]
O = main.LED[0]

ne4 = NE(4)

O(ne4(A, B))

compile(sys.argv[1], main)


