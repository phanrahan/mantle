import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico3.alu import DefineArith
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(7)
megawing.LED.on(3)

main = megawing.main()
SUB = main.SWITCH[4]
SEL = main.SWITCH[5]
CIN = main.SWITCH[6]
A = main.SWITCH[0:2]
B = main.SWITCH[2:4]
O = main.LED[0:2]
COUT = main.LED[2]

Arith2 = DefineArith(2)
alu = Arith2()

O( alu( A, B, SUB, SEL ) )
wire( CIN, alu.CIN )
wire( alu.COUT, COUT )

compile(sys.argv[1], main)

