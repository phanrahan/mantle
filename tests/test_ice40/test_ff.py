import magma as m
from magma.backend.verilog import compile
from mantle.lattice.ice40 import SB_DFF

def test_dff():
    main = m.DefineCircuit('main', 'I', m.In(m.Bit), "O", m.Out(m.Bit), "CLK", m.In(m.Clock))
    dff = SB_DFF()
    m.wire(main.I, dff.D)
    m.wire(dff.Q, main.O)
    m.EndCircuit()

    print(compile(main)) # compile will wire up the CLK
    print(repr(main))

  
