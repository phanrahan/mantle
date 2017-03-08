import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(5)
megawing.LED.on(2)

main = megawing.main()
I0 = main.SWITCH[0:2]
I1 = main.SWITCH[2:4]
S = main.SWITCH[4]
O = main.LED

mux = Mux(2,2)
mux(I0,I1,S)
wire(mux.O, O)

compile(sys.argv[1], main)


