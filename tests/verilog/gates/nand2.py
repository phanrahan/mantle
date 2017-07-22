import sys
from magma import *
from mantle.verilog.gates import NAnd

main = DefineCircuit("main", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))

nand2 = NAnd(2)

wire( nand2(main.I0, main.I1), main.O)

compile(sys.argv[1], main)


