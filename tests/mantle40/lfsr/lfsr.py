import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, Counter
from mantle.util.lfsr import LFSR

icestick = IceStick()
icestick.Clock.on()
for i in range(8):
    icestick.J3[i].output().on()

main = icestick.main()

clock = Counter(22)

lfsr = LFSR(8, has_ce=True)

wire( lfsr( CE=clock.COUT ), main.J3 )

compile(sys.argv[1], main)


