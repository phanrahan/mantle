import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "input I0", Bit, "input I1", Bit, "output O", Bit)
print(main.interface)

and2 = AndN(2)
print(and2.interface)
print(type(and2.I))

and2(array(main.I0, main.I1))
print('wire and2')
wire(and2, main.O)

compile(sys.argv[1], main)


