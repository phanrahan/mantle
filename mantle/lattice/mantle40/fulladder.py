from magma import *
from ..ice40.PLB import SB_CARRY, A0, A1, A2
from .LUT import LUT3

__all__  = ["FullAdder", 'fulladder']

class FullAdder(Circuit):
    name = "FullAdder"
    IO = ["I0", In(Bit), "I1", In(Bit), "CIN", In(Bit), "O", Out(Bit), "COUT", Out(Bit)]
    @classmethod
    def definition(io):
        sum = LUT3(A0^A1^A2)
        carry = SB_CARRY() # (A0&A1)|(A1&A2)|(A2&A0)
        wire( sum(io.I0,io.I1,io.CIN), io.O )
        wire( carry(io.I0,io.I1,io.CIN), io.COUT )

def fulladder(A, B, CIN, **kwargs):
    return FullAdder()(A, B, CIN, **kwargs)
