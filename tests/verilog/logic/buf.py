import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "I", In(Bit), "O", Out(Bit))

buf = Buf()

buf(main.I)
wire(buf, main.O)

compile(sys.argv[1], main)


