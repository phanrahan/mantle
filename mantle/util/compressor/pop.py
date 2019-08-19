from magma import Circuit, Bits, In, Out, bits, wire, cache_definition
from magma.bitutils import log2
from .compressor import compressor

__all__ = ['DefinePopCount', 'PopCount', 'popcount']

def DefinePopCount(n):
    class _PopCount(Circuit):
        name = 'PopCount{}'.format(n)
        IO = ['I', In(Bits[ n ]), 'O', Out(Bits[ log2(n)+1 ])]
        @classmethod
        def definition(io):
            r = compressor([io.I.as_list()])
            wire( bits(r), io.O )
    return _PopCount

def PopCount(n, **kwargs):
    return DefinePopCount(n)(**kwargs)

def popcount(I, **kwargs):
    return PopCount(len(I), **kwargs)(I)
