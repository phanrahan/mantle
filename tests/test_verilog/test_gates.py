from magma import *
import magma as m
from magma.backend.verilog import compile
from magma.testing import check_files_equal
from mantle.verilog import gates

def test_args():
    class Main(m.Circuit):
        a = gates.And(2, name='a')
        assert repr(a) == 'a = and(name="a")'
        assert repr(a[0]) == 'a[0]'
        assert repr(a[1]) == 'a[1]'
        assert repr(a[2]) == 'a[2]'

def test_wire():
    class Main(m.Circuit):
        a = gates.And(2, name='a')
        m.wire(a[0], a[1])
        m.wire(a[0], a[2])

def test_and2():
    And2 = DefineCircuit("And2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
    inst0 = gates.And(2)
    wire(And2.I0, inst0[1])
    wire(And2.I1, inst0[2])
    wire(inst0[0], And2.O)
    EndCircuit()

    assert repr(And2) == '''\
And2 = DefineCircuit("And2", "I0", In(Bit), "I1", In(Bit), "O", Out(Bit))
and_inst0 = and()
wire(And2.I0, and_inst0[1])
wire(And2.I1, and_inst0[2])
wire(and_inst0[0], And2.O)
EndCircuit()'''

    assert compile(And2) == '''\
module And2 (input  I0, input  I1, output  O);
wire  and_inst0_0;
and and_inst0 (and_inst0_0, I0, I1);
assign O = and_inst0_0;
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
nand_inst0 = nand()
wire(NAnd2.I0, nand_inst0[1])
wire(NAnd2.I1, nand_inst0[2])
wire(nand_inst0[0], NAnd2.O)
EndCircuit()'''

    assert compile(NAnd2) == '''\
module NAnd2 (input  I0, input  I1, output  O);
wire  nand_inst0_0;
nand nand_inst0 (nand_inst0_0, I0, I1);
assign O = nand_inst0_0;
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
or_inst0 = or()
wire(or2.I0, or_inst0[1])
wire(or2.I1, or_inst0[2])
wire(or_inst0[0], or2.O)
EndCircuit()'''

    assert compile(or2) == '''\
module or2 (input  I0, input  I1, output  O);
wire  or_inst0_0;
or or_inst0 (or_inst0_0, I0, I1);
assign O = or_inst0_0;
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
nor_inst0 = nor()
wire(nor2.I0, nor_inst0[1])
wire(nor2.I1, nor_inst0[2])
wire(nor_inst0[0], nor2.O)
EndCircuit()'''

    assert compile(nor2) == '''\
module nor2 (input  I0, input  I1, output  O);
wire  nor_inst0_0;
nor nor_inst0 (nor_inst0_0, I0, I1);
assign O = nor_inst0_0;
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
xor_inst0 = xor()
wire(xor2.I0, xor_inst0[1])
wire(xor2.I1, xor_inst0[2])
wire(xor_inst0[0], xor2.O)
EndCircuit()'''

    assert compile(xor2) == '''\
module xor2 (input  I0, input  I1, output  O);
wire  xor_inst0_0;
xor xor_inst0 (xor_inst0_0, I0, I1);
assign O = xor_inst0_0;
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
nxor_inst0 = nxor()
wire(nxor2.I0, nxor_inst0[1])
wire(nxor2.I1, nxor_inst0[2])
wire(nxor_inst0[0], nxor2.O)
EndCircuit()'''

    assert compile(nxor2) == '''\
module nxor2 (input  I0, input  I1, output  O);
wire  nxor_inst0_0;
nxor nxor_inst0 (nxor_inst0_0, I0, I1);
assign O = nxor_inst0_0;
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
buf_inst0 = buf()
wire(buffer.I, buf_inst0[1])
wire(buf_inst0[0], buffer.O)
EndCircuit()'''

    assert compile(buffer) == '''\
module buffer (input  I, output  O);
wire  buf_inst0_0;
buf buf_inst0 (buf_inst0_0, I);
assign O = buf_inst0_0;
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
not_inst0 = not()
wire(n.I, not_inst0[1])
wire(not_inst0[0], n.O)
EndCircuit()'''

    assert compile(n) == '''\
module n (input  I, output  O);
wire  not_inst0_0;
not not_inst0 (not_inst0_0, I);
assign O = not_inst0_0;
endmodule

'''
