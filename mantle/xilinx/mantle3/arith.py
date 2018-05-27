from magma import *
from .logic import Invert, Not
from .fulladder import FullAdder

__all__  = ['DefineAdd'] 
__all__ += ['DefineSub']
__all__ += ['DefineNegate']
__all__ += ['DefineASR']

#
# create an n-bit Adder from n FullAdders
#
# I0:In(Bits(n)), I1:In(Bits(n)), CIN:In(Bit), O:Out(Bits(n)), COUT:Out(Bit)
#
# if cin, CIN is added to the circuit
# if cout: COUT is added to the circuit
#
@cache_definition
def DefineAdd(n, cin=False, cout=False):
    pass

@cache_definition
def DefineSub(n, cin=False, cout=False):
    pass

@cache_definition
def DefineNegate(width):
    pass

@cache_definition
def DefineASR(width, shift):
    pass
