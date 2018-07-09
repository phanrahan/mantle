from magma import Circuit, Bit, Bits, In, Out, bits, wire, map_
from magma.bitutils import log2
from mantle import Mux2

__all__  = ['DefineShift', 'Shift', 'shift']
__all__ += ['DefineRotate', 'Rotate', 'rotate']

def DefineShiftK(n, k, op):
    assert k < n
    T = Bits(n)
    class _ShiftK(Circuit):
        name = f'Shift{n}_{k}'
        IO = ['I', In(T), 'S', In(Bit), 'SI', In(Bit), "O", Out(T)]
        @classmethod
        def definition(io):
            Is = [io.I[i] for i in range(n)]
            muxes = map_(Mux2, n)
            for i in range(n):
                if   op == 'lsl':
                    shifti = i - k
                    I = bits([Is[i], Is[shifti] if shifti >= 0 else io.SI])
                elif op == 'lsr' or op == 'asr':
                    shifti = i + k
                    I = bits([Is[i], Is[shifti] if shifti <  n else io.SI])
                else:
                    assert False
                muxes[i]( I, io.S )
            for i in range(n):
                Is[i] = muxes[i].O
            wire(bits(Is), io.O)
    return _ShiftK

def ShiftK(n, k, op):
    return DefineShiftK(n, k, op)()

def DefineShift(n, op):
    assert n in [2, 4, 8, 16]
    logn = log2(n)
    T = Bits(n)
    class _Shift(Circuit):
        name = f'Shift{n}'
        IO = ['I', In(T), 'S', In(Bits(logn)), 'SI', In(Bit), "O", Out(T)]
        @classmethod
        def definition(io):
            I = io.I
            for k in range(logn):
                 I = ShiftK(n, 1<<k, op)(I, io.S[k], io.SI)
            wire(I, io.O)
    return _Shift

def Shift(n, op):
    return DefineShift(n, op)()

def shift(i, s, si, op):
    n = len(i)
    assert log2(n) == len(s)
    return Shift(n, op)(i, s, si)


def DefineRotateK(n, k, op):
    assert k < n
    T = Bits(n)
    class _RotateK(Circuit):
        name = f'Rotate{n}_{k}'
        IO = ['I', In(T), 'S', In(Bit), "O", Out(T)]
        @classmethod
        def definition(io):
            Is = [io.I[i] for i in range(n)]
            muxes = map_(Mux2, n)
            for i in range(n):
                if  op == 'rol':
                    shifti = (i - k + n) % n
                    I = bits([Is[i], Is[shifti]])
                elif op == 'ror':
                    shifti = (i + k) % n
                    I = bits([Is[i], Is[shifti]])
                else:
                    assert False
                muxes[i]( I, io.S )
            for i in range(n):
                Is[i] = muxes[i].O
            wire(bits(Is), io.O)
    return _RotateK

def RotateK(n, k, op):
    return DefineRotateK(n, k, op)()

def DefineRotate(n, op):
    assert n in [2, 4, 8, 16]
    logn = log2(n)
    T = Bits(n)
    class _Rotate(Circuit):
        name = f'Rotate{n}'
        IO = ['I', In(T), 'S', In(Bits(logn)), "O", Out(T)]
        @classmethod
        def definition(io):
            I = io.I
            for k in range(logn):
                 I = RotateK(n, 1<<k, op)(I, io.S[k])
            wire(I, io.O)
    return _Rotate

def Rotate(n, op):
    return DefineRotate(n, op)()

def rotate(i, s, op):
    n = len(i)
    assert log2(n) == len(s)
    return Rotate(n, op)(i, s)
