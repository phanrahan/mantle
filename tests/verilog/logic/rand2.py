import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "I", In(Array(2,Bit)), "O", Out(Bit))

and2 = ReduceAnd()

wire( and2(main.I), main.O )

EndCircuit()

compile(sys.argv[1], main)


