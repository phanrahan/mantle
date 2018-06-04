from magma import *
from .LUT import A0, A1
from .fulladder import FullCarry

__all__  = ["HalfAdder", 'halfadder']

class HalfAdder(Circuit):
    IO = ["I0", In(Bit), "I1", In(Bit), "O", Out(Bit), "COUT", Out(Bit)]
    @classmethod
    def definition(io):
        fc = FullCarry(1, A0, A0)
        wire( io.I0, fc.I0 )
        wire( io.I1, fc.CIN )
        wire( fc.O, io.O )
        wire( fc.COUT, io.COUT )
        
def halfadder(a, b):
    return HalfAdder()(a, b)

