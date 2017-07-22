import sys
from magma import *
from mantle.verilog.gates import Buf

main = DefineCircuit("main", "I", In(Bit), "O", Out(Bit))

buf = Buf()

wire(buf(main.I), main.O)

compile(sys.argv[1], main)


