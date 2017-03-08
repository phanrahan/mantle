import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()

megawing.Switch.on(4)
megawing.LED.on(2)

main = megawing.main()
A = main.SWITCH[0:2]
B = main.SWITCH[2:4]
C = main.LED

sub2 = Sub(2)

sub2(A,B)
wire(sub2.O, C)

compile(sys.argv[1], main)


