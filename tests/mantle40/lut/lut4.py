import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, LUT4, I0, I1, I2, I3

icestick = IceStick()
icestick.J1[0].rename('I0').input().on()
icestick.J1[1].rename('I1').input().on()
icestick.J1[2].rename('I2').input().on()
icestick.J1[3].rename('I3').input().on()
icestick.J3[0].rename('D0').output().on()


main = icestick.main()

lut = LUT4(I0&I1&I2&I3)
lut(main.I0, main.I1, main.I2, main.I3)
wire(lut.O, main.D0)

compile(sys.argv[1], main)
