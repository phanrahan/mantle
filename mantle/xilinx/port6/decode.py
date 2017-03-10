from magma import *
from .ROM import ROMN
from .flatcascade import FlatCascade

__all__  = ['Decode']

def Decode(i, n, invert=False):
    """
    Decode the n-bit number i.
    @return: 1 if the n-bit input equals i
    """

    if n <= 8:
        i = 1 << i
        if invert:
            m = 1 << n
            mask = (1 << m) - 1
            i = mask & (~i)
        return ROMN(i,n)
    else:
        m = (n + 5) / 6
        data = m * [0]
        for j in range(m):
            data[j] = 1 << (i & 0x3f)
            i = i >> 6
        return FlatCascade(n, 6, data, 0, 0, 1)
