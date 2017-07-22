import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.J1[0].rename('I0').input().on()
icestick.J1[1].rename('I1').input().on()
icestick.J1[2].rename('I2').input().on()
icestick.J1[3].rename('I3').input().on()
icestick.D1.on()

main = icestick.main()

lut0 = LUT4(I0&I1&I2&I3)
lut0(main.I0, main.I1, main.I2, main.I3)

lut1 = LUT4(I0&I1&I2&I3)
#lut1(main.I0, lut0.O, main.I2, main.I3)
#lut1(main.I0, main.I1, lut0.O, main.I3)
lut1(main.I0, main.I1, main.I2, lut0.O)

wire(lut1.O, main.D1)

compile(sys.argv[1], main)
