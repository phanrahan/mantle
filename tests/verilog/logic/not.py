import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "I", In(Bit), "O", Out(Bit))

n = Not()

wire( n(main.I), main.O )

compile(sys.argv[1], main)


