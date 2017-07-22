import sys
from magma import *
from mantle.verilog.gates import NOr

main = DefineCircuit("main", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))

nor2 = NOr(2)

wire( nor2(main.I0, main.I1), main.O)

compile(sys.argv[1], main)


