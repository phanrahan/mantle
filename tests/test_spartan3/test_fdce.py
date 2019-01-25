import magma
magma.config.set_database_hash_backend("verilog")
from magma import DefineCircuit, EndCircuit, In, Out, Bit, Clock, wire
from magma.backend.verilog import compile
from mantle.xilinx.spartan3 import FDCE

def test_fdce():
    main = DefineCircuit('main', 'I', In(Bit), "O", Out(Bit), "CLK", In(Clock))
    dff = FDCE()
    wire(1, dff.CE)
    wire(0, dff.CLR)
    wire(main.I, dff.D)
    wire(dff.Q, main.O)
    EndCircuit()

    print(compile(main))
    print(repr(main))

