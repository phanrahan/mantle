from magma import *
from mantle import LUT, DefineAdd

__all__ = ['DefineArbiter', 'Arbiter', 'arbiter']

#
# Given an input array with various bits set,
# an Arbiter returns an array with only a single bit set,
# in this case the lowest bit set is retained
#
def DefineArbiter(n):
    T = Bits[ n ]
    class _Arbiter(Circuit):
        name = 'Arbiter'+str(n)
        IO = ['I', In(T), 'O', Out(T)]
        @classmethod
        def definition(Arb):
            ones = n * [1]
            y = DefineAdd(n)()(Arb.I, array(ones))  # y = x - 1
            def a(y):
                return LUT([0, 1, 0, 0]) # A0 & ~A1
            arb = join(col(a, n))
            arb(Arb.I, y)
            wire(arb.O, Arb.O)
    return _Arbiter

def Arbiter(n, **kwargs):
    return DefineArbiter(n)(**kwargs)

def arbiter(I, **kwargs):
    return Arbiter(len(I), **kwargs)(I)
