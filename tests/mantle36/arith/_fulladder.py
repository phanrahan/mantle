import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()

megawing.Switch.on(3)
megawing.LED.on(2)

main = megawing.main()

fa = FullAdder(2, A0^A1,A0&A1)

fa( main.SWITCH[0], main.SWITCH[1] )
wire( main.SWITCH[2], fa.CIN )
wire( fa.O, main.LED[0] )
wire( fa.COUT, main.LED[1] )

compile(sys.argv[1], main)


