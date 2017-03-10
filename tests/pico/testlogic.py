import sys
from magma import *
from mantle import *
from mantle.xilinx.cores.pico3.alu import DefineLogic
from loam.shields.megawing import MegaWing

megawing = MegaWing()
megawing.Clock.on()
megawing.Switch.on(6)
megawing.LED.on(2)

main = megawing.main()
A = main.SWITCH[0:2]
B = main.SWITCH[2:4]
S0 = main.SWITCH[4]
S1 = main.SWITCH[5]
O = main.LED

Logic2 = DefineLogic(2)
alu = Logic2()

#  case 00: B
#  case 01: A | B
#  case 10: A & B
#  case 11: A ^ B
O( alu(A, B, S0, S1) )

#print(hex(I0 & 0xF))
#print(hex(I1 & 0xF))
#print(hex((I0|I1) & 0xF))
#print(hex((I0&I1) & 0xF))
#print(hex((I0^I1) & 0xF))
compile(sys.argv[1], main)

