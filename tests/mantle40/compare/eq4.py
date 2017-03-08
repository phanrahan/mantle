import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.J1[0].rename('I0').input().on()
icestick.J1[1].rename('I1').input().on()
icestick.J1[2].rename('I2').input().on()
icestick.J1[3].rename('I3').input().on()
icestick.D1.on()

main = icestick.main()
I0 = array(main.I0, main.I1, main.I2, main.I3)
I1 = array(0, 1, 0, 1)

eq4 = EQ(4)
print(eq4.interface)
eq4(I0,I1)
wire(eq4.O, main.D1)

compile(sys.argv[1], main)
