import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(4)
megawing.LED.on(2)

main = megawing.main()
A = array(main.SWITCH[0], main.SWITCH[1])
B = array(main.SWITCH[2], main.SWITCH[3])

and2 = And(2,2)
print(and2.interface)

and2(A, B)

wire(and2, main.LED)

compile(sys.argv[1], main)


