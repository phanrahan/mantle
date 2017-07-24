import sys
from magma import array, wire, compile
from loam.boards.icestick import IceStick, AddC

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('A0').input().on()
icestick.J1[1].rename('B0').input().on()
icestick.J1[2].rename('CIN').input().on()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()
A = array(main.A0)
B = array(main.B0)
O = array(main.D1)

add = AddC(1)

add(A, B)
wire(main.CIN, add.CIN)

wire(add.O[0], main.D1)
wire(add.COUT, main.D2)

compile(sys.argv[1], main)
