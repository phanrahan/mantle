import sys
from magma import wire, compile
from mantle.lattice.ice40.PLL import SB_PLL
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.PMOD0[0].rename('O').output().on()

main = icestick.main()

pll = SB_PLL(25000000, 12000000)

wire( main.CLK, pll.I )
wire( pll.O, main.O )

compile(sys.argv[1], main)
