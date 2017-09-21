from magma import *
from magma.backend.verilog import compile
from magma.testing import check_files_equal
from mantle.verilog import gates

def test_args():
    a = gates.And(2, name='a')
    assert repr(a) == 'a = and(name="a")'
    assert repr(a[0]) == 'a[0]'
    assert repr(a[1]) == 'a[1]'
    assert repr(a[2]) == 'a[2]'

def test_wire():
    a = gates.And(2, name='a')
    wire(a[0], a[1])
    wire(a[0], a[2])

def test_and2():
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

def test_nand2():
    NAnd2 = DefineCircuit("NAnd2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
    inst0 = gates.NAnd(2)
    wire(NAnd2.I0, inst0[1])
    wire(NAnd2.I1, inst0[2])
    wire(inst0[0], NAnd2.O)
    EndCircuit()

    assert repr(NAnd2) == '''\
NAnd2 = DefineCircuit("NAnd2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
inst0 = nand()
wire(NAnd2.I0, inst0[1])
wire(NAnd2.I1, inst0[2])
wire(inst0[0], NAnd2.O)
EndCircuit()'''

    assert compile(NAnd2) == '''\
module NAnd2 (input  I0, input  I1, output  O);
wire  inst0_0;
nand inst0 (inst0_0, I0, I1);
assign O = inst0_0;
endmodule

'''

def test_or2():
    or2 = DefineCircuit("or2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
    inst0 = gates.Or(2)
    wire(or2.I0, inst0[1])
    wire(or2.I1, inst0[2])
    wire(inst0[0], or2.O)
    EndCircuit()

    assert repr(or2) == '''\
or2 = DefineCircuit("or2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
inst0 = or()
wire(or2.I0, inst0[1])
wire(or2.I1, inst0[2])
wire(inst0[0], or2.O)
EndCircuit()'''

    assert compile(or2) == '''\
module or2 (input  I0, input  I1, output  O);
wire  inst0_0;
or inst0 (inst0_0, I0, I1);
assign O = inst0_0;
endmodule

'''

def test_nor2():
    nor2 = DefineCircuit("nor2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
    inst0 = gates.NOr(2)
    wire(nor2.I0, inst0[1])
    wire(nor2.I1, inst0[2])
    wire(inst0[0], nor2.O)
    EndCircuit()

    assert repr(nor2) == '''\
nor2 = DefineCircuit("nor2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
inst0 = nor()
wire(nor2.I0, inst0[1])
wire(nor2.I1, inst0[2])
wire(inst0[0], nor2.O)
EndCircuit()'''

    assert compile(nor2) == '''\
module nor2 (input  I0, input  I1, output  O);
wire  inst0_0;
nor inst0 (inst0_0, I0, I1);
assign O = inst0_0;
endmodule

'''

def test_xor2():
    xor2 = DefineCircuit("xor2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
    inst0 = gates.XOr(2)
    wire(xor2.I0, inst0[1])
    wire(xor2.I1, inst0[2])
    wire(inst0[0], xor2.O)
    EndCircuit()

    assert repr(xor2) == '''\
xor2 = DefineCircuit("xor2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
inst0 = xor()
wire(xor2.I0, inst0[1])
wire(xor2.I1, inst0[2])
wire(inst0[0], xor2.O)
EndCircuit()'''

    assert compile(xor2) == '''\
module xor2 (input  I0, input  I1, output  O);
wire  inst0_0;
xor inst0 (inst0_0, I0, I1);
assign O = inst0_0;
endmodule

'''

def test_nxor2():
    nxor2 = DefineCircuit("nxor2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
    inst0 = gates.NXOr(2)
    wire(nxor2.I0, inst0[1])
    wire(nxor2.I1, inst0[2])
    wire(inst0[0], nxor2.O)
    EndCircuit()

    assert repr(nxor2) == '''\
nxor2 = DefineCircuit("nxor2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
inst0 = nxor()
wire(nxor2.I0, inst0[1])
wire(nxor2.I1, inst0[2])
wire(inst0[0], nxor2.O)
EndCircuit()'''

    assert compile(nxor2) == '''\
module nxor2 (input  I0, input  I1, output  O);
wire  inst0_0;
nxor inst0 (inst0_0, I0, I1);
assign O = inst0_0;
endmodule

'''

def test_buf():
    buffer = DefineCircuit("buffer", "I", In(Bit), "O", Out(Bit))
    inst0 = gates.Buf()
    wire(buffer.I, inst0[1])
    wire(inst0[0], buffer.O)
    EndCircuit()

    assert repr(buffer) == '''\
buffer = DefineCircuit("buffer", "I", In(Bit), "O", Out(Bit))
inst0 = buf()
wire(buffer.I, inst0[1])
wire(inst0[0], buffer.O)
EndCircuit()'''

    assert compile(buffer) == '''\
module buffer (input  I, output  O);
wire  inst0_0;
buf inst0 (inst0_0, I);
assign O = inst0_0;
endmodule

'''

def test_not():
    n = DefineCircuit("n", "I", In(Bit), "O", Out(Bit))
    inst0 = gates.Not()
    wire(n.I, inst0[1])
    wire(inst0[0], n.O)
    EndCircuit()

    assert repr(n) == '''\
n = DefineCircuit("n", "I", In(Bit), "O", Out(Bit))
inst0 = not()
wire(n.I, inst0[1])
wire(inst0[0], n.O)
EndCircuit()'''

    assert compile(n) == '''\
module n (input  I, output  O);
wire  inst0_0;
not inst0 (inst0_0, I);
assign O = inst0_0;
endmodule

'''
