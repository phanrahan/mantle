import sys
from magma import *
from mantle import *

main = DefineCircuit("main", "I", In(Array(1,Bit)), "O", Out(Array(1,Bit)))

buf1 = Buf(1)

wire( buf1(main.I), main.O)

compile(sys.argv[1], main)


