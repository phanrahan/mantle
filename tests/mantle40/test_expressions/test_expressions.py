import os
os.environ["MANTLE"] = "lattice"
from magma import *
from mantle import *


def test_bit():
    @circuit(clock=False)
    def circ(a : In(Bit), b : In(Bit), c : Out(Bit)):
        c = a + b

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Bit), "b", In(Bit), "c", Out(Bit))  # 1: def circ(a : In(Bit), b : In(Bit), c : Out(Bit)):
inst0 = Add(1)(circ.a, circ.b)  # 2:     c = a + b
wire(inst0, circ.c)  # 2:     c = a + b
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
circ = DefineCircuit("circ", "a", In(Array(5, Bit)), "b", In(Array(5, Bit)), "c", Out(Array(5, Bit)))  # 1: def circ(a : In(Array(5, Bit)), b : In(Array(5, Bit)), c : Out(Array(5, Bit))):
inst0 = Add(5)(circ.a, circ.b)  # 2:     c = a + b
wire(inst0, circ.c)  # 2:     c = a + b
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
circ = DefineCircuit("circ", "a", In(Array(5, Bit)), "b", In(Array(5, Bit)), "c", Out(Array(5, Bit)))  # 1: def circ(a : In(Array(5, Bit)), b : In(Array(5, Bit)), c : Out(Array(5, Bit))):
inst0 = Sub(5)(circ.a, circ.b)  # 2:     c = -(a - b)
inst1 = Negate(5)(inst0)  # 2:     c = -(a - b)
wire(inst1, circ.c)  # 2:     c = -(a - b)
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
circ = DefineCircuit("circ", "a", In(Array(5, Bit)), "b", In(Array(5, Bit)), "c", Out(Array(5, Bit)))  # 1: def circ(a : In(Array(5, Bit)), b : In(Array(5, Bit)), c : Out(Array(5, Bit))):
inst0 = Xor(2, width=5)(circ.b, circ.a)  # 2:     c = ~((a | b ^ a) & b) >> 2
inst1 = Or(2, width=5)(circ.a, inst0)  # 2:     c = ~((a | b ^ a) & b) >> 2
inst2 = And(2, width=5)(inst1, circ.b)  # 2:     c = ~((a | b ^ a) & b) >> 2
inst3 = Invert(5)(inst2)  # 2:     c = ~((a | b ^ a) & b) >> 2
inst4 = RightShift(5, 2)(inst3)  # 2:     c = ~((a | b ^ a) & b) >> 2
wire(inst4, circ.c)  # 2:     c = ~((a | b ^ a) & b) >> 2
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
circ = DefineCircuit("circ", "a", In(Bit), "b", Out(Bit), "CLK", In(Bit))  # 1: def circ(a : In(Bit), b : Out(Bit)):
wire(circ.a, circ.b)  # 2:     b = a
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
circ = DefineCircuit("circ", "a", In(Bit), "b", Out(Bit), "CLK", In(Bit))  # 1: def circ(a : In(Bit), b : Out(Bit)):
wire(circ.a, circ.b)  # 2:     wire(a, b)
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
circ = DefineCircuit("circ", "a", In(Bit), "b", Out(Bit), "CLK", In(Bit))  # 1: def circ(a : In(Bit), b : Out(Bit)):
c = Register(1)  # 2:     c = Register(1)
wire(circ.a, c.I[0])  # 3:     wire(a, c.I[0])
wire(c.O[0], circ.b)  # 4:     wire(c.O[0], b)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_assign_constant():
    @circuit
    def circ(b : Out(Array(3, Bit))):
        b = 6

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "b", Out(Array(3, Bit)), "CLK", In(Bit))  # 1: def circ(b : Out(Array(3, Bit))):
wire(int2seq(6, 3), circ.b)  # 2:     b = 6
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_width_promotion():
    @circuit
    def circ(b : Out(Array(3, Bit))):
        a = Register(4)
        a(1)
        c = Register(4)
        c.I = 1

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "b", Out(Array(3, Bit)), "CLK", In(Bit))  # 1: def circ(b : Out(Array(3, Bit))):
a = Register(4)  # 2:     a = Register(4)
wire(a.I, int2seq(1, 4))
c = Register(4)  # 4:     c = Register(4)
wire(int2seq(1, 4), c.I)  # 5:     c.I = 1
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_width_promotion_binop():
    @circuit
    def circ(a : In(Array(3, Bit)), b : Out(Array(3, Bit))):
        b = a + 1


    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(3, Bit)), "b", Out(Array(3, Bit)), "CLK", In(Bit))  # 1: def circ(a : In(Array(3, Bit)), b : Out(Array(3, Bit))):
