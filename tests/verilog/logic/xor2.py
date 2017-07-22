import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "input I0", Bit, "input I1", Bit, "output O", Bit)

xor2 = XOr(2)

xor2(main.I0, main.I1)
wire(xor2, main.O)

compile(sys.argv[1], main)


