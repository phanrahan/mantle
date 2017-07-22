import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.J1[0].rename('I0').input().on()
icestick.J1[1].rename('I1').input().on()
icestick.J1[2].rename('I2').input().on()
icestick.J3[0].rename('D0').output().on()

main = icestick.main()

lut = LUT3(I0&I1&I2)
lut(main.I0, main.I1, main.I2)
wire(lut.O, main.D0)

compile(sys.argv[1], main)
