from magma import Circuit, Bit, Array, In, Out, wire, join
from ..ice40 import A0
from .LUT import LUT1

__all__ = ['DefineBuf', 'Buf']

def DefineBuf(width=None):
    """
    Generate Buf module

    I0 : Array(width, Bit) -> O : Array(n, Bit)
    """
    T = Array(width, Bit)
    class _Buf(Circuit):

        name = 'Buf%d' % width
        IO  = ['I', In(T), 'O', Out(T)]

        @classmethod
        def definition(def_):
            def buf(y):
                return Buf(loc=(0,y/8, y%8))
            buffer = join(col(buf, width))
            wire(def_.I, buffer.I0)
            wire(buffer.O, def_.O)

    return _Buf

def Buf(width=None, **kwargs):
    if width is None:
        return LUT1(A0, **kwargs)
    return DefineBuf(width)(**kwargs)

