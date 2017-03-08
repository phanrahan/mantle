from magma import *
from ..ice40.PLB import SB_CARRY, I0, I1, I2, I3
from .LUT import LUT4

__all__  = ["HalfAdder", "FullAdder"]
__all__ += ['Adders', 'DefineAdders']

#
# A : Bit, B : Bit -> S : Bit, COUT : BIT
#
def HalfAdder(**kwargs):
    A = In(Bit)()
    B = In(Bit)()

    sum = LUT4(I1^I2^I3, **kwargs)
    carry = SB_CARRY() # (I0&I1)|(I1&I2)|(I2&I0)

    sum(0,A,B,0)
    carry(A,B,0)

    return AnonymousCircuit("I0", A, "I1", B, "O", sum.O, "COUT", carry.CO)

#
# A : Bit, B : Bit, CIN : Bit -> S : Bit, COUT : Bit
#
def FullAdder(**kwargs):
    A = In(Bit)()
    B = In(Bit)()
    CIN = In(Bit)()

    sum = LUT4(I1^I2^I3, **kwargs)
    carry = SB_CARRY() # (I0&I1)|(I1&I2)|(I2&I0)

    sum(0,A,B,CIN)
    carry(A,B,CIN)

    return AnonymousCircuit("I0", A, "I1", B, "CIN", CIN, 
                            "O", sum.O, "COUT", carry.CO)

AdderCache = {}

def _AdderName(n, cin, cout):
    return "Add{}{}{}".format(
        "cin"  if cin  else "",
        "cout" if cout else "",
        n
    )

#
# create an n-bit Adder from n FullAdders
#
# I0:Array(n,Bit), I1:Array(n,Bit), CIN:Bit -> O:Array(n.Bit), COUT:Bit
#
# if cin, CIN is added to the circuit
# if cout: COUT is added to the circuit
#
def DefineAdders(n, cin, cout, forkargs=[]):
    name = _AdderName(n, cin, cout)
    if name in AdderCache:
       return AdderCache[name]

    ArrayN = Array(n,Bit)
    args = ["I0", In(ArrayN), "I1", In(ArrayN)]
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Out(ArrayN)]
    if cout:
        args += ['COUT', Out(Bit)]

    Adders = DefineCircuit( name, *args )

    def f(y):
        return FullAdder(loc=(0,y/8, y%8))

    c = braid( col(f, n), foldargs={"CIN":"COUT"}, forkargs=forkargs)

    wire(Adders.I0, c.I0)
    wire(Adders.I1, c.I1)

    wire(c.O, Adders.O)

    if cin:
        wire(Adders.CIN, c.CIN)
    else:
        wire(0, c.CIN)

    if cout:
        wire(c.COUT, Adders.COUT)

    EndCircuit()

    AdderCache[name] = Adders
    return Adders

def Adders(n, cin, cout, forkargs=[], **kwargs):
    return DefineAdders(n, cin, cout, forkargs=forkargs)(**kwargs)
