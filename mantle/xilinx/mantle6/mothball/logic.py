from magma import *
from ..spartan6 import A0, A1, A2, A3, A4, A5
from .LUT import *
from .ROM import *
from .flatcascade import FlatCascade

__all__  = ['And',  'AndN',  'And2',  'And3',  'And4',  'And5',  'And6']
__all__ += ['NAnd', 'NAndN', 'NAnd2', 'NAnd3', 'NAnd4', 'NAnd5', 'NAnd6']
__all__ += ['Or',   'OrN',   'Or2',   'Or3',   'Or4',   'Or5',   'Or6']
__all__ += ['Nor',  'NorN',  'Nor2',  'Nor3',  'Nor4',  'Nor5',  'Nor6']
__all__ += ['Xor',  'XorN',  'Xor2',  'Xor3',  'Xor4',  'Xor5',  'Xor6']
__all__ += ['NXor', 'NXorN', 'NXor2', 'NXor3', 'NXor4', 'NXor5', 'NXor6']

__all__ += ['Buf', 'Buffer']
__all__ += ['Not', 'Invert']


def And2(**kwargs):
    return LUT2(A0&A1, **kwargs)

def And3(**kwargs):
    return LUT3(A0&A1&A2, **kwargs)

def And4(**kwargs):
    return LUT4(A0&A1&A2&A3, **kwargs)

def And5(**kwargs):
    return LUT5(A0&A1&A2&A3&A4, **kwargs)

def And6(**kwargs):
    return LUT6(A0&A1&A2&A3&A4&A5, **kwargs)

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
                if height == 5: return And5(loc=(0,y/8, y%8))
                if height == 6: return And6(loc=(0,y/8, y%8))
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
        if n == 5:
            return ROM5(A0&A1&A2&A3&A4, **kwargs)
        if n == 6:
            return ROM6(A0&A1&A2&A3&A4&A5, **kwargs)
    else:
        return FlatCascade(n, 6, A0&A1&A2&A3&A4&A5, 1, 0, 1, **kwargs)



def NAnd2(**kwargs):
    return LUT2(~(A0&A1), **kwargs )

def NAnd3(**kwargs):
    return LUT3(~(A0&A1&A2), **kwargs)

def NAnd4(**kwargs):
    return LUT4(~(A0&A1&A2&A3), **kwargs)

def NAnd5(**kwargs):
    return LUT5(~(A0&A1&A2&A3&A4), **kwargs)

def NAnd6(**kwargs):
    return LUT6(~(A0&A1&A2&A3&A4&A5), **kwargs)

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
                if height == 5: return NAnd5(loc=(0,y/8, y%8))
                if height == 6: return NAnd6(loc=(0,y/8, y%8))
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
        if n == 5:
            return ROM5(~(A0&A1&A2&A3&A4), **kwargs)
        if n == 6:
            return ROM6(~(A0&A1&A2&A3&A4&A5), **kwargs)
    else:
        return FlatCascade(n, 6, A0&A1&A2&A3&A4&A5, 1, 1, 0, **kwargs)


def Or2(**kwargs):
    return LUT2(A0|A1, **kwargs)

def Or3(**kwargs):
    return LUT3(A0|A1|A2, **kwargs)

def Or4(**kwargs):
    return LUT4(A0|A1|A2|A3, **kwargs)

def Or5(**kwargs):
    return LUT5(A0|A1|A2|A3|A4, **kwargs)

def Or6(**kwargs):
    return LUT6(A0|A1|A2|A3|A4|A5, **kwargs)

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
            def orm(y):
                if height == 2: return Or2(loc=(0,y/8, y%8))
                if height == 3: return Or3(loc=(0,y/8, y%8))
                if height == 4: return Or4(loc=(0,y/8, y%8))
                if height == 5: return Or5(loc=(0,y/8, y%8))
                if height == 6: return Or6(loc=(0,y/8, y%8))
            ormxn = join(col(orm, width))
            wire(def_.I0, ormxn.I0)
            wire(def_.I1, ormxn.I1)
            wire(ormxn.O, def_.O)

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
        if n == 5:
            return ROM5(A0|A1|A2|A3|A4, **kwargs)
        if n == 6:
            return ROM6(A0|A1|A2|A3|A4|A5, **kwargs)
    else:
        return FlatCascade(n, 6, ~(A0|A1|A2|A3|A4|A5), 0, 1, 0, **kwargs)


def Nor2(**kwargs):
    return LUT2(~(A0|A1), **kwargs)

def Nor3(**kwargs):
    return LUT3(~(A0|A1|A2), **kwargs)

def Nor4(**kwargs):
    return LUT4(~(A0|A1|A2|A3), **kwargs)

def Nor5():
    return LUT5(~(A0|A1|A2|A3|A4))

def Nor6():
    return LUT6(~(A0|A1|A2|A3|A4|A5))

def DefineNor(height, width):
    """
    Generate Nor module

    I0 : Array(width, Bit), I1 : Array(n, Bit) -> O : Array(n, Bit)
    """

    T = Array(width, Bit)
    class _Nor(Circuit):
        assert height > 1 and height <= 4

        name = 'Nor%dx%d' % (height, width)

        if   height == 2:
            IO  = ['input I0', T, 'input I1', T]
        elif height == 3:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T]
        elif height == 4:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T, 'input I3', T]
        IO  += ['output O', T]

        @classmethod
        def definition(def_):
            def orm(y):
                if height == 2: return Nor2(loc=(0,y/8, y%8))
                if height == 3: return Nor3(loc=(0,y/8, y%8))
                if height == 4: return Nor4(loc=(0,y/8, y%8))
                if height == 5: return Nor5(loc=(0,y/8, y%8))
                if height == 6: return Nor6(loc=(0,y/8, y%8))
            normxn = join(col(norm, width))
            wire(def_.I0, normxn.I0)
            wire(def_.I1, normxn.I1)
            wire(normxn.O, def_.O)

    return _Nor

