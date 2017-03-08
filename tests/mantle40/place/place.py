import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.PMOD0[0].rename('I0').input().on()
icestick.PMOD0[1].rename('I1').input().on()
icestick.PMOD0[2].rename('I2').input().on()
icestick.PMOD0[3].rename('I3').input().on()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()
A = array(main.I0, main.I1)
B = array(main.I2, main.I3)
C = array(main.D1, main.D2)

and2 = And(2,2)
print(and2.interface)
and2(A,B)
wire(and2.O, C)

#compile(sys.argv[1], main, output='blif')
compile(sys.argv[1], main)
