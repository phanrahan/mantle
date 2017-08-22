import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "I", In(Bits(2)), "O", Out(Bit))

xor2 = ReduceXOr()

wire( xor2(main.I), main.O )

EndCircuit()

compile(sys.argv[1], main)


