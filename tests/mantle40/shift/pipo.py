import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, Counter, PIPO

icestick = IceStick()
icestick.Clock.on()
for i in range(6):
    icestick.J1[i].input().on()
for i in range(4):
    icestick.J3[i].output().on()

main = icestick.main()
SI = main.J1[0]
PI = main.J1[1:5]
LOAD = main.J1[5]

clock = Counter(22)

pipo = PIPO(4, init=1, has_ce=True)

pipo(SI, PI, LOAD, CE=clock.COUT)
wire( pipo.O, main.J3 )

compile(sys.argv[1], main)
