from magma import uncurry
from mantle import LUTN

__all__  = ['Decode', 'decode']

def Decode(i, n, invert=False, **kwargs):
    """
    Decode the n-bit number i.

    @return: 1 if the n-bit input equals i
    """

    assert n <= 8

    i = 1 << i
    if invert:
        m = 1 << n
        mask = (1 << m) - 1
        i = mask & (~i)
    return uncurry(LUTN(i, n, **kwargs))

def decode(I, i, invert=False, **kwargs):
    return Decode(i, len(I), invert=invert, **kwargs)(I)

