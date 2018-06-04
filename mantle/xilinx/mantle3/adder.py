from magma import *
from .LUT import A0, A1
from .fullcarry import FullCarry

__all__ = ['Adders', 'DefineAdders']

AdderCache = {}

def _AdderName(n, k, expr1, expr2, cin, cout):
    expr1 = uint(expr1, 1<<k)
    expr2 = uint(expr2, 1<<k)

    if   expr1 == A0^A1 and expr2 == A0&A1:
        name = ('Adc%d' if cout else 'Add%d') % n
    elif expr1 == (A0^(~A1))&0xffff and expr2 == A0:
        name = ('Sbc%d' if cout else 'Sub%d') % n
    else:
        name = 'Adders%d_%X_%X' % (n, expr1, expr2)

    if cin:
        name += '_cin%d' % cin
    else:
        name += '_cinNone'

    if cout:
        name += '_cout%d' % cout
    else:
        name += '_coutNone'

    return name


#
# create an n-bit Adder from n FullAdders
#
#   I0rn], ..., Ik[n], <CIN> -> O[n], <COUT>
#
# if cin is None, CIN is added to the circuit 
# if cin==0 or cin==1, cin is wired to CIN
#
# if cout: COUT is added to the circuit
#
def DefineAdders(n, k, expr1, expr2, cin, cout, forkargs=[]):
    name = _AdderName(n, k, expr1, expr2, cin is None, cout)
    if name in AdderCache:
       return AdderCache[name]

    ArrayN = Bits(n)
    args = []
    if k >= 1: args += ["I0", In(Bit) if 'I0' in forkargs else In(ArrayN)]
    if k >= 2: args += ["I1", In(Bit) if 'I1' in forkargs else In(ArrayN)]
    if k >= 3: args += ["I2", In(Bit) if 'I2' in forkargs else In(ArrayN)]
    if k >= 4: args += ["I3", In(Bit) if 'I3' in forkargs else In(ArrayN)]
    args += ["O", Out(ArrayN)]
    if cin is None:
        args += ['CIN', In(Bit)]
    if cout:
        args += ['COUT', Out(Bit)]

    Adders = DefineCircuit( name, *args )

    def f(x):
        return FullCarry(k, expr1, expr2)
    c = braid( col(f, n), foldargs={"CIN":"COUT"}, forkargs=forkargs)

    if k >= 1: wire(Adders.I0, c.I0)
    if k >= 2: wire(Adders.I1, c.I1)
    if k >= 3: wire(Adders.I2, c.I2)
    if k >= 4: wire(Adders.I3, c.I3)

    wire(c.O, Adders.O)
    if cin is not None:
        wire(cin, c.CIN)
    else:
        wire(Adders.CIN, c.CIN)
    if cout:
        wire(c.COUT, Adders.COUT)

    EndCircuit()

    AdderCache[name] = Adders
    return Adders

def Adders(n, k, expr1, expr2, cin, cout, forkargs=[]):
    return DefineAdders(n, k, expr1, expr2, cin, cout, forkargs=[])()
