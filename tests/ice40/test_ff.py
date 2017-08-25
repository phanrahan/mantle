import os
os.environ['MANTLE_TARGET'] = 'ice40'
from magma import *
from magma.backend.verilog import compile
from mantle.lattice.ice40 import SB_DFF

def test_dff():
    main = DefineCircuit('main', 'I', In(Bit), "O", Out(Bit), "CLK", In(Clock))
    dff = SB_DFF()
    wire(main.I, dff.D)
    wire(dff.Q, main.O)
    EndCircuit()

    print(compile(main)) # compile will wire up the CLK
    print(repr(main))

test_dff()
  
