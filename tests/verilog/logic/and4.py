import sys
from magma import *
from mantle import *

main = DefineCircuit("main",
        "input I0", Bit, "input I1", Bit, "input I2", Bit, "input I3", Bit,
        "output O", Bit)

and4 = And4()

and4(main.I0, main.I1, main.I2, main.I3)
wire(and4, main.O)

compile(sys.argv[1], main)


