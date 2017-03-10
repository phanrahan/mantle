import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()

megawing.Switch.on(8)
megawing.LED.on(4)

main = megawing.main()
A = main.SWITCH[0:4]
B = main.SWITCH[4:8]
C = main.LED

add = Add(4)

add(A,B)
wire(add.O, C)

compile(sys.argv[1], main)


