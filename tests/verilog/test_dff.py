from magma import *
from magma.backend.verilog import compile
from mantle.verilog import DFF

def test_dff():
    main = DefineCircuit('main', 'I', In(Bit), "O", Out(Bit), "CLK", In(Clock))
    dff = DFF()
    wire(main.I, dff.D)
    wire(dff.Q, main.O)
    #wire(main.CLK, dff.CLK)
    EndCircuit()

    print(repr(main))
    print(compile(main))

test_dff()
  
