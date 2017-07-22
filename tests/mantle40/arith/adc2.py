import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('A0').input().on()
icestick.J1[1].rename('A1').input().on()
icestick.J1[2].rename('B0').input().on()
icestick.J1[3].rename('B1').input().on()
icestick.J1[4].rename('CIN').input().on()
icestick.D1.on()
icestick.D2.on()
icestick.D3.on()

main = icestick.main()
A = array(main.A0, main.A1)
B = array(main.B0, main.B1)
O = array(main.D1, main.D2)

add = AddC(2)
wire(main.CIN, add.CIN)

add(A, B)

wire(add.O[0], main.D1)
wire(add.O[1], main.D2)
wire(add.COUT, main.D3)

compile(sys.argv[1], main)
