import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
for i in range(6):
    icestick.J3[i].output().on()

main = icestick.main()

counter = Counter(4)
wire( main.CLKIN, main.J3[0])
wire(counter, main.J3[1:5])
wire(counter.COUT, main.J3[5])

compile(sys.argv[1], main)
