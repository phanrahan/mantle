import sys
from magma import *
from mantle import *
from mantle.util.lhca import LHCA
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(8):
    icestick.J3[i].output().on()

main = icestick.main()

clock = Counter(22)

lhca = LHCA(8, ce=True)

wire( lhca( CE=clock.COUT ), main.J3 )

compile(sys.argv[1], main)


