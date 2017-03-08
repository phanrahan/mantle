import sys
from magma import *
from parts.xilinx.spartan6.primitives.RAMB import ROMB
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(8)

main = megawing.main()

rom = range(2048)
for i in range(2048):
    byte = i & 0xff
    rom[i] = byte << 1

romb = ROMB( rom, 9 )

I = array(main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3],
          main.SWITCH[4], main.SWITCH[5], main.SWITCH[6], main.SWITCH[7],
          GND, GND, GND)

O = main.LED

wire( I, romb.A )
wire( romb.O[1:9], O )

compile(sys.argv[1], main)
