import sys
from magma import *
from mantle import *

main = DefineCircuit("main", 
        "input I0", Bit, "input I1", Bit, "input I2", Bit, "input I3", Bit,
        "output O0", Bit, "output O1", Bit)

and2 = And(2,2)

and2(array(main.I0, main.I1), array(main.I2, main.I3))
wire(and2, array(main.O0, main.O1))

compile(sys.argv[1], main)


