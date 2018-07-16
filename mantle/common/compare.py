from mantle import DefineEQ, DefineNE
from mantle import DefineULE, DefineUGE, DefineUGT, DefineULT
from mantle import DefineSLE, DefineSGE, DefineSGT, DefineSLT

def EQ(n, **kwargs):
    return DefineEQ(n)(**kwargs)

def NE(n, **kwargs):
    return DefineNE(n)(**kwargs)

def UGE(n, **kwargs):
    return DefineUGE(n)(**kwargs)

def ULE(n, **kwargs):
    return DefineULE(n)(**kwargs)

def ULT(n, **kwargs):
    return DefineULT(n)(**kwargs)

def UGT(n, **kwargs):
    return DefineUGT(n)(**kwargs)

def SGE(n, **kwargs):
    return DefineSGE(n)(**kwargs)

def SLE(n, **kwargs):
    return DefineSLE(n)(**kwargs)

def SLT(n, **kwargs):
    return DefineSLT(n)(**kwargs)

def SGT(n, **kwargs):
    return DefineSGT(n)(**kwargs)

