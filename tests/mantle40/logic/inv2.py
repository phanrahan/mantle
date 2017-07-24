import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, Invert

icestick = IceStick()
for i in range(2):
    icestick.J1[i].input().on()
for i in range(2):
    icestick.J3[i].output().on()

main = icestick.main()

inv = Invert(2)
wire( inv(main.J1), main.J3 )

compile(sys.argv[1], main)
