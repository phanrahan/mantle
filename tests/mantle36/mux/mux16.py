import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(8)
megawing.LED.on(1)

main = megawing.main()
I = array(main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3],
          main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3],
          main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3],
          main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3])
S = array(main.SWITCH[4], main.SWITCH[5], main.SWITCH[6], main.SWITCH[7])

mux = Mux16()

mux(I,S)
wire(mux.O, main.LED[0])


compile(sys.argv[1], main)


