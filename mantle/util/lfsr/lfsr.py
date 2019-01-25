import os
from magma import *
from mantle import *
from mantle.common.sipo import SIPO

__all__ = ['DefineLFSR', '_lfsrtaps']

_lfsrtaps = {}


def DefineLFSR(n, init=1, has_ce=False, has_reset=False):
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

    name = 'LFSR{}'.format(n)
    if init:
        name += '_' + str(init)
    if has_ce:
        name += 'CE'
    if has_reset:
        name += 'R'
    lfsr = DefineCircuit(name, "O", Out(Bits(n)), 
             *ClockInterface(has_ce=has_ce, has_reset=has_reset))
    shift = SIPO(n, init=init, has_ce=has_ce, has_reset=has_reset)

    t = []
    for i in range(nt):
        t.append(shift.O[tap[i] - 1])
    t = array(t)

    s = uncurry(XOr(nt))(t)
    shift(s)

    wire(shift.O, lfsr.O)
    wire(shift.CLK, lfsr.CLK)
    if has_reset:
        wire(shift.RESET, lfsr.RESET)
    if has_ce:
        wire(shift.CE, lfsr.CE)
    EndDefine()
    return lfsr
