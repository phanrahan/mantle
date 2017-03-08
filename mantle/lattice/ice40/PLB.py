from magma import *

__all__  = ['A0', 'A1', 'A2', 'A3']
__all__ += ['I0', 'I1', 'I2', 'I3']
__all__ += ['ALL', 'ANY', 'PARITY']
__all__ += ['ZERO', 'ONE']
__all__ += ['LUTS_PER_LOGICBLOCK', 'BITS_PER_LUT', 'LOG_BITS_PER_LUT']

__all__ += ['SB_LUT4']
__all__ += ['SB_CARRY']

__all__ += ['SB_DFF',    'SB_DFFE', 
            'SB_DFFSR',  'SB_DFFESR',
            'SB_DFFSS',  'SB_DFFESS',
            'SB_DFFR',   'SB_DFFER',
            'SB_DFFS',   'SB_DFFES',
            'SB_DFFN',   'SB_DFFNE', 
            'SB_DFFNSR', 'SB_DFFNESR',
            'SB_DFFNSS', 'SB_DFFNESS',
            'SB_DFFNR',  'SB_DFFNER',
            'SB_DFFNS',  'SB_DFFNES']

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

SB_LUT4 = DeclareCircuit('SB_LUT4',
               "I0", In(Bit),
               "I1", In(Bit),
               "I2", In(Bit),
               "I3", In(Bit),
               "O",  Out(Bit), cells=1) 

# Implements (I0&I1)|(I1&I2)|(I2&I0)
SB_CARRY = DeclareCircuit('SB_CARRY',
               "I0", In(Bit), # from I1
               "I1", In(Bit), # from I2
               "CI", In(Bit),
               "CO", Out(Bit)) 

# Positive edge versions

# DFF - D Flip-Flop
SB_DFF = DeclareCircuit('SB_DFF',
               "C", In(Bit),
               "D", In(Bit),
               "Q", Out(Bit))

# DFF w/ Clock enable
SB_DFFE = DeclareCircuit('SB_DFFE',
               "C", In(Bit),
               "E", In(Bit),
               "D", In(Bit),
               "Q", Out(Bit))

# DFF w/ Synchronous Reset
SB_DFFSR = DeclareCircuit('SB_DFFSR',
               "C", In(Bit),
               "R", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))

# DFF w/ Asynchronous Reset
SB_DFFR = DeclareCircuit('SB_DFFR',
               "C", In(Bit),
               "R", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))
    
# DFF w/ Synchronous Set
SB_DFFSS = DeclareCircuit('SB_DFFSS',
               "C", In(Bit),
               "S", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))

# DFF w/ Asynchronous Set
SB_DFFS = DeclareCircuit('SB_DFFS',
               "C", In(Bit),
               "S", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))
    
# DFF w/ Synchronous Reset, Clock enable
SB_DFFESR = DeclareCircuit('SB_DFFESR',
               "C", In(Bit),
               "R", In(Bit), 
               "E", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))

# DFF w/ Asynchronous Reset, Clock enable
SB_DFFER = DeclareCircuit('SB_DFFER',
               "C", In(Bit),
               "R", In(Bit), 
               "E", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))
    
# DFF w/ Synchronous Set, Clock enable
SB_DFFESS = DeclareCircuit('SB_DFFESS',
               "C", In(Bit),
               "S", In(Bit), 
               "E", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))

# DFF w/ Asynchronous Set, Clock enable
SB_DFFES = DeclareCircuit('SB_DFFES',
               "C", In(Bit),
               "S", In(Bit), 
               "E", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))

# Negative edge versions
SB_DFFN = DeclareCircuit('SB_DFFN',
               "C", In(Bit),
               "D", In(Bit),
               "Q", Out(Bit))

# DFFN w/ Clock enable
SB_DFFNE = DeclareCircuit('SB_DFFNE',
               "C", In(Bit),
               "E", In(Bit),
               "D", In(Bit),
               "Q", Out(Bit))

# DFFN w/ Synchronous Reset
SB_DFFNSR = DeclareCircuit('SB_DFFNSR',
               "C", In(Bit),
               "R", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))

# DFFN w/ Asynchronous Reset
SB_DFFNR = DeclareCircuit('SB_DFFNR',
               "C", In(Bit),
               "R", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))
    
# DFFN w/ Synchronous Set
SB_DFFNSS = DeclareCircuit('SB_DFFNSS',
               "C", In(Bit),
               "S", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))

# DFFN w/ Asynchronous Set
SB_DFFNS = DeclareCircuit('SB_DFFNS',
               "C", In(Bit),
               "S", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))
    
# DFFN w/ Synchronous Reset, Clock enable
SB_DFFNESR = DeclareCircuit('SB_DFFNESR',
               "C", In(Bit),
               "R", In(Bit), 
               "E", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))

# DFFN w/ Asynchronous Reset, Clock enable
SB_DFFNER = DeclareCircuit('SB_DFFNER',
               "C", In(Bit),
               "R", In(Bit), 
               "E", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))
    
# DFFN w/ Synchronous Set, Clock enable
SB_DFFNESS = DeclareCircuit('SB_DFFNESS',
               "C", In(Bit),
               "S", In(Bit), 
               "E", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))

# DFFN w/ Asynchronous Set, Clock enable
SB_DFFNES = DeclareCircuit('SB_DFFNES',
               "C", In(Bit),
               "S", In(Bit), 
               "E", In(Bit), 
               "D", In(Bit),
               "Q", Out(Bit))

if __name__ == '__main__':
    lut = SB_LUT4()
    print(lut.interface)
