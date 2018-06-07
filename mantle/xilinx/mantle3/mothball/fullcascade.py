from magma import *
from .LUT import A0, A1
from .carry import FullCarry
from .halfcascade import InputArgs

__all__ = ['DefineFullCascade', 'FullCascade']

NameCache = {}

def _FullCascadeName(n, k, lutexpr, andexpr, cin, cout):
    lutexpr = lutexpr & 0xffff # uint(lutexpr, 1<<k)
    andexpr = andexpr & 0xffff # uint(andexpr, 1<<k)

    #if   lutexpr == A0^A1 and andexpr == A0&A1:
    #    name = ('Adc%d' if cout else 'Add%d') % n
    #elif lutexpr == (A0^(~A1))&0xffff and andexpr == A0:
    #    name = ('Sbc%d' if cout else 'Sub%d') % n
    name = 'FullCascade%d_%04X_%04X' % (n, lutexpr, andexpr)

    if cin:
        name += '_cin'

    if cout:
        name += '_cout'

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
def DefineFullCascade(n, k, lutexpr, andexpr, cin, cout, forkargs=[], name=None):
    if name is None:
        name = name + str(n)
    else:
        name = _FullCascadeName(n, k, lutexpr, andexpr, cin is None, cout)

    if name in NameCache:
       return NameCache[name]

    args = InputArgs(n, k, forkargs) + ['O', Out(Bits(n))]
    if cin is None:
        args += ['CIN', In(Bit)]
    if cout:
        args += ['COUT', Out(Bit)]

    Adders = DefineCircuit( name, *args )

    def f(x):
        return FullCarry(k, lutexpr, andexpr)
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

    NameCache[name] = Adders
    return Adders

def FullCascade(n, k, lutexpr, andexpr, cin, cout, forkargs=[], name=None):
    return DefineFullCascade(n, k, lutexpr, andexpr, cin, cout, forkargs=[], name=name)()
