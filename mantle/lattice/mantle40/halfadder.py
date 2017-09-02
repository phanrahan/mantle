from magma import *
from ..ice40.PLB import SB_CARRY, A0, A1, A2, A3
from .LUT import LUT2

__all__  = ["HalfAdder", 'halfadder']

class HalfAdder(Circuit):
    IO = ["I0", In(Bit), "I1", In(Bit), "O", Out(Bit), "COUT", Out(Bit)]
    @classmethod
    def definition(io):
        sum = LUT2(A0^A1)
        carry = SB_CARRY() # (A0&A1)|(A1&A2)|(A2&A0)
        wire( sum(io.I0,io.I1), io.O )
        wire( carry(io.I0,io.I1,0), io.COUT )

def halfadder(a, b, **kwargs):
    return HalfAdder()(a, b, **kwargs)

