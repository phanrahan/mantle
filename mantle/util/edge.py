from mantle import FF
from mantle import LUT2, I0, I1

__all__ = ['rising', 'falling']

def rising(a):
    ff = FF()
    return LUT2(I0 & ~I1)(a, ff(a))


def falling(a):
    ff = FF()
    return LUT2(~I0 & I1)(a, ff(a))
