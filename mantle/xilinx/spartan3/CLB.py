from magma import *

__all__  = ['A0', 'A1', 'A2', 'A3']
__all__ += ['I0', 'I1', 'I2', 'I3']
__all__ += ['ALL', 'ANY', 'PARITY']
__all__ += ['ZERO', 'ONE']
__all__ += ['LUTS_PER_LOGICBLOCK', 'BITS_PER_LUT', 'LOG_BITS_PER_LUT']

__all__ += ['_LUT1', '_LUT2', '_LUT3', '_LUT4']
__all__ += ['MUXF5', 'MUXF6', 'MUXF7', 'MUXF8']
__all__ += ['MUXCY', 'MUXCY_L', 'MUXCY_D', 'ANDCY', 'XORCY', 'CARRY']
__all__ += ['FDRSE', 'FDCPE', 'FDCE']

LUTS_PER_LOGICBLOCK = 2
LOG_BITS_PER_LUT = 4
BITS_PER_LUT = 1 << LOG_BITS_PER_LUT

ZERO = 0
ONE = (1<<BITS_PER_LUT)-1

A0 = 0xAAAA
A1 = 0xCCCC
A2 = 0xF0F0
A3 = 0xFF00

I0 = A0
I1 = A1
I2 = A2
I3 = A3

ALL = A0 & A1 & A2 & A3
ANY = A0 | A1 | A2 | A3 
PARITY = A0 ^ A1 ^ A2 ^ A3 

_LUT1 = DeclareCircuit('LUT1',
               "input I0", Bit,
               "output O", Bit)

_LUT2 = DeclareCircuit('LUT2',
               "input I0", Bit,
               "input I1", Bit,
               "output O", Bit)

_LUT3 = DeclareCircuit('LUT3',
               "input I0", Bit,
               "input I1", Bit,
               "input I2", Bit,
               "output O", Bit)

_LUT4 = DeclareCircuit('LUT4',
               "input I0", Bit,
               "input I1", Bit,
               "input I2", Bit,
               "input I3", Bit,
               "output O", Bit) 

# D-FF with Clock Enable and Aynchronous Clear
FDCE = DeclareCircuit('FDCE',
               "input  C",   Bit,
               "input  CE",  Bit,
               "input  CLR", Bit,
               "input  D",   Bit,
               "output Q",   Bit)
    
# D-FF with Clock Enable and Aynchronous Preset and Clear
FDCPE = DeclareCircuit('FDCPE',
               "input  C",   Bit,
               "input  CE",  Bit,
               "input  CLR", Bit,
               "input  PRE", Bit,
               "input  D",   Bit,
               "output Q",   Bit) 

# D-FF with Synchronous Reset and Set and Clock Enable
FDRSE = DeclareCircuit('FDRSE',
               "input  C",   Bit,
               "input  CE",  Bit,
               "input  R",   Bit,
               "input  S",   Bit,
               "input  D",   Bit,
               "output Q",   Bit) 

MUXF5 = DeclareCircuit('MUXF5',
               "input I0", Bit,
               "input I1", Bit,
               "input  S", Bit,
               "output O", Bit)

MUXF6 = DeclareCircuit('MUXF6',
               "input I0", Bit,
               "input I1", Bit,
               "input  S", Bit,
               "output O", Bit)

MUXF7 = DeclareCircuit('MUXF7',
               "input I0", Bit,
               "input I1", Bit,
               "input  S", Bit,
               "output O", Bit)

MUXF8 = DeclareCircuit('MUXF8',
               "input I0", Bit,
               "input I1", Bit,
               "input  S", Bit,
               "output O", Bit)


MUXCY = DeclareCircuit('MUXCY',
               "input DI", Bit,
               "input CI", Bit,
               "input  S", Bit,
               "output O", Bit)

MUXCY_L = DeclareCircuit('MUXCY_L',
               "input DI", Bit,
               "input CI", Bit,
               "input  S", Bit,
               "output LO", Bit)

MUXCY_D = DeclareCircuit('MUXCY_D',
               "input DI", Bit,
               "input CI", Bit,
               "input  S", Bit,
               "output O", Bit,
               "output LO", Bit)

XORCY = DeclareCircuit('XORCY',
               "input LI", Bit,
               "input CI", Bit,
               "output O", Bit)

def CARRY(I0, I1, CIN):
    mux = MUXCY()
    wire(I0,  mux.S)
    wire(I1,  mux.DI)
    wire(CIN, mux.CI)

    xor = XORCY()
    wire(I0,  xor.LI)
    wire(CIN, xor.CI)

    return xor.O, mux.O

ANDCY = DeclareCircuit('MULT_AND',
               "input I0", Bit,
               "input I1", Bit,
               "output LO", Bit)

