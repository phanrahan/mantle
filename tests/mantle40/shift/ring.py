import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, Counter, Ring

icestick = IceStick()
icestick.Clock.on()
for i in range(8):
    icestick.J3[i].output().on()

main = icestick.main()

clock = Counter(22)

ring = Ring(8, ce=True)

wire( ring( CE=clock.COUT ), main.J3 )

compile(sys.argv[1], main)


