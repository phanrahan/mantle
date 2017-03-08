import sys
from magma import *
from mantle import *

mux = Mux2()
print mux.interface

mux = Mux4()
print mux.interface

mux = Mux8()
print mux.interface

mux = Mux16()
print mux.interface

mux = MuxN(4)
print mux.interface

mux = Mux(2,1)
print mux.interface
