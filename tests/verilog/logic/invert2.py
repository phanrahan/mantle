import sys
from magma import *
from mantle import *

main = DefineCircuit("main", 
        "input I0", Bit, "input I1", Bit, 
        "output O0", Bit, "output O1", Bit)

invert2 = Invert(2)

wire( invert2(array([main.I0, main.I1])), array([main.O0, main.O1]))

compile(sys.argv[1], main)


