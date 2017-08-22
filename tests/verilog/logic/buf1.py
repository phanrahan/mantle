import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "I", In(Bits(1)), "O", Out(Bits(1)))

buf1 = Buf(1)

wire( buf1(main.I), main.O)

compile(sys.argv[1], main)


