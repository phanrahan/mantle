import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, Not

icestick = IceStick()
icestick.J1[0].rename('I0').input().on()
icestick.D5.on()

main = icestick.main()

n = Not()
n(main.I0)
wire(n.O, main.D5)

compile(sys.argv[1], main)
