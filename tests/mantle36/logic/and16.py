import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(8)
megawing.LED.on(1)

main = megawing.main()

Array16 = Array(16,Bit)
I = array(main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3],
          main.SWITCH[4], main.SWITCH[5], main.SWITCH[6], main.SWITCH[7],
          main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3],
          main.SWITCH[4], main.SWITCH[5], main.SWITCH[6], main.SWITCH[7])
O = main.LED[0]

a = AndN(16)

a(I)
wire(a.O, O)

compile(sys.argv[1], main)


