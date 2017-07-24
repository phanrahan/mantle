import sys
from magma import array, wire, compile
from loam.boards.icestick import IceStick, NE

icestick = IceStick()
icestick.J1[0].rename('I0').input().on()
icestick.J1[1].rename('I1').input().on()
icestick.J1[2].rename('I2').input().on()
icestick.J1[3].rename('I3').input().on()
icestick.D1.on()

main = icestick.main()
I0 = array(main.I0, main.I1, main.I2, main.I3)
I1 = array(0,1,0,1)

ne4 = NE(4)
ne4(I0,I1)
wire(ne4.O, main.D1)

compile(sys.argv[1], main)