inst0 = Add(3)(circ.a, int2seq(1, 3))  # 2:     b = a + 1
wire(inst0, circ.b)  # 2:     b = a + 1
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_subscript():
    @circuit
    def circ(a : In(Array(4, Bit)), b : Out(Bit), c : In(Array(2, Bit)), d : Out(Bit)):
        b = a[0]
        d = a[c]


    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(4, Bit)), "b", Out(Bit), "c", In(Array(2, Bit)), "d", Out(Bit), "CLK", In(Bit))  # 1: def circ(a : In(Array(4, Bit)), b : Out(Bit), c : In(Array(2, Bit)), d : Out(Bit)):
wire(circ.a[0], circ.b)  # 2:     b = a[0]
inst0 = MuxN(4)(circ.a, circ.c)  # 3:     d = a[c]
wire(inst0, circ.d)  # 3:     d = a[c]
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_And():
    @circuit
    def circ(a : In(Array(4, Bit)), b : Out(Bit), c : In(Array(4, Bit)), d : Out(Bit)):
        b = a[0] and a[1]
        d = a and c


    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(4, Bit)), "b", Out(Bit), "c", In(Array(4, Bit)), "d", Out(Bit), "CLK", In(Bit))  # 1: def circ(a : In(Array(4, Bit)), b : Out(Bit), c : In(Array(4, Bit)), d : Out(Bit)):
inst0 = And(2, width=1)(circ.a[0], circ.a[1])  # 2:     b = a[0] and a[1]
inst1 = AndN(1)(inst0)  # 2:     b = a[0] and a[1]
wire(inst1, circ.b)  # 2:     b = a[0] and a[1]
inst2 = And(2, width=4)(circ.a, circ.c)  # 3:     d = a and c
inst3 = AndN(4)(inst2)  # 3:     d = a and c
wire(inst3, circ.d)  # 3:     d = a and c
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_Or():
    @circuit
    def circ(a : In(Array(4, Bit)), b : Out(Bit), c : In(Array(4, Bit)), d : Out(Bit)):
        b = a[0] or a[1]
        d = a or c


    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(4, Bit)), "b", Out(Bit), "c", In(Array(4, Bit)), "d", Out(Bit), "CLK", In(Bit))  # 1: def circ(a : In(Array(4, Bit)), b : Out(Bit), c : In(Array(4, Bit)), d : Out(Bit)):
inst0 = Or(2, width=1)(circ.a[0], circ.a[1])  # 2:     b = a[0] or a[1]
inst1 = OrN(1)(inst0)  # 2:     b = a[0] or a[1]
wire(inst1, circ.b)  # 2:     b = a[0] or a[1]
inst2 = Or(2, width=4)(circ.a, circ.c)  # 3:     d = a or c
inst3 = OrN(4)(inst2)  # 3:     d = a or c
wire(inst3, circ.d)  # 3:     d = a or c
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_Not():
    @circuit
    def circ(a : In(Array(4, Bit)), b : Out(Bit)):
        b = not a


    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(4, Bit)), "b", Out(Bit), "CLK", In(Bit))  # 1: def circ(a : In(Array(4, Bit)), b : Out(Bit)):
inst0 = NorN(4)(circ.a)  # 2:     b = not a
wire(inst0, circ.b)  # 2:     b = not a
EndCircuit()
"""
    assert circ.__magma_source == expected


def test_EQ():
    @circuit
    def circ(a : In(Array(4, Bit)), b : In(Array(4, Bit)), c : Out(Bit)):
        c = a == b


    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(4, Bit)), "b", In(Array(4, Bit)), "c", Out(Bit), "CLK", In(Bit))  # 1: def circ(a : In(Array(4, Bit)), b : In(Array(4, Bit)), c : Out(Bit)):
inst0 = EQ(4)(circ.a, circ.b)  # 2:     c = a == b
wire(inst0, circ.c)  # 2:     c = a == b
EndCircuit()
"""
    assert circ.__magma_source == expected
