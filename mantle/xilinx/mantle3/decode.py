from magma import *
from .LUT import ZERO
from .ROM import ROMN
from .cascade import FlatHalfCascade

__all__  = ['DefineDecode', 'Decode', 'decode']

def DefineDecode(i, n, invert=False):
    """
    Decode the n-bit number i.

    @return: 1 if the n-bit input equals i
    """

    class _Decode(Circuit):
        name = 'Decode_{}_{}'.format(i, n)
        IO = ['I', In(Bits[n]), 'O', Out(Bit)]

        @classmethod
        def definition(io):
            if n <= 8:
                j = 1 << i
                if invert:
                    m = 1 << n
                    mask = (1 << m) - 1
                    j = mask & (~j)
                decode = ROMN(j, n)
            else:
                nluts = (n + 3) // 4
                data = nluts * [0]
                for j in range(nluts):
                    data[j] = (i >> 4*j) & 0xf # 4-bit pieces
                decode = FlatHalfCascade(n, 4, data, ZERO, 1)
            wire(io.I, decode.I)
            wire(decode.O, io.O)

    return _Decode

def Decode(i, n, invert=False):
    return DefineDecode(i, n, invert=invert)()

def decode(I, i, invert=False):
    return Decode(i, len(I), invert=invert)(I)
