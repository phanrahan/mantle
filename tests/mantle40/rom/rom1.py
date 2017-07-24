import sys
from magma import array, wire, compile
from loam.boards.icestick import IceStick, ROM1, I0

icestick = IceStick()
icestick.J1[0].rename('I0').input().on()
icestick.J3[0].rename('D0').output().on()

main = icestick.main()
I = array(main.I0)

rom = ROM1(I0)
rom(I)
wire(rom.O, main.D0)

compile(sys.argv[1], main)
