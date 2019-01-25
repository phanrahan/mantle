from magma import *
from .gates import Buf as gatesbuf

__all__ = ['DefineBuf', 'Buf']

def DefineOp(name, height, op):

    if height != 1:
        name += str(height)
    args = [name]
    for i in range(height):
        args += ['I{}'.format(i), In(Bit)]
    args += ['O', Out(Bit)]

    c = DefineCircuit(*args)
    op = op(height)
    EndCircuit()
    if   height == 1:
        wire(op(c.I0), c.O)
    elif height == 2:
        wire(op(c.I0, c.I1), c.O)
    elif height == 3:
        wire(op(c.I0, c.I1, c.I2), c.O)
    elif height == 4:
        wire(op(c.I0, c.I1, c.I2, c.I3), c.O)
    return c

def DefineOpW(name, height, width, op):
    if height == 1:
        name += str(width)
    else:
        name += str(height) + 'x' + str(width)
    T = Bits(width)
    args = [name]
    for i in range(height):
        args += ['I{}'.format(i), In(T)]
    args += ['O', Out(T)]

    c = DefineCircuit(*args)
    def f(y):
        return op(height)
    op = join(col(f, width))
    EndCircuit()
    if   height == 1:
        wire(op(c.I0), c.O)
    elif height == 2:
        wire(op(c.I0, c.I1), c.O)
    elif height == 3:
        wire(op(c.I0, c.I1, c.I2), c.O)
    elif height == 4:
        wire(op(c.I0, c.I1, c.I2, c.I3), c.O)
    return c

def DefineBuf(width=None):
    if width is None:
        return DefineOp('Buf', 1, gatesbuf)
    return DefineOpW('Buf', 1, width, gatesbuf)

def Buf(width=None):
    return DefineBuf(width)()
