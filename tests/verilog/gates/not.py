import sys
from magma import *
from mantle.verilog.gates import Not

main = DefineCircuit("main", "I", In(Bit), "O", Out(Bit))

not_ = Not()

wire( not_(main.I), main.O)

compile(sys.argv[1], main)


