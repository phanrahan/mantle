import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('I0').input().on()
icestick.J3[0].rename('D0').output().on()

main = icestick.main()

clock = Counter(22)

siso = SISO(4, init=1, ce=True)

siso(main.I0, CE=clock.COUT)
wire( siso.O, main.D0 )

compile(sys.argv[1], main)
