import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.J1[0].rename('I0').input().on()
icestick.J3[0].rename('D0').output().on()

main = icestick.main()
I = array(main.I0)

rom = ROM1(I0)
rom(I)
wire(rom.O, main.D0)

compile(sys.argv[1], main)
