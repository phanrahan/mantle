import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(3)
megawing.LED.on(1)

main = megawing.main()
I = main.SWITCH[0:2]
S = main.SWITCH[2]

mux2 = Mux2()

mux2(I,S)
wire(mux2.O, main.LED[0])

compile(sys.argv[1], main)


