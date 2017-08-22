from magma import *
from mantle import Adders, And, Mux
from .register import Register
from .decode import Decode

__all__ = ['DefineCounterLoad', 'CounterLoad']

CounterCache = {}

def _CounterName(name, n, ce, r, s):
    name += '%d' % n
    if ce: name += 'CE'
    if r:  name += 'R'
    if s:  name += 'S'
    return name

#
# Create an n-bit counter with increment and load
#
#   DATA : In(Bits(n)), LOAD : In(Bit), O : Out(Bits(n)), COUT : Out(Bit)
#
def DefineCounterLoad(n, cin=False, cout=True, incr=1, next=False, has_ce=False, has_reset=False, has_set=False):

    name = _CounterName('CounterLoad', n, has_ce, has_reset, has_set)
    if name in CounterCache:
         return CounterCache[name]

    args = []
    args += ['DATA', In(Bits(n))]
    args += ['LOAD', In(Bit)]
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Out(Bits(n))]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(has_ce, has_reset, has_set)

    Counter = DefineCircuit(name, *args)

    add = Adders(n, cin=cin, cout=cout)
    mux = Mux(2, n)
    reg = Register(n, has_ce=has_ce, has_reset=has_reset, has_set=has_set)

    wire( reg.O, add.I0 )
    wire( array(incr, n), add.I1 )

    wire( add.O, mux.I0 )
    wire( Counter.DATA, mux.I1 )
    wire( Counter.LOAD, mux.S )

    reg(mux)

    if next:
        wire( mux.O, Counter.O )
    else:
        wire( reg.O, Counter.O )

    if cin:
        wire( Counter.CIN, add.CIN )

    if cout:
        wire( add.COUT, Counter.COUT ) # this is fishy because of the LOAD

    wireclock(Counter, reg)

    EndCircuit()

    CounterCache[name] = Counter
    return Counter

def CounterLoad(n, cin=False, cout=True, incr=1, 
        has_ce=False, has_reset=False, has_set=False, **kwargs):
    """Construct a n-bit counter."""
    return DefineCounterLoad(n, cin=cin, cout=cout, incr=incr, next=next, 
               has_ce=has_ce, has_reset=has_reset, has_set=has_set)(**kwargs)


