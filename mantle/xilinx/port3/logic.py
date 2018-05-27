from magma import *
from .flatcascade import FlatCascade
from .LUT import LUT2, LUT3, LUT4, A0, A1, A2, A3
from .ROM import ROM1, ROM2, ROM3, ROM4

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


def And2(**kwargs):
    return LUT2(A0&A1, **kwargs)

def And3(**kwargs):
    return LUT3(A0&A1&A2, **kwargs)

def And4(**kwargs):
    return LUT4(A0&A1&A2&A3, **kwargs)

def DefineAnd(height, width):
    """
    Generate And module

    I0 : Array(width, Bit), I1 : Array(n, Bit) -> O : Array(n, Bit)
    """

    T = Array(width, Bit)
    class _And(Circuit):
        assert height > 1 and height <= 4

        name = 'And%dx%d' % (height, width)

        if   height == 2:
            IO  = ['input I0', T, 'input I1', T]
        elif height == 3:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T]
        elif height == 4:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T, 'input I3', T]
        IO  += ['output O', T]

        @classmethod
        def definition(def_):
            def andm(y):
                if height == 2: return And2(loc=(0,y/8, y%8))
                if height == 3: return And3(loc=(0,y/8, y%8))
                if height == 4: return And4(loc=(0,y/8, y%8))
            andmxn = join(col(andm, width))
            wire(def_.I0, andmxn.I0)
            wire(def_.I1, andmxn.I1)
            wire(andmxn.O, def_.O)

    return _And

def And(height, width=2, **kwargs):
    return DefineAnd(height, width)(**kwargs)

def AndN(n, **kwargs):
    """And gate with n-bit input."""

    if n <= 4:
        if n == 1:
            return ROM1(~(A0), **kwargs)
        if n == 2:
            return ROM2(~(A0&A1), **kwargs)
        if n == 3:
            return ROM3(~(A0&A1&A2), **kwargs)
        if n == 4:
            return ROM4(~(A0&A1&A2&A3), **kwargs)
    else:
        return FlatCascade(n, 4, A0&A1&A2&A3, 1, 0, 1, **kwargs)


def NAnd2(**kwargs):
    return LUT2(~(A0&A1), **kwargs )

def NAnd3(**kwargs):
    return LUT3(~(A0&A1&A2), **kwargs)

def NAnd4(**kwargs):
    return LUT4(~(A0&A1&A2&A3), **kwargs)

def DefineNAnd(height, width):
    """
    Generate And module

    I0 : Array(width, Bit), I1 : Array(n, Bit) -> O : Array(n, Bit)
    """

    T = Array(width, Bit)
    class _NAnd(Circuit):
        assert height > 1 and height <= 4

        name = 'NAnd%dx%d' % (height, width)

        if   height == 2:
            IO  = ['input I0', T, 'input I1', T]
        elif height == 3:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T]
        elif height == 4:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T, 'input I3', T]
        IO  += ['output O', T]

        @classmethod
        def definition(def_):
            def nandm(y):
                if height == 2: return NAnd2(loc=(0,y/8, y%8))
                if height == 3: return NAnd3(loc=(0,y/8, y%8))
                if height == 4: return NAnd4(loc=(0,y/8, y%8))
            nandmxn = join(col(nandm, width))
            wire(def_.I0, nandmxn.I0)
            wire(def_.I1, nandmxn.I1)
            wire(nandmxn.O, def_.O)

    return _NAnd

def NAnd(height, width=2, **kwargs):
    return DefineNAnd(height, width)(**kwargs)

def NAndN(n, **kwargs):
    """NAnd gate with n-bit input."""

    if n <= 4:
        if n == 1:
            return ROM1(~(A0), **kwargs)
        if n == 2:
            return ROM2(~(A0&A1), **kwargs)
        if n == 3:
            return ROM3(~(A0&A1&A2), **kwargs)
        if n == 4:
            return ROM4(~(A0&A1&A2&A3), **kwargs)
    else:
        return FlatCascade(n, 4, A0&A1&A2&A3, 1, 1, 0, **kwargs)


def Or2(**kwargs):
    return LUT2(A0|A1, **kwargs)

def Or3(**kwargs):
    return LUT3(A0|A1|A2, **kwargs)

