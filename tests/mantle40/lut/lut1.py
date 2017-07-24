import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, LUT1, I0

icestick = IceStick()
icestick.J1[0].rename('I0').input().on()
icestick.J3[0].rename('D0').output().on()

main = icestick.main()

lut = LUT1(~I0)
lut(main.I0)
wire(lut.O, main.D0)

compile(sys.argv[1], main)
