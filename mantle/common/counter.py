from magma import *
from mantle import And, DefineAdd
from mantle import Mux
from mantle import Add
from mantle import Register
from mantle import Decode
import math

__all__  = ['DefineCounter', 'Counter']
__all__ += ['DefineUpCounter', 'UpCounter']
__all__ += ['DefineDownCounter', 'DownCounter']
__all__ += ['DefineUpDownCounter', 'UpDownCounter']


def _CounterName(name, incr, has_ce, has_reset, cin, cout):
    if incr != 1: name += f'_{incr}'
    if has_ce: name += 'CE'
    if has_reset:  name += 'R'
    if cin: name += '_CIN'
    if cout: name += '_COUT'
    return name

#
# Create an n-bit counter with a given increment.
#
# O : Out(UInt(n)), COUT : Out(Bit)
#
def DefineCounter(n, cin=False, cout=True, incr=1, has_ce=False, has_reset=False):

    name = _CounterName(f'Counter{n}', incr, has_ce, has_reset, cin, cout)

    args = []
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Out(UInt[ n ])]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(has_ce, has_reset)

    Counter = DefineCircuit(name, *args)

    add = DefineAdd(n, cin=cin, cout=cout)()
    reg = Register(n, has_ce=has_ce, has_reset=has_reset)

    wire( reg.O, add.I0 )
    wire( array(incr, n), add.I1 )

    reg(add.O)

    next = False
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

def Counter(n, cin=False, cout=True, incr=1,
             has_ce=False, has_reset=False, **kwargs):
    """Construct a n-bit up counter."""
    return DefineUpCounter(n, cin=cin, cout=cout, incr=incr,
               has_ce=has_ce, has_reset=has_reset)(**kwargs)

DefineUpCounter = DefineCounter
UpCounter = Counter

#
# Create an n-bit down counter.
#
# O : Out(UInt(n)), COUT : Out(Bit)
#
def DefineDownCounter(n, cin=False, cout=True, decr=1,
    has_ce=False, has_reset=False):
    incr = (1 << n) - (decr)
    return DefineCounter(n, cin=cin, cout=cout, incr=incr,
               has_ce=has_ce, has_reset=has_reset)

def DownCounter(n, cin=False, cout=True, decr=1,
    has_ce=False, has_reset=False, **kwargs):
    return DefineDownCounter(n, cin=cin, cout=cout, decr=decr,
               has_ce=has_ce, has_reset=has_reset)(**kwargs)


#
# Create an n-bit up-down counter.
#
# U : In(Bit), D : In(Bit), O : Out(UInt(n)), COUT : Out(Bit)
#
def DefineUpDownCounter(n, cout=True, has_ce=False, has_reset=False):

    name = _CounterName(f'UpDownCounter{n}', 1, has_ce, has_reset, False, cout)

    args = []

    args += ["U", In(Bit)]
    args += ["D", In(Bit)]

    args += ["O", Out(UInt[ n ])]
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

    next = False
    if next:
        wire( add.O, Counter.O )
    else:
        wire( reg.O, Counter.O )

    if cout:
        wire( add.COUT, Counter.COUT )

    wireclock(Counter, reg)

    EndCircuit()

    return Counter

def UpDownCounter(n, cout=True, has_ce=False, has_reset=False, **kwargs):
    """Construct an n-bit updown counter."""
    return DefineUpDownCounter(n, cout=cout,
              has_ce=has_ce, has_reset=has_reset)(**kwargs)


def DefineCeilFloorUpDownCounter(m, has_ce=False, has_reset=False):
    """
    Counter between 0 and m - 1 that uses the minimum number of bits.
    
    This counter counts up by 1 if U is True and D is False, down by 1 if U is False and D is True,
    no change if both are False or True
    
    Also, unlike normal updown counter, up by 1 has no effect if already at m - 1 and
    down by 1 has nefect if already at 0.
    
    :param m: The value the counter counts up to
    :param has_ce: Whether this counter should a clock-enable input
    :return: An updown counter circuit
    """
    class CeilFloorUpDownCounter(Circuit):
        num_bits = math.ceil(math.log(m, 2))
        name = "CeilFloorUpDownCounter_m{}_hasCE{}_hasReset{}".format(str(m), str(has_ce), str(has_reset))
        IO = ['U', In(Bit), 'D', In(Bit), 'O', Out(UInt[num_bits])] + ClockInterface(has_ce, has_reset)

        @classmethod
        def definition(ceilFloorUpDownCounter):
            up_down_counter = UpDownCounter(ceilFloorUpDownCounter.num_bits, False, has_ce, has_reset)
            at_max = Decode(m - 1, up_down_counter.O.N)(up_down_counter.O)
            at_min = Decode(0, up_down_counter.O.N)(up_down_counter.O)

            # only increase counter if input says to increase and not at max
            should_increase = ~at_max & ceilFloorUpDownCounter.U & ~ceilFloorUpDownCounter.D
            wire(should_increase, up_down_counter.U)
            # only decrease counter if input says to decrease and not at min
            should_decrease = ~at_min & ~ceilFloorUpDownCounter.U & ceilFloorUpDownCounter.D
            wire(should_decrease, up_down_counter.D)

            wire(up_down_counter.O, ceilFloorUpDownCounter.O)

    return CeilFloorUpDownCounter

def CeilFloorUpDownCounter(m, has_ce=False, has_reset=False):
    return DefineCeilFloorUpDownCounter(m, has_ce, has_reset)()
