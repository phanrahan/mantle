from __future__ import division
import sys
if sys.version_info > (3, 0):
    from functools import reduce
    from functools import lru_cache
from collections.abc import Sequence
from magma import *
from .LUT import LUT, LUT1, LUT2, LUT3, LUT4, A0, A1, A2, A3

# unary operators
__all__  = ['DefineReduceAnd', 'ReduceAnd']
__all__ += ['DefineReduceNAnd', 'ReduceNAnd']
__all__ += ['DefineReduceOr', 'ReduceOr']
__all__ += ['DefineReduceNOr', 'ReduceNOr']
__all__ += ['DefineReduceXOr', 'ReduceXOr']
__all__ += ['DefineReduceNXOr', 'ReduceNXOr']

# binary operators
__all__ += ['DefineAnd', 'And']
__all__ += ['DefineNAnd', 'NAnd']
__all__ += ['DefineOr', 'Or']
__all__ += ['DefineNOr', 'NOr']
__all__ += ['DefineXOr', 'XOr']
__all__ += ['DefineNXOr', 'NXOr']

# unary operators
__all__ += ['DefineInvert', 'Invert']
__all__ += ['Not']

def FlatCascade(n, k, expr, cin, **kwargs):

        def f(y):
            e = expr[y] if isinstance(expr, Sequence) else expr
            return LUT( e, n=k+1 )

        # number of luts
        m = (n+k-1) // k
        c = braid( col(f, m), foldargs={"I0":"O"})

        wire(cin, c.I0)

        c = flat(uncurry(c))

        for i in range(n, len(c.I)):
            wire(cin, c.I[i])

        return AnonymousCircuit( ['I', c.I[0:n], 'O', c.O] )

def DefineReduceOp(opname, n, luts, cascadeexpr, cin):
    T = Bits[ n ]
    class _ReduceOp(Circuit):
        name = '{}{}'.format(opname, n)
        IO = ['I', In(T), 'O', Out(Bit)]

        @classmethod
        def definition(io):
            if   n == 1: a = uncurry(LUT1(luts[n - 1]))
            elif n == 2: a = uncurry(LUT2(luts[n - 1]))
            elif n == 3: a = uncurry(LUT3(luts[n - 1]))
            elif n == 4: a = uncurry(LUT4(luts[n - 1]))
            else: a = FlatCascade(n, 1, cascadeexpr, cin)
            wire(a(io.I), io.O)
    return _ReduceOp

def DefineReduceAnd(n):
    luts = [A0, A0&A1, A0&A1&A2, A0&A1&A2&A3]
    return DefineReduceOp('And', n, luts, A0 & A1, 1)

def ReduceAnd(height=2, **kwargs):
    return DefineReduceAnd(height)(**kwargs)

def DefineReduceNAnd(n):
    luts = [~A0, ~(A0&A1), ~(A0&A1&A2), ~(A0&A1&A2&A3)]
    return DefineReduceOp('NAnd', n, luts, A0 & ~A1, 0)

def ReduceNAnd(height=2, **kwargs):
    return DefineReduceNAnd(height)(**kwargs)

def DefineReduceOr(n):
    luts = [A0, A0|A1, A0|A1|A2, A0|A1|A2|A3]
    return DefineReduceOp('Or', n, luts, A0 | A1, 0)

def ReduceOr(height=2, **kwargs):
    return DefineReduceOr(height)(**kwargs)

def DefineReduceNOr(n):
    luts = [~A0, ~(A0|A1), ~(A0|A1|A2), ~(A0|A1|A2|A3)]
    return DefineReduceOp('NOr', n, luts, A0 | ~A1, 1)

def ReduceNOr(height=2, **kwargs):
    return DefineReduceNOr(height)(**kwargs)

def DefineReduceXOr(n):
    luts = [A0, A0^A1, A0^A1^A2, A0^A1^A2^A3]
    return DefineReduceOp('XOr', n, luts, A0 ^ A1, 0)

def ReduceXOr(height=2, **kwargs):
    return DefineReduceXOr(height)(**kwargs)

def DefineReduceNXOr(n):
    luts = [~A0, ~(A0^A1), ~(A0^A1^A2), ~(A0^A1^A2^A3)]
    return DefineReduceOp('NXOr', n, luts, A0 ^ ~A1, 1)

def ReduceNXOr(height=2, **kwargs):
    return DefineReduceNXOr(height)(**kwargs)


def DefineOp(opname, op, height=2, width=1):
    """
    Generate Op module

    I0 : In(Bits(width)), I1 : In(Bits(width)), O : Out(Bits(width))
    """
    T = Bits[ width ]
    class _Op(Circuit):

        name = '{}{}x{}'.format(opname, height, width)

        IO = sum([['I{}'.format(i), In(T)] for i in range(height)], [])
        IO  += ['O', Out(T)]

        @classmethod
        def definition(io):
            def opm(y):
                return curry(op(height))
            opmxn = join(col(opm, width))
            for port in ('I{}'.format(i) for i in range(height)):
                wire(getattr(io, port), getattr(opmxn, port))
            wire(opmxn.O, io.O)
    return _Op

def DefineAnd(height=2, width=1):
    return DefineOp('And', ReduceAnd, height, width)

def And(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceAnd(height, **kwargs))
    return DefineAnd(height, width)(**kwargs)

def DefineNAnd(height=2, width=None):
    return DefineOp('NAnd', ReduceNAnd, height, width)

def NAnd(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceNAnd(height, **kwargs))
    return DefineNAnd(height, width)(**kwargs)

def DefineOr(height=2, width=None):
    return DefineOp('Or', ReduceOr, height, width)

def Or(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceOr(height, **kwargs))
    return DefineOr(height, width)(**kwargs)

def DefineNOr(height=2, width=None):
    return DefineOp('NOr', ReduceNOr, height, width)

def NOr(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceNOr(height, **kwargs))
    return DefineNOr(height, width)(**kwargs)

def DefineXOr(height=2, width=None):
    return DefineOp('XOr', ReduceXOr, height, width)

def XOr(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceXOr(height, **kwargs))
    return DefineXOr(height, width)(**kwargs)

def DefineNXOr(height=2, width=None):
    return DefineOp('NXOr', ReduceNXOr, height, width)

def NXOr(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceNXOr(height, **kwargs))
    return DefineNXOr(height, width)(**kwargs)


def DefineInvert(width):
    """
    Generate Invert module

    I0 : Bits(width) -> O : Bits(width)
    """

    T = Bits[ width ]
    class _Invert(Circuit):
        name = 'Invert%d' % width

        IO  = ['I', In(T), 'O', Out(T)]

        @classmethod
        def definition(def_):
            def not_(y):
                return Not(loc=(0,y/8, y%8))
            invert = join(col(not_, width))
            wire(def_.I, invert.I0)
            wire(invert.O, def_.O)

    return _Invert

def Invert(n, **kwargs):
    return DefineInvert(n)(**kwargs)


def Not(**kwargs):
    """Not gate - 1-bit input."""
    return LUT1(~A0, **kwargs)


