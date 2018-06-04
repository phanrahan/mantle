from magma import *
from .fullcarry import FullCarry
from .LUT import LUTN, A0, A1, A2

__all__ = ['FullAdder', 'fulladder']

class FullAdder(Circuit):
    IO = ["I0", In(Bit), "I1", In(Bit), "CIN", In(Bit), "O", Out(Bit), "COUT", Out(Bit)]
    @classmethod
    def definition(io):
        fc = FullCarry(2, A0^A1, A0&A1)
        wire( io.I0, fc.I0 )
        wire( io.I1, fc.I1 )
        wire( io.CIN, fc.CIN )
        wire( fc.O, io.O )
        wire( fc.COUT, io.COUT )

def fulladder(a, b, c):
    return FullAdder()(a, b, c)

