from magma import *
from mantle import And, Decode, Or
from .counter import Counter
import math

__all__ = ['DefineUpCounterModM', 'UpCounterModM']
#__all__ += ['DefineDownCounterModM', 'DownCounterModM']
__all__ += ['DefineCounterModM', 'CounterModM', 'SizedCounterModM']

def _CounterName(name, n, m, cin, cout, ce, r, s):
    name += '{}'.format(n)
    name += 'Mod{}'.format(m)
    if cin: name += 'CIN'
    if cout: name += 'COUT'
    if ce: name += 'CE'
    if r:  name += 'R'
    if s:  name += 'S'
    return name

#
# Create an n-bit mod-m counter
#
@cache_definition
def DefineCounterModM(m, n, cin=False, cout=True, incr=1, next=False,
    has_ce=False, has_reset=False):

    r = has_reset
    s = False
    name = _CounterName('Counter', n, m, cin, cout, has_ce, r, s)

    args = []
    if cin:
        args += ['CIN', In(Bit)]

    args += ["O", Out(UInt(n))]
    if cout:
        args += ["COUT", Out(Bit)]

    args += ClockInterface(has_ce, r, s)

    CounterModM = DefineCircuit(name, *args)

    counter = Counter(n, cin=cin, cout=False, incr=incr, next=next,
                   has_ce=has_ce, has_reset=True)
    reset = Decode(m - 1, n)(counter.O)

    if has_reset:
        reset = Or(2)(reset, CounterModM.RESET)

    if has_ce:
        CE = CounterModM.CE
        reset = And(2)(reset, CE)
        # reset is sometimes called rollover or RO
        # note that we don't return RO in Counter

        # should also handle r in the definition

    wire(reset, counter.RESET) # synchronous reset

    if has_ce:
        wire(CE, counter.CE)

    if cin:
        wire( CounterModM.CIN, counter.CIN )

    wire( counter.O, CounterModM.O )

    if cout:
        wire( reset, CounterModM.COUT )

    EndCircuit()

    return CounterModM

def CounterModM(m, n, cin=False, cout=True, incr=1, next=False,
    has_ce=False, has_reset=False, **kwargs):
    return DefineCounterModM(m, n, cin, cout, incr, next, has_ce, has_reset=has_reset)(**kwargs)

def SizedCounterModM(m, cin=False, cout=False, incr=1, next=False,
    has_ce=False, **kwargs):
    """
    This is that counts from 0 to m - 1 that uses the minimum number of bits
    :param m: The value the counter counts up to
    :param cin: Whether this counter should have a carry input
    :param cout: Whether this counter should a carry output
    :param incr: How much this counter should increment by per clock. Default is 1.
    :param next:
    :param has_ce: Whether this counter should a clock-enable input
    :param kwargs: Args passed to the counter circuit when it is being initialized
    :return: A counter circuit
    """
    return DefineCounterModM(m, math.ceil(math.log(m, 2)), cin, cout, incr, next, has_ce)(**kwargs)

DefineUpCounterModM = DefineCounterModM
UpCounterModM = CounterModM
