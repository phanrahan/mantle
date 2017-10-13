import os
from magma import *
from mantle import *
from mantle.common.sipo import SIPO

__all__ = ['DefineLFSR', '_lfsrtaps']

_lfsrtaps = {}


@cache_definition
def DefineLFSR(n, init=1, has_ce=False):
    def readtaps():
        global _lfsrtaps

        if len(_lfsrtaps) != 0:
            return

        import csv

        name = os.path.join(os.path.dirname(__file__), 'lfsr.csv')

        f = open(name)
        row = csv.reader(f)

        for data in row:
            if data[0].isdigit():
                tap = int(data[0])
                _lfsrtaps[tap] = [int(v) for v in data[1].split(',')]

    readtaps()

    tap = _lfsrtaps[n]
    nt = len(tap)

    lfsr = DefineCircuit('lfsr{}{}{}'.format(n, init, has_ce),
        "O", Out(Bits(n)), *ClockInterface(has_ce))
    shift = SIPO(n, init=init, has_ce=has_ce)

    t = []
    for i in range(nt):
        t.append(shift.O[tap[i] - 1])
    t = array(t)

    s = uncurry(XOr(nt))(t)
    shift(s)

    wire(shift.O, lfsr.O)
    wireclock(shift, lfsr)
    wiredefaultclock(shift, lfsr)
    EndDefine()
    return lfsr
