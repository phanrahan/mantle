from magma import Circuit, Bits, In, Out, wire, join
from .LUT import LUT1, A0

__all__ = ['DefineBuf', 'Buf']

def DefineBuf(width=1):
    """
    Generate Buf module

    I : In(Bits(width)), O : Out(Bits(width))
    """
    T = Bits[ width ]
    class BufN(Circuit):

        name = 'Buf{}'.format(width)
        IO  = ['I', In(T), 'O', Out(T)]

        @classmethod
        def definition(def_):
            def buf(y):
                return Buf(loc=(0,y//8, y%8))
            buffer = join(col(buf, width))
            wire(def_.I, buffer.I0)
            wire(buffer.O, def_.O)

    return BufN

def Buf(width=None, **kwargs):
    if width is None:
        return LUT1(A0, **kwargs)
    return DefineBuf(width)(**kwargs)

