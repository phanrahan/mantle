import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(6)
megawing.LED.on(2)

main = megawing.main()
I0 = array(main.SWITCH[0], main.SWITCH[0])
I1 = array(main.SWITCH[1], main.SWITCH[1])
I2 = array(main.SWITCH[2], main.SWITCH[2])
I3 = array(main.SWITCH[3], main.SWITCH[3])
S = main.SWITCH[4:6]
O = main.LED

mux = Mux(4,2)
mux(I0,I1,I2,I3,S)
wire(mux.O, O)

compile(sys.argv[1], main)


