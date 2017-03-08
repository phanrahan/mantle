import sys
from magma import *
from mantle import *
from shields.megawing import MegaWing

megawing = MegaWing()
megawing.Switch.on(4)
megawing.LED.on(8)

#      a
#     ---
#  f |   | b
#     -g-
#  e |   | c
#     ---    . dp
#      d

# common anode
mem = [[1,1,1,1,1,1,0,0],
       [0,1,1,0,0,0,0,0],
       [1,1,0,1,1,0,1,0],
       [1,1,1,1,0,0,1,0],
       [0,1,1,0,0,1,1,0],
       [1,0,1,1,0,1,1,0],
       [0,0,1,1,1,1,1,0],
       [1,1,1,0,0,0,0,0],
       [1,1,1,1,1,1,1,0],
       [1,1,1,0,0,1,1,0],
       [1,1,1,0,1,1,1,0],
       [0,0,1,1,1,1,1,0],
       [1,0,0,1,1,1,0,0],
       [0,1,1,1,1,0,1,0],
       [1,0,0,1,1,1,1,0],
       [1,0,0,0,1,1,1,0]]


main = megawing.main()
I = main.SWITCH
O = main.LED

rom = ROM16xN(mem)

rom(I)
wire( rom.O, O )

compile(sys.argv[1], main)

