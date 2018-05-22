import os
from magma import *
from mantle import *

__all__ = ['LHCA']

_lhcataps = {}


def LHCA(n, init=1, has_ce=False):

    def readtaps():
        global _lhcataps

        if len(_lhcataps) != 0:
            return

        import csv

        name = os.path.join(os.path.dirname(__file__), 'lhca.csv')

        f = open(name)

        row = csv.reader(f)

        for data in row:
            if data[0].isdigit():
                tap = int(data[0])
                _lhcataps[tap] = [int(v) for v in data[1].split(',')]

    readtaps()

    taps = _lhcataps[n]

    reg = Register(n, init=init, has_ce=has_ce)

    def lut(y):
        tap = (y + 1) in taps
        if y == 0:
            if tap:
                return LUT2(A0^A1)(reg.O[y], reg.O[y + 1])
            else:
                return LUT1(A0)(reg.O[y + 1])
        elif y == n - 1:
            if tap:
                return LUT2(A0^A1)(reg.O[y - 1], reg.O[y])
            else:
                return LUT1(A0)(reg.O[y - 1])
        else:
            if tap:
                return LUT3(A0^A1^A2)(reg.O[y - 1], reg.O[y], reg.O[y + 1])
            else:
                return LUT2(A0^A1)(reg.O[y - 1], reg.O[y + 1])

    # col returns a list of outputs, convert to an array
    luts = array(col(lut, n))
    reg(luts)

    args = ["O", reg.O] + reg.interface.clockargs()

    return AnonymousCircuit(args)