def Or4(**kwargs):
    return LUT4(A0|A1|A2|A3, **kwargs)

def DefineOr(height, width):
    """
    Generate Or module

    I0 : Array(width, Bit), I1 : Array(n, Bit) -> O : Array(n, Bit)
    """

    T = Array(width, Bit)
    class _Or(Circuit):
        assert height > 1 and height <= 4

        name = 'Or%dx%d' % (height, width)

        if   height == 2:
            IO  = ['input I0', T, 'input I1', T]
        elif height == 3:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T]
        elif height == 4:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T, 'input I3', T]
        IO  += ['output O', T]

        @classmethod
        def definition(def_):
            def Orm(y):
                if height == 2: return Or2(loc=(0,y/8, y%8))
                if height == 3: return Or3(loc=(0,y/8, y%8))
                if height == 4: return Or4(loc=(0,y/8, y%8))
            Ormxn = join(col(Orm, width))
            wire(def_.I0, Ormxn.I0)
            wire(def_.I1, Ormxn.I1)
            wire(Ormxn.O, def_.O)

    return _Or

def Or(height, width=2, **kwargs):
    return DefineOr(height, width)(**kwargs)

def OrN(n, **kwargs):
    """Or gate with n-bit input."""

    if n <= 4:
        if n == 1:
            return ROM1(A0, **kwargs)
        if n == 2:
            return ROM2(A0|A1, **kwargs)
        if n == 3:
            return ROM3(A0|A1|A2, **kwargs)
        if n == 4:
            return ROM4(A0|A1|A2|A3, **kwargs)
    else:
        return FlatCascade(n, 4, ~(A0|A1|A2|A3), 0, 1, 0, **kwargs)


def NOr2(**kwargs):
    return LUT2(~(A0|A1), **kwargs)

def NOr3(**kwargs):
    return LUT3(~(A0|A1|A2), **kwargs)

def NOr4(**kwargs):
    return LUT4(~(A0|A1|A2|A3), **kwargs)

def DefineNOr(height, width):
    """
    Generate NOr module

    I0 : Array(width, Bit), I1 : Array(n, Bit) -> O : Array(n, Bit)
    """

    T = Array(width, Bit)
    class _NOr(Circuit):
        assert height > 1 and height <= 4

        name = 'NOr%dx%d' % (height, width)

        if   height == 2:
            IO  = ['input I0', T, 'input I1', T]
        elif height == 3:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T]
        elif height == 4:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T, 'input I3', T]
        IO  += ['output O', T]

        @classmethod
        def definition(def_):
            def Orm(y):
                if height == 2: return NOr2(loc=(0,y/8, y%8))
                if height == 3: return NOr3(loc=(0,y/8, y%8))
                if height == 4: return NOr4(loc=(0,y/8, y%8))
            nOrmxn = join(col(nOrm, width))
            wire(def_.I0, nOrmxn.I0)
            wire(def_.I1, nOrmxn.I1)
            wire(nOrmxn.O, def_.O)

    return _NOr

def NOr(height, width=2, **kwargs):
    return DefineNOr(height, width)(**kwargs)

def NOrN(n, **kwargs):
    """NOr gate with n-bit input."""

    if n <= 4:
        if n == 1:
            return ROM1(~(A0), **kwargs)
        if n == 2:
            return ROM2(~(A0|A1), **kwargs)
        if n == 3:
            return ROM3(~(A0|A1|A2), **kwargs)
        if n == 4:
            return ROM4(~(A0|A1|A2|A3), **kwargs)
    else:
        return FlatCascade(n, 4, ~(A0|A1|A2|A3), 0, 0, 1, **kwargs)


def XOr2(**kwargs):
    return LUT2(A0^A1, **kwargs)

def XOr3(**kwargs):
    return LUT3(A0^A1^A2, **kwargs)

def XOr4(**kwargs):
    return LUT4(A0^A1^A2^A3)

