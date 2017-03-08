import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "input I", Bit, "output O", Bit)

buf = Buf()

buf(main.I)
wire(buf, main.O)

compile(sys.argv[1], main)


