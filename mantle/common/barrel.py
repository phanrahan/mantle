from magma import Circuit, Bit, Bits, In, Out, bits, wire, map_
from magma.bitutils import log2
from mantle import Mux2

__all__  = ['DefineShift', 'Shift']
__all__  = ['DefineLSL', 'LSL']
__all__ += ['DefineLSR', 'LSR']
__all__ += ['DefineASR', 'ASR']

__all__ += ['DefineRotate', 'Rotate']
__all__ += ['DefineROL', 'ROL']
__all__ += ['DefineROR', 'ROR']

def DefineShiftK(n, k, op):
    assert k < n
    T = Bits[ n ]
    class _ShiftK(Circuit):
        name = f'{op.upper()}{n}_{k}'
        IO = ['I', In(T), 'S', In(Bit), "O", Out(T)]
        @classmethod
        def definition(io):
            Is = [io.I[i] for i in range(n)]
            muxes = map_(Mux2, n)
            for i in range(n):
                if   op == 'lsl':
                    shifti = i - k
                    I = bits([Is[i], Is[shifti] if shifti >= 0 else 0])
                elif op == 'lsr':
                    shifti = i + k
                    I = bits([Is[i], Is[shifti] if shifti <  n else 0])
                elif op == 'asr':
                    shifti = i + k
                    I = bits([Is[i], Is[shifti] if shifti <  n else Is[n-1]])
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
    T = Bits[ n ]
    class _Shift(Circuit):
        name = f'{op.upper()}{n}'
        IO = ['I', In(T), 'S', In(Bits[ logn ]), "O", Out(T)]
        @classmethod
        def definition(io):
            I = io.I
            for k in range(logn):
                 I = ShiftK(n, 1<<k, op)(I, io.S[k])
            wire(I, io.O)
    return _Shift

def Shift(n, op):
    return DefineShift(n, op)()


def DefineLSL(n):
    return DefineShift(n, 'lsl')

def LSL(n):
    return Shift(n, 'lsl')

def DefineLSR(n):
    return DefineShift(n, 'lsr')

def LSR(n):
    return Shift(n, 'lsr')

def DefineASR(n):
    return DefineShift(n, 'asr')

def ASR(n):
    return Shift(n, 'asr')



def DefineRotateK(n, k, op):
    assert k < n
    T = Bits[ n ]
    class _RotateK(Circuit):
        name = f'{op.upper()}{n}_{k}'
        IO = ['I', In(T), 'S', In(Bit), "O", Out(T)]
        @classmethod
        def definition(io):
            Is = [io.I[i] for i in range(n)]
            muxes = map_(Mux2, n)
            for i in range(n):
                if  op == 'rol':
                    rotatei = (i - k + n) % n
                    I = bits([Is[i], Is[rotatei]])
                elif op == 'ror':
                    rotatei = (i + k) % n
                    I = bits([Is[i], Is[rotatei]])
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
    T = Bits[ n ]
    class _Rotate(Circuit):
        name = f'{op.upper()}{n}'
        IO = ['I', In(T), 'S', In(Bits[ logn ]), "O", Out(T)]
        @classmethod
        def definition(io):
            I = io.I
            for k in range(logn):
                 I = RotateK(n, 1<<k, op)(I, io.S[k])
            wire(I, io.O)
    return _Rotate

def Rotate(n, op):
    return DefineRotate(n, op)()

def DefineROL(n):
    return DefineRotate(n, 'rol')

def ROL(n):
    return Rotate(n, 'rol')

def DefineROR(n):
    return DefineRotate(n, 'ror')

def ROR(n):
    return Rotate(n, 'ror')
