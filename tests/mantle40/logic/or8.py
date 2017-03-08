import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
for i in range(8):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

or8 = OrN(8)
or8(main.J1)
wire(or8.O, main.D5)

compile(sys.argv[1], main)
