import sys
if sys.version_info > (3, 0):
    from functools import reduce
    from functools import lru_cache
from magma import *
from .flatcascade import FlatCascade
from .LUT import LUT1, LUT2, LUT3, LUT4, A0, A1, A2, A3

# binary operators
__all__  = ['DefineAnd', 'And', 'ReduceAnd']
__all__ += ['DefineNAnd', 'NAnd', 'ReduceNAnd']
__all__ += ['DefineOr', 'Or', 'ReduceOr']
__all__ += ['DefineNOr', 'NOr', 'ReduceNOr']
__all__ += ['DefineXOr', 'XOr', 'ReduceXOr']
__all__ += ['DefineNXOr', 'NXOr', 'ReduceNXOr']

# unary operators
__all__ += ['DefineInvert', 'Invert']
__all__ += ['Not']

# logical shifts
__all__ += ['LeftShift', 'RightShift']


def AndN(n, **kwargs):
    """And gate with n-bit input."""
    if n == 1 :return LUT2(A0, **kwargs)
    if n == 2 :return LUT2(A0&A1, **kwargs)
    if n == 3: return LUT3(A0&A1&A2, **kwargs)
    if n == 4: return LUT4(A0&A1&A2&A3, **kwargs)
    return curry(FlatCascade(n, 1, A0&A1, 1, **kwargs))

def DefineAnd(height=2, width=None):
    """
    Generate And module

    I0 : Bits(width), I1 : Bits(width) -> O : Bits(width)
    """

    T = Bits(width)
    class _And(Circuit):
        assert height > 1 and height <= 4

        name = 'And%dx%d' % (height, width)

        if   height == 2:
            IO  = ['I0', In(T), 'I1', In(T)]
        elif height == 3:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T)]
        elif height == 4:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T), 'I3', In(T)]
        IO  += ['O', Out(T)]

        @classmethod
        def definition(def_):
            def andm(y):
                return AndN(height, loc=(0,y/8, y%8))
            andmxn = join(col(andm, width))
            wire(def_.I0, andmxn.I0)
            wire(def_.I1, andmxn.I1)
            wire(andmxn.O, def_.O)

    return _And

def And(height=2, width=None, **kwargs):
    if width is None:
        return AndN(height, **kwargs)
    return DefineAnd(height, width)(**kwargs)

def ReduceAnd(height=2, **kwargs):
    return uncurry(And(height, **kwargs))


def NAndN(n, **kwargs):
    if n == 1 :return LUT2(~(A0), **kwargs)
    if n == 2 :return LUT2(~(A0&A1), **kwargs)
    if n == 3: return LUT3(~(A0&A1&A2), **kwargs)
    if n == 4: return LUT4(~(A0&A1&A2&A3), **kwargs)
    return curry(FlatCascade(n, 1, A0 | ~A1, 0, **kwargs))

def DefineNAnd(height=2, width=None):
    """
    Generate And module

    I0 : Bits(width), I1 : Bits(width) -> O : Bits(width)
    """

    T = Bits(width)
    class _NAnd(Circuit):
        assert height > 1 and height <= 4

        name = 'NAnd%dx%d' % (height, width)

        if   height == 2:
            IO  = ['I0', In(T), 'I1', In(T)]
        elif height == 3:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T)]
        elif height == 4:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T), 'I3', In(T)]
        IO  += ['O', Out(T)]

        @classmethod
        def definition(def_):
            def nandm(y):
                return NAndN(height, loc=(0,y/8, y%8))
            nandmxn = join(col(nandm, width))
            wire(def_.I0, nandmxn.I0)
            wire(def_.I1, nandmxn.I1)
            wire(nandmxn.O, def_.O)

    return _NAnd

def NAnd(height=2, width=None, **kwargs):
    if width is None:
        return NAndN(height, **kwargs)
    return DefineNAnd(height, width)(**kwargs)

def ReduceNAnd(height=2, **kwargs):
    return uncurry(NAnd(height, **kwargs))


