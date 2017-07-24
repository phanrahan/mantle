import sys
from magma import wire, compile
from loam.boards.icestick import IceStick, CascadedRing, Ring

icestick = IceStick()
icestick.Clock.on()
for i in range(8):
    icestick.J3[i].output().on()

main = icestick.main()

ce = CascadedRing( [10, 10, 10, 10, 10, 10, 8] )

ring = Ring(8, ce=True)

wire( ring( CE=ce ), main.J3 )

compile(sys.argv[1], main)
