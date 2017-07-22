import sys
from magma import *
from mantle import *
from loam.boards.icestick import IceStick

icestick = IceStick()
for i in range(2):
    icestick.J1[i].input().on()
for i in range(2):
    icestick.J3[i].output().on()

main = icestick.main()

and2 = And2()
and2(main.J1[0], main.J1[1])
wire(and2.O, main.J3[0])

or2 = Or2()
or2(main.J1[0], main.J1[1])
wire(or2.O, main.J3[1])

compile(sys.argv[1], main)
