from .logic import DefineOp, DefineOpW
from .gates import Buf as gatesbuf

__all__ = ['DefineBuf', 'Buf']

def DefineBuf(width=None):
    if width is None:
        return DefineOp('Buf', 1, gatesbuf)
    return DefineOpW('Buf', 1, width, gatesbuf)

def Buf(width=None):
    return DefineBuf(width)()
