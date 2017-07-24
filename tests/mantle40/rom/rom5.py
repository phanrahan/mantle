import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, ROM5

icestick = IceStick()
for i in range(5):
    icestick.J1[i].input().on()
icestick.J3[0].rename('D0').output().on()


main = icestick.main()

rom = ROM5(31*[0]+[1])
rom(main.J1)
wire(rom.O, main.D0)

compile(sys.argv[1], main)
