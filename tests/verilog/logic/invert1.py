import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "I", In(Array(1,Bit)), "O", Out(Array(1,Bit)))

invert1 = Invert(1)

wire( invert1(main.I), main.O)

compile(sys.argv[1], main)


