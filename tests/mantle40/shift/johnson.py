import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, Counter, Johnson

icestick = IceStick()
icestick.Clock.on()
for i in range(4):
    icestick.J3[i].output().on()

main = icestick.main()

clock = Counter(22)

johnson = Johnson(4, has_ce=True)

johnson(CE=clock.COUT)

wire(johnson.O, main.J3)

compile(sys.argv[1], main)