def OrN(n, **kwargs):
    """Or gate with n-bit input."""
    if n == 1 :return LUT2(A0, **kwargs)
    if n == 2 :return LUT2(A0|A1, **kwargs)
    if n == 3: return LUT3(A0|A1|A2, **kwargs)
    if n == 4: return LUT4(A0|A1|A2|A3, **kwargs)
    return curry(FlatCascade(n, 1, A0|A1, 0, **kwargs))

def DefineOr(height=2, width=None):
    """
    Generate Or module

    I0 : Bits(width), I1 : Bits(width) -> O : Bits(width)
    """

    T = Bits(width)
    class _Or(Circuit):
        assert height > 1 and height <= 4

        name = 'Or%dx%d' % (height, width)

        if   height == 2:
            IO  = ['I0', In(T), 'I1', In(T)]
        elif height == 3:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T)]
        elif height == 4:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T), 'I3', In(T)]
        IO  += ['O', Out(T)]

        @classmethod
        def definition(def_):
            def orm(y):
                return OrN(height, loc=(0,y/8, y%8))
            ormxn = join(col(orm, width))
            wire(def_.I0, ormxn.I0)
            wire(def_.I1, ormxn.I1)
            if height >= 3:
                wire(def_.I2, ormxn.I2)
            if height == 4:
                wire(def_.I3, ormxn.I3)
            wire(ormxn.O, def_.O)

    return _Or

def Or(height=2, width=None, **kwargs):
    if width is None:
        return OrN(height, **kwargs)

    if height > 4:
        half = height // 2
        or1 = Or(half, width, **kwargs)
        or2 = Or(height - half, width, **kwargs)
        output = Or(2, width, **kwargs)
        wire(or1.O, output.I0)
        wire(or2.O, output.I1)
        args = []
        for i in range(half):
            args.append("I{}".format(i))
            args.append(getattr(or1, "I{}".format(i)))
        for i in range(height - half):
            args.append("I{}".format(i + half))
            args.append(getattr(or2, "I{}".format(i)))
        args.append("O")
        args.append(output.O)
        return AnonymousCircuit(*args)
    else:
        return DefineOr(height, width)(**kwargs)

def ReduceOr(height=2, **kwargs):
    return uncurry(Or(height, **kwargs))



def NOrN(n, **kwargs):
    if n == 1: return LUT2(~(A0), **kwargs)
    if n == 2: return LUT2(~(A0|A1), **kwargs)
    if n == 3: return LUT3(~(A0|A1|A2), **kwargs)
    if n == 4: return LUT4(~(A0|A1|A2|A3), **kwargs)
    return curry(FlatCascade(n, 1, A0 & ~A1, 1, **kwargs))

def DefineNOr(height=2, width=None):
    """
    Generate Nor module

    I0 : Bits(width), I1 : Bits(width) -> O : Bits(width)
    """

    T = Bits(width)
    class _NOr(Circuit):
        assert height > 1 and height <= 4

        name = 'Nor%dx%d' % (height, width)

        if   height == 2:
            IO  = ['I0', In(T), 'I1', In(T)]
        elif height == 3:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T)]
        elif height == 4:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T), 'I3', In(T)]
        IO  += ['O', Out(T)]

        @classmethod
        def definition(def_):
            def orm(y):
                return NorN(height, loc=(0,y/8, y%8))
            normxn = join(col(norm, width))
            wire(def_.I0, normxn.I0)
            wire(def_.I1, normxn.I1)
            wire(normxn.O, def_.O)

    return _Nor

def NOr(height=2, width=None, **kwargs):
    if width is None:
        return NOrN(height, **kwargs)
    return DefineNOr(height, width)(**kwargs)

def ReduceNOr(height=2, **kwargs):
    return uncurry(NOr(height, **kwargs))


