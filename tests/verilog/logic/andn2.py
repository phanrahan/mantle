import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))

and2 = uncurry(And(2))

wire( and2(array([main.I0, main.I1])), main.O)

compile(sys.argv[1], main)


