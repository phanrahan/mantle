from magma import *
from ..port import I0, I1, LUT2
from .arith import Add

__all__ = ['DefineArbiter', 'Arbiter']

#
# Given an input array with various bits set,
# an Arbiter returns an array with only a single bit set,
# in this case the lowest bit set is retained
#
def DefineArbiter(n):

    T = Array(n, Bit)
    class _Arbiter(Circuit):
        name = 'Arbiter'+str(n)
        IO = ['input I', T, 'output O', T]
        @classmethod
        def definition(Arb):
            ones = n * [1]
            y = Add(n)(Arb.I, array(*ones) )  # y = x - 1
            def a(y):
                return LUT2(I0 & ~I1)
            arb = join(col(a, n))
            arb(Arb.I, y)
            wire(arb.O, Arb.O)
    return _Arbiter

def Arbiter(n):
    return DefineArbiter(n)()
