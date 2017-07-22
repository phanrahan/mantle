import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.J1[0].rename('A0').input().on()
icestick.J1[1].rename('A1').input().on()
icestick.J1[2].rename('B0').input().on()
icestick.J1[3].rename('B1').input().on()
icestick.D1.on()

main = icestick.main()
A = array(main.A0,main.A1,0,0,0,0,0,0)
B = array(main.B0,main.B1,0,0,0,0,0,0)
O = main.D1

ult = ULT(8, loc=(4,1))
ult(A, B)
wire(ult.O, main.D1)

#compile(sys.argv[1], main, output='blif', origin=(0,0))
compile(sys.argv[1], main)
