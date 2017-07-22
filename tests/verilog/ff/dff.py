import sys
from magma import *
from mantle.verilog.FF import *

main = DefineCircuit("main", "I", In(Bit), "O", Out(Bit), "CLK", In(Bit))

dff = DFF()

wire( dff(main.I), main.O)

compile(sys.argv[1], main)


