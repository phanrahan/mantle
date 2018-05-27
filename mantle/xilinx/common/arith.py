from magma import *
from ..port import Adders, A0, A1

__all__  = ['DefineAdd', 'Add', 'AddC'] 
__all__ += ['DefineSub', 'Sub', 'SubC']
__all__ += ['DefineNegate']
__all__ += ['DefineASR']

def DefineAdd():
    pass

def Add(n, cin=0):
    return Adders(n, 2, A0^A1, A0&A1, cin, False)
    
def AddC(n, cin=0):
    return Adders(n, 2, A0^A1, A0&A1, cin, True)

def DefineSub():
    pass

def Sub(n, cin=1):
    return Adders(n, 2, A0^(~A1), A0, cin, False)
    
def SubC(n, cin=1):
    return Adders(n, 2, A0^(~A1), A0, cin, True)
    
def DefineNegate():
    pass

def DefineASR():
    pass
