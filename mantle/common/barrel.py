from magma import Circuit, Bit, Bits, In, Out, bits, wire, map_
from magma.bitutils import log2
from mantle import Mux2

__all__ = ['DefineBarrel', 'Barrel', 'barrel']

def DefineBarrelShift(n, k):
    assert k < n
    T = Bits(n)
    class _BarrelShift(Circuit):
        name = 'BarrelShift{}_{}'.format(n, k)
        IO = ['I', In(T), 'S', In(Bit), 'SI', In(Bit), "O", Out(T)]
        @classmethod
        def definition(io):
            Is = [io.I[i] for i in range(n)]
            muxes = map_(Mux2, n)
            for i in range(n):
                shifti = i - k 
                I = bits([Is[i], Is[shifti] if shifti >= 0 else io.SI])
                muxes[i]( I, io.S )
            for i in range(n):
                Is[i] = muxes[i].O
            wire(bits(Is), io.O)
    return _BarrelShift

def BarrelShift(n, k):
    return DefineBarrelShift(n, k)()



def DefineBarrel(n):
    assert n in [2, 4, 8, 16]
    logn = log2(n)
    T = Bits(n)
    class _Barrel(Circuit):
        name = 'Barrel{}'.format(n)
        IO = ['I', In(T), 'S', In(Bits(logn)), 'SI', In(Bit), "O", Out(T)]
        @classmethod
        def definition(io):
            I = io.I
            for k in range(logn):
                 I = BarrelShift(n, 1<<k)(I, io.S[k], io.SI)
            wire(I, io.O)
    return _Barrel

def Barrel(n):
    return DefineBarrel(n)()

def barrel(i, s, si):
    n = len(i)
    assert log2(n) == len(s)
    return Barrel(n)(i, s, si)
