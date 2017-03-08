import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(6)
megawing.LED.on(1)

main = megawing.main()
SI = main.SWITCH[0]
PI = main.SWITCH[1:5]
LOAD = main.SWITCH[5]
O = main.LED[0]

print('clock')

clock = Counter(24)

piso = PISO(4, init=1, ce=True)
print(piso.interface)

piso(SI, PI, LOAD, CE=clock.COUT)

wire(piso, O)

compile(sys.argv[1], main)


