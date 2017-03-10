import sys
from magma import *
from mantle import *
from loam.shields.megawing import MegaWing

N = 4

megawing = MegaWing()
megawing.Switch.on(N)
megawing.LED.on(1)

main = megawing.main()

def parity(i):
   parity = 0
   while (i):
       parity = ~parity
       i &= i - 1
   return 1 if parity != 0 else 0

def bitset(i,mask):
   return 1 if i & mask else 0

PowN = 1 << 4

rom = range(PowN)
for i in range(PowN):
    #rom[i] = bitset(i, 1 << 0)
    rom[i] = parity(i)

ROM = ROM4 if N==4 else ROM5

rom = ROM(rom)

wire( rom(main.SWITCH), main.LED[0] )

compile(sys.argv[1], main)
