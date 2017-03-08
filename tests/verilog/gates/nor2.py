import sys
from magma import *
from mantle.verilog.gates import *

main = DefineCircuit("main", "input I0", Bit, "input I1", Bit, "output O", Bit)

nor2 = NOr(2)

nor2(main.I0, main.I1)
wire(nor2, main.O)

compile(sys.argv[1], main)


