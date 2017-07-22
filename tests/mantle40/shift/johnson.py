import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(4):
    icestick.J3[i].output().on()

main = icestick.main()

clock = Counter(22)

johnson = Johnson(4, ce=True)

johnson(CE=clock.COUT)

wire(johnson.O, main.J3)

compile(sys.argv[1], main)
