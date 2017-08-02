import sys
from magma import array, wire, compile
from loam.boards.icestick import IceStick, Mux

icestick = IceStick()
icestick.J1[0].rename('I0').input().on()
icestick.J1[1].rename('I1').input().on()
icestick.J1[2].rename('S').input().on()
icestick.D1.on()

main = icestick.main()
I = array(main.I0, main.I1)
S = main.S

#mux = Mux2()
mux = Mux(2)
print(mux.interface)
mux(I, S)
wire(mux.O, main.D1)

compile(sys.argv[1], main)
