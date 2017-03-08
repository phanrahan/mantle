import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()

megawing.Switch.on(8)
megawing.LED.on(3)

main = megawing.main()
I = main.SWITCH
O = main.LED

arb = Arbiter( 8 )
enc = Encoder( 8 )

O( enc( arb (I) ) )
 
compile(sys.argv[1], main)
