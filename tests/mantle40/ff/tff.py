import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.D5.on()

main = icestick.main()

clock = Counter(24)

tff = TFF()

tff(clock.COUT)

wire(tff, main.D5)

compile(sys.argv[1], main)
