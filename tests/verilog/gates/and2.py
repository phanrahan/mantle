import sys
from magma import *
from mantle.verilog.gates import *

main = DefineCircuit("main", "input I0", Bit, "input I1", Bit, "output O", Bit)

and2 = And(2)

and2(main.I0, main.I1)
wire(and2, main.O)

compile(sys.argv[1], main)


