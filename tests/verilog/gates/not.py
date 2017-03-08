import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "input I", Bit, "output O", Bit)

not_ = Not()

not_(main.I)
wire(not_, main.O)

compile(sys.argv[1], main)


