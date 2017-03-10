import sys
from magma import *
from mantle.xilinx.spartan3.RAMB import ROMB
from loam.shields.megawing import MegaWing


megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(8)

main = megawing.main()

rom = range(2048)
for i in range(2048):
    byte = i & 0xff
    rom[i] = byte

romb = ROMB( rom, 8 )

I = array(main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3],
          main.SWITCH[4], main.SWITCH[5], main.SWITCH[6], main.SWITCH[7],
          GND, GND, GND)

O = main.LED

wire( I, romb.A )
wire( romb.O, O )

compile(sys.argv[1], main)
