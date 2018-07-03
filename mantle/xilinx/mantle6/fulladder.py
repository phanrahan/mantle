from magma import *
from .LUT import LUT3, A0, A1, A2

__all__ = ['FullAdder', 'fulladder']

class FullAdder(Circuit):
    IO = ["I0", In(Bit), "I1", In(Bit), "I2", In(Bit), "O", Out(Bit), "COUT", Out(Bit)]
    @classmethod
    def definition(io):
        s = LUT3(A0^A1^A2)
        c = LUT3(A0&A1|A1&A2|A2&A0)
        wire( s(io.I0, io.I1, io.I2), io.O )
        wire( c(io.I0, io.I1, io.I2), io.COUT )

def fulladder(a, b, c):
    return FullAdder()(a, b, c)

