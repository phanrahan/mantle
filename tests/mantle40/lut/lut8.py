import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, LUT8

icestick = IceStick()
icestick.J1[0].rename('I0').input().on()
icestick.J1[1].rename('I1').input().on()
icestick.J1[2].rename('I2').input().on()
icestick.J1[3].rename('I3').input().on()
icestick.J1[4].rename('I4').input().on()
icestick.J1[5].rename('I5').input().on()
icestick.J1[6].rename('I6').input().on()
icestick.J1[7].rename('I7').input().on()
icestick.J3[0].rename('D0').output().on()


main = icestick.main()

lut = LUT8(255*[0]+[1])
lut(main.I0, main.I1, main.I2, main.I3, main.I4, main.I5, main.I6, main.I7)
wire(lut.O, main.D0)

compile(sys.argv[1], main)
