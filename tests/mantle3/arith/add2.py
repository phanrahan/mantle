import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()

megawing.Switch.on(4)
megawing.LED.on(2)

main = megawing.main()
A = main.SWITCH[0:2]
B = main.SWITCH[2:4]
C = main.LED

add = Add(2)

add(A,B)
wire(add.O, C)

compile(sys.argv[1], main)