def XOrN(n, **kwargs):
    if n == 1: return LUT2(A0, **kwargs)
    if n == 2: return LUT2(A0^A1, **kwargs)
    if n == 3: return LUT3(A0^A1^A2, **kwargs)
    if n == 4: return LUT4(A0^A1^A2^A3, **kwargs)
    return curry(FlatCascade(n, 1, A0^A1, 0, **kwargs))

def DefineXOr(height=2, width=1):
    """
    Generate Exclusive Or module

    I0 : Bits(width), I1 : Bits(width) -> O : Bits(width)
    """

    T = Bits(width)
    class _XOr(Circuit):
        assert height > 1 and height <= 4

        name = 'Xor%dx%d' % (height, width)

        if   height == 2:
            IO  = ['I0', In(T), 'I1', In(T)]
        elif height == 3:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T)]
        elif height == 4:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T), 'I3', In(T)]
        IO  += ['O', Out(T)]

        @classmethod
        def definition(def_):
            def xorm(y):
                return XorN(height, loc=(0,y/8, y%8))
            xormxn = join(col(xorm, width))
            wire(def_.I0, xormxn.I0)
            wire(def_.I1, xormxn.I1)
            wire(xormxn.O, def_.O)

    return _Xor

def XOr(height=2, width=None, **kwargs):
    if width is None:
        return XOrN(height, **kwargs)
    return DefineXOr(height, width)(**kwargs)

def ReduceXOr(height=2, **kwargs):
    return uncurry(XOr(height, **kwargs))


def NXOrN(n, **kwargs):
    if n == 1: return LUT2(~(A0), **kwargs)
    if n == 2: return LUT2(~(A0^A1), **kwargs)
    if n == 3: return LUT3(~(A0^A1^A2), **kwargs)
    if n == 4: return LUT4(~(A0^A1^A2^A3), **kwargs)
    return None

def DefineNXOr(height=2, width=None):
    """
    Generate Or module

    I0 : Bits(width), I1 : Bits(width) -> O : Bits(width)
    """

    T = Bits(width)
    class _NXOr(Circuit):
        assert height > 1 and height <= 4

        name = 'NXor%dx%d' % (height, width)

        if   height == 2:
            IO  = ['I0', In(T), 'I1', In(T)]
        elif height == 3:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T)]
        elif height == 4:
            IO  = ['I0', In(T), 'I1', In(T), 'I2', In(T), 'I3', In(T)]
        IO  += ['O', Out(T)]

        @classmethod
        def definition(def_):
            def nxorm(y):
                return NXorN(height, loc=(0,y/8, y%8))
            nxormxn = join(col(nxorm, width))
            wire(def_.I0, nxormxn.I0)
            wire(def_.I1, nxormxn.I1)
            wire(nxormxn.O, def_.O)

    return _NXor

def NXOr(height=2, width=None, **kwargs):
    if width is None: 
        return NOrN(height, **kwargs)
    return DefineNXOr(height, width)(**kwargs)

def ReduceNXOr(height=2, **kwargs):
    return uncurry(NXOr(height, **kwargs))



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


def LeftShift(width, shift_amount):
    T = Bits(width)
    class _LeftShift(Circuit):
        name = 'LeftShift_w{}_a{}'.format(width, shift_amount)

        IO = ["I", In(T), "O", Out(T)]

        @classmethod
        def definition(io):
            for i in range(shift_amount, width):
                wire(io.I[i - shift_amount], io.O[i])
            for i in range(0, shift_amount):
                wire(0, io.O[i])
    return _LeftShift

def RightShift(width, shift_amount):
    T = Bits(width)
    class _RightShift(Circuit):
        name = 'RightShift_w{}_a{}'.format(width, shift_amount)

        IO = ["I", In(T), "O", Out(T)]

        @classmethod
        def definition(io):
            for i in range(0, width - shift_amount):
                wire(io.I[i + shift_amount], io.O[i])
            for i in range(width - shift_amount, width):
                wire(0, io.O[i])
    return _RightShift
