import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(6):
    icestick.J1[i].input().on()
icestick.J3[0].rename('D0').output().on()

main = icestick.main()
SI = main.J1[0]
PI = main.J1[1:5]
LOAD = main.J1[5]

clock = Counter(22)

piso = PISO(4, init=1, ce=True)

piso(SI, PI, LOAD, CE=clock.COUT)
wire( piso.O, main.D0 )

compile(sys.argv[1], main)
