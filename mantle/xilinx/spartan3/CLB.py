from magma import *
from .simulation import *

__all__  = ['A0', 'A1', 'A2', 'A3']
__all__ += ['I0', 'I1', 'I2', 'I3']
__all__ += ['ALL', 'ANY', 'PARITY']
__all__ += ['ZERO', 'ONE']
__all__ += ['LUTS_PER_LOGICBLOCK', 'BITS_PER_LUT', 'LOG_BITS_PER_LUT']

__all__ += ['_LUT1', '_LUT2', '_LUT3', '_LUT4']
__all__ += ['MUXF5', 'MUXF6', 'MUXF7', 'MUXF8']
__all__ += ['MUXCY']
#__all__ += ['MUXCY', 'MUXCY_L', 'MUXCY_D']
__all__ += ['ANDCY', 'XORCY']
__all__ += ['CARRY']
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
               "I0", In(Bit),
               "O",  Out(Bit),
               stateful=False,
               simulate=simulate_lut1)

_LUT2 = DeclareCircuit('LUT2',
               "I0", In(Bit),
               "I1", In(Bit),
               "O",  Out(Bit),
               stateful=False,
               simulate=simulate_lut2)

_LUT3 = DeclareCircuit('LUT3',
               "I0", In(Bit),
               "I1", In(Bit),
               "I2", In(Bit),
               "O",  Out(Bit),
               stateful=False,
               simulate=simulate_lut3)

_LUT4 = DeclareCircuit('LUT4',
               "I0", In(Bit),
               "I1", In(Bit),
               "I2", In(Bit),
               "I3", In(Bit),
               "O",  Out(Bit),
               stateful=False,
               simulate=simulate_lut4) 

# D-FF with Clock Enable and Aynchronous Clear
FDCE = DeclareCircuit('FDCE',
               "C",   In(Clock),
               "CE",  In(Enable),
               "CLR", In(Bit),
               "D",   In(Bit),
               "Q",   Out(Bit),
               stateful=True,
               simulate=gen_simulate_fdce(has_reset=True, sync=False))
    
# D-FF with Clock Enable and Aynchronous Preset and Clear
FDCPE = DeclareCircuit('FDCPE',
               "C",   In(Clock),
               "CE",  In(Enable),
               "CLR", In(Bit),
               "PRE", In(Bit),
               "D",   In(Bit),
               "Q",   Out(Bit),
               stateful=True,
               simulate=gen_simulate_fdce(has_reset=True, has_set=True, sync=False)) 

# D-FF with Synchronous Reset and Set and Clock Enable
FDRSE = DeclareCircuit('FDRSE',
               "C",   In(Clock),
               "CE",  In(Enable),
               "R",   In(Reset),
               "S",   In(Reset),
               "D",   In(Bit),
               "Q",   Out(Bit),
               stateful=True,
               simulate=gen_simulate_fdce(has_set=True, has_reset=True, sync=True))

MUXF5 = DeclareCircuit('MUXF5',
               "I0", In(Bit),
               "I1", In(Bit),
               "S",  In(Bit),
               "O",  Out(Bit),
               stateful=False,
               simulate=simulate_mux)

MUXF6 = DeclareCircuit('MUXF6',
               "I0", In(Bit),
               "I1", In(Bit),
               "S",  In(Bit),
               "O",  Out(Bit),
               stateful=False,
               simulate=simulate_mux)

MUXF7 = DeclareCircuit('MUXF7',
               "I0", In(Bit),
               "I1", In(Bit),
               "S",  In(Bit),
               "O",  Out(Bit),
               stateful=False,
               simulate=simulate_mux)

MUXF8 = DeclareCircuit('MUXF8',
               "I0", In(Bit),
               "I1", In(Bit),
               "S", In(Bit),
               "O", Out(Bit),
               stateful=False,
               simulate=simulate_mux)


MUXCY = DeclareCircuit('MUXCY',
               "DI", In(Bit),
               "CI", In(Bit),
               "S", In(Bit),
               "O", Out(Bit),
               stateful=False,
               simulate=simulate_mux)

#MUXCY_L = DeclareCircuit('MUXCY_L',
#               "DI", In(Bit),
#               "CI", In(Bit),
#               "S", In(Bit),
#               "LO", Out(Bit))

#MUXCY_D = DeclareCircuit('MUXCY_D',
#               "DI", In(Bit),
#               "CI", In(Bit),
#               "S", In(Bit),
#               "O", Out(Bit),
#               "LO", Out(Bit))

XORCY = DeclareCircuit('XORCY',
               "LI", In(Bit),
               "CI", In(Bit),
               "O", Out(Bit),
               stateful=False,
               simulate=simulate_xor)

ANDCY = DeclareCircuit('MULT_AND',
               "I0", In(Bit),
               "I1", In(Bit),
               "LO", Out(Bit),
               stateful=False,
               simulate=simulate_and)

def CARRY(I0, I1, CIN):
    mux = MUXCY()
    wire(I0,  mux.S)
    wire(I1,  mux.DI)
    wire(CIN, mux.CI)

    xor = XORCY()
    wire(I0,  xor.LI)
    wire(CIN, xor.CI)

    return xor.O, mux.O

