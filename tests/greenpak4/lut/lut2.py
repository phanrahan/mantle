import sys
from magma import *
from mantle.silego.greenpak4 import GP_LUT2

main = DefineCircuit("main", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))

lut = GP_LUT2(INIT="4'h8")
wire(main.I0, lut.IN0)
wire(main.I1, lut.IN1)
wire(lut.OUT, main.O)

compile(sys.argv[1], main)
