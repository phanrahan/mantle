from magma import curry
from mantle import DefineReduceAnd, DefineReduceNAnd
from mantle import DefineReduceOr, DefineReduceNOr
from mantle import DefineReduceXOr, DefineReduceNXOr
from mantle import DefineAnd, DefineNAnd
from mantle import DefineOr, DefineNOr
from mantle import DefineXOr, DefineNXOr
from mantle import DefineInvert

def ReduceAnd(height=2, **kwargs):
    return DefineReduceAnd(height)(**kwargs)

def ReduceNAnd(height=2, **kwargs):
    return DefineReduceNAnd(height)(**kwargs)

def ReduceOr(height=2, **kwargs):
    return DefineReduceOr(height)(**kwargs)

def ReduceNOr(height=2, **kwargs):
    return DefineReduceNOr(height)(**kwargs)

def ReduceXOr(height=2, **kwargs):
    return DefineReduceXOr(height)(**kwargs)

def ReduceNXOr(height=2, **kwargs):
    return DefineReduceNXOr(height)(**kwargs)


def And(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceAnd(height, **kwargs))
    return DefineAnd(height, width)(**kwargs)

def NAnd(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceNAnd(height, **kwargs))
    return DefineNAnd(height, width)(**kwargs)

def Or(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceOr(height, **kwargs))
    return DefineOr(height, width)(**kwargs)

def NOr(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceNOr(height, **kwargs))
    return DefineNOr(height, width)(**kwargs)

def XOr(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceXOr(height, **kwargs))
    return DefineXOr(height, width)(**kwargs)

def NXOr(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceNXOr(height, **kwargs))
    return DefineNXOr(height, width)(**kwargs)

def Invert(n, **kwargs):
    return DefineInvert(n)(**kwargs)

