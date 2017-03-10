from magma import *

__all__ = ['BUFG', 'BUFGCE']

BUFG = DeclareCircuit('BUFG', "input I", Bit, "output O", Bit)

BUFGCE = DeclareCircuit('BUFGCE', "input CE", Bit, "input I", Bit, "output O", Bit)