def Nor(height, width=2, **kwargs):
    return DefineNor(height, width)(**kwargs)

def NorN(n, **kwargs):
    """Nor gate with n-bit input."""

    if n <= 4:
        if n == 1:
            return ROM1(~(A0), **kwargs)
        if n == 2:
            return ROM2(~(A0|A1), **kwargs)
        if n == 3:
            return ROM3(~(A0|A1|A2), **kwargs)
        if n == 4:
            return ROM4(~(A0|A1|A2|A3), **kwargs)
        if n == 5:
            return ROM5(~(A0|A1|A2|A3|A4), **kwargs)
        if n == 6:
            return ROM6(~(A0|A1|A2|A3|A4|A5), **kwargs)
    else:
        return FlatCascade(n, 6, ~(A0|A1|A2|A3|A4|A5), 0, 0, 1, **kwargs)


def Xor2(**kwargs):
    return LUT2(A0^A1, **kwargs)

def Xor3(**kwargs):
    return LUT3(A0^A1^A2, **kwargs)

def Xor4(**kwargs):
    return LUT4(A0^A1^A2^A3, **kwargs)

def Xor5():
    return LUT5(A0^A1^A2^A3^A4, **kwargs)

def Xor6():
    return LUT6(A0^A1^A2^A3^A4^A5, **kwargs)

def DefineXor(height, width):
    """
    Generate Or module

    I0 : Array(width, Bit), I1 : Array(n, Bit) -> O : Array(n, Bit)
    """

    T = Array(width, Bit)
    class _Xor(Circuit):
        assert height > 1 and height <= 4

        name = 'Xor%dx%d' % (height, width)

        if   height == 2:
            IO  = ['input I0', T, 'input I1', T]
        elif height == 3:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T]
        elif height == 4:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T, 'input I3', T]
        IO  += ['output O', T]

        @classmethod
        def definition(def_):
            def xorm(y):
                if height == 2: return Xor2(loc=(0,y/8, y%8))
                if height == 3: return Xor3(loc=(0,y/8, y%8))
                if height == 4: return Xor4(loc=(0,y/8, y%8))
                if height == 5: return Xor5(loc=(0,y/8, y%8))
                if height == 6: return Xor6(loc=(0,y/8, y%8))
            xormxn = join(col(xorm, width))
            wire(def_.I0, xormxn.I0)
            wire(def_.I1, xormxn.I1)
            wire(xormxn.O, def_.O)

    return _Xor

def Xor(height, width=2, **kwargs):
    return DefineXor(height, width)(**kwargs)

def XorN(n, **kwargs):
    """XNor gate with n-bit input."""

    if n <= 6:
        if n == 1:
            return ROM1(A0, **kwargs)
        if n == 2:
            return ROM2(A0^A1, **kwargs)
        if n == 3:
            return ROM3(A0^A1^A2, **kwargs)
        if n == 4:
            return ROM4(A0^A1^A2^A3, **kwargs)
        if n == 5:
            return ROM5(A0^A1^A2^A3^A4, **kwargs)
        if n == 6:
            return ROM6(A0^A1^A2^A3^A4^A5, **kwargs)
    return None


def NXor2(**kwargs):
    return LUT2(~(A0^A1), **kwargs)

def NXor3(**kwargs):
    return LUT3(~(A0^A1^A2), **kwargs)

def NXor4(**kwargs):
    return LUT4(~(A0^A1^A2^A3), **kwargs)

def NXor5(**kwargs):
    return LUT5(~(A0^A1^A2^A3^A4), **kwargs)

def NXor6():
    return LUT6(~(A0^A1^A2^A3^A4^A5), **kwargs)

def DefineNXor(height, width):
    """
    Generate Or module

    I0 : Array(width, Bit), I1 : Array(n, Bit) -> O : Array(n, Bit)
    """

    T = Array(width, Bit)
    class _NXor(Circuit):
        assert height > 1 and height <= 4

        name = 'NXor%dx%d' % (height, width)

        if   height == 2:
            IO  = ['input I0', T, 'input I1', T]
        elif height == 3:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T]
        elif height == 4:
            IO  = ['input I0', T, 'input I1', T, 'input I2', T, 'input I3', T]
        IO  += ['output O', T]

        @classmethod
        def definition(def_):
            def nxorm(y):
                if height == 2: return NXor2(loc=(0,y/8, y%8))
                if height == 3: return NXor3(loc=(0,y/8, y%8))
                if height == 4: return NXor4(loc=(0,y/8, y%8))
                if height == 5: return NXor5(loc=(0,y/8, y%8))
                if height == 6: return NXor6(loc=(0,y/8, y%8))
            nxormxn = join(col(nxorm, width))
            wire(def_.I0, nxormxn.I0)
            wire(def_.I1, nxormxn.I1)
            wire(nxormxn.O, def_.O)

    return _NXor

def NXor(height, width=2, **kwargs):
    return DefineNXor(height, width)(**kwargs)

def NXorN(n, **kwargs):
    """XNor gate with n-bit input."""

    if n <= 6:
        if n == 1:
            return ROM1(~(A0), **kwargs)
        if n == 2:
            return ROM2(~(A0^A1), **kwargs)
        if n == 3:
            return ROM3(~(A0^A1^A2), **kwargs)
        if n == 4:
            return ROM4(~(A0^A1^A2^A3), **kwargs)
        if n == 5:
            return ROM5(~(A0^A1^A2^A3^A4), **kwargs)
        if n == 6:
            return ROM6(~(A0^A1^A2^A3^A4^A5), **kwargs)
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

