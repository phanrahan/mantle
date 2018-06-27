from magma import *
from magma.bitutils import lutinit
from ..spartan6.CLB import *

__all__  = ['Mux2', 'Mux4', 'Mux8', 'Mux16']
__all__ += ['MuxN']
__all__ += ['DefineMux', 'Mux']


# """Construct a Mux with 2 1-bit inputs."""
class Mux2(Circuit):
    IO = ["I", In(Bits(2)), "S", In(Bit), "O", Out(Bit) ]

    @classmethod
    def definition(io):
        MUX2DATA = (~A2&A0)|(A2&A1)
        lut = _LUT3(INIT=lutinit(MUX2DATA,1<<3))
        wire( lut(io.I[0], io.I[1], io.S), io.O)

# """Construct a Mux with 4 1-bit inputs."""
class Mux4(Circuit):
    IO = ["I", In(Bits(4)), "S", In(Bits(2)), "O", Out(Bit) ]

    @classmethod
    def definition(io):
        MUX4DATA = (~A4&~A5&A0)|(A4&~A5&A1)|(~A4&A5&A2)|(A4&A5&A3)
        lut = _LUT6(INIT=lutinit(MUX4DATA,1<<6))
        wire( lut(io.I[0], io.I[1], io.I[2], io.I[3], io.S[0], io.S[1]), io.O)

# """Construct a Mux with 8 1-bit inputs."""
class Mux8(Circuit):
    IO = ["I", In(Bits(8)), "S", In(Bits(3)), "O", Out(Bit) ]

    @classmethod
    def definition(mux8):

        mux0 = Mux4()
        mux1 = Mux4()
        mux = MUXF7()

        mux0(mux8.I[0:4], mux8.S[0:2])
        mux1(mux8.I[4:8], mux8.S[0:2])
        mux( mux0.O, mux1.O, mux8.S[2] )
        wire( mux.O, mux8.O )

# """Construct a Mux with 16 1-bit inputs."""
class Mux16(Circuit):
    IO = ["I", In(Bits(16)), "S", In(Bits(4)), "O", Out(Bit) ]

    @classmethod
    def definition(mux16):

        mux0 = Mux8()
        mux1 = Mux8()
        mux = MUXF8()

        mux0(mux16.I[0:8],  mux16.S[0:3])
        mux1(mux16.I[8:16], mux16.S[0:3])
        mux(mux0.O, mux1.O, mux16.S[3])
        wire(mux.O, mux16.O)

def MuxN(height):

    assert height in [2, 4, 8, 16]

    if height == 2:
        return Mux2()
    elif height == 4:
        return Mux4()
    elif height == 8:
        return Mux8()
    elif height == 16:
        return Mux16()

MuxCache = {}

# Mux Module name
def _MuxName(height, width):
    return 'Mux%dx%d' % (height, width)

def DefineMux(height, width):

    """Construct a Mux. Height inputs are width bits wide."""
    name = _MuxName(height, width)
    if name in MuxCache:
        return MuxCache[name]

    assert height in [2, 4, 8, 16]

    AW = In(Bits(width))
    if   height == 2:
        args = ['I0', AW, 
                'I1', AW,
                'S', In(Bit)]
    elif height == 4:
        args = ['I0', AW, 
                'I1', AW,
                'I2', AW,
                'I3', AW,
                'S', In(Bits(2))]
    elif height == 8:
        args = ['I0', AW, 
                'I1', AW,
                'I2', AW,
                'I3', AW,
                'I4', AW,
                'I5', AW,
                'I6', AW,
                'I7', AW,
                'S', In(Bits(3))]
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
                'I15', AW,
                'S', In(Bits(4))]

    args += ['O', Out(AW)]
    D = DefineCircuit(name, *args)

    def amux(y):
        return curry(MuxN(height), prefix='I')
    muxes = col(amux, width)

    # Array of arrays ...
    mux = braid(muxes, forkargs=['S'])

    if   height == 2:  mux( D.I0, D.I1, D.S )
    elif height == 4:  mux( D.I0, D.I1, D.I2, D.I3, D.S )
    elif height == 8:  mux( D.I0, D.I1, D.I2, D.I3, D.I4, D.I5, D.I6, D.I7, D.S )
    elif height == 16: mux( D.I0, D.I1, D.I2, D.I3, D.I4, D.I5, D.I6, D.I7, 
                            D.I8, D.I9, D.I10, D.I11, D.I12, D.I13, D.I14, D.I15, D.S )
    wire( mux.O, D.O )

    EndCircuit()

    MuxCache[name] = D
    return D

def Mux(height, width):
    return DefineMux(height, width)()

