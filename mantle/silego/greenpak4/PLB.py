from magma import *

__all__  = ['A0', 'A1', 'A2', 'A3']
__all__ += ['I0', 'I1', 'I2', 'I3']
__all__ += ['ALL', 'ANY', 'PARITY']
__all__ += ['ZERO', 'ONE']

__all__ += ['GP_LUT2']
__all__ += ['GP_LUT3']
__all__ += ['GP_LUT4']

ZERO = 0x0000
ONE  = 0xFFFF

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

GP_LUT2 = DeclareCircuit('GP_2LUT',
               "IN0", In(Bit),
               "IN1", In(Bit),
               "OUT",  Out(Bit)) 

GP_LUT3 = DeclareCircuit('GP_3LUT',
               "IN0", In(Bit),
               "IN1", In(Bit),
               "IN2", In(Bit),
               "OUT",  Out(Bit)) 

GP_LUT4 = DeclareCircuit('GP_4LUT',
               "IN0", In(Bit),
               "IN1", In(Bit),
               "IN2", In(Bit),
               "IN3", In(Bit),
               "OUT",  Out(Bit)) 

