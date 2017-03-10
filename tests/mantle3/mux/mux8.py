import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(7)
megawing.LED.on(1)

main = megawing.main()
I = array(main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3],
          main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3])
S = array(main.SWITCH[4], main.SWITCH[5], main.SWITCH[6])

mux = Mux8()

mux(I,S)
wire(mux.O, main.LED[0])


compile(sys.argv[1], main)


