from magma import *
from .LUT import A0, A1
#from .carry import HalfCarry

__all__  = ["HalfAdder", 'halfadder']

class HalfAdder(Circuit):
    IO = ["I0", In(Bit), "I1", In(Bit), "O", Out(Bit), "COUT", Out(Bit)]
    @classmethod
    def definition(io):
        wire( io.I0 ^ io.I1, io.O )
        wire( io.I1 & io.I1, io.COUT )
        
def halfadder(a, b):
    return HalfAdder()(a, b)

