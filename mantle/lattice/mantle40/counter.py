from magma import *
from .register import Register
from .decode import Decode
from .adder import Adders
from .logic import And2
from .MUX import Mux

__all__  = ['DefineCounter', 'Counter']
__all__ += ['DefineUpDownCounter', 'UpDownCounter']
__all__ += ['DefineCounterLoad', 'CounterLoad']
__all__ += ['DefineCounterModM', 'CounterModM']

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
def DefineCounter(n, cin=False, cout=True, incr=1, next=False, ce=False, r=False, s=False):

    name = _CounterName('Counter', n, ce, r, s)
    if name in CounterCache:
         return CounterCache[name]

    args = []
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Array(n, Out(Bit))]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(ce, r, s)

    Counter = DefineCircuit(name, *args)

    add = Adders(n, cin=cin, cout=cout)
    reg = Register(n, ce=ce, r=r, s=s)

    wire( reg.O, add.I0 )
    wire( array(*int2seq(incr, n)), add.I1 )

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

def Counter(n, cin=False, cout=True, incr=1, next=False, ce=False, r=False, s=False,
                **kwargs):
    """Construct a n-bit counter."""
    return DefineCounter(n, cin=cin, cout=cout, incr=incr, next=next, 
               ce=ce, r=r, s=s)(**kwargs)
#
# Create an n-bit counter with increment and load
#
#   DATA : Array(n, Bit), LOAD : Bit  -> O : Array(n, Bit), COUT : Bit
#
def DefineCounterLoad(n, cin=False, cout=True, incr=1, next=False, ce=False, r=False, s=False):

    name = _CounterName('CounterLoad', n, ce, r, s)
    if name in CounterCache:
         return CounterCache[name]

    args = []
    args += ['DATA', Array(n, In(Bit))]
    args += ['LOAD', In(Bit)]
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Array(n, Out(Bit))]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(ce, r, s)

    Counter = DefineCircuit(name, *args)

    add = Adders(n, cin=cin, cout=cout)
    mux = Mux(2, n)
    reg = Register(n, ce=ce, r=r, s=s)

    wire( reg.O, add.I0 )
    wire( array(*int2seq(incr, n)), add.I1 )

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

def CounterLoad(n, cin=False, cout=True, incr=1, ce=False, r=False, s=False,
                **kwargs):
    """Construct a n-bit counter."""
    return DefineCounterLoad(n, cin=cin, cout=cout, incr=incr, next=next, 
               ce=ce, r=r, s=s)(**kwargs)


#
# Create an n-bit updown counter.
#
#   U : Bit, D : Bit -> O : Array[n,Bit], COUT : Bit
#
def DefineUpDownCounter(n, cout=True, next=False, ce=False, r=False, s=False):

    name = _CounterName('UpDownCounter', n, ce, r, s)
    if name in CounterCache:
         return CounterCache[name]

    args = []

    args += ["U", In(Bit)]
    args += ["D", In(Bit)]

    args += ["O", Array(n, Out(Bit))]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(ce, r, s)

    Counter = DefineCircuit(name, *args)

    add = Adders(n, cin=True, cout=cout)
    reg = Register(n, ce=ce, r=r, s=s)

    wire( reg.O, add.I0 )
    wire( array(*(n*[Counter.D])), add.I1 )
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

def UpDownCounter(n, cout=True, next=False, ce=False, r=False, s=False,
                     **kwargs):
    """Construct an n-bit updown counter."""
    return DefineUpDownCounter(n, cout=cout, next=next, 
                 ce=ce, r=r, s=s)(**kwargs)

#
# Create an n-bit mod-m counter
#
def DefineCounterModM(m, n, cin=False, cout=True, incr=1, next=False, ce=False):

    r = False
    s = False
    name = _CounterName('CounterModM', n, ce, r, s)
    if name in CounterCache:
         return CounterCache[name]

    args = []
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Array(n, Out(Bit))]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(ce, r, s)

    CounterModM = DefineCircuit(name, *args)

    counter = Counter(n, cin=cin, cout=cout, incr=incr, next=next,
                   ce=ce, r=True, s=False)
    reset = Decode(m - 1, n)(counter)

    if ce:
        CE = In(Bit)()
        reset = And2()(reset, CE)
        # reset is sometimes called rollover or RO
        # note that we don't return RO in Counter

        # should also handle r in the definition

    wire(reset, counter.RESET) # synchronous reset

    if ce: 
        wire(CE, counter.CE)

    if cin:
        wire( CounterModM.CIN, counter.CIN )

    wire( counter.O, CounterModM.O )

    if cout:
        wire( reset, CounterModM.COUT )

    wire(CounterModM.CLK, counter.CLK)
    if hasattr(counter,"CE"):
        wire(CounterModM.CE, counter.CE)

    EndCircuit()

    CounterCache[name] = CounterModM
    return CounterModM

def CounterModM(m, n, cin=False, cout=True, incr=1, next=False, ce=False, **kwargs):
    return DefineCounterModM(m, n, cin=False, cout=True, incr=1, next=False, ce=False)(**kwargs)
