import sys
from magma import *
from mantle import *
from mantle.util.lfsr import LFSR
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(8):
    icestick.J3[i].output().on()

main = icestick.main()

clock = Counter(22)

lfsr = LFSR(8, ce=True)

wire( lfsr( CE=clock.COUT ), main.J3 )

compile(sys.argv[1], main)


