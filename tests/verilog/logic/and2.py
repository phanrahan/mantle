import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "input I0", Bit, "input I1", Bit, "output O", Bit)

#and2 = And(2)
and2 = And()

and2(main.I0, main.I1)
wire(and2, main.O)

EndCircuit()

compile(sys.argv[1], main)


