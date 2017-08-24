from magma import *
from magma.backend.verilog import compile
from mantle.verilog import gates

def test_and():
    And2 = DefineCircuit("And2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
    inst0 = gates.And(2)
    wire(And2.I0, inst0[1])
    wire(And2.I1, inst0[2])
    wire(inst0[0], And2.O)
    EndCircuit()

    assert repr(And2) == '''\
And2 = DefineCircuit("And2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
inst0 = and()
wire(And2.I0, inst0[1])
wire(And2.I1, inst0[2])
wire(inst0[0], And2.O)
EndCircuit()'''

    assert compile(And2) == '''\
module And2 (input  I0, input  I1, output  O);
wire  inst0_0;
and inst0 (inst0_0, I0, I1);
assign O = inst0_0;
endmodule

'''

def test_args():
    a = gates.And(2, name='a')
    assert repr(a) == 'a = and(name=a)'
    assert repr(a[0]) == 'a[0]'
    assert repr(a[1]) == 'a[1]'
    assert repr(a[2]) == 'a[2]'

def test_wire():
    a = gates.And(2, name='a')
    wire(a[0], a[1])
    wire(a[0], a[2])

