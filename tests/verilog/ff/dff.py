import sys
from magma import *
from mantle import *

main = DefineCircuit("main", 
        "input I", Bit, "output O", Bit, "input CLK", Bit)

dff = DFF()

dff(main.I)
wire(dff, main.O)

compile(sys.argv[1], main)


