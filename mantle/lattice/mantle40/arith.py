from magma import *
from .logic import Invert
from .adder import Adders

__all__  = ['Add', 'AddC'] 
__all__ += ['Sub', 'SubC']
__all__ += ['Negate']
__all__ += ['ShiftRightArithmetic']

def Add(n, **kwargs):
    return Adders(n, False, True, **kwargs)
    
def AddC(n, **kwargs):
    return Adders(n, True, True, **kwargs)

def Sub(n, **kwargs):
    invert = Invert(n)
    adder =  Adders(n, True, True, **kwargs)
    wire(1, adder.CIN)
    wire(invert.O, adder.I1)
    return AnonymousCircuit("I0", adder.I0, "I1", invert.I, 
                            "O",  adder.O, "COUT", adder.COUT)
    
def SubC(n, **kwargs):
    invert = Invert(n)
    adder =  Adders(n, True, True, **kwargs)
    wire(invert.O, adder.I1)
    return AnonymousCircuit("I0",   adder.I0, "I1", invert.I, "CIN",  adder.CIN,
                            "O",    adder.O,  "COUT", adder.COUT)

def Negate(n, **kwargs):
    invert = Invert(n)
    adder =  Adders(n, True, False, **kwargs)
    wire(1, adder.CIN)
    wire(constarray(0,n), adder.I0)
    wire(invert.O, adder.I1)
    return AnonymousCircuit("I", invert.I, "O", adder.O)
    

def ShiftRightArithmetic(width, shift_amount, **kwargs):
    T = Array(width, Bit)
    class _ShiftRightArithmetic(Circuit):
        name = 'ShiftRightArithmetic_w{}_a{}'.format(width, shift_amount)

        IO = ["I", In(T), "O", Out(T)]

        @classmethod
        def definition(io):
            for i in range(0, width - shift_amount):
                wire(io.I[i + shift_amount], io.O[i])
            for i in range(width - shift_amount, width):
                wire(io.I[width-1], io.O[i])
    return _ShiftRightArithmetic


    

