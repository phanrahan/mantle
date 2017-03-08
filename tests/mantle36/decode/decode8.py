import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()

megawing.Switch.on(8)
megawing.LED.on(1)

main = megawing.main()
I = main.SWITCH
O = main.LED[0]

three = Decode(3,8)

O(three(I))


compile(sys.argv[1], main)


