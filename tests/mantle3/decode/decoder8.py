import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(3)
megawing.LED.on(8)

main = megawing.main()

decoder = Decoder( 3 )

main.LED( decoder( main.SWITCH ) )

compile(sys.argv[1], main)
