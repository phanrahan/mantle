from magma import *
from mantle.xilinx.port import OrN

__all__ = ['DefineEncoder', 'Encoder']

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
        IO = ['input I', Array(n, Bit), 'output O', Array(logn, Bit)]
        @classmethod
        def definition(Enc):
            def f(y):
                or_ = OrN(n/2)
                os = []
                for i in range(n):
                    if i & (1 << y): os.append(Enc.I[i])
                wire(array(*os), or_)
                return AnonymousCircuit("output O", or_.O)
            enc = join( col(f, logn) )
            wire(enc.O, Enc.O)
    return _Encoder

def Encoder(n):
    return DefineEncoder(n)()

