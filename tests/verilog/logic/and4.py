import sys
from magma import *
from mantle import *

main = DefineCircuit("main",
        "I0", In(Bit), "I1", In(Bit), "I2", In(Bit), "I3", In(Bit),
        "O", Out(Bit))

and4 = And(4)

and4(main.I0, main.I1, main.I2, main.I3)
wire(and4, main.O)

compile(sys.argv[1], main)


