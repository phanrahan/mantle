import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(3)
megawing.LED.on(1)

main = megawing.main()
I = main.SWITCH
O = main.LED[0]

rom = ROM3(4*[0,1])

rom(I)
wire(rom.O, O)

compile(sys.argv[1], main)


