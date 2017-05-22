from magma import *
from magma.simulator_interactive_frontend import simulate
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.D1.on()
icestick.D2.on()
icestick.D3.on()
main = icestick.main()
baud_clock = Counter(2)
wire(baud_clock.O[0], main.D1)
wire(baud_clock.O[1], main.D2)
wire(baud_clock.COUT, main.D3)

simulate(main)

