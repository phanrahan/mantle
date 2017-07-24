import sys
from magma import array, wire, compile
from mantle.lattice.ice40.RAMB import ROMB
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
icestick.J1[7].rename('I7').input().on()
icestick.J3[0].rename('D0').output().on()
icestick.J3[1].rename('D1').output().on()
icestick.J3[2].rename('D2').output().on()
icestick.J3[3].rename('D3').output().on()

main = icestick.main()
I = array(main.I0, main.I1, main.I2, main.I3,
          main.I4, main.I5, main.I6, main.I7, 0, 0)
O = array(main.D0, main.D1, main.D2, main.D3)

N = 4
M = 4096//N
rom = M * [0]
for i in range(M):
    rom[i] = i & 0xf

romb = ROMB( rom )
#print(romb.interface)

wire( 1, romb.RE    )
wire( 1, romb.RCLKE )
wire( I, romb.RADDR )
wire( romb.RDATA, O)

compile(sys.argv[1], main)
