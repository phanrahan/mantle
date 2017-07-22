import sys
from magma import *
from mantle import *

main = DefineCircuit("main", 
        "input I0", Bit, "input I1", Bit, "input I2", Bit, "output O", Bit)

and3 = And(3)

and3(main.I0, main.I1, main.I2)
wire(and3, main.O)

compile(sys.argv[1], main)


