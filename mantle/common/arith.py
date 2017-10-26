from mantle import DefineAdd, DefineSub, DefineNegate, DefineASR

def Add(n, cin=False, cout=False, **kwargs):
    return DefineAdd(n, cin, cout)(**kwargs)

def Sub(n, cin=False, cout=False, **kwargs):
    return DefineSub(n, cin, cout)(**kwargs)

def Negate(width, **kwargs):
    return DefineNegate(width)(**kwargs)

def ASR(width, shift, **kwargs):
    return DefineASR(width, shift)(**kwargs)
