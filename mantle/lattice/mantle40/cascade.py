from magma import *
from magma.bitutils import int2uint
from .LUT import LUT

__all__ = ['DefineCascade', 'Cascade']

def _Name(n, k, expr):
    expr = int2uint(expr, 1<<k)
    return 'Cascade%dx%d_%X' % (n, k, expr)

#
# n is the number of luts 
# k is the number of bits per lut
# expr goes into LUT
#
def DefineCascade(n, k, expr, cin, forkargs={}):

    assert k <= 3

    T = Bits(n)
    args = []
    if k >= 1: args += ["I0", In(Bit) if 'I0' in forkargs else In(T)]
    if k >= 2: args += ["I1", In(Bit) if 'I1' in forkargs else In(T)]
    if k >= 3: args += ["I2", In(Bit) if 'I2' in forkargs else In(T)]
    args += ["O", Out(Bit)]

    class _Cascade(Circuit):
        name = _Name(n, k, expr)
        IO = args

        @classmethod
        def definition(cascade):

            def f(y):
                return LUT(expr, k+1, loc=(0,y/8, y%8))

            c = braid( col(f, n), foldargs={"I0":"O"}, forkargs=forkargs )

            wire( cin, c.I0 )
            if k >= 1: wire(cascade.I0, c.I1)
            if k >= 2: wire(cascade.I1, c.I2)
            if k >= 3: wire(cascade.I2, c.I3)
            wire( c.O, cascade.O )

    return _Cascade

def Cascade(n, k, expr, cin, forkargs={}, **kwargs):
    return DefineCascade(n, k, expr, cin, forkargs)(**kwargs)


