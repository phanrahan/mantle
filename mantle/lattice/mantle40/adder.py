from magma import *
from .fulladder import FullAdder

__all__ = ['Adders', 'DefineAdders']

AdderCache = {}

def _AdderName(n, cin, cout):
    return "Adder{}{}{}".format(
        "Cin"  if cin  else "",
        "Cout" if cout else "",
        n
    )

#
# create an n-bit Adder from n FullAdders
#
# I0:In(Bits(n)), I1:In(Bits(n)), CIN:In(Bit), O:Out(Bits(n)), COUT:Out(Bit)
#
# if cin, CIN is added to the circuit
# if cout: COUT is added to the circuit
#
def DefineAdders(n, cin, cout, forkargs=[]):
    name = _AdderName(n, cin, cout)
    if name in AdderCache:
       return AdderCache[name]

    T = Bits(n)
    args = ["I0", In(T), "I1", In(T)]
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Out(T)]
    if cout:
        args += ['COUT', Out(Bit)]

    Adders = DefineCircuit( name, *args )

    def f(y):
        return FullAdder(loc=(0,y//8, y%8))

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
