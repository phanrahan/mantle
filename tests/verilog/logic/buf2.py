import sys
from magma import *
from mantle import *

main = DefineCircuit("main", 
          "I0", In(Bit), "I1", In(Bit), "O0", Out(Bit), "O1", Out(Bit))

buf2 = Buf(2)

wire( buf2(array([main.I0, main.I1])), array([main.O0, main.O1]))

compile(sys.argv[1], main)


