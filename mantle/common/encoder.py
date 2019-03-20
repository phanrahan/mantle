from magma import *
from magma.bitutils import log2
from mantle import Or

__all__ = ['DefineEncoder', 'Encoder', 'encoder']

#
# Given an n-bit input array with only a single bit set,
# return the position of the set bit.
#
# NB. The current implementation only works for n<=8
#
def DefineEncoder(n):
    assert n <= 8
    logn = log2(n)
    class _Encoder(Circuit):
        name = 'Encoder'+str(n)
        IO = ['I', In(Bits[ n ]), 'O', Out(Bits[ logn ])]
        @classmethod
        def definition(Enc):
            def f(y):
                or_ = uncurry(Or(n//2))
                os = []
                for i in range(n):
                    if i & (1 << y): os.append(Enc.I[i])
                wire(array(os), or_)
                return AnonymousCircuit("O", or_.O)
            enc = join( col(f, logn) )
            wire(enc.O, Enc.O)
    return _Encoder

def Encoder(n, **kwargs):
    return DefineEncoder(n)(**kwargs)

def encoder(I, **kwargs):
    return Encoder(len(I), **kwargs)(I)
