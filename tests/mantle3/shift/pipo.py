import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(6)
megawing.LED.on(4)

main = megawing.main()
SI = main.SWITCH[0]
PI = main.SWITCH[1:5]
LOAD = main.SWITCH[5]
O = main.LED

clock = Counter(24)

pipo = PIPO(4, init=1, ce=True)
print pipo.interface
pipo(SI, PI, LOAD, CE=clock.COUT)

wire( pipo.O, O )

compile(sys.argv[1], main)


