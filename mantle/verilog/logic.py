import sys
if sys.version_info > (3, 0):
    from functools import reduce
    from functools import lru_cache
import operator
from magma import *
from . import gates

# binary operators
__all__  = ['DefineAnd', 'And', 'ReduceAnd']
__all__ += ['DefineNAnd', 'NAnd', 'ReduceNAnd']
__all__ += ['DefineOr', 'Or', 'ReduceOr']
__all__ += ['DefineNOr', 'NOr', 'ReduceNOr']
__all__ += ['DefineXOr', 'XOr', 'ReduceXOr']
__all__ += ['DefineNXOr', 'NXOr', 'ReduceNXOr']

# unary operators
__all__ += ['DefineInvert', 'Invert']
__all__ += ['Not']

@lru_cache(maxsize=None)
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

@lru_cache(maxsize=None)
def DefineOpW(name, height, width, op):
    if height == 1:
        name += str(width)
    else:
        name += str(height) + 'x' + str(width)
    T = Array(width, Bit)
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


def DefineAnd(height=2, width=None):
    if width is None:
        return DefineOp('And', height, gates.And)
    return DefineOpW('And', height, width, gates.And)

def And(height=2, width=None):
    return DefineAnd(height, width)()

def ReduceAnd(height=2):
    return uncurry(And(height))


def DefineNAnd(height=2, width=None):
    if width is None:
        return DefineOp('NAnd', height, gates.NAnd)
    return DefineOpW('NAnd', height, width, gates.NAnd)

def NAnd(height=2, width=None, **kwargs):
    return DefineNAnd(height, width)(**kwargs)

def ReduceNAnd(height=2):
    return uncurry(NAnd(height))


def DefineOr(height=2, width=None):
    if width is None:
        return DefineOp('Or', height, gates.Or)
    return DefineOpW('Or', height, width, gates.Or)

def Or(height=2, width=None, **kwargs):
    return DefineOr(height, width)(**kwargs)

def ReduceOr(height=2):
    return uncurry(Or(height))


def DefineNOr(height=2, width=None):
    if width is None:
        return DefineOp('NOr', height, gates.NOr)
    return DefineOpW('NOr', height, width, gates.NOr)

def NOr(height=2, width=None, **kwargs):
    return DefineNOr(height, width)(**kwargs)

def ReduceNOr(height=2):
    return uncurry(NOr(height))


def DefineXOr(height=2, width=None):
    if width is None:
        return DefineOp('XOr', height, gates.XOr)
    return DefineOpW('XOr', height, width, gates.XOr)

def XOr(height=2, width=None, **kwargs):
    return DefineXOr(height, width)(**kwargs)

def ReduceXOr(height=2):
    return uncurry(XOr(height))


def DefineNXOr(height=2, width=None):
    if width is None:
        return DefineOp('NXOr', height, gates.NXOr)
    return DefineOpW('NXOr', height, width, gates.NXOr)

def NXOr(height=2, width=None, **kwargs):
    return DefineNXOr(height, width)(**kwargs)

def ReduceNXOr(height=2):
    return uncurry(NXOr(height))


def DefineInvert(width=None):
    if width is None:
        return DefineOp('Invert', 1, gates.Not)
    return DefineOpW('Invert', 1, width, gates.Not)

def Invert(width):
    return DefineInvert(width)()


Not = DefineOp('Not', 1, gates.Not)

