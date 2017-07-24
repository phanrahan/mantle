import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, Register

icestick = IceStick()
icestick.Clock.on()
for i in range(4):
    icestick.J1[i].input().on()
    icestick.J3[i].output().on()

main = icestick.main()

reg = Register(4)
wire( reg(main.J1), main.J3 )

compile(sys.argv[1], main)
