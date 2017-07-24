import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, Decoder

icestick = IceStick()
for i in range(2):
    icestick.J1[i].input().on()
for i in range(4):
    icestick.J3[i].output().on()

main = icestick.main()

decoder = Decoder(2)

wire( decoder(main.J1), main.J3 )

compile(sys.argv[1], main)
