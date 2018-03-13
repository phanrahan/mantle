from magma import uncurry, cache_definition
from mantle import LUT
import os

__all__  = ['Decode', 'decode']

@cache_definition
def DefineCoreIRDecode(i, n):
    from mantle import eq
    from magma import Bits, In, Bit, DefineCircuit, EndDefine, wire, bits, Out
    circ = DefineCircuit(f"Decode{i}{n}", "I", In(Bits(n)), "O", Out(Bit))
    wire(circ.O, eq(circ.I, bits(i, n)))
    EndDefine()
    return circ

def Decode(i, n, invert=False, **kwargs):
    """
    Decode the n-bit number i.

    @return: 1 if the n-bit input equals i
    """

    assert n <= 8

    if os.environ["MANTLE"] == "coreir":
        return DefineCoreIRDecode(i, n)()
    i = 1 << i
    if invert:
        m = 1 << n
        mask = (1 << m) - 1
        i = mask & (~i)
    return uncurry(LUT(i, n, **kwargs))

def decode(I, i, invert=False, **kwargs):
    return Decode(i, len(I), invert=invert, **kwargs)(I)

