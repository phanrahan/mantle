import sys
from magma import *
from parts.xilinx.spartan3.primitives.SRL import SRL16
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(5)
megawing.LED.on(1)

main = megawing.main()
A = main.SWITCH[0:4]
I = main.SWITCH[4]
O = main.LED[0]

srl16 = SRL16(init=1)
O( srl16( A, I ) )

compile(sys.argv[1], main)


