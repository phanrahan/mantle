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
icestick.J3[4].rename('D4').output().on()
icestick.J3[5].rename('D5').output().on()
icestick.J3[6].rename('D6').output().on()
icestick.J3[7].rename('D7').output().on()

main = icestick.main()
I = array(main.I0, main.I1, main.I2, main.I3,
          main.I4, main.I5, main.I6, main.I7, 0)
O = array(main.D0, main.D1, main.D2, main.D3,
          main.D4, main.D5, main.D6, main.D7)


N = 8
M = 4096//N
rom = M * [0]
for i in range(M):
    rom[i] = i & 0xff

romb = ROMB( rom )
print(romb.interface)

wire( 1, romb.RE    )
wire( 1, romb.RCLKE )
wire( I, romb.RADDR )
wire( romb.RDATA, O)

compile(sys.argv[1], main)
