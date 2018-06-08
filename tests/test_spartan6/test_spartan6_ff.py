from magma import DefineCircuit, EndCircuit, In, Out, Bit, Clock, wire
from magma.backend.verilog import compile
from mantle.xilinx.spartan6 import FDCE

def test_fdce6():
    main = DefineCircuit('main', 'I', In(Bit), "O", Out(Bit), "CLK", In(Clock))
    dff = FDCE()
    wire(1, dff.CE)
    wire(0, dff.CLR)
    wire(main.I, dff.D)
    wire(dff.Q, main.O)
    EndCircuit()

    print(compile(main)) # compile will wire up the CLK
    print(repr(main))

