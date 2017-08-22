import sys
from magma import *
from mantle import *

main = DefineCircuit("main", 
        "I0", In(Bit), "I1", In(Bit), "I2", In(Bit), "I3", In(Bit),
        "O0", Out(Bit), "O1", Out(Bit))

and2 = And(2,2)

and2(array([main.I0, main.I1]), array([main.I2, main.I3]))
wire(and2, array([main.O0, main.O1]))

compile(sys.argv[1], main)


