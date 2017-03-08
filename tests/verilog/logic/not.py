import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "input I", Bit, "output O", Bit)

_not = Not()

_not(main.I)
wire(_not, main.O)

compile(sys.argv[1], main)


