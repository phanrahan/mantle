from __future__ import division
from collections import Sequence
from magma import *
from .LUT import LUTN

__all__ = ['DefineFlatCascade', 'FlatCascade']

def _Name(n, k, expr):
    if isinstance(expr, Sequence):
        expr = "_".join(["%X" % uint(e, 1<<k) for e in expr])
    else:
        expr = "%X" % uint(expr, 1<<k)
    return 'FlatCascade%dx%d_%s' % (n, k, expr)

def DefineFlatCascade(n, k, expr, cin):
    assert k <= 3

    class _FlatCascade(Circuit):
        name = _Name(n, k+1, expr)
        IO = ["I", In(Array(n, Bit)), "O", Out(Bit)]
        @classmethod
        def definition(cascade):
            def f(y):
                e = expr[y] if isinstance(expr, Sequence) else expr
                return LUTN( e, k+1, loc=(0,y/8, y%8) )

            m = (n+k-1) // k
            #c = braid( col(f, m), flatargs=['I1','I2','I3'], foldargs={"I0":"O"})
            c = braid( col(f, m), foldargs={"I0":"O"})
            for i in range(m):
                if i == 0:
                    wire(cin, c.I0)
                for j in range(k):
                    l = i*k+j
                    if l < n:
                        if   j == 0:
                            wire(cascade.I[l], c.I1[i])
                        elif j == 1:
                            wire(cascade.I[l], c.I2[i])
                        elif j == 2:
                            wire(cascade.I[l], c.I3[i])
                    else:
                        if   j == 0:
                            wire(cin, c.I1[i])
                        elif j == 1:
                            wire(cin, c.I2[i])
                        elif j == 2:
                            wire(cin, c.I3[i])

            wire(c.O, cascade.O)

    return _FlatCascade

def FlatCascade(n, k, expr, cin, **kwargs):
    return DefineFlatCascade(n, k, expr, cin)(**kwargs)

