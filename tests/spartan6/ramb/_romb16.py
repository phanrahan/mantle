import sys
from magma import *
from mantle.xilinx.spartan6.RAMB import ROMB
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(8)
megawing.LED.on(8)

main = megawing.main()

rom = range(1024)
for i in range(1024):
    byte = i & 0xff
    rom[i] = byte << 8

print('romb')
romb = ROMB( rom, 16 )

I = array(main.SWITCH[0], main.SWITCH[1], main.SWITCH[2], main.SWITCH[3],
          main.SWITCH[4], main.SWITCH[5], main.SWITCH[6], main.SWITCH[7],
          GND, GND)

O = main.LED

print('wiring addr')
wire( I, romb.A )
print('wiring data')
wire( romb.O[8:16], O )

compile(sys.argv[1], main)
