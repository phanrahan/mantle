import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
for i in range(8):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

and8 = AndN(8)
and8(main.J1)
wire(and8.O, main.D5)

compile(sys.argv[1], main)
