import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, NOr

icestick = IceStick()
for i in range(2):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

nor2 = NOr(2)
nor2(main.J1[0], main.J1[1])
wire(nor2.O, main.D5)

compile(sys.argv[1], main)
