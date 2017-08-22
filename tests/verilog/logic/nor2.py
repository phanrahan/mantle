import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))

nor2 = NOr(2)

nor2(main.I0, main.I1)
wire(nor2, main.O)

compile(sys.argv[1], main)


