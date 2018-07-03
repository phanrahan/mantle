from magma import *
from .LUT import LUT2, A0, A1

__all__  = ["HalfAdder", 'halfadder']

class HalfAdder(Circuit):
    IO = ["I0", In(Bit), "I1", In(Bit), "O", Out(Bit), "COUT", Out(Bit)]
    @classmethod
    def definition(io):
        s = LUT2(A0^A1)
        c = LUT2(A0&A1)
        wire( s(io.I0, io.I1), io.O )
        wire( c(io.I0, io.I1), io.COUT )
        
def halfadder(a, b):
    return HalfAdder()(a, b)

