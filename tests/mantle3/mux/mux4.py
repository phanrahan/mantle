import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(6)
megawing.LED.on(1)

main = megawing.main()
I = main.SWITCH[0:4]
S = main.SWITCH[4:6]

mux = Mux4()

mux(I,S)
wire(mux.O, main.LED[0])


compile(sys.argv[1], main)


