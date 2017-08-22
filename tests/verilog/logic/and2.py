import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))

and2 = And()

and2(main.I0, main.I1)
wire(and2, main.O)

EndCircuit()

compile(sys.argv[1], main)


