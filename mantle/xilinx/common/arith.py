from magma import *
from mantle.xilinx.port import Adders, A0, A1

__all__  = ['Add', 'AddC'] 
__all__ += ['Sub', 'SubC']

def Add(n, cin=0):
    return Adders(n, 2, A0^A1, A0&A1, cin, False)
    
def AddC(n, cin=0):
    return Adders(n, 2, A0^A1, A0&A1, cin, True)

def Sub(n, cin=1):
    return Adders(n, 2, A0^(~A1), A0, cin, False)
    
def SubC(n, cin=1):
    return Adders(n, 2, A0^(~A1), A0, cin, True)
    
