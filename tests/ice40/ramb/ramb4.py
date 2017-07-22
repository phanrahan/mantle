import sys
from magma import *
from mantle.lattice.ice40.RAMB import RAMB
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()
icestick.J1[0].rename('I0').input().on()
icestick.J1[1].rename('I1').input().on()
icestick.J1[2].rename('I2').input().on()
icestick.J1[3].rename('I3').input().on()
icestick.J1[4].rename('I4').input().on()
icestick.J1[5].rename('I5').input().on()
icestick.J1[6].rename('I6').input().on()
icestick.J3[0].rename('D0').output().on()
icestick.J3[1].rename('D1').output().on()

main = icestick.main()
WDATA = array(main.I0, main.I1, 0, 0)
WADDR = array(main.I2, main.I3, 0,0,0,0,0,0,0,0)
RADDR = array(main.I4, main.I5, 0,0,0,0,0,0,0,0)
WE = main.I6
O = array(main.D0, main.D1)

N = 4
M = 4096//N
rom = M * [0]
for i in range(M):
    rom[i] = i & 0xf

ramb = RAMB( rom )
#print(ramb.interface)

wire( WE, ramb.WE    )
wire( 1, ramb.WCLKE )
wire( WADDR, ramb.WADDR )
wire( WDATA, ramb.WDATA )

wire( 1, ramb.RE    )
wire( 1, ramb.RCLKE )
wire( RADDR, ramb.RADDR )
wire( ramb.RDATA[0:2], O)

compile(sys.argv[1], main)
