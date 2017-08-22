from magma import *
from mantle import Adders, And, Mux
from .register import Register
from .decode import Decode

__all__  = ['DefineUpCounter', 'UpCounter']
#__all__ += ['DefineDownCounter', 'DownCounter']
__all__ += ['DefineUpDownCounter', 'UpDownCounter']
__all__ += ['DefineCounter', 'Counter']


CounterCache = {}

def _CounterName(name, n, ce, r, s):
    name += '%d' % n
    if ce: name += 'CE'
    if r:  name += 'R'
    if s:  name += 'S'
    return name

#
# Create an n-bit counter with increment.
#
#   _ -> O[n], COUT
#
def DefineUpCounter(n, cin=False, cout=True, incr=1, next=False, 
    has_ce=False, has_reset=False, has_set=False):

    name = _CounterName('Counter', n, has_ce, has_reset, has_set)
    if name in CounterCache:
         return CounterCache[name]

    args = []
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Out(Bits(n))]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(has_ce, has_reset, has_set)

    Counter = DefineCircuit(name, *args)

    add = Adders(n, cin=cin, cout=cout)
    reg = Register(n, has_ce=has_ce, has_reset=has_reset, has_set=has_set)

    wire( reg.O, add.I0 )
    wire( array(int2seq(incr, n)), add.I1 )

    reg(add)

    if next:
        wire( add.O, Counter.O )
    else:
        wire( reg.O, Counter.O )

    if cin:
        wire( Counter.CIN, add.CIN )

    if cout:
        wire( add.COUT, Counter.COUT )

    wireclock(Counter, reg)

    EndCircuit()

    CounterCache[name] = Counter
    return Counter

def UpCounter(n, cin=False, cout=True, incr=1, next=False, 
             has_ce=False, has_reset=False, has_set=False, **kwargs):
    """Construct a n-bit up counter."""
    return DefineUpCounter(n, cin=cin, cout=cout, incr=incr, next=next, 
               has_ce=has_ce, has_reset=has_reset, has_set=has_set)(**kwargs)

#
# Create an n-bit updown counter.
#
#   U : Bit, D : Bit -> O : Bits(n), COUT : Bit
#
def DefineUpDownCounter(n, cout=True, next=False, 
    has_ce=False, has_reset=False, has_set=False):

    name = _CounterName('UpDownCounter', n, has_ce, has_reset, has_set)
    if name in CounterCache:
         return CounterCache[name]

    args = []

    args += ["U", In(Bit)]
    args += ["D", In(Bit)]

    args += ["O", Out(Bits(n))]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(has_ce, has_reset, has_set)

    Counter = DefineCircuit(name, *args)

    add = Adders(n, cin=True, cout=cout)
    reg = Register(n, has_ce=has_ce, has_reset=has_reset, has_set=has_set)

    wire( reg.O, add.I0 )
    wire( array((n*[Counter.D])), add.I1 )
    wire( Counter.U, add.CIN )

    reg(add)

    if next:
        wire( add.O, Counter.O )
    else:
        wire( reg.O, Counter.O )

    if cout:
        wire( add.COUT, Counter.COUT )

    wireclock(Counter, reg)

    EndCircuit()

    CounterCache[name] = Counter
    return Counter

def UpDownCounter(n, cout=True, next=False, 
                    has_ce=False, has_reset=False, has_set=False, **kwargs):
    """Construct an n-bit updown counter."""
    return DefineUpDownCounter(n, cout=cout, next=next, 
                 has_ce=has_ce, has_reset=has_reset, has_set=has_set)(**kwargs)


DefineCounter = DefineUpCounter
Counter = UpCounter
