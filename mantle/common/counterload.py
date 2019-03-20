from magma import *
from mantle import And, DefineAdd
from mantle import Mux
from .register import Register
from .counter import _CounterName

__all__ = ['DefineCounterLoad', 'CounterLoad']

#
# Create an n-bit counter with increment and load
#
#   DATA : In(UInt(n)), LOAD : In(Bit), O : Out(UInt(n)), COUT : Out(Bit)
#
def DefineCounterLoad(n, cin=False, cout=True, incr=1, has_ce=False, has_reset=False):

    name = _CounterName(f'CounterLoad{n}', incr, has_ce, has_reset, cin, cout)

    args = []
    args += ['DATA', In(UInt[ n ])]
    args += ['LOAD', In(Bit)]
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Out(UInt[ n ])]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(has_ce, has_reset)

    Counter = DefineCircuit(name, *args)

    add = DefineAdd(n, cin=cin, cout=cout)()
    mux = Mux(2, n)
    reg = Register(n, has_ce=has_ce, has_reset=has_reset)

    wire( reg.O, add.I0 )
    wire( array(incr, n), add.I1 )

    wire( add.O, mux.I0 )
    wire( Counter.DATA, mux.I1 )
    wire( Counter.LOAD, mux.S )

    reg(mux.O)

    next = False
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

    return Counter

def CounterLoad(n, cin=False, cout=True, incr=1,
        has_ce=False, has_reset=False, **kwargs):
    """Construct a n-bit counter."""
    return DefineCounterLoad(n, cin=cin, cout=cout, incr=incr, 
               has_ce=has_ce, has_reset=has_reset)(**kwargs)


