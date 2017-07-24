import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, Counter, SIPO

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('I0').input().on()
for i in range(4):
    icestick.J3[i].output().on()

main = icestick.main()

clock = Counter(22)

sipo = SIPO(4, init=1, ce=True)

sipo(main.I0, CE=clock.COUT)
wire( sipo.O, main.J3 )

compile(sys.argv[1], main)
