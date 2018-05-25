from magma import *
from ..port import Adders, A0, A1, And2, Decode
from .register import Register

__all__  = ['DefineCounter', 'Counter']
__all__ += ['DefineUpDownCounter', 'UpDownCounter']
__all__ += ['CounterModM']

CounterCache = {}

def _CounterName(name, n, ce, r, s, expr1=None, expr2=None):
    name += '%d' % n
    if ce: name += 'CE'
    if r:  name += 'R'
    if s:  name += 'S'
    if expr1 is not None: name += '_%04X' % expr1
    if expr2 is not None: name += '_%04X' % expr2
    return name

#
# Create an n-bit counter primitive.
#
#   I0[n], ..., I_k-1[n], <CIN> -> O[n], COUT
#
# if cin is None, CIN is added to the circuit
# if cin==0 or cin==1, cin is wired to CIN
#
# Note that there is one less input to the counter than to the adder.
#
def DefineCounter(n, expr1, expr2, k, cin=1, next=False, ce=False, r=False, s=False):

    name = _CounterName('Counter', n, ce, r, s, expr1, expr2)
    if name in CounterCache:
         return CounterCache[name]

    ArrayN = Array(n, Bit)
    args = []
    if k >= 2: args += ['input I0', ArrayN]
    if k >= 3: args += ['input I1', ArrayN]
    if k >= 4: args += ['input I2', ArrayN]
    args += ["output O", ArrayN]
    if cin is None: args += ['input CIN', Bit]
    args += ["output COUT", Bit]
    args += ClockInterface(ce, r, s)

    Counter = DefineCircuit(name, *args)

    add = Adders(n, k, expr1, expr2, None, True)
    reg = Register(n, ce=ce, r=r, s=s)

    wire( reg.O, add.I0 )
    if k >= 2: wire( Counter.I0, add.I1 )
    if k >= 3: wire( Counter.I1, add.I2 )
    if k >= 4: wire( Counter.I2, add.I3 )

    reg(add)
    if next:
        wire( add.O, Counter.O )
    else:
        wire( reg.O, Counter.O )

    wire( add.COUT, Counter. COUT )
    if cin is None:
        wire( Counter.CIN, add.CIN )
    else:
        wire( cin, add.CIN )

    wireclock(Counter, reg)

    EndCircuit()

    CounterCache[name] = Counter
    return Counter

def Counter(n, next=False, ce=False, r=False, s=False):
    """Construct a n-bit counter."""
    return DefineCounter(n, A0, A0, k=1, cin=1, next=next, ce=ce, r=r, s=s)()

def DefineUpDownCounter(n, next=False, ce=False, r=False, s=False):
    """Construct a n-bit up-down counter."""
    name = _CounterName('UpDownCounter', n, ce, r, s)
    if name in CounterCache:
         return CounterCache[name]

    ArrayN = Array(n,Bit)
    args = [ "input U", Bit, 
             "input D", Bit, 
             "output O", ArrayN, 
             "output COUT", Bit ]
    args += ClockInterface(ce,r,s)

    UpDownCounter = DefineCircuit(name, *args)

    # I0 = n 1s, CIN=0 -1
    # I0 = n 1s, CIN=1 +0
    # I0 = n 0s, CIN=1 +1
    counter = DefineCounter(n, A0^A1, A0, k=2, 
                             cin=None, next=next, ce=ce, r=r, s=s)()

    print('wiring updown counter')
    print(counter.interface)
    # promote UoDownCounter.D to Array4
    D = array(UpDownCounter.D, UpDownCounter.D, UpDownCounter.D, UpDownCounter.D )
    counter(D, CIN=UpDownCounter.U)
    print('end wiring counter')
    wire(counter.O, UpDownCounter.O)
    wire(counter.COUT, UpDownCounter.COUT)

    wireclock(UpDownCounter, counter)

    EndCircuit()

    CounterCache[name] = UpDownCounter
    return UpDownCounter


def UpDownCounter(n, next=False, ce=False, r=False, s=False):
    return DefineUpDownCounter(n, next=next, ce=ce, r=r, s=s)()


# 
# Create an n-bit mod-m counter
#
def CounterModM(m, n):

    CE = Bit()

    counter = Counter(n, ce=True, r=True)

    reset = Decode(m - 1, n)(counter)
    reset = And2()(reset, CE)

    wire(reset, counter.RESET) # synchronous reset
    wire(CE, counter.CE)

    return AnonymousCircuit("output O", counter.O, 
                   "input CE",  CE, 
                   "input CLK", counter.CLK,
                   "output COUT", reset)
                   #"output COUT", reset.O)

#def CounterIncr(n, cout=None, site=None, **kwargs):
#    """Construct a n-bit counter with an n-bit increment."""
#
#    e1 = 'A^B'
#    e2 = 'A'
#
#    def counter(x, y, s, e):
#        ci = None
#        if y % 2 == 0:
#            ci = True if y == 0 else 'CIN'
#        co = None
#        if y % 2 == 1:
#            co = cout if y == n - 1 else 'COUT'
#        #print(x, y, s, e, ci, co)
#        return Counter1(expr1=e1, expr2=e2, cin=ci, cout=co,
#                        site=s, elem=e, **kwargs)
#
#    c = join(col(counter, n, site))
#
#    wire( 0, c.CIN )
#    if cout:
#        c.O.append(c.COUT)
#
#    return c
