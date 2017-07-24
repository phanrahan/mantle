import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, ReduceNOr

icestick = IceStick()
for i in range(8):
    icestick.J1[i].input().on()
icestick.D5.on()

main = icestick.main()

nor8 = ReduceNOr(8)
nor8(main.J1)
wire(nor8.O, main.D5)

compile(sys.argv[1], main)
