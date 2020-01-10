from magma import *
import magma as m
from .LUT import LUT3, A0, A1, A2

__all__  = ['Mux2', 'Mux4', 'Mux8', 'Mux16']
__all__ += ['DefineMux', 'Mux']

#
# C ? B : A
#
MUX2DATA = (~A2&A0)|(A2&A1)

"""Construct a Mux with 2 1-bit inputs."""
class Mux2(Circuit):
    IO = ["I", In(Bits[ 2 ]), "S", In(Bit), "O", Out(Bit) ]
    @classmethod
    def definition(mux2):
        lut = LUT3(MUX2DATA)
        wire(mux2.I[0], lut.I0)
        wire(mux2.I[1], lut.I1)
        wire(mux2.S, lut.I2)
        wire(lut.O, mux2.O)


# """Construct a Mux with 4 1-bit inputs."""
class Mux4(Circuit):
    IO = ["I", In(Bits[ 4 ]), "S", In(Bits[ 2 ]), "O", Out(Bit) ]
    @classmethod
    def definition(mux4):
        mux0 = Mux2()
        mux1 = Mux2()
        mux = Mux2()
        mux0(mux4.I[0:2],mux4.S[0])
        mux1(mux4.I[2:4],mux4.S[0])
        mux( array( [mux0.O, mux1.O] ), mux4.S[1] )
        wire( mux.O, mux4.O )

# """Construct a Mux with 8 1-bit inputs."""
class Mux8(Circuit):
    IO = ["I", In(Bits[ 8 ]), "S", In(Bits[ 3 ]), "O", Out(Bit) ]
    @classmethod
    def definition(mux8):
        mux0 = Mux4()
        mux1 = Mux4()
        mux = Mux2()
        mux0(mux8.I[0:4], mux8.S[0:2])
        mux1(mux8.I[4:8], mux8.S[0:2])
        mux( array( [mux0.O, mux1.O] ), mux8.S[2] )
        wire( mux.O, mux8.O )

# """Construct a Mux with 16 1-bit inputs."""
class Mux16(Circuit):
    IO = ["I", In(Bits[ 16 ]), "S", In(Bits[ 4 ]), "O", Out(Bit) ]
    @classmethod
    def definition(mux16):
        mux0 = Mux8()
        mux1 = Mux8()
        mux = Mux2()
        mux0(mux16.I[0:8],  mux16.S[0:3])
        mux1(mux16.I[8:16], mux16.S[0:3])
        mux( array( [mux0.O, mux1.O] ), mux16.S[3])
        wire(mux.O, mux16.O)

def MuxN(height, **kwargs):
    assert height in [2, 4, 8, 16]

    if height == 2:
        return Mux2(**kwargs)
    elif height == 4:
        return Mux4(**kwargs)
    elif height == 8:
        return Mux8(**kwargs)
    elif height == 16:
        return Mux16(**kwargs)

# Mux Module name
def _MuxName(height, width):
    return f'Mux{height}x{width}'

def _MuxInterface(height, width):
    AW = In(Bits[ width ])
    if   height == 2:
        args = ['I0', AW,
                'I1', AW]
        args += ['S', In(Bit)]
    elif height == 4:
        args = ['I0', AW,
                'I1', AW,
                'I2', AW,
                'I3', AW]
        args += ['S', In(Bits[ 2 ])]
    elif height == 8:
        args = ['I0', AW,
                'I1', AW,
                'I2', AW,
                'I3', AW,
                'I4', AW,
                'I5', AW,
                'I6', AW,
                'I7', AW]
        args += ['S', In(Bits[ 3 ])]
    elif height == 16:
        args = ['I0',  AW,
                'I1',  AW,
                'I2',  AW,
                'I3',  AW,
                'I4',  AW,
                'I5',  AW,
                'I6',  AW,
                'I7',  AW,
                'I8',  AW,
                'I9',  AW,
                'I10', AW,
                'I11', AW,
                'I12', AW,
                'I13', AW,
                'I14', AW,
                'I15', AW]
        args += ['S', In(Bits[ 4 ])]

    args += ['O', Out(AW)]

    return args


def DefineMux(height=2, width=1):

    """
    Construct a Mux. Height inputs are width bits wide.
    """

    assert height in [2, 4, 8, 16]
    if width is None:
        if height == 2:
            return Mux2
        elif height == 4:
            return Mux4
        elif height == 8:
            return Mux8
        elif height == 16:
            return Mux16

    class _Mux(Circuit):
        name = _MuxName(height, width)
        IO = _MuxInterface(height, width)
        @classmethod
        def definition(Mux):
            def amux(y):
                if height == 2:
                    return curry(MuxN(height, loc=(0,y//8,y%8)), prefix='I')
                return curry(MuxN(height), prefix='I')
            mux = braid(col(amux, width), forkargs=['S'])

            if   height == 2:  mux( Mux.I0, Mux.I1, Mux.S )
            elif height == 4:  mux( Mux.I0, Mux.I1, Mux.I2, Mux.I3, Mux.S )
            elif height == 8:  mux( Mux.I0, Mux.I1, Mux.I2, Mux.I3,
                                    Mux.I4, Mux.I5, Mux.I6, Mux.I7, Mux.S )
            elif height == 16: mux( Mux.I0, Mux.I1, Mux.I2, Mux.I3,
                                    Mux.I4, Mux.I5, Mux.I6, Mux.I7,
                                    Mux.I8, Mux.I9, Mux.I10, Mux.I11,
                                    Mux.I12, Mux.I13, Mux.I14, Mux.I15, Mux.S )
            wire( mux.O, Mux.O )
    return _Mux

def Mux(height=2, width=None, T=None, **kwargs):
    if T is not None:
        assert width is None, "Can only specify width **or** T"
        if issubclass(T, m.Bit):
            width = None
        elif issubclass(T, m.Bits) or \
                issubclass(T, m.Array) and issubclass(T.T, m.Bit):
            width = len(T)
        else:
            raise NotImplementedError(type(T))
    if width is None:
        return curry(MuxN(height, **kwargs), prefix="I")

    return DefineMux(height, width)(**kwargs)

