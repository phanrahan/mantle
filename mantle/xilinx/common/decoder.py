from magma import *
from mantle.xilinx.port import Decode

__all__  = ['Decoder']

def DefineDecoder(n, invert=False):
    """
    n-bit to 2^n decoder.
    """

    class _Decoder(Circuit):
        name = 'Decoder'+str(n)+("Invert" if invert else "")
        IO = ['input I', Array(n, Bit), 'output O', Array(1<<n, Bit)]
        @classmethod
        def definition(Dec):
            def decode(y):
                return Decode(y, n, invert)
            dec = fork(col(decode, 1<<n))
            wire(Dec.I, dec.I)
            wire(dec.O, Dec.O)
    return _Decoder

def Decoder(n, invert=False):
    return DefineDecoder(n, invert)()

