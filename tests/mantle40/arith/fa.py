import sys
from magma import *
from mantle import *
from boards.icestick import IceStick

icestick = IceStick()
icestick.J1[0].rename('A0').input().on()
icestick.J1[1].rename('A1').input().on()
icestick.J1[2].rename('B0').input().on()
icestick.J1[3].rename('B1').input().on()
icestick.D1.on()
icestick.D2.on()
icestick.D3.on()

main = icestick.main()
A0 = main.A0
A1 = main.A1
B0 = main.B0
B1 = main.B1

add0 = FullAdder()
add1 = FullAdder()

add0(A0, B0)
wire(0, add0.CIN)
add1(A1, B1)
wire(add0.COUT, add1.CIN)

wire(add0.O, main.D1)
wire(add1.O, main.D2)
wire(add1.COUT, main.D3)

compile(sys.argv[1], main)
