import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.PMOD0[0].rename('I0').input().on()
icestick.PMOD0[1].rename('I1').input().on()
icestick.PMOD0[2].rename('I2').input().on()
icestick.PMOD0[3].rename('I3').input().on()
icestick.D1.on()

main = icestick.main()

lut = LUT4(I0&I1&I2&I3)
lut(main.I0, main.I1, main.I2, main.I3)

dff = DFF(loc=(2,2,0))
dff(lut)

wire(dff.O, main.D1)

compile(sys.argv[1], main, output='blif')
