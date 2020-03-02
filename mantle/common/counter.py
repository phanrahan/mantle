import math
import magma as m
from mantle import And, DefineAdd
from mantle import Mux
from mantle import Add
from mantle import Register
from mantle import Decode


__all__  = ['DefineCounter', 'Counter']
__all__ += ['DefineUpCounter', 'UpCounter']
__all__ += ['DefineDownCounter', 'DownCounter']
__all__ += ['DefineUpDownCounter', 'UpDownCounter']


def counter_name(name, incr, has_ce, has_reset, cin, cout):
    if incr != 1: name += f'_{incr}'
    if has_ce: name += 'CE'
    if has_reset:  name += 'R'
    if cin: name += '_CIN'
    if cout: name += '_COUT'
    return name


def DefineCounter(n, cin=False, cout=True, incr=1,
                  has_ce=False, has_reset=False):
    """
    Create an n-bit counter with a given increment.

    O : m.Out(m.UInt(n)), COUT : m.Out(m.Bit)
    """
    name_ = counter_name(f'Counter{n}', incr, has_ce, has_reset, cin, cout)
    args = {}
    if cin:
        args["CIN"] = m.In(m.Bit)
    args["O"] = m.Out(m.UInt[n])
    if cout:
        args["COUT"] = m.Out(m.Bit)

    class _Counter(m.Circuit):
        name = name_
        io = m.IO(**args)
        io += m.ClockIO(has_ce, has_reset)

        add = DefineAdd(n, cin=cin, cout=cout)()
        reg = Register(n, has_ce=has_ce, has_reset=has_reset)

        m.wire(reg.O, add.I0)
        m.wire(m.array(incr, n), add.I1)
        reg(add.O)

        next = False
        if next:
            m.wire(add.O, io.O)
        else:
            m.wire(reg.O, io.O)
        if cin:
            m.wire(io.CIN, add.CIN)
        if cout:
            m.wire(add.COUT, io.COUT)

    return _Counter


def Counter(n, cin=False, cout=True, incr=1,
            has_ce=False, has_reset=False, **kwargs):
    """Construct a n-bit up counter"""
    defn = DefineUpCounter(n, cin=cin, cout=cout, incr=incr, has_ce=has_ce,
                           has_reset=has_reset)
    return defn(**kwargs)


DefineUpCounter = DefineCounter
UpCounter = Counter


def DefineDownCounter(n, cin=False, cout=True, decr=1,
                      has_ce=False, has_reset=False):
    """
    Create an n-bit down counter.

    O : m.Out(m.UInt(n)), COUT : m.Out(m.Bit)
    """
    incr = (1 << n) - (decr)
    return DefineCounter(n, cin=cin, cout=cout, incr=incr, has_ce=has_ce,
                         has_reset=has_reset)


def DownCounter(n, cin=False, cout=True, decr=1,
                has_ce=False, has_reset=False, **kwargs):
    defn = DefineDownCounter(n, cin=cin, cout=cout, decr=decr,
                             has_ce=has_ce, has_reset=has_reset)
    return defn(**kwargs)


def DefineUpDownCounter(n, cout=True, has_ce=False, has_reset=False):
    """
    Create an n-bit up-down counter.

    U : In(Bit), D : In(Bit), O : Out(UInt(n)), COUT : Out(Bit)
    """
    name_ = counter_name(f'UpDownCounter{n}', 1, has_ce,
                         has_reset, False, cout)

    args = {"U": m.In(m.Bit), "D": m.In(m.Bit), "O": m.Out(m.UInt[n])}
    if cout:
        args["COUT"] = m.Out(m.Bit)

    class _Counter(m.Circuit):
        name = name_
        io = m.IO(**args)
        io += m.ClockIO(has_ce, has_reset)

        add = Add(n, cin=True, cout=cout)
        reg = Register(n, has_ce=has_ce, has_reset=has_reset)
    
        m.wire(reg.O, add.I0)
        m.wire(m.array(n * [io.D]), add.I1)
        m.wire(io.U, add.CIN)
    
        reg(add)
    
        next = False
        if next:
            m.wire(add.O, io.O)
        else:
            m.wire(reg.O, io.O)
        if cout:
            m.wire(add.COUT, io.COUT)
    
    return _Counter


def UpDownCounter(n, cout=True, has_ce=False, has_reset=False, **kwargs):
    """Construct an n-bit updown counter."""
    defn = DefineUpDownCounter(n, cout=cout,
                               has_ce=has_ce, has_reset=has_reset)
    return defn(**kwargs)


def DefineCeilFloorUpDownCounter(n, has_ce=False, has_reset=False):
    """
    Counter between 0 and n - 1 that uses the minimum number of bits.

    This counter counts up by 1 if U is True and D is False, down by 1 if U is
    False and D is True, no change if both are False or True.

    Also, unlike normal updown counter, up by 1 has no effect if already at (n -
    1) and down by 1 has nefect if already at 0.

    :param n: The value the counter counts up to
    :param has_ce: Whether this counter should a clock-enable input
    :return: An updown counter circuit
    """
    num_bits = math.ceil(math.log(n, 2))

    class _Counter(m.Circuit):
        name = (f"CeilFloorUpDownCounter_m{str(n)}_hasCE{str(has_ce)}_"
                f"hasReset{str(has_reset)}")
        io = m.IO(U=m.In(m.Bit), D=m.In(m.Bit), O=m.Out(m.UInt[num_bits]))
        io += m.ClockIO(has_ce, has_reset)

        up_down_counter = UpDownCounter(num_bits, False, has_ce, has_reset)
        at_max = Decode(n - 1, up_down_counter.O.N)(up_down_counter.O)
        at_min = Decode(0, up_down_counter.O.N)(up_down_counter.O)

        # Only increase counter if input says to increase and not at max.
        should_increase = ~at_max & io.U & ~io.D
        m.wire(should_increase, up_down_counter.U)
        # Only decrease counter if input says to decrease and not at min.
        should_decrease = ~at_min & ~io.U & io.D
        m.wire(should_decrease, up_down_counter.D)

        m.wire(up_down_counter.O, io.O)

    return _Counter


def CeilFloorUpDownCounter(m, has_ce=False, has_reset=False):
    return DefineCeilFloorUpDownCounter(m, has_ce, has_reset)()
