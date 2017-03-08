import os
from magma import *
from mantle import *

__all__ = ['LFSR']

_lfsrtaps = {}


def LFSR(n, init=1, ce=False):
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

    shift = SIPO(n, init=init, ce=ce)

    t = []
    for i in range(nt):
        t.append(shift.O[tap[i] - 1])
    t = array(*t)

    s = XorN(nt)(t)
    shift(s)

    args = ["output O", shift.O] + shift.interface.clockargs()
    return AnonymousCircuit(args)
