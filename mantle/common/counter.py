from magma import *
from mantle.common.arith import Add
from mantle import And, Mux, DefineAdd
from .register import Register
from .decode import Decode

__all__  = ['DefineCounter', 'Counter']
__all__ += ['DefineUpCounter', 'UpCounter']
__all__ += ['DefineDownCounter', 'DownCounter']
__all__ += ['DefineUpDownCounter', 'UpDownCounter']


def _CounterName(name, n, ce, r):
    name += '%d' % n
    if ce: name += 'CE'
    if r:  name += 'R'
    return name

#
# Create an n-bit counter with a given increment.
#
# O : Out(UInt(n)), COUT : Out(Bit)
#
@cache_definition
def DefineCounter(n, cin=False, cout=True, incr=1, next=False,
    has_ce=False, has_reset=False):

    name = _CounterName('Counter', n, has_ce, has_reset)

    args = []
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Out(UInt(n))]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(has_ce, has_reset)

    Counter = DefineCircuit(name, *args)

    add = DefineAdd(n, cin=cin, cout=cout)()
    reg = Register(n, has_ce=has_ce, has_reset=has_reset)

    wire( reg.O, add.I0 )
    wire( array(incr, n), add.I1 )

    reg(add.O)

    if next:
        wire( add.O, Counter.O )
    else:
        wire( reg.O, Counter.O )

    if cin:
        wire( Counter.CIN, add.CIN )

    if cout:
        wire( add.COUT, Counter.COUT )

    wireclock(Counter, reg)
    wiredefaultclock(Counter, reg)

    EndCircuit()

    return Counter

def Counter(n, cin=False, cout=True, incr=1, next=False,
             has_ce=False, has_reset=False, **kwargs):
    """Construct a n-bit up counter."""
    return DefineUpCounter(n, cin=cin, cout=cout, incr=incr, next=next,
               has_ce=has_ce, has_reset=has_reset)(**kwargs)

DefineUpCounter = DefineCounter
UpCounter = Counter

#
# Create an n-bit down counter.
#
# O : Out(UInt(n)), COUT : Out(Bit)
#
def DefineDownCounter(n, cin=False, cout=True, decr=1, next=False,
    has_ce=False, has_reset=False):
    incr = (1 << n) - (decr)
    return DefineCounter(n, cin=cin, cout=cout, incr=incr, next=False,
               has_ce=has_ce, has_reset=has_reset)

def DownCounter(n, cin=False, cout=True, decr=1, next=False,
    has_ce=False, has_reset=False, **kwargs):
    return DefineDownCounter(n, cin=cin, cout=cout, decr=decr, next=next,
               has_ce=has_ce, has_reset=has_reset)(**kwargs)


#
# Create an n-bit up-down counter.
#
# U : In(Bit), D : In(Bit), O : Out(UInt(n)), COUT : Out(Bit)
#
def DefineUpDownCounter(n, cout=True, next=False,
    has_ce=False, has_reset=False):

    name = _CounterName('UpDownCounter', n, has_ce, has_reset)

    args = []

    args += ["U", In(Bit)]
    args += ["D", In(Bit)]

    args += ["O", Out(UInt(n))]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(has_ce, has_reset)

    Counter = DefineCircuit(name, *args)

    add = Add(n, cin=True, cout=cout)
    reg = Register(n, has_ce=has_ce, has_reset=has_reset)

    wire( reg.O, add.I0 )
    wire( array(n*[Counter.D]), add.I1 )
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

    return Counter

def UpDownCounter(n, cout=True, next=False,
                    has_ce=False, has_reset=False, **kwargs):
    """Construct an n-bit updown counter."""
    return DefineUpDownCounter(n, cout=cout, next=next,
                 has_ce=has_ce, has_reset=has_reset)(**kwargs)


