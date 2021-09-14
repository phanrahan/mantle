from magma import *
from mantle import And, DefineAdd
from magma.passes.clock import drive_undriven_other_clock_types_in_inst
from mantle import Mux
from .register import Register
from .counter import counter_name

__all__ = ['DefineCounterLoad', 'CounterLoad']

#
# Create an n-bit counter with increment and load
#
#   DATA : In(UInt(n)), LOAD : In(Bit), O : Out(UInt(n)), COUT : Out(Bit)
#
def DefineCounterLoad(n, cin=False, cout=True, incr=1, has_ce=False, has_reset=False):

    name_ = counter_name(f'CounterLoad{n}', incr, has_ce, has_reset, cin, cout)

    args = []
    args += ['DATA', In(UInt[ n ])]
    args += ['LOAD', In(Bit)]
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Out(UInt[ n ])]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(has_ce, has_reset)

    class Counter(Circuit):
        name = name_
        io = IO(**dict(zip(args[::2], args[1::2])))

        add = DefineAdd(n, cin=cin, cout=cout)()
        mux = Mux(2, n)
        reg = Register(n, has_ce=has_ce, has_reset=has_reset)

        wire( reg.O, add.I0 )
        wire( array(incr, n), add.I1 )

        wire( add.O, mux.I0 )
        wire( io.DATA, mux.I1 )
        wire( io.LOAD, mux.S )

        reg(mux.O)

        next = False
        if next:
            wire( mux.O, io.O )
        else:
            wire( reg.O, io.O )

        if cin:
            wire( io.CIN, add.CIN )

        if cout:
            wire( add.COUT, io.COUT ) # this is fishy because of the LOAD

    drive_undriven_other_clock_types_in_inst(Counter, Counter.reg)

    return Counter

def CounterLoad(n, cin=False, cout=True, incr=1,
        has_ce=False, has_reset=False, **kwargs):
    """Construct a n-bit counter."""
    return DefineCounterLoad(n, cin=cin, cout=cout, incr=incr,
               has_ce=has_ce, has_reset=has_reset)(**kwargs)
