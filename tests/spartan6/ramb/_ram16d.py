import sys
from magma import *
from parts.xilinx.spartan6.primitives.RAMB import RAMB16D
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(8)

main = megawing.main()

romb = RAMB16D_16(
        64 * [0xabcd,0xdcba,0xcdef,0xffff] +
        64 * [0xdbdd,0xdcba,0xcaea,0xffff] +
        64 * [0xdddd,0xeeee,0xcccc,0x0000] +
        64 * [0x0000,0x1111,0x2222,0x3333], 16)

wire(main.CLK, romb.CLKA)
wire(main.CLK, romb.CLKB)
wire(1,romb.ENA)
wire(1,romb.ENB)
#wire(1,romb.REGCEA)
#wire(1,romb.REGCEB)
wire(array,romb.WEA)
wire(array,romb.WEB)
wire(array(*([0]*16)), romb.IA)
wire(array(*([0]*16)), romb.IB)

I = array(main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3],
          main.SWITCH[4], main.SWITCH[5], main.SWITCH[6], main.SWITCH[7], 
          0, 0)

O = main.LED

wire( I, romb.AA )
wire( I, romb.AB )
wire( romb.OA[:8],O)

compile(sys.argv[1], main)
