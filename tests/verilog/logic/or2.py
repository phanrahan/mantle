import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))

or2 = Or(2)

or2(main.I0, main.I1)
wire(or2, main.O)

compile(sys.argv[1], main)


