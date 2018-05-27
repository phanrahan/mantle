from magma import *

# unary operators
__all__  = ['DefineReduceAnd', 'ReduceAnd']
__all__ += ['DefineReduceNAnd', 'ReduceNAnd']
__all__ += ['DefineReduceOr', 'ReduceOr']
__all__ += ['DefineReduceNOr', 'ReduceNOr']
__all__ += ['DefineReduceXOr', 'ReduceXOr']
__all__ += ['DefineReduceNXOr', 'ReduceNXOr']

# binary operators
__all__ += ['DefineAnd', 'And']
__all__ += ['DefineNAnd', 'NAnd']
__all__ += ['DefineOr', 'Or']
__all__ += ['DefineNOr', 'NOr']
__all__ += ['DefineXOr', 'XOr']
__all__ += ['DefineNXOr', 'NXOr']

# unary operators
__all__ += ['DefineInvert', 'Invert']
__all__ += ['Not']

# logical shifts
__all__ += ['DefineLSL', 'LSL']
__all__ += ['DefineLSR', 'LSR']

def FlatCascade(n, k, expr, cin, **kwargs):
    pass

@cache_definition
def DefineReduceAnd(n):
    pass

def ReduceAnd(height=2, **kwargs):
    return DefineReduceAnd(height)(**kwargs)

@cache_definition
def DefineReduceNAnd(n):
    pass

def ReduceNAnd(height=2, **kwargs):
    return DefineReduceNAnd(height)(**kwargs)

@cache_definition
def DefineReduceOr(n):
    pass

def ReduceOr(height=2, **kwargs):
    return DefineReduceOr(height)(**kwargs)

@cache_definition
def DefineReduceNOr(n):
    pass

def ReduceNOr(height=2, **kwargs):
    return DefineReduceNOr(height)(**kwargs)

@cache_definition
def DefineReduceXOr(n):
    pass

def ReduceXOr(height=2, **kwargs):
    return DefineReduceXOr(height)(**kwargs)

@cache_definition
def DefineReduceNXOr(n):
    pass

def ReduceNXOr(height=2, **kwargs):
    return DefineReduceNXOr(height)(**kwargs)

def DefineOp():
    pass

@cache_definition
def DefineAnd(height=2, width=1):
    return DefineOp('And', ReduceAnd, height, width)

def And(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceAnd(height, **kwargs))
    return DefineAnd(height, width)(**kwargs)

@cache_definition
def DefineNAnd(height=2, width=None):
    return DefineOp('NAnd', ReduceNAnd, height, width)

def NAnd(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceNAnd(height, **kwargs))
    return DefineNAnd(height, width)(**kwargs)

@cache_definition
def DefineOr(height=2, width=None):
    return DefineOp('Or', ReduceOr, height, width)

def Or(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceOr(height, **kwargs))
    return DefineOr(height, width)(**kwargs)

@cache_definition
def DefineNOr(height=2, width=None):
    return DefineOp('NOr', ReduceNOr, height, width)

def NOr(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceNOr(height, **kwargs))
    return DefineNOr(height, width)(**kwargs)

@cache_definition
def DefineXOr(height=2, width=None):
    return DefineOp('XOr', ReduceXOr, height, width)

def XOr(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceXOr(height, **kwargs))
    return DefineXOr(height, width)(**kwargs)

@cache_definition
def DefineNXOr(height=2, width=None):
    return DefineOp('NXOr', ReduceNXOr, height, width)

def NXOr(height=2, width=None, **kwargs):
    if width is None:
        return curry(ReduceNXOr(height, **kwargs))
    return DefineNXOr(height, width)(**kwargs)


@cache_definition
def DefineInvert(width):
    """
    Generate Invert module

    I0 : Bits(width) -> O : Bits(width)
    """

    T = Bits(width)
    class _Invert(Circuit):
        name = 'Invert%d' % width

        IO  = ['I', In(T), 'O', Out(T)]

        @classmethod
        def definition(def_):
            def not_(y):
                return Not(loc=(0,y/8, y%8))
            invert = join(col(not_, width))
            wire(def_.I, invert.I0)
            wire(invert.O, def_.O)

    return _Invert

def Invert(n, **kwargs):
    return DefineInvert(n)(**kwargs)


def Not(**kwargs):
    """Not gate - 1-bit input."""
    return LUT1(~A0, **kwargs)


def DefineFixedLSL(width, shift):
    T = Bits(width)
    class _LSL(Circuit):
        name = 'FixedLSL{}_{}'.format(width, shift)
        IO = ["I", In(T), "O", Out(T)]

        @classmethod
        def definition(io):
            for i in range(shift, width):
                wire(io.I[i - shift], io.O[i])
            for i in range(0, shift):
                wire(0, io.O[i])
    return _LSL

def FixedLSL(width, shift, **kwargs):
    return DefineFixedLSL(width, shift)(**kwargs)

DefineLSL = DefineFixedLSL
LSL = FixedLSL

def DefineFixedLSR(width, shift):
    T = Bits(width)
    class _LSR(Circuit):
        name = 'FixedLSR{}_{}'.format(width, shift)
        IO = ["I", In(T), "O", Out(T)]

        @classmethod
        def definition(io):
            for i in range(0, width - shift):
                wire(io.I[i + shift], io.O[i])
            for i in range(width - shift, width):
                wire(0, io.O[i])
    return _LSR

def FixedLSR(width, shift, **kwargs):
    return DefineFixedLSR(width, shift)(**kwargs)

DefineLSR = DefineFixedLSR
LSR = FixedLSR