def DefineXOr(height, width):
    """
    Generate Or module

    I0 : Array(width, Bit), I1 : Array(n, Bit) -> O : Array(n, Bit)
    """

    T = Array(width, Bit)
    class _XOr(Circuit):
        assert height > 1 and height <= 4

        name = 'XOr%dx%d' % (height, width)

        if   height == 2:
            IO  = ['input I0', T, 'input I1', T]
        elif height == 3:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T]
        elif height == 4:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T, 'input I3', T]
        IO  += ['output O', T]

        @classmethod
        def definition(def_):
            def xOrm(y):
                if height == 2: return XOr2(loc=(0,y/8, y%8))
                if height == 3: return XOr3(loc=(0,y/8, y%8))
                if height == 4: return XOr4(loc=(0,y/8, y%8))
            xOrmxn = join(col(xOrm, width))
            wire(def_.I0, xOrmxn.I0)
            wire(def_.I1, xOrmxn.I1)
            wire(xOrmxn.O, def_.O)

    return _XOr

def XOr(height, width=2, **kwargs):
    return DefineXOr(height, width)(**kwargs)

def XOrN(n, **kwargs):
    """XNOr gate with n-bit input."""

    if n <= 4:
        if n == 1:
            return ROM1(~(A0), **kwargs)
        if n == 2:
            return ROM2(~(A0^A1), **kwargs)
        if n == 3:
            return ROM3(~(A0^A1^A2), **kwargs)
        if n == 4:
            return ROM4(~(A0^A1^A2^A3), **kwargs)
    return None



def NXOr2(**kwargs):
    return LUT2(~(A0^A1), **kwargs)

def NXOr3(**kwargs):
    return LUT3(~(A0^A1^A2), **kwargs)

def NXOr4(**kwargs):
    return LUT4(~(A0^A1^A2^A3), **kwargs)

def DefineNXOr(height, width):
    """
    Generate Or module

    I0 : Array(width, Bit), I1 : Array(n, Bit) -> O : Array(n, Bit)
    """

    T = Array(width, Bit)
    class _NXOr(Circuit):
        assert height > 1 and height <= 4

        name = 'NXOr%dx%d' % (height, width)

        if   height == 2:
            IO  = ['input I0', T, 'input I1', T]
        elif height == 3:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T]
        elif height == 4:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T, 'input I3', T]
        IO  += ['output O', T]

        @classmethod
        def definition(def_):
            def nxOrm(y):
                if height == 2: return NXOr2(loc=(0,y/8, y%8))
                if height == 3: return NXOr3(loc=(0,y/8, y%8))
                if height == 4: return NXOr4(loc=(0,y/8, y%8))
            nxOrmxn = join(col(nxOrm, width))
            wire(def_.I0, nxOrmxn.I0)
            wire(def_.I1, nxOrmxn.I1)
            wire(nxOrmxn.O, def_.O)

    return _NXOr

def NXOr(height, width=2, **kwargs):
    return DefineNXOr(height, width)(**kwargs)

def NXOrN(n, **kwargs):
    """XNOr gate with n-bit input."""

    if n <= 4:
        if n == 1:
            return ROM1(~(A0), **kwargs)
        if n == 2:
            return ROM2(~(A0^A1), **kwargs)
        if n == 3:
            return ROM3(~(A0^A1^A2), **kwargs)
        if n == 4:
            return ROM4(~(A0^A1^A2^A3), **kwargs)
    return None



def Buf(**kwargs):
    """Buffer - 1-bit input."""
    return LUT1(A0, **kwargs)

def DefineBuffer(width):
    """
    Generate Buffer module

    I0 : Array(width, Bit) -> O : Array(n, Bit)
    """
    T = Array(width, Bit)
    class _Buffer(Circuit):

        name = 'Buffer%d' % width
        IO  = ['input I', T, 'output O', T]

        @classmethod
        def definition(def_):
            def buf(y):
                return Buf(loc=(0,y/8, y%8))
            buffer = join(col(buf, width))
            wire(def_.I, buffer.I0)
            wire(buffer.O, def_.O)

    return _Buffer

def Buffer(n, **kwargs):
    return DefineBuffer(n)(**kwargs)


def Not(**kwargs):
    """Not gate - 1-bit input."""
    return LUT1(~A0, **kwargs)

def DefineInvert(width):
    """
    Generate Invert module

    I0 : Array(width, Bit) -> O : Array(n, Bit)
    """

    T = Array(width, Bit)
    class _Invert(Circuit):
        name = 'Invert%d' % width

        IO  = ['input I', T, 'output O', T]

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

