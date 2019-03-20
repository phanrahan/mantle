import magma as m
from .LUT import LUT
from .compare import EQ

__all__  = ['DefineDecode', 'Decode', 'decode']

@m.cache_definition
def DefineDecode(i, n):
    circ = m.DefineCircuit(f"Decode{n}_{i:X}", "I", m.In(m.Bits[ n ]), "O", m.Out(m.Bit))
    m.wire(circ.O, EQ(n)(circ.I, m.bits(i, n)))
    m.EndDefine()
    return circ

def Decode(i, n, invert=False, **kwargs):
    """
    Decode the n-bit number i.

    @return: 1 if the n-bit input equals i
    """

    if n <= 4:
        i = 1 << i
        if invert:
            mask = (1 << (1 << n)) - 1
            i = mask & (~i)
        return m.uncurry(LUT(i, n, **kwargs))

    return DefineDecode(i, n)()

def decode(I, i, invert=False, **kwargs):
    return Decode(i, len(I), invert=invert, **kwargs)(I)

