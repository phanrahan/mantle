from magma import *
from mantle import *
from loam.boards.icestick import IceStick


def test_bit():
    @circuit(clock=False)
    def circ(a : In(Bit), b : In(Bit), c : Out(Bit)):
        c = a + b

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Bit), "b", In(Bit), "c", Out(Bit))
inst1 = Add(1)(circ.a, circ.b)
wire(inst1, circ.c)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_array():
    @circuit(clock=False)
    def circ(a : In(Array(5, Bit)), b : In(Array(5, Bit)), c : Out(Array(5, Bit))):
        c = a + b

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(5, Bit)), "b", In(Array(5, Bit)), "c", Out(Array(5, Bit)))
inst1 = Add(5)(circ.a, circ.b)
wire(inst1, circ.c)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_sub():
    @circuit(clock=False)
    def circ(a : In(Array(5, Bit)), b : In(Array(5, Bit)), c : Out(Array(5, Bit))):
        c = -(a - b)

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(5, Bit)), "b", In(Array(5, Bit)), "c", Out(Array(5, Bit)))
inst1 = Sub(5)(circ.a, circ.b)
inst2 = Negate(5)(inst1)
wire(inst2, circ.c)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_logic_ops():
    @circuit(clock=False)
    def circ(a : In(Array(5, Bit)), b : In(Array(5, Bit)), c : Out(Array(5, Bit))):
        c = ~((a | b ^ a) & b) >> 2
    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(5, Bit)), "b", In(Array(5, Bit)), "c", Out(Array(5, Bit)))
inst1 = Xor(2, width=5)(circ.b, circ.a)
inst2 = Or(2, width=5)(circ.a, inst1)
inst3 = And(2, width=5)(inst2, circ.b)
inst4 = Invert(5)(inst3)
inst5 = RightShift(5, 2)(inst4)
wire(inst5, circ.c)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_clock():
    @circuit
    def circ(a : In(Bit), b : Out(Bit)):
        b = a

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Bit), "b", Out(Bit), "CLK", In(Bit))
wire(circ.a, circ.b)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_wire():
    @circuit
    def circ(a : In(Bit), b : Out(Bit)):
        wire(a, b)

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Bit), "b", Out(Bit), "CLK", In(Bit))
wire(circ.a, circ.b)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_register():
    @circuit
    def circ(a : In(Bit), b : Out(Bit)):
        c = Register(1)
        wire(a, c.I[0])
        wire(c.O[0], b)

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Bit), "b", Out(Bit), "CLK", In(Bit))
c = Register(1)
wire(circ.a, c.I[0])
wire(c.O[0], circ.b)
EndCircuit()
"""
    assert circ.__magma_source == expected
