from magma import *
from .decode import Decode

__all__  = ['Decoder', 'decoder']

@cache_definition
def DefineDecoder(n, invert=False):
    """
    n-bit to 2^n decoder.
    """

    class _Decoder(Circuit):
        name = 'Decoder'+str(n)+("Invert" if invert else "")
        IO = ['I', In(Bits(n)), 'O', Out(Bits(1<<n))]
        @classmethod
        def definition(io):
            def decode(y):
                return Decode(y, n, invert, loc=(0,y/8, y%8))
            dec = fork(col(decode, 1<<n))
            wire(dec(io.I), io.O)
    return _Decoder

def Decoder(n, invert=False, **kwargs):
    return DefineDecoder(n, invert)(**kwargs)

def decoder(I, invert=False, **kwargs):
    return Decoder(len(I), invert=invert, **kwargs)(I)
