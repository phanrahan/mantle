import magma as m
from mantle import EQ, LUT


__all__  = ['DefineDecode', 'Decode', 'decode']


@m.cache_definition
def DefineDecode(i, n):

    class _Decode(m.Circuit):
        name = f"Decode{i}{n}"
        io = m.IO(I=m.In(m.Bits[n]), O=m.Out(m.Bit))
        m.wire(io.O, EQ(n)(io.I, m.bits(i, n)))

    return _Decode


def Decode(i, n, invert=False, **kwargs):
    """
    Decode the n-bit number i.

    @return: 1 if the n-bit input equals i
    """

    if n <= 4:
        i = 1 << i
        if invert:
            mask = (1 << (1<<n)) - 1
            i = mask & (~i)
        return m.uncurry(LUT(i, n, **kwargs))

    return DefineDecode(i, n)()


def decode(I, i, invert=False, **kwargs):
    return Decode(i, len(I), invert=invert, **kwargs)(I)
