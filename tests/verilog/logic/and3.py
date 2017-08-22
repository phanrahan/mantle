import sys
from magma import *
from mantle import *

main = DefineCircuit("main", 
        "I0", In(Bit), "I1", In(Bit), "I2", In(Bit), "O", Out(Bit))

and3 = And(3)

and3(main.I0, main.I1, main.I2)
wire(and3, main.O)

compile(sys.argv[1], main)


